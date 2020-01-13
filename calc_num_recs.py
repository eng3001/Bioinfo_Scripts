#!/bin/python

file1 = "/projects/bgmp/wyatte/Lyme_Lizard/rmadapt_files_Cutadapt/Full_R1_R2/rmadapt_all_sceloporus_R1.fastq"
file2 = "/projects/bgmp/wyatte/Lyme_Lizard/rmadapt_files_Cutadapt/Full_R1_R2/rmadapt_all_sceloporus_R2.fastq"

rec_count1 = 0
rec_count2 = 0

with open(file1) as fh1:
    for line in fh1:
        if line.startswith("@K"):
            rec_count1 = rec_count1 + 1

with open(file2) as fh2:
    for line in fh2:
        if line.startswith("@K"):
            rec_count2 = rec_count2 + 1

print("Total records in R1: ", rec_count1)
print("Total records in R2: ", rec_count2)
