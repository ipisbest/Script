import csv
filename="Data.csv"
fields = ['IP', 'HTTPS.title','HTTPS.status','HTTP.title','HTTP.status','CN']
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# writing the fields
	csvwriter.writerow(fields)