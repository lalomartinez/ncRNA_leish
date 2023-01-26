#!/usr/bin/env python
# coding: utf-8

# usage 
# python3 download_data_SRA.py list_of_accession.txt number_of_threads

#example 
# python3 download_data_SRA.py /path/of/files/list_of_accession.txt 6 
#6 is default of fasterq-dump


#this script allows to download data from SRA NCBI 


import os 
import sys 

list_of_data = sys.argv[1]
threads=  sys.argv[2]
name= list_of_data.split("/")
name1=name[-1].split(".")
folder_name= name1[0]
path="/".join(name[:-1])
folder=path+"/"+folder_name

with open(list_of_data, "r") as fp:
    for line in fp:
        aux= line.rstrip() 
        cmd= "prefetch "+ aux +" -O " + folder 
        os.system(cmd)
        nfolder=folder+"/"+aux+"/"+aux+".sra"
        cmd2= "fasterq-dump --split-files " + nfolder + " -O "+ folder+"/"+aux + " -e " + threads   
        os.system(cmd2)
        #print(cmd2)
        cmd3= "gzip " + folder+"/"+aux+"/"+"*.fastq"
        os.system(cmd3)
        cmd4="rm "+ nfolder
        os.system(cmd4)



