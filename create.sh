#!/bin/bash

d="upmemsdk-0.1.0 upmemsdk.egg-info dist build"

for f in $d; do 
   if [ -d "$f" ]; then
      rm -rf $f
      echo "Removed $f"
   fi
done
python setup.py sdist bdist_wheel



