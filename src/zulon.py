# -*- coding: utf-8 -*-
#
# src/zulon.py
#
# The main file for the zulon program
#
#  Author : Andrew Kubera
# Created : 9/28/2013
#

import sys, getopt
import about
import lexer

def usage():
  print "usage:\t%s [options] args" % (about.name)
  print "Options:"
  for o in prog_options:
    h = ("-%s, " % (o[0]) if (o[0] and not o[3]) else ("-%s arg, " % (o[0]) if o[3] else " "),
         "--%s" % (o[1]) if o[1] else " ",
         o[2]
        )
    print "   %s%s\t%s" % h

def print_version():
  print "%s: %s" % (about.name, about.version)

def do_g(arg):
  print "G",arg
  
def do_a():
  print "A"

def main(argv):
  
  shorts  = "".join([("%s:" if x[3] else "%s") % x[0] for x in prog_options])
  longs   = [x[1] for x in prog_options if x[1]]

  try:
    opts, args = getopt.getopt(argv, shorts, longs)
  except getopt.GetoptError:
    print "Usage Error"
    print argv
    print shorts
    print longs
    usage()
    sys.exit(2)                     

  
  func_map = [ (("-%s" % po[0] if po[0] else '', "--%s" % po[1] if po[1] else ''), po[4])
                    for po in prog_options]

  # loop through all arguments and call the functions in func_map
  for opt, arg in opts:
    for func in func_map:
      if opt in func[0]:
        #print "calling",func[1]
        
        try:
          func[1]() if arg == '' else func[1](arg)
        except:
          try:
            func[3]()
          except IndexError:
            print "Error!"
            usage()
            sys.exit(2)


#
# Short name, long name, Description, accepts argument, function handle
#
prog_options = [ ("h", "help", "Display this information", False, usage),
                 ("a", "A", "just a test", True, lexer.ParseFile),
                 ("g", "", "just g test", True, do_g),
                 ("v", "version", "Print the program's version number", False, print_version)
               ]


if __name__ == "__main__":
  # call the main function
  main(sys.argv[1:])




