#!/bin/python
import os

R1_file = "/projects/bgmp/wyatte/BioBE/shotgun_seq_data/R1_file_names.txt"
R2_file = "/projects/bgmp/wyatte/BioBE/shotgun_seq_data/R2_file_names.txt"

R1_list = []
R2_list = []

with open(R1_file) as R1_fn:
    for line in R1_fn:
        line = line.strip()
        R1_list.append(line)

with open(R2_file) as R2_fn:
    for line in R2_fn:
        line = line.strip()
        R2_list.append(line)

num_files = len(R1_list)
i = 0

os.chdir("/projects/bgmp/wyatte/software/fastq-pair/build")
print(os.getcwd())

while i < num_files:
    path = "/projects/bgmp/wyatte/BioBE/shotgun_seq_data/"
    file_R1 = path + R1_list.pop()
    file_R2 = path + R2_list.pop()
    fastq_pair_commant = "./fastq_pair " + file_R1 + " " + file_R2
    os.system(fastq_pair_commant)
    i = i + 1
