#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from persistry.Manager import Persistry

p = Persistry(sys.argv[1])
p.analysis()