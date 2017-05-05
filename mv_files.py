#!/usr/bin/python
# Lucas Le Lann
# 05/02/2017

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

transmart_file = open("transmart_files_17_03_2017.csv","r") 
error_file = open("not_in_transmart_files.csv","a") 
dict_class={}
for files in glob.glob(".\\PHASE\\*.txt"):
	for line in open(files,'r'):
		#print line
		class_tmp=str(files).replace(".txt","")
		patient_class=class_tmp.split("\\")[2]
		ligne=line.split(";")
		#print str(files)
		patient_ID=ligne[0]
		patient_disease=ligne[1]
	
		dict_class[patient_ID]=patient_class


list_patient=dict_class.keys()
#print list_patient[1]
for CENTER in os.listdir(".\\UNCLASSIFIED\\"):
	for patient in os.listdir(".\\UNCLASSIFIED\\" + CENTER):
		#list_patient=dict_class.keys()
		#list_class=transmart_file[1]
		fold_patient=".\\UNCLASSIFIED\\" + CENTER+"\\"+patient
		if patient in list_patient:
			print patient
			patient_class=dict_class[patient]
			if patient_class == "PHASE_I":
				patient_path="PHASE_I"
			elif patient_class == "PHASE_II":
				patient_path="PHASE_II"
			elif "INCEPTION" in patient_class :
				if "M0" in patient_class :
					patient_path="INCEPTION\\M0"
				elif "M6" in patient_class :
					patient_path="INCEPTION\\M6"
				elif "M12" in patient_class :
					patient_path="INCEPTION\\M12"
				else:
					print "error in INCEPTION"
			else:
				print "error "
			#print fold_patient
			path=".\\CLASSIFIED\\"+patient_path+"\\"+ CENTER +"_"+patient
			#print path
			#print fold_patient
			shutil.copytree(fold_patient, path)
		else:
			print "patient not working " + patient