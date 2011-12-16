#!/usr/bin/env python
import sys
from optparse import OptionParser

import vobject

import tui

def get_action_list():
    return [x[4:] for x in globals() if x.startswith("act_")]

def act_edit(card):
    while True:
        firstname = card.n.value.given
        lastname = card.n.value.family

        print u"First name: %s, Last name: %s" % (firstname, lastname)
        print ""
        answer = tui.editLine(None, prompt="Edit, Swap, Delete, Validate: (esdV) ").lower()
        if answer == "e":
            firstname = tui.editLine(firstname, prompt="First name: ")
            lastname = tui.editLine(lastname, prompt="Last name: ")
        elif answer == "s":
            firstname, lastname = lastname, firstname
        elif answer == "d":
            return False
        elif answer in ("", "v"):
            return True
        else:
            print "Invalid answer"
            continue

        # We reach this point if a change was made
        card.n.value.given = firstname
        card.n.value.family = lastname
        card.fn.value = "%s %s" % (firstname, lastname)

def act_title(card):
    firstname = card.n.value.given.title()
    lastname = card.n.value.family.title()

    card.fn.value = "%s %s" % (firstname, lastname)
    card.n.value.given = firstname
    card.n.value.family = lastname
    return True

USAGE="""%%prog <action> <in.vcf> <out.vcf>

Where action can be one of: %s
""" % ", ".join(get_action_list())

def main():
    parser = OptionParser(usage=USAGE)

    (options, args) = parser.parse_args()

    if len(args) != 3:
        parser.error("Wrong number of arguments")

    action_name, src, dst = args

    if not action_name in get_action_list():
        parser.error("Unknown action '%s'" % action_name)

    action = eval("act_" + action_name)

    src_file = open(src)
    dst_file = open(dst, "w")

    for card in vobject.readComponents(src_file):
        if not "fn" in card.contents:
            print "no FN in", card, "skipping"
            continue
        keep = action(card)
        if keep:
            dst_file.write(card.serialize())
            dst_file.write("\r\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
