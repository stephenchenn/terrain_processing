from osgeo import gdal, osr
import os

for filename in os.listdir('oriented_files'):
    # , gdal.GA_Update
    dataset = gdal.Open(os.path.join("oriented_files", filename))

    tileindex = (filename.split("-")[-1]).split(".")[-2]

    file_name = "ortho_TasNetworks_Tile-" + tileindex + ".pgw"

    try:
        with open(os.path.join("pgws", file_name)) as f:
            lines = f.readlines()
            geotransform = tuple(map(float, lines))
            geotransform = ([geotransform[4], geotransform[0], geotransform[1],geotransform[5], geotransform[2], geotransform[3]])
            dataset.SetGeoTransform(geotransform)

            # Define the CRS using an EPSG code (e.g., EPSG:4326 for WGS84)
            crs = osr.SpatialReference()
            crs.ImportFromEPSG(28355)

            # Set the CRS of the dataset
            dataset.SetProjection(crs.ExportToWkt())
        
        # os.remove(os.path.join("pgws", file_name))

    except FileNotFoundError as e:
        print("skipping: " + file_name)