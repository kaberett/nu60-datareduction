#!/usr/bin/python

import csv, math, sys, re

if len(sys.argv) < 2:
	print >> sys.stderr, "Usage: %s file.csv [file2.csv ...]" % sys.argv[0]
	sys.exit(1)

files = sys.argv[1:]

###
# load data up
###
def loadData(file):
	# define a new array to read stuff into
	data = [["Measurement", "Value (V)", "Internal precision (1se)"]]

	# I only actually want data from the second block of running totals
	# TODO: does this need to be flexible for other element runs?
	i = 0
	for line in f:
		if i < 2:
			if "Running total results" in line:
				i += 1
			continue
		else:
			try:
				if line[8] != ' ':
					data.append( [ line[8:37], line[37:52], line[52:64] ])
			except:
				continue
	return data

###
# transpose the table
###
def transposeData(data):
	transposed = []
	# this ultimately wants to be user-controlled - scrape off the row titles,
	# present as a drop-down list, and let the user choose which to include in
	# the reduced data table, with tickyboxes for whether to include internal
	# precision.
	transposed.append([ 'file', 'sample', data[1][0], 'internal precision', data[2][0], 'internal precision', 
					   data[7][0], 'internal precision', data[12][0], 'internal precision',
					   data[13][0], 'internal precision', data[16][0], 'internal precision',
					   data[17][0], 'internal precision', data[18][0], 'internal precision',
					   data[19][0], 'internal precision', data[20][0], 'internal precision',
					   data[21][0], 'internal precision', data[22][0], 'internal precision',
					   data[23][0], 'internal precision', data[25][0], 'internal precision',
					   data[26][0], 'internal precision'])
	# would this next bit be less vile if I were looping over the lists of lists?
	# Probably, because not hard-coded so more flexible when the above ends up
	# changing...
	transposed.append([ runNo, '', float(data[1][1]), float(data[1][2]), float(data[2][1]), float(data[2][2]), 
					   float(data[7][1]), float(data[7][2]), float(data[12][1]), float(data[12][2]),
					   float(data[13][1]), float(data[13][2]), float(data[16][1]), float(data[16][2]),
					   float(data[17][1]), float(data[17][2]), float(data[18][1]), float(data[18][2]),
					   float(data[19][1]), float(data[19][2]), float(data[20][1]), float(data[20][2]),
					   float(data[21][1]), float(data[21][2]), float(data[22][1]), float(data[22][2]),
					   float(data[23][1]), float(data[23][2]), float(data[25][1]), float(data[25][2]),
					   float(data[26][1]), float(data[26][2])])
	return transposed

###
# actually do the thing (damn, I'm good at comments)
###
for filename in files:
	# pull run number out of filename
	runNo = re.search(r'[0-9][0-9]*', filename).group(0)

	# dump final running totals for the file into a table
	with open(filename, 'r') as f:
		data = loadData(f)

	# transpose 'em
	with open('transposeddata.txt', 'a') as f:
		transposed = transposeData(data)
		first = True
		for row in transposed:
			if first:
				first = False
				continue
			str_row = str(row)[1:-1]
			f.write(str_row+'\n')
