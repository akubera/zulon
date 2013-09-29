# -*- coding: utf-8 -*-
#
# src/lexer.py
#
# The lexer script for zulon
#
#  Author : Andrew Kubera
# Created : 9/28/2013
#

from plex import *

letter = Range("AZaz")
digit = Range("09")

ident = letter + Rep1(digit | letter)
command = Str("\\") + ident
comment = Str("%")

lexicon = Lexicon([
    (comment, Begin('COMMENT')),
    (command, "_T_COMMAND"),
    (ident, "Identifier"),
    (Str("Perl"),        "the_other_language"),
    (Str("rocks"),       "is_excellent"),
    (Str("sucks"),       "is_differently_good"),
    (Rep1(Any(" \t\n")), IGNORE),
    (Rep1(Any("''")), IGNORE),
    State('COMMENT', [
        (Eol, Begin('')),
        (AnyChar,   IGNORE)
    ])
])


def ParseFile(filename):
  print "Parsing File: ", filename
  f = open(filename, "r")
  scanner = Scanner(lexicon, f, filename)

  while 1:
    token = scanner.read()
    print token
    if token[0] is None:
        break