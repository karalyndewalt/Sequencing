"""
Question 2 -
Write a function that converts 4 letter sequences into the shipping label
format.
seq input:
"-Gdo-Gdo-Ado-Ado-Udo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
seq out:
"[GGAAU]GGCUUUU"
"""


def label_fomat(seq):
    """Returns sequence in lable format

    >>> seq = "-Gdo-Gdo-Ado-Ado-Udo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"
    >>> label_fomat(seq)
    '[GGAAU]GGCUUUU'

    """

    out = []
    stack = []
    tokens = seq.split('o')

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

    return "".join(out)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
