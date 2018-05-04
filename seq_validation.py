"""
 Write a function that validates an arbitrary input sequence against the
 definition and constraints.

 Given more time I would have written two functions -
 1) validate(seq)
    calls _val_seq
    use error code returned to construct message

 2) _val_seq(seq)
    returns tuple (error/passcode, (position, char))

 """

MODIFIERS = {"-", "m", "b", "d"}

BASES = {"A", "G", "C", "T", "U", "R",
         "Y", "S", "W", "K", "M", "B",
         "D", "H", "V", "N",}

SUGARS = {"d", "r", "e", "m", "y", "l", "k", "o"}

LINKAGES = {"o", "s",}


def validate(seq):
    """Returns validity of seq, with helpful errors

    >>> seq = "-Gdo-Gdo-Ado-Ado-Udo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"

    >>> validate(seq)
    'Validation complete, no errors found.'

    >>> validate("-Gdo-Gdx")
    'Error: Valid sequence must end in SUGAR.'

    >>> validate("xGdo-Gd")
    'Error at seq pos: 0, x not a valid MODIFIER.'

    >>> validate("-Xdo-Gd")
    'Error at seq pos: 1, X not a valid BASE.'

    >>> validate("-Gdx-Gd")
    'Error at seq pos: 3, x not a valid LINKAGE.'

    """

    look_ups = {0: MODIFIERS, 1: BASES, 2: SUGARS, 3: LINKAGES}
    str_constr = {0: "MODIFIER", 1: "BASE", 2: "SUGAR", 3: "LINKAGE"}

    if seq[-1] not in look_ups[2]:
        return "Error: Valid sequence must end in SUGAR."

    for pos, char in enumerate(seq):
        pos_count = pos%4
        char = pos[1]
        if char not in look_ups[pos_count]:
            msg = "Error at seq pos: {pos}, {char} not a valid {constr}."
            return msg.format(pos=pos, char=char, constr=str_constr[pos_count])
        # move counter
        # pos_count = 0 if (pos_count >= 3) else (pos_count + 1)

    return  "Validation complete, no errors found."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
