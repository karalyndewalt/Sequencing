"""Question 1
Part A: Write a function that returns counts for the different
parts of the sequence (bases and linkages).
notes:
Part B: Assuming you can ask a chemist for a lookup table of masses write a
function that converts your counts into a mass.
"""


BASE_MASSES = {"o":1, "A": 2, "G": 3, "U": 4, "C":5, "d": 0, "r": 0, "-": 0}

ALT_BASE_MASSES = {"o":1,
                   "-Ad": 2, "-Ar": 2.5,
                   "-Gd": 3, "-Gr": 3.5,
                   "-Cd": 4, "-Cr": 4.5,
                   "-Td": 5,
                   "-Ur": 6,}


def count_seq(seq):
    """Returns dict of counts of bases and linkages in seq

    >>> seq_d = "-Gdo-Gdo-Ado-Ado-Ud"
    >>> counts_d = count_seq(seq_d)
    >>> sorted(counts_d.items())
    [('-', 5), ('A', 2), ('G', 2), ('U', 1), ('d', 5), ('o', 4)]

    >>> seq_r = "-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> counts_r = count_seq(seq_r)
    >>> sorted(counts_r.items())
    [('-', 7), ('C', 1), ('G', 2), ('U', 4), ('o', 6), ('r', 7)]
    """

    seq_counts = {}
    for char in seq:
        seq_counts.setdefault(char, 0)
        seq_counts[char] += 1

    return seq_counts


def count_seq_preserve(seq):
    """ Returns dict of base counts preserving RNA/DNA and modifier

    >>> seq_d = "-Gdo-Gdo-Ado-Ado-Ud"
    >>> counts_d = count_seq_preserve(seq_d)
    >>> sorted(counts_d.items())
    [('-Ad', 2), ('-Gd', 2), ('-Ud', 1), ('o', 4)]

    >>> seq_r = "-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> counts_r = count_seq_preserve(seq_r)
    >>> sorted(counts_r.items())
    [('-Cr', 1), ('-Gr', 2), ('-Ur', 4), ('o', 6)]

    >>> seq_combo = "-Gdo-Gdo-Ado-Ado-Udo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> counts_combo = count_seq_preserve(seq_combo)
    >>> sorted(counts_combo.items())
    [('-Ad', 2), ('-Cr', 1), ('-Gd', 2), ('-Gr', 2), ('-Ud', 1), ('-Ur', 4), ('o', 11)]

    """
    # would want to validate sequence first.
    seq_counts = {}
    bases = seq.split('o')

    seq_counts['o'] = len(bases) - 1

    for base in bases:
        seq_counts.setdefault(base, 0)
        seq_counts[base] += 1

    return seq_counts


def get_mass(seq):
    """Returns total mass of a sequence

    >>> seq_d = "-Gdo-Gd"
    >>> get_mass(seq_d)
    7

    >>> seq_r = "-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> get_mass(seq_r)
    41.5

    >>> seq_combo = "-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> get_mass(seq_combo)
    61.5
    """

    counts = count_seq_preserve(seq)
    mass = 0
    for item in counts.iteritems():
        base, count = item
        base_mass = ALT_BASE_MASSES[base] * count
        mass += base_mass
    return mass


def _old_get_mass(seq):
    """Returns total mass of a sequence
    >>> seq_d = "-Gdo"
    >>> _old_get_mass(seq_d)
    4
    """

    counts = count_seq(seq)
    mass = 0
    for item in counts.iteritems():
        base, count = item
        base_mass = BASE_MASSES[base] * count
        mass += base_mass
    return mass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
