#!/bin/bash

# Clone the files from github
sudo apt-get remove -y --purge man-db
sudo apt update
sudo apt install git -y
git clone https://github.com/stephenchenn/terrain_processing.git

# GDAL
# Update the package list
sudo apt-get update
# Install GDAL
sudo apt-get install gdal-bin -y

# PYTHON CLIENT FOR GOOGLE CLOUD STORAGE API
# Install Python3 pip
sudo apt install python3-pip -y
# Install Google Cloud SDK
pip install google.cloud
# Install Google Cloud Storage library
pip install google-cloud-storage