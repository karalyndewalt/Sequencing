"""Class based approach to Sequence project"""

MODIFIERS = {"-", "m", "b", "d"}

BASES = {"A", "G", "C", "T", "U", "R",
         "Y", "S", "W", "K", "M", "B",
         "D", "H", "V", "N",}

SUGARS = {"d", "r", "e", "m", "y", "l", "k", "o"}

LINKAGES = {"o", "s",}

BASE_MASSES = {"o":1, "A": 2, "G": 3, "U": 4, "C":5, "d": 0, "r": 0, "-": 0}

ALT_BASE_MASSES = {"o":1,
                   "-Ad": 2, "-Ar": 2.5,
                   "-Gd": 3, "-Gr": 3.5,
                   "-Cd": 4, "-Cr": 4.5,
                   "-Td": 5,
                   "-Ur": 6.5,}


class Sequence(object):
    """Class for DNA/RNA sequences"""

    look_ups = {0: MODIFIERS, 1: BASES, 2: SUGARS, 3: LINKAGES}
    str_const = {0: "MODIFIER",
                 1: "BASE",
                 2: "SUGAR",
                 3: "LINKAGE",
                 4: "Final Character",
                }


    def __init__(self, seq=None):

        if seq:
            codes = self._validate(seq)
            if codes[0] == -1:
                self.seq = seq
                self.counts = self._get_counts()
                self.mass = self._get_mass()
            print self._validation_messages(codes)

        else:
            self.seq = None
            self.counts = {}
            self.mass = None


    def _validate(self, seq):
        """Returns tuple (code, (pos, problem_char))

        >>> seq = "-Gdo-Gdo-Ado-Ado-Udo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
        >>> new_seq = Sequence()

        >>> new_seq._validate(seq)
        (-1, (-1, None))

        >>> new_seq._validate("-Gdo-Gdo")
        (4, (7, 'o'))

        >>> new_seq._validate("-Gdo-Go")
        (-1, (-1, None))

        >>> new_seq._validate("xGdo-Gd")
        (0, (0, 'x'))

        >>> new_seq._validate("-Xdo-Gd")
        (1, (1, 'X'))

        >>> new_seq._validate("-Gxo-Gd")
        (2, (2, 'x'))

        >>> new_seq._validate("-Gdx-Gd")
        (3, (3, 'x'))

        """
        # check for linkage at the end of sequence. Linkage not valid,
        # but 'o' is a valid SUGAR and LINKAGE.
        # if lst char 'o' must be preceded by BASE
        # "-Go" -- valid
        # "-Gdo" -- invalid

        if seq[-1] in self.look_ups[2] and seq[-2] not in self.look_ups[1]:
            return (4, (len(seq)-1, seq[-1]))

        pos_code = 0

        for pair in enumerate(seq):
            pos, char = pair

            if char not in self.look_ups[pos_code]:
                return (pos_code, (pos, char))

            pos_code = 0 if (pos_code >= 3) else (pos_code + 1)

        return (-1, (-1, None))


    def _validation_messages(self, codes):
        """Returns validity of seq, with helpful errors

        >>> new_seq = Sequence()

        >>> new_seq._validation_messages((-1, (-1, None)))
        'Validation complete, no errors found.'

        >>> new_seq._validation_messages((4, (7, 'x')))
        'Error at seq pos: 7, x not a valid Final Character.'

        >>> new_seq._validation_messages((0, (0, 'x')))
        'Error at seq pos: 0, x not a valid MODIFIER.'

        >>> new_seq._validation_messages((1, (1, 'X')))
        'Error at seq pos: 1, X not a valid BASE.'

        >>> new_seq._validation_messages((2, (2, 'x')))
        'Error at seq pos: 2, x not a valid SUGAR.'

        >>> new_seq._validation_messages((3, (3, 'x')))
        'Error at seq pos: 3, x not a valid LINKAGE.'

        """
        # validity = self._check_seq(seq)

        error_code, pos_char = codes
        pos, char = pos_char

        if error_code >= 0:
            temp = "Error at seq pos: {pos}, {char} not a valid {const}."
            message = temp.format(pos=pos,
                                  char=char,
                                  const=self.str_const[error_code])
        else:
            message = "Validation complete, no errors found."

        return message


    def _get_counts(self):
        """ Returns dict of base counts preserving RNA/DNA and modifier

        """

        seq_counts = {}
        bases = self.seq.split('o')

        seq_counts['o'] = len(bases) - 1

        for base in bases:
            seq_counts.setdefault(base, 0)
            seq_counts[base] += 1

        return seq_counts


    def _get_mass(self):
        """Returns total mass of a sequence

        """

        # counts = count_seq_preserve(seq)
        mass = 0
        for item in self.counts.iteritems():
            base, count = item
            base_mass = ALT_BASE_MASSES[base] * count
            mass += base_mass
        return mass


    def get_label(self):
        """Returns sequence in lable format

        """
        out = []
        stack = []
        tokens = self.seq.split('o')

        for base in tokens:
            if base[2] == 'd':
                stack.append(base[1])
            # rna found
            else:
                if stack:
                    out.append('[')
                    out.extend(stack)
                    out.append(']')
                    # reset stack
                    stack = []

                out.append(base[1])

        if stack:
            out.append('[')
            out.extend(stack)
            out.append(']')

        return "".join(out)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
