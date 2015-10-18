# -*- coding: utf-8 -*-

import csv

class SaveJSONtoCSV(object):
	def __init__(self,output_file,json):
		self.data=json
		self.output_file=output_file
		

	def write(self, rows_list=["Rank","Title","Year"]):
		#print 'writing to file %s rows ' % self.file
		with open(self.output_file, 'wb') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(rows_list) #here should be a variable instead
			for row in self.data:
				print 'writing', row
				writer.writerow([row['Rank'],row['Title'].encode('utf8'),row['Year']])
		print 'succes!'

# kindola:
    # def save_to_csv(cls, list, file):
    #         with open(file, 'w') as csvfile:
    #             fieldnames = ['Year', 'Title']
    #             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #             writer.writeheader()
    #             for element in list:
    #                 writer.writerow(element)