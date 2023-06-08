#!/bin/bash

# prepare directories
mkdir -p pgws oriented_files raw_files

# fetch terrain files
python3 fetch_terrain.py

# fix orientation (rotate by 90 degrees clockwise and flip horizontally)
python3 rotate.py

# generate pgws
python3 generate_pgw.py

# generate tif.aux.xml files from pgws
python3 geotransform_terrain.py

# compress result
zip -r processed.zip oriented_files/