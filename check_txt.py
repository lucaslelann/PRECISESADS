#!/usr/bin/python
# Lucas Le Lann
# 25/01/2016

from collections import defaultdict
import os.path
import glob, os
import sys
import csv
import shutil
from datetime import timedelta, datetime
os.remove("list_todo.txt") 
os.remove("list_partialydone.txt") 
os.remove("list_done.txt") 

zero= open("list_todo.txt","w") 
one = open("list_partialydone.txt","w") 
two = open("list_done.txt","w") 
for CENTER in os.listdir(".\\FCS_FILES\\"):
	#print CENTER
	zero.write(CENTER+";\n")
	one.write(CENTER+";\n")
	two.write(CENTER+";\n")
	for patient in os.listdir(".\\FCS_FILES\\" + CENTER):
		files= glob.glob(".\FCS_FILES\\" + CENTER + "\\"+patient+"\\*.txt" )
		number_files = len(files)
		print number_files
		if number_files == 0:
			print patient
			zero.write(patient+";\n")
		elif number_files == 1:
			print patient
			one.write(patient+";\n")
		elif number_files == 2:
			print patient
			two.write(patient+";\n")
		else:
			print "NOT OK"
