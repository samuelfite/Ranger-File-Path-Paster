#!/bin/bash
cp -f ./config/commands.py      ~/.config/ranger/commands.py
cp -f ./container/directory.py  /usr/local/lib/python2.7/dist-packages/ranger/container/directory.py
cp -f ./core/fm.py              /usr/local/lib/python2.7/dist-packages/ranger/core/fm.py
cp -f ./core/loader.py          /usr/local/lib/python2.7/dist-packages/ranger/core/loader.py

