import re
import sys


US_PHONE_RE = re.compile(r"""^[ \t]*
                         (?P<parenthesis>\()?
                         [- ]?
                         (?P<area>\d{3})
                         (?(parenthesis)\))
                         [- ]?
                         (?P<local_a>\d{3})
                         [- ]?
                         (?P<local_b>\d{4})
                         [ \t]*$
                         """, re.VERBOSE)

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        line = line.strip()
        if not line:
            continue
        match = US_PHONE_RE.match(line)
        if match:
            print("({0}) {1} {2}".format(match.group("area"),
                match.group("local_a"), match.group("local_b")))
        else:
            print("Invalid U.S. phone number: {0}".format(line))