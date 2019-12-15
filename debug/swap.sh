#! /bin/bash

echo "Swapping pywren/executor.py with arg1: $1"
LIB_PATH="$(python3 -c "import pywren.executor as _; print(_.__file__)")"
cp "$1" $LIB_PATH