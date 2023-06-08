import os

for filename in os.listdir('oriented_files'):
    # Extracting the numbers from the file name
    tileindex = (filename.split("-")[-1]).split(".")[-2]
    x = int(tileindex.split("_")[0]) - 0.5
    y = int(tileindex.split("_")[1]) + 500.5

    filename = "ortho_TasNetworks_Tile-" + tileindex + ".pgw"

    # Creating the subdirectory if it doesn't exist
    subdirectory = 'pgws'
    os.makedirs(subdirectory, exist_ok=True)

    # Creating and writing to the pgw file
    pgw_filename = f"{subdirectory}/{filename}"
    with open(pgw_filename, 'w') as pgw_file:
        pgw_file.write("1\n")
        pgw_file.write("0.0\n")
        pgw_file.write("0.0\n")
        pgw_file.write("-1\n")
        pgw_file.write(f"{x}\n")
        pgw_file.write(f"{y}")

    print(f"{filename} created successfully.")