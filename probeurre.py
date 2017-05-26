#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of Probeurre.
"""
from argparse import ArgumentParser
from tqdm import tqdm
import server
import os
import json
from pprint import pprint

# Argument parsing
parser = ArgumentParser(
    description="shows statistics about analyzed comments.")
parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")
parser.add_argument("-d", "--directory", help="directory to read analyses from")
parser.add_argument("-w", "--workdir", help="working directory relatively to the expected docker image")
parser.add_argument("-e", "--extracted", help="extracted file path")
parser.add_argument("-a", "--analyzed", help="analyzed file path")
args = parser.parse_args()

workdir = args.workdir if args.workdir else '1'
extractedPath = os.path.join('/probeurre-data', workdir, 'extracted.json')
analyzedPath = os.path.join('/probeurre-data', workdir, 'analyzed.json')

if args.extracted:
    extractedPath = args.extracted

if args.analyzed:
    analyzedPath = os.path.join(os.getcwd(), args.analyzed)

with open(analyzedPath, encoding="utf8") as analyzedFile:
    dataAnalyzed = json.load(analyzedFile)

with open(extractedPath, encoding="utf8") as extractedFile:
    dataExtracted = json.load(extractedFile)


todos = 0
for key in dataAnalyzed:
    file = dataAnalyzed[key]
    if (len(file.keys()) > 0):
        todos += len(file.keys())

comments = 0
for key in dataExtracted:
    file = dataExtracted[key]
    if (len(file.keys()) > 0):
        comments += len(file.keys())

print(str(comments) + " comment lines")
print(str(todos) + " TODOs found")


repos = None

server.run("127.0.0.1", 5555, analyzed={}, extracted={}, nbAnalyzed=todos, nbExtracted=comments)