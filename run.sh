#!/bin/bash

# prepare directories
mkdir -p pgws oriented_files geotransformed_files error_logs raw_files

# fetch terrain files
python3 fetch_terrain.py

# fix orientation (rotate by 90 degrees clockwise and flip horizontally)
python3 rotate.py

# fetch pgw files
python3 fetch_pgws.py

# correct scaling of pgw files
python3 fix_scaling.py

# generate tif.aux.xml files from pgws
python3 geotransform_terrain.py

# adding tif.aux.xml into tif files
chmod +x translate.sh
./translate.sh

# compress result
zip -r processed.zip geotransformed_files/