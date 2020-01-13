#!/bin/python
import argparse
import re
import os

#defining the arguments to the python script
def get_args():
	parser = argparse.ArgumentParser(description="group scaffolds into separate \
	files based upon the length of the scaffold")
	parser.add_argument("-f", "--file", help="File name", type=str)
	return parser.parse_args()

args = get_args()

FILE = args.file

Max_Length = 0

with open(FILE,"r") as fh:
    line1 = fh.readline()
    line2 = fh.readline()

    Max_Length = len(line2)

print("Max length: " + str(Max_Length))
Running_Length = 0
first_scaff = 0
num_scaffolds = 0

with open(FILE,"r") as fh:
	while True:
		num_scaffolds = num_scaffolds + 1 # keep track of the number of scaffolds
		header_line = fh.readline() # Read in header line line
		#header_line = header_line.strip() # remove new line character in header line

		if len(header_line) == 0: # Check if header line is blank, if its length is 0 it means eof
			rename_file = first_scaff + "-" + scaffold_num + ".fasta"
			rename_command = "mv temp.fasta " + rename_file
			os.system(rename_command)
			break

		seq_line = fh.readline() # Read in sequence line
		#seq_line = seq_line.strip() # Remove new line character in sequence line

		match_obj_scaffold_val = re.search(">scaffold(\d+)", header_line) # Use regex to extract the scaffold number

		scaffold_num = match_obj_scaffold_val.group(1) # save the scaffold number as a variable

		if Running_Length == 0: # Keep track of the first scaffold number
			first_scaff = scaffold_num

		Running_Length = Running_Length + len(seq_line) # keep track of the running length

		if int(Running_Length) >= int(Max_Length):
			if num_scaffolds == 1:
				num_scaffolds = 0 # Reset the number of scaffolds
				Running_Length = 0 # Reset the running seuqnce length
				out_file_name = scaffold_num + ".fasta"
				f = open(out_file_name, "a")
				f.write(header_line)
				f.write(seq_line)
				f.close()
			else:
				num_scaffolds = 0 # Reset the number of scaffolds
				Running_Length = 0 # Reset the running seuqnce length
				out_file_name = "temp.fasta"
				f = open(out_file_name, "a")
				f.write(header_line)
				f.write(seq_line)
				f.close()
				rename_file = first_scaff + "-" + scaffold_num + ".fasta"
				rename_command = "mv temp.fasta " + rename_file
				os.system(rename_command)
		else:
			num_scaffolds = num_scaffolds + 1
			out_file_name = "temp.fasta"
			f = open(out_file_name, "a")
			f.write(header_line)
			f.write(seq_line)
			f.close()
