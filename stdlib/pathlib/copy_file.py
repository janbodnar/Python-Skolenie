#!/usr/bin/env python

from pathlib import Path
from shutil import copyfile

source = Path('words.txt')
destination = Path('words_bck.txt')
copyfile(source, destination)

