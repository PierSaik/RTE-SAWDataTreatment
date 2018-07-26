# -*- coding: utf-8 -*-

# Copyright (c) 2016, Pierre Saikaly  (saikalypierre@gmail.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

#===========================#
# created on 05 july 2018
#===========================#

# Import Python dependencies :
#----------------------------
import time
from datetime import datetime, date, time
import os
import csv
import numpy as np

# Import Python visualisation dependencies :
# -----------------------------------------
import matplotlib.pyplot as plt

def Avg10Minute(Sensx_Data):
	"""
		Make an average on SenseorData for every point inbetween 10 minutes steps
		Input :
			- SensData : Senseor data define as (Date, temperature)
		Output :
			- SensDataAvg : Senseor data averaged with 10 minutes steps
		Used in : Main
	"""
	
	

def SensSort(Sensx_DataRaw):
	"""
		Sort raw SenseorData based on their index. 
		Input :
			- SensData_Raw : Senseor data coming from csv file define as (Date, temperature)
		Output :
			- One 
		Used in : Main
	"""	


def main():

	Sens0_DataRaw = [0,0,0,0,0]
	Sens1_DataRaw = [0,0,0,0,0]
	Sens2_DataRaw = [0,0,0,0,0]
	i = 0
	Sens0_DataRaw_np = np.zeros(shape=(0,2))
	Sens1_DataRaw_np = np.zeros(shape=(0,2))
	Sens2_DataRaw_np = np.zeros(shape=(0,2))
	
	with open('2017-11_000000177_measures.csv', newline='') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader, None) # skip header
		for row in reader:
			i = i+1
			print(i) 
			if not row[0].startswith('#'): # skip comments
				if row[3] == '0':
					print('yeah0')
					Sens0_DataRaw_np = np.vstack((Sens0_DataRaw_np, [np.datetime64(datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")), float(row[4])]))
				if row[3] == '1':
					print('yeah1')
					Sens1_DataRaw_np = np.vstack((Sens1_DataRaw_np, [np.datetime64(datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")), float(row[4])]))
				if row[3] == '2':
					print('yeah2')
					Sens2_DataRaw_np = np.vstack((Sens2_DataRaw_np, [np.datetime64(datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")), float(row[4])]))
	#print(Sens0_DataRaw)
	#print(Sens1_DataRaw)
	#print(Sens2_DataRaw)
	print(Sens0_DataRaw_np[0,0])
	date_start = np.datetime64(Sens0_DataRaw_np[0,0],'D')
	date_end   = np.datetime64(Sens0_DataRaw_np[end,0],'D') + np.timedelta64(1,'D')
	date_cond  = date_start
	while date_cond < date_end:
		date_cond1 = date_cond + np.timedelta64(10,'s')
		B = np.where(date_cond1>Sens0_DataRaw_np[:,0]>date_cond,1,0)
		MOY = Sens0_DataRaw_np[:,1] * np.transpose(B)
		print(MOY)
		date_cond = date_cond + np.timedelta64(10 ,'s')

		
		
	#Sens0_DataRaw_np = np.array(Sens0_DataRaw).astype("float")
	
	#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
	
	#Modif test github

if __name__ == '__main__': 
	main()


