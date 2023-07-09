#!/bin/env python3

import shubhlipi as sh

sh.delete_folder("dist")
sh.cmd("python setup.py sdist")
sh.cmd("twine upload dist/*", direct=False)
