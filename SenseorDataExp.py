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
from datetime import datetime, date
import os
import sys
import glob
import csv
import numpy as np
import math
import argparse
import re

# Import Python visualisation dependencies :
# -----------------------------------------
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
	


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
	# allowed_chars = '\d[:/;Na-.$]*'

	with open(csvfile, "r+") as f:
		print(csvfile) 
		lines = (line for line in f if not line.startswith('#') if line.count(';')==4 if (isfloat(line[:9]) and isfloat(line[33]) and isfloat(line[35:])))
		# if csvfile == "2018-05_000000177_measures.csv":
			# for line in lines:
				# print(line.count(";"))
		Sens_DataRaw = np.loadtxt(lines, delimiter=';', skiprows=1, usecols=(0,3,4))
		#print(Sens_DataRaw[:,1])
		Sens0_DataRaw_np = Sens_DataRaw[np.where(Sens_DataRaw[:,1]==0)][:,[0,2]]
		Sens1_DataRaw_np = Sens_DataRaw[np.where(Sens_DataRaw[:,1]==1)][:,[0,2]]
		Sens2_DataRaw_np = Sens_DataRaw[np.where(Sens_DataRaw[:,1]==2)][:,[0,2]]

		# for row in reader:
			# i = i+1
			# print(i) 
			# if not row[0].startswith('#') and len(row)>3: # skip comments and skip corrupted data
				# if row[3] == '0':
					# print('SAW 1')
					# try:
						# Sens0_DataRaw_np = np.vstack((Sens0_DataRaw_np, [float(row[0]), float(row[4])]))
						# print('YEAH0')
					# except ValueError:
						# print("Not a float")
				# if row[3] == '1':
					# print('SAW 2')
					# try:
						# Sens1_DataRaw_np = np.vstack((Sens1_DataRaw_np, [float(row[0]), float(row[4])]))
						# print('YEAH1')
					# except ValueError:
						# print("Not a float")
				# if row[3] == '2':
					# print('SAW 3')
					# try:
						# Sens2_DataRaw_np = np.vstack((Sens2_DataRaw_np, [float(row[0]), float(row[4])]))
						# print('YEAH2')
					# except ValueError:
						# print("Not a float")

	return Sens0_DataRaw_np, Sens1_DataRaw_np, Sens2_DataRaw_np				

def main(time_parameter):
	# Local variables :
	# -----------------
	i = 0
	j = 0
	Sens0_np = np.zeros(shape=(0,2))
	Sens1_np = np.zeros(shape=(0,2))
	Sens2_np = np.zeros(shape=(0,2))
	Sens0_DataAvg_np = np.zeros(shape=(0,2))
	Sens1_DataAvg_np = np.zeros(shape=(0,2))
	Sens2_DataAvg_np = np.zeros(shape=(0,2))
	
	# Initializing visualisation :
	# ----------------------------
	plt.rcParams['axes.grid'] = True
	plt.rcParams.update({'font.size' :6})
	fig, axes = plt.subplots(len(glob.glob('*.csv')), 3, squeeze=False, sharex=False, sharey=True)
	# fig.suptitle("SENSeOR - Analyse - Moyenne 10 min", fontsize=8)
	xfmt = pltdates.DateFormatter('%d-%m')
	# ax = fig.gca()
	# ax.xaxis_date()
	# xfmt = pltdates.DateFormatter('%d-%m-%Y')
	# ax.xaxis.set_major_formatter(xfmt)
	# fig.autofmt_xdate()

	# Extracting SENSeOR Data from CSV file :
	# ---------------------------------------
	for file_csv in glob.glob('*.csv'):
		[Sens0_out, Sens1_out, Sens2_out] = SensSort(file_csv)
		Sens0_np = np.vstack((Sens0_np, Sens0_out))
		Sens1_np = np.vstack((Sens1_np, Sens1_out))
		Sens2_np = np.vstack((Sens2_np, Sens2_out))
		# Averaging SENSeOR Data according to timestamp :
		# -----------------------------------------------
		Sens0_DataAvg_np = AvgXSeconds(Sens0_out, time_parameter)
		Sens1_DataAvg_np = AvgXSeconds(Sens1_out, time_parameter)
		Sens2_DataAvg_np = AvgXSeconds(Sens2_out, time_parameter)
		Dateplt0 = []
		for i in range(0,len(Sens0_DataAvg_np)):
			Dateplt0 = Dateplt0 + [pltdates.date2num((datetime.fromtimestamp(Sens0_DataAvg_np[i,0])))]
		axes[j,0].plot(Dateplt0,Sens0_DataAvg_np[:,1], linewidth=2.0)
		axes[j,0].set_ylabel('T SAW 0', fontsize=6)
		axes[j,0].set_title("Données " + str(datetime.fromtimestamp(Sens0_DataAvg_np[0,0]).year) + "-" + str(datetime.fromtimestamp(Sens0_DataAvg_np[0,0]).month), fontsize=6)
		#axes[j,0].margins(0.1)
		axes[j,0].xaxis_date()
		axes[j,0].xaxis.set_major_formatter(xfmt)
		plt.setp(axes[j,0].get_xticklabels(), rotation=30, horizontalalignment='right')
			
		Dateplt1 = []
		for i in range(0,len(Sens1_DataAvg_np)):
			Dateplt1 = Dateplt1 + [pltdates.date2num((datetime.fromtimestamp(Sens1_DataAvg_np[i,0])))]
		axes[j,1].plot(Dateplt1,Sens1_DataAvg_np[:,1],'r', linewidth=2.0)
		axes[j,1].set_ylabel('T SAW 1', fontsize=6)
		axes[j,1].set_title("Données " + str(datetime.fromtimestamp(Sens1_DataAvg_np[0,0]).year) + "-" + str(datetime.fromtimestamp(Sens1_DataAvg_np[0,0]).month), fontsize=6)
		#axes[j,1].margins(0.1)
		axes[j,1].xaxis_date()
		axes[j,1].xaxis.set_major_formatter(xfmt)
		plt.setp(axes[j,1].get_xticklabels(), rotation=30, horizontalalignment='right')
		
		Dateplt2 = []		
		for i in range(0,len(Sens2_DataAvg_np)):
			Dateplt2 = Dateplt2 + [pltdates.date2num((datetime.fromtimestamp(Sens2_DataAvg_np[i,0])))]
		axes[j,2].plot(Dateplt2,Sens2_DataAvg_np[:,1],'g', linewidth=2.0)
		axes[j,2].set_ylabel('T SAW 2', fontsize=6)
		axes[j,2].set_title("Données " + str(datetime.fromtimestamp(Sens2_DataAvg_np[0,0]).year) + "-" + str(datetime.fromtimestamp(Sens2_DataAvg_np[0,0]).month), fontsize=6)
		axes[j,2].xaxis_date()
		axes[j,2].xaxis.set_major_formatter(xfmt)
		plt.setp(axes[j,2].get_xticklabels(), rotation=30, horizontalalignment='right')
		# axes[j,2].margins(0.2)
		j += 1



	# plt.xticks(rotation=90)
	# plt.margins(0.2)
	# Tweak spacing to prevent clipping of tick-labels
	# plt.gcf().autofmt_xdate()
	plt.tight_layout()
	plt.show()

if __name__ == '__main__': 
	
	parser = argparse.ArgumentParser(description='Compute and plot SENSeOR SAW sensor data and averages it on demand. To run the program, you have to be where the .csv of SENSeOR are located')
	parser.add_argument('-t','--time_parameter', help='select time parameter',
			 required=True)
	args = parser.parse_args()

	main(int(args.time_parameter))



