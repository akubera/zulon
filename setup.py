#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import sys, os

try:
    from commands import getstatusoutput
except ImportError:
    from subprocess import getstatusoutput

try:
   from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
   from distutils.command.build_py import build_py

project_name = "zulon"
version = '0.0.1'
license = "MIT"


# this directory
setup_dir = os.path.dirname(os.path.abspath(__file__))

#files = [
#     (os.path.join(prefix, 'src'), [
    
zulon_scripts = ['src/zulon.py']

setup(
  name = project_name,
  license = "MIT",
  version = version,
  description = "My New Project",
  long_description = """
    My project which doesn't actually do anything at this time. Eventually 
    there will be something to run. I hope.""",
  author = 'Andrew Kubera',
  author_email = 'andrewkubera@gmail.com',
  requires = ["plex (>=2.0)"],
  provides = ['zulon'],
  scripts = zulon_scripts
)

