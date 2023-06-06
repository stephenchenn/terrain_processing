import numpy as np
from osgeo import gdal
import os

def rotate_flip_dem_image(input_path, output_path, clockwise=True, flip_horizontal=False):
    # Open the DEM image using GDAL
    dataset = gdal.Open(input_path, gdal.GA_ReadOnly)
    
    # Read the image data and convert it into a NumPy array
    image_data = dataset.ReadAsArray()
    
    # Rotate the array by 90 degrees
    rotation_direction = -1 if clockwise else 1
    rotated_data = np.rot90(image_data, k=rotation_direction)
    
    # Flip the array horizontally if specified
    if flip_horizontal:
        rotated_data = np.fliplr(rotated_data)
    
    # Create an output dataset with the rotated and flipped data
    driver = dataset.GetDriver()
    output_dataset = driver.CreateCopy(output_path, dataset)
    output_dataset.GetRasterBand(1).WriteArray(rotated_data)
    output_dataset.FlushCache()
    
    # Close the datasets
    dataset = None
    output_dataset = None

for file_name in os.listdir('raw_files'):
    input_path = os.path.join('raw_files', file_name)
    output_path = os.path.join('oriented_files', file_name)
    rotate_flip_dem_image(input_path, output_path, clockwise=True, flip_horizontal=True)
    os.remove(input_path)