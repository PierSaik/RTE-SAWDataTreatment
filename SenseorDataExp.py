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
	
	

def SensSort(Sensx_DataRaw):
	"""
		Sort raw SenseorData based on their index. 
		Input :
			- SensData_Raw : Senseor data coming from csv file define as (timestamp, temperature)
		Output :
			- One 
		Used in : Main
	"""	


def main():

	#Sens0_DataRaw = [0,0,0,0,0]
	#Sens1_DataRaw = [0,0,0,0,0]
	#Sens2_DataRaw = [0,0,0,0,0]
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
					Sens0_DataRaw_np = np.vstack((Sens0_DataRaw_np, [float(row[0]), float(row[4])]))
				if row[3] == '1':
					print('yeah1')
					Sens1_DataRaw_np = np.vstack((Sens1_DataRaw_np, [float(row[0]), float(row[4])]))
					#Sens1_DataRaw_np = np.vstack((Sens1_DataRaw_np, [np.datetime64(datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")), float(row[4])]))
				if row[3] == '2':
					print('yeah2')
					Sens2_DataRaw_np = np.vstack((Sens2_DataRaw_np, [float(row[0]), float(row[4])]))
					#Sens2_DataRaw_np = np.vstack((Sens2_DataRaw_np, [np.datetime64(datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")), float(row[4])]))
	#print(Sens0_DataRaw)
	#print(Sens1_DataRaw)
	#print(Sens2_DataRaw)
	#print(Sens0_DataRaw_np[0,0])
	#date_start = np.datetime64(Sens0_DataRaw_np[0,0],'D')
	#date_end   = np.datetime64(Sens0_DataRaw_np[1000,0D') + np.timedelta64(1,'D')
	#date_cond  = np.datetime64(date_start, 'D')

	day = 86400
	paramater  = 600
	Sens0_DataAvg_np = np.zeros(shape=(0,2))
	date_start = (Sens0_DataRaw_np[0,0] // day) * day
	date_end   = (Sens0_DataRaw_np[len(Sens0_DataRaw_np)-1,0] // day + 1) *day
	date_cond  = date_start
	print("date_cond = ", date_cond)
	print("premiere_date = ", Sens0_DataRaw_np[0,0])
	print(Sens0_DataRaw_np[0,0] - date_cond)


	while date_cond < date_end:
		temp_values = np.where(Sens0_DataRaw_np[:,0]//600 == date_cond//600 ) 
		#print(temp_values)
		temp_avg    = np.average(Sens0_DataRaw_np[temp_values,1])
		#print(temp_avg)
		if temp_avg == temp_avg:
			Sens0_DataAvg_np = np.vstack((Sens0_DataAvg_np, [date_cond,temp_avg]))
		date_cond  += 600

	#print(Sens0_DataAvg_np)

		# #MOY = 0
		# n = 0
		# for i in range(0,len(Sens0_DataRaw_np)):
		# 	if 600>(Sens0_DataRaw_np[i,0] - date_cond):
		# 		MOY = MOY + Sens0_DataRaw_np[i,1]
		# 		n = n + 1
		# #if n != 0:
		# 	#print(MOY/n)
		# date_cond = date_cond + 600

	Datets = []
	for i in range(0,len(Sens0_DataAvg_np)):
		Datets = Datets + [(datetime.fromtimestamp(Sens0_DataAvg_np[i,0]).strftime('%Y-%m-%d %H:%M:%S'))]

	plt.plot(Datets,Sens0_DataAvg_np[:,1])
	plt.show()
		
		
	#Sens0_DataRaw_np = np.array(Sens0_DataRaw).astype("float")
	
	#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")


if __name__ == '__main__': 
	main()


