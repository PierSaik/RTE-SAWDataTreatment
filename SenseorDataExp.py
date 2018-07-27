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
import argparse

# Import Python visualisation dependencies :
# -----------------------------------------
import matplotlib.pyplot as plt

def AvgXSeconds(Sensx_Data, time_parameter):
	"""
		Make an average on SenseorData for every point inbetween steps
		Input :
			- Sensx_Data : Senseor data define as (timestamp, temperature)
		Output :
			- Sens_DataAvg_np : Senseor data averaged
		Used in : Main
	"""
	# Local Variables :
	# -----------------
	day = 86400
	Sens_DataAvg_np = np.zeros(shape=(0,2))
	date_start = (Sensx_Data[0,0] // day) * day
	date_end   = ((Sensx_Data[len(Sensx_Data)-1,0] // day + 1)) * day
	date_cond  = date_start
	# print("date_cond = ", date_cond)
	# print("premiere_date = ", (Sensx_Data[0,0])
	# print((Sensx_Data[0,0] - date_cond)

	while date_cond < date_end:
		temp_values = np.where(Sensx_Data[:,0]//time_parameter == date_cond//time_parameter ) 
		#print(temp_values)
		temp_avg    = np.average(Sensx_Data[temp_values,1])
		#print(temp_avg)
		if temp_avg == temp_avg:
			Sens_DataAvg_np = np.vstack((Sens_DataAvg_np, [date_cond,temp_avg]))
		date_cond  += time_parameter
	
	return Sens_DataAvg_np

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

def main(time_parameter):
	# Local variables :
	# -----------------
	i = 0
	Sens0_np = np.zeros(shape=(0,2))
	Sens1_np = np.zeros(shape=(0,2))
	Sens2_np = np.zeros(shape=(0,2))
	Sens0_DataAvg_np = np.zeros(shape=(0,2))
	Sens1_DataAvg_np = np.zeros(shape=(0,2))
	Sens2_DataAvg_np = np.zeros(shape=(0,2))

	# Extracting SENSeOR Data from CSV file :
	# ---------------------------------------
	for file_csv in glob.glob('*.csv'):
		[Sens0_out, Sens1_out, Sens2_out] = SensSort(file_csv)
		Sens0_np = np.vstack((Sens0_np, Sens0_out))
		Sens1_np = np.vstack((Sens1_np, Sens1_out))
		Sens2_np = np.vstack((Sens2_np, Sens2_out))
	print(Sens0_np)

	# Averaging SENSeOR Data according to timestamp :
	# -----------------------------------------------
	Sens0_DataAvg_np = AvgXSeconds(Sens0_np, time_parameter)

	Datets = []
	for i in range(0,len(Sens0_DataAvg_np)):
		Datets = Datets + [(datetime.fromtimestamp(Sens0_DataAvg_np[i,0]).strftime('%Y-%m-%d %H:%M:%S'))]

	plt.plot(Datets,Sens0_DataAvg_np[:,1])
	plt.show()

if __name__ == '__main__': 
	
	parser = argparse.ArgumentParser(description='Compute and plot SENSeOR SAW sensor data and averages it on demand. To run the program, you have to be where the .csv of SENSeOR are located')
	parser.add_argument('-t','--time_parameter', help='select time parameter',
			 required=True)
	args = parser.parse_args()

	main(int(args.time_parameter))



