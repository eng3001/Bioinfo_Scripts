#!/bin/python

#SUMMARY: Script checks the bitwise flag of the STAR aligned reads to decide

# if a library is stranded or not.

import argparse

#defining the arguments to the python script
def get_args():
	parser = argparse.ArgumentParser(description="count up the number of reads \
    that are properly mapped to the reference genome and the number of reads \
    that are not mapped to the genome")
	parser.add_argument("-f", "--file", help="File name", type=str)
	return parser.parse_args()

args = get_args()

FILE = args.file

line_array = []
QName_dict = {}
reverse = 0
forward = 0
num_reads = 0
unmapped = 0
mapped = 0

with open(FILE,"r") as fh:
    for line in fh:
        if not line.startswith("@"): #Test if liine doesnt start '@' enter if statement
            line_array = line.split()
            qName = line_array[0]
            flag = int(line_array[1])
            num_reads += 1
            if ((flag & 4) == 4):
                unmapped += 1
            elif ((flag & 16) == 16): #Checks if sequence is being reverse complemented
                reverse += 1
                mapped += 1
            else:
                forward += 1
                mapped += 1

print("Number of forward reads:", forward)
print("Number of reverse reads:", reverse)
print("Number of unmapped reads:", unmapped)
print("Number of total reads:", num_reads)
print("Number of mapped reads:", mapped)
print("Percent of forward reads:", ((forward/mapped)*100))
print("Percent of reverse reads:", ((reverse/mapped)*100))


# If the counts of forward or reverse is significantly higher than another
# then the library is stranded. If they are relatively the same amount, the
# library is unstranded.
