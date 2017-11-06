import re

# typical email address
"""
    asdf@coli.uni-saarland.de
    240jaw049gj09a@gmail.com
"""
# .*@.*..*

# prices
"""
    $99.99
    $148.04
    $0.12
    $99
"""
# .?\d*.?\d{0,2}
# \$([0-9]+)(\.[0-9]{2})

# years between 1984 and 2009
# start from: [12][0-9][0-9][0-9]
# [1][9][8][5-9]|[1][9][9][0-9]|[2][0][0][0-8]

if __name__ == "__main__":
    with open("../Files/goldbug.txt") as input_file:
        for line in input_file:
            # '.*(\')+'
            m = re.search('.*[w|W]ell.*', line)

            if m:
                print(m)
