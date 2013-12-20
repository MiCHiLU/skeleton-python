#!/usr/bin/env python
# -*- coding: utf-8 -*-

from doctest import testmod
import sys

import sample

if testmod(sample).failed:
  sys.exit(1)
