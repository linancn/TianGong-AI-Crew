#!/usr/bin/env python
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from main import train

if __name__ == "__main__":
    train()