#!/bin/bash
rm -rf scf release
mkdir scf && mkdir release
cp -r conf server index.py README.md ./scf
pip3 install -r requirements.txt -t ./scf
cd scf
zip -r ../release/lit-ncov-scf-`date +%Y%m%d`.zip ./*