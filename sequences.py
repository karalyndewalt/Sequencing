"""Class based approach to Sequence project"""

MODIFIERS = {"-", "m", "b", "d"}

BASES = {"A", "G", "C", "T", "U", "R",
         "Y", "S", "W", "K", "M", "B",
         "D", "H", "V", "N",}

SUGARS = {"d", "r", "e", "m", "y", "l", "k", "o"}

LINKAGES = {"o", "s",}


class Sequence(object):

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
            print self._validtion_messages(codes)
        else:
            self.seq = None


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


    def _validtion_messages(self, codes):
        """Returns validity of seq, with helpful errors

        >>> new_seq = Sequence()

        >>> new_seq._validtion_messages((-1, (-1, None)))
        'Validation complete, no errors found.'

        >>> new_seq._validtion_messages((4, (7, 'x')))
        'Error at seq pos: 7, x not a valid Final Character.'

        >>> new_seq._validtion_messages((0, (0, 'x')))
        'Error at seq pos: 0, x not a valid MODIFIER.'

        >>> new_seq._validtion_messages((1, (1, 'X')))
        'Error at seq pos: 1, X not a valid BASE.'

        >>> new_seq._validtion_messages((2, (2, 'x')))
        'Error at seq pos: 2, x not a valid SUGAR.'

        >>> new_seq._validtion_messages((3, (3, 'x')))
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
