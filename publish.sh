#!/bin/sh -e

#echo "test once again"
#./test.sh

python3 -m pip install --upgrade twine

python3 -m twine check dist/*

python3 -m twine upload dist/*
