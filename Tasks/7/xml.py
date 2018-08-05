
import os
import re
import sys


TAG_RE = re.compile(r"<(?P<tag>\w+)(?P<attributes>[^>]*?)/?>")

ATTRIBUTE_RE = re.compile(r"""
                    (?!<\w)(?P<name>[-\w]+)=
                    (?P<quote>(?P<single>')|(?P<double>"))?
                    (?P<value>(?(single)[^']+?|(?(double)[^"]+?|\S+)))
                    (?(quote)(?P=quote))
                    """, re.VERBOSE)


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} infile".format(os.path.basename(sys.argv[0])))
        sys.exit(2)

    with open(sys.argv[1], encoding="utf8") as fh:
        xml = fh.read()

    for tag_match in TAG_RE.finditer(xml):
        attributes = tag_match.group("attributes")
        if attributes:
            print("{0}".format(tag_match.group("tag")))
            for attribute_match in ATTRIBUTE_RE.finditer(attributes):
                print("    {0} = {1}".format(
                      attribute_match.group("name"),
                      attribute_match.group("value")))


main()