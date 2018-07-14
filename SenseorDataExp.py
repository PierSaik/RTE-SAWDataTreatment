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
	
	with open('2017-11_000000177_measures.csv', newline='') as f:
		reader = csv.reader(f, delimiter=';')
		next(reader, None) # skip header
		for row in reader:
			i = i+1
			print(i) 
			if not row[0].startswith('#'): # skip comments
				if row[3] == '1':
					print('yeah1')
					Sens1_DataRaw = Sens1_DataRaw + row
				if row[3] == '0':
					print('yeah0')
					Sens0_DataRaw = Sens0_DataRaw + row
				if row[3] == '2':
					print('yeah2')
					Sens2_DataRaw = Sens2_DataRaw + row
	print(Sens0_DataRaw)
	print(Sens1_DataRaw)
	print(Sens2_DataRaw)


if __name__ == '__main__': 
	main()


