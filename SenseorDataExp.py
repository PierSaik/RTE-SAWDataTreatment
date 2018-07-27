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
import sys
import glob
import csv
import numpy as np
import math

# Import Python visualisation dependencies :
# -----------------------------------------
import matplotlib.pyplot as plt

def AvgXSeconds(Sensx_Data, seconds_add):
	"""
		Make an average on SenseorData for every point inbetween steps
		Input :
			- SensData : Senseor data define as (timestamp, temperature)
		Output :
			- SensDataAvg : Senseor data averaged
		Used in : Main
	"""
	
	

def SensSort(csvfile):
	"""
		Sort raw SenseorData based on their index. 
		Input :
			- Sensx_DataRaw_np : Outputs
			- SensData_Raw : Senseor data coming from csv file define as (timestamp, temperature)
		Output :
			- None
		Used in : Main
	"""
	# Local variables :
	# -----------------
	i = 0
	Sens0_DataRaw_np = np.zeros(shape=(0,2))
	Sens1_DataRaw_np = np.zeros(shape=(0,2))
	Sens2_DataRaw_np = np.zeros(shape=(0,2))

	with open(csvfile, newline='') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader, None) # skip header
		for row in reader:
			i = i+1
			print(i) 
			if not row[0].startswith('#'): # skip comments
				if row[3] == '0':
					print('yeah0')
					Sens0_DataRaw_np = np.vstack((Sens0_DataRaw_np, [float(row[0]), float(row[4])]))
				if row[3] == '1':
					print('yeah1')
					Sens1_DataRaw_np = np.vstack((Sens1_DataRaw_np, [float(row[0]), float(row[4])]))
				if row[3] == '2':
					print('yeah2')
					Sens2_DataRaw_np = np.vstack((Sens2_DataRaw_np, [float(row[0]), float(row[4])]))

	return Sens0_DataRaw_np, Sens1_DataRaw_np, Sens2_DataRaw_np				

def main():

	i = 0
	Sens0_np = np.zeros(shape=(0,2))
	Sens1_np = np.zeros(shape=(0,2))
	Sens2_np = np.zeros(shape=(0,2))
	
	for file_csv in glob.glob('*.csv'):
		[Sens0_out, Sens1_out, Sens2_out] = SensSort(file_csv)
		Sens0_np = np.vstack((Sens0_np, Sens0_out))
		Sens1_np = np.vstack((Sens1_np, Sens1_out))
		Sens2_np = np.vstack((Sens2_np, Sens2_out))
	print(Sens0_np)

	day = 86400
	time_parameter  = 600
	Sens0_DataAvg_np = np.zeros(shape=(0,2))
	date_start = (Sens0_np[0,0] // day) * day
	date_end   = (Sens0_np[len(Sens0_np)-1,0] // day + 1) *day
	date_cond  = date_start
	print("date_cond = ", date_cond)
	print("premiere_date = ", Sens0_np[0,0])
	print(Sens0_np[0,0] - date_cond)


	while date_cond < date_end:
		temp_values = np.where(Sens0_np[:,0]//time_parameter == date_cond//time_parameter ) 
		#print(temp_values)
		temp_avg    = np.average(Sens0_np[temp_values,1])
		#print(temp_avg)
		if temp_avg == temp_avg:
			Sens0_DataAvg_np = np.vstack((Sens0_DataAvg_np, [date_cond,temp_avg]))
		date_cond  += time_parameter


	Datets = []
	for i in range(0,len(Sens0_DataAvg_np)):
		Datets = Datets + [(datetime.fromtimestamp(Sens0_DataAvg_np[i,0]).strftime('%Y-%m-%d %H:%M:%S'))]

	plt.plot(Datets,Sens0_DataAvg_np[:,1])
	plt.show()

if __name__ == '__main__': 
	main()


