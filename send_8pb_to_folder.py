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

# FUNCTION

def trad_date(DATE_trad):
	if "JAN" in DATE_trad:
		date0=DATE_trad.replace("JAN","/01/")
	elif "FEB" in DATE_trad:
		date0=DATE_trad.replace("FEB","/02/")
	elif "MAR" in DATE_trad:
		date0=DATE_trad.replace("MAR","/03/")
	elif "APR" in DATE_trad:
		date0=DATE_trad.replace("APR","/04/")
	elif "MAY" in DATE_trad:
		date0=DATE_trad.replace("MAY","/05/")
	elif "JUN" in DATE_trad:
		date0=DATE_trad.replace("JUN","/06/")
	elif "JUL" in DATE_trad:
		date0=DATE_trad.replace("JUL","/07/")
	elif "AUG" in DATE_trad:
		date0=DATE_trad.replace("AUG","/08/")
	elif "SEP" in DATE_trad:
		date0=DATE_trad.replace("SEP","/09/")
	elif "SEPT" in DATE_trad:
		date0=DATE_trad.replace("SEPT","/09/")
	elif "OCT" in DATE_trad:
		date0=DATE_trad.replace("OCT","/10/")
	elif "OKT" in DATE_trad:
		date0=DATE_trad.replace("OKT","/10/")
	elif "NOV" in DATE_trad:
		date0=DATE_trad.replace("NOV","/11/")
	elif "DEC" in DATE_trad:
		date0=DATE_trad.replace("DEC","/12/")
	elif "DIC" in DATE_trad:
		date0=DATE_trad.replace("DIC","/12/")
	else:
		print "ERROR DATE IS NOT IN THE RIGHT FORMAT for " + patient
	return date0




# Creation dict
Dict={}
list_cent=["CHP","DRFZ","FPS","IDIBELL","IRCCS","KUL","MHH","SAS","UBO","UCL","UNIGE",]
for cent in list_cent:
	Dict[cent]=[]
#
for file in os.listdir("..\\Normalization_check_MFI\\REF"):
	#print file
	tools = file.split("_")
	date=tools[0]
	center= tools[1]
	Dict[center].append(date)
#print Dict


# asigne the 8pbvalues to the right patient

for CENTER in os.listdir(".\\FCS_FILES"):
	#print CENTER
	#CENTER = "DRFZ"
	for patient in os.listdir(".\FCS_FILES\\" + CENTER):
		file= glob.glob(".\FCS_FILES\\" + CENTER + "\\"+patient+"\\*" )
		#print [ x for x in file if "Panel" in x ]
		file_split=[ x for x in file if "Panel" in x ][0].split("_")
		#print file[0]
		DATE_raw=file_split[-1]
		#print DATE_raw
		DATE=DATE_raw.split(".")
		DATE=DATE[0]
		#print DATE
		
		#print '..\Normalization_check_MFI\\'+ CENTER+'\\'+DATE+'_'+CENTER+'.txt'
		for filepb in glob.glob('..\Normalization_check_MFI\\'+ CENTER+'\\'+DATE+'_'+CENTER+'.txt'):
			
			path="..\\Normalization_INCEPTION\\FCS_FILES\\" + CENTER + "\\"+patient+"\\"+DATE+'_'+CENTER+'.txt'
			shutil.copy(filepb, path)
		if os.path.isfile(path):
			print "OMG is it ALIVE ?"
			print DATE
			print CENTER
			compared_DATE=DATE.split("\\")[-1]
			print compared_DATE
			date_patient=trad_date(compared_DATE)
			i=0
			for date_ref in Dict[CENTER]:
				#print date_ref+" date_ref"
				tdate_ref=trad_date(date_ref)
				patient_date = datetime.strptime(date_patient, "%d/%m/%Y")
				ref_date = datetime.strptime(tdate_ref, "%d/%m/%Y")
				#print patient_date
				if i==0:
					REF=date_ref 
					ref_date_patient=ref_date
					ref_delta=ref_date-patient_date
					i+=1
				else:
					if ref_date<patient_date:
						new_delta=patient_date - ref_date
						# print "patient "+ str(patient_date)
						# print "ref date "+ str(ref_date)
						# print "new delta "+ str(new_delta)
						if new_delta<ref_delta and ref_date<patient_date:
							REF=date_ref
							refdate2=ref_date
							ref_delta=new_delta
			#print REF
			for filepb in glob.glob('..\Normalization_check_MFI\\REF\\'+REF+'_'+CENTER+'_REF.txt'):
				
				path="..\\Normalization_INCEPTION\\FCS_FILES\\" + CENTER + "\\"+patient+"\\"
				shutil.copy(filepb, path)
