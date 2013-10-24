#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil


FAKE = False #or True  # only messages, no real changes
HOME_DIR = os.path.expanduser('~')
ROOT = os.path.dirname(os.path.abspath(__file__))
HOME_CFGS = os.path.join(ROOT, 'home')
LINKS = json.load(open(os.path.join(ROOT, 'symlinks.json')))


def main():
    print '=== make symlinks%s:' % ' (FAKE mode)' if FAKE else ''

    home_links = LINKS.get('home', {}).get('links', [])
    for path in home_links:
        link = os.path.join(HOME_DIR, path)
        target = os.path.join(HOME_CFGS, path)
        assert os.path.exists(target), 'config not found: %s' % target
        if not os.path.exists(link):
            symlink(link, target)
        elif os.path.islink(link):
            realpath = os.path.realpath(link)
            if realpath == target:
                print '. symlink already exists:', link
            else:
                print
                print '! wrong symlink:', link
                print '!    expected =>', target
                print '!         got =>', realpath
                if query_yes_no('? fix it?'):
                    unlink(link)
                    symlink(link, target)
        elif os.path.isfile(link):
            print
            print '! found file instead symlink:', link
            if query_yes_no('? fix it?'):
                unlink(link)
                symlink(link, target)
        elif os.path.isdir(link):
            print
            print '! found dir instead symlink:', link
            if query_yes_no('? fix it?'):
                rmtree(link)
                symlink(link, target)


def unlink(path):
    print '- unlink:      ', path
    if not FAKE:
        os.unlink(path)


def rmtree(path):
    print '- remove dir:', path
    if not FAKE:
        shutil.rmtree(path)


def symlink(link, target):
    print '+ make symlink:', link
    if not FAKE:
        dirname = os.path.dirname(link)
        try:
            os.makedirs(dirname)
            print '+ mkdir:', dirname
        except OSError:
            pass
        os.symlink(target, link)


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

if __name__ == "__main__":
    main()
