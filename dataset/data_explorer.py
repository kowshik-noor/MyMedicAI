# printing out each file name as well as its header
# so that i can figure out the vertices, edges, and attributes
import os

output_folder = './processed_data'

for root, dirs, files in os.walk(output_folder):
    # go through the files in the output folder
    for fi in files:
        filepath = os.path.join(root, fi)
        with open(filepath, encoding="iso-8859-1") as data_file:
            # print filename, header and 1st row of data
            print(fi)
            print(data_file.readline(), data_file.readline())
