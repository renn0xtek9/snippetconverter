#!/bin/bash
rm -rf sdist
python3 setup.py sdist
twine upload --verbose dist/*
