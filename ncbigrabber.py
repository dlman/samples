# script takes a file that consists of FR and DQ ids
# and via the Entrez API that accesses NCBI through the Bio-Python module
# extracts the pIR ID that is associated with the DQ id

from Bio import Entrez
import sys
import os
import re
Entrez.email = "dlman8@hotmail.com"
falist = open("FAListDQsnip4.txt")
output = open("FAListCompletepart4.txt" ,"w")

for line in falist:
	splitter = line.split()
	try:
		FRnum = splitter[0]
		#grabs dq num
		refNum = splitter[1]  
		#only doing dqs for now
		if refNum.find("DQ") >= 0: 
			#if multiple dq nums
			if refNum.find(",") >= 0:  
				newSeq = True
				multisplit = re.split('[,]',refNum)
				for sequence in multisplit:
					handle = Entrez.esearch(db="nucleotide", term = sequence)
					record = Entrez.read(handle)
					IDNum = record["IdList"]
					singleID = IDNum[0]
					handle = Entrez.esummary(db="nucleotide", id=singleID)
					record = Entrez.read(handle)
					pIR = record[0]["Title"]
					pIRonly = re.split('[ ,]',pIR)
					#printing multiple pir numbers on a line
					if newSeq is True: 
						output.write(FRnum + "\t" + refNum + "\t" + pIRonly[3] + ",")
						newSeq = False
					else:
						output.write(pIRonly[3])
					print pIRonly[3]

			#for single dq numbers
			else: 
				handle = Entrez.esearch(db="nucleotide", term = refNum)
				record = Entrez.read(handle)
				IDNum = record["IdList"]
				singleID = IDNum[0]
				handle = Entrez.esummary(db="nucleotide", id=singleID)
				record = Entrez.read(handle)
				pIR = record[0]["Title"]
				pIRonly = re.split('[ ,]',pIR)
				output.write(FRnum + "\t" + refNum + "\t" + pIRonly[3])
				print pIRonly[3]
			#new line for the next fr number
			output.write("\n") 
	#if no dq num exists in the database
	except IndexError:   
		refNum = ""
		print refNum