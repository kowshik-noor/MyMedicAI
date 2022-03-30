# all of this so that i can make the dataset smaller when i wrangle it
import os

# specify data folders
data_folder = "./raw_data"
output_folder = "./processed_data"

# make everything 10K lines max
num_lines = 10000

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
        os.mkdir(output_folder)

# go through all the files in the data folder
for root, dirs, files in os.walk(data_folder):
    for fi in files:
        filepath = os.path.join(root, fi)

        # create an output file with the 10K prefix in our output folder
        output_file = open(os.path.join(output_folder,("10K_"+fi)), 'w+')

        # for each datafile
        with open(filepath, encoding='iso-8859-1') as data_file:
            # go through each line in the file until we hit numLines
            try:
                head = [next(data_file) for x in range(num_lines)]
                output_file.writelines(head)
            # copy the whole file if it is less than numLines
            except StopIteration:
                data_file = open(filepath, encoding='iso-8859-1')
                lines = data_file.readlines()
                output_file.writelines(lines)
                output_file.close()

            output_file.close()
