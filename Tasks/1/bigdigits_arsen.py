#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys


Zero = ["  000  ",
        " 0   0 ",
        "0     0",
        "0     0",
        "0     0",
        " 0   0 ",
        "  000  "]
One = [" 1 ", "11 ", " 1 ", " 1 ", " 1 ", " 1 ", "111"]
Two = [" 222 ", "2   2", "2  2 ", "  2  ", " 2   ", "2    ", "22222"]
Three = [" 333 ", "3   3", "    3", "  3 ", "    3", "3   3", " 333 "]
Four = ["   4  ", "  44  ", " 4 4  ", "4  4  ", "444444", "   4  ",
        "   4  "]
Five = ["55555", "5    ", "5    ", " 555 ", "    5", "5   5", " 555 "]
Six = [" 666 ", "6    ", "6    ", "6666 ", "6   6", "6   6", " 666 "]
Seven = ["77777", "    7", "   7 ", "  7  ", " 7   ", "7    ", "7    "]
Eight = [" 888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", " 888 "]
Nine = [" 9999", "9   9", "9   9", " 9999", "    9", "    9", "    9"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
