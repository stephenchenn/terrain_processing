from google.cloud import storage
import os

# Create a client object for interacting with the storage API
client = storage.Client()

# Specify the name of the bucket
bucket_name = "eq-c2rw-research"

# Specify the path of the directory within the bucket
directory_path = "TasNetworksProcessedFiles/DEM/DTM"

# Get a reference to the bucket and the directory within it
bucket = client.get_bucket(bucket_name)
blobs = bucket.list_blobs(prefix=directory_path)

files = ['TasNetworks_Tile-523000_5252500.tif','TasNetworks_Tile-523000_5253000.tif','TasNetworks_Tile-523000_5253500.tif','TasNetworks_Tile-523500_5252500.tif','TasNetworks_Tile-523500_5253000.tif','TasNetworks_Tile-523500_5253500.tif','TasNetworks_Tile-524000_5252500.tif','TasNetworks_Tile-524000_5253000.tif','TasNetworks_Tile-524000_5253500.tif','TasNetworks_Tile-524500_5252500.tif','TasNetworks_Tile-524500_5253000.tif','TasNetworks_Tile-524500_5253500.tif']

# create folder
folder_name = 'raw_files'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for file in files:
    blob = bucket.blob(os.path.join(directory_path,file))

    file_name = os.path.join(folder_name, os.path.basename(blob.name))

    # Download the blob's content and save it to a file
    with open(file_name, 'wb') as file_obj:
        blob.download_to_file(file_obj)

    print(os.path.basename(blob.name) + ' downloaded successfully.')