#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of Probeurre.
"""
from argparse import ArgumentParser
from tqdm import tqdm
import server
import os

# Argument parsing
parser = ArgumentParser(
    description="shows statistics about analyzed comments.")
parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")
parser.add_argument("-d", "--directory", help="directory to read analyses from")
args = parser.parse_args()

relativeWorkingDir = args.directory if args.directory else 'repos'
workingDir = os.path.join(os.getcwd(), relativeWorkingDir)
repos = args.repo

server.run("127.0.0.1", 5555, downloaded=repos)