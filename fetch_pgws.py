from google.cloud import storage
from google.cloud.exceptions import NotFound
import os
import logging

# Set up the logging configuration
logging.basicConfig(filename='error_logs/pgw_not_found.log', level=logging.ERROR)

client = storage.Client()
bucket_name = 'eq-c2rw-research'

bucket = client.get_bucket(bucket_name)

directory_path = "TasNetworksProcessedFiles/Ortho/RGB/Orthophoto"
destination_folder = 'pgws'

for filename in os.listdir('oriented_files'):
    tileindex = (filename.split("-")[-1]).split(".")[-2]
    file_name = "ortho_TasNetworks_Tile-" + tileindex + ".pgw"

    blob = bucket.blob(os.path.join(directory_path,file_name))
    des_file = os.path.join(destination_folder,file_name)
    try:
        with open(des_file, 'wb') as file_obj:
            blob.download_to_file(file_obj)
        print(os.path.basename(blob.name) + ' downloaded successfully.')
    except NotFound:
        logging.error("File not found: %s", file_name)
        os.remove(des_file)
        os.remove(os.path.join("oriented_files",filename))