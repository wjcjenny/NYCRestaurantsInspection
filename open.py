import csv
#from geopy.geocoders import Nominatim
#geolocator = Nominatim()

new_combined_list = []
with open('need_data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		#print row[3].strip(' ')+" "+row[4].strip(' ')+", New York, NY, "+row[5].strip(' ')
		wu_str = '\"' + row[1].strip(' ')+" "+row[2].strip(' ')+", New York, NY, "+row[3].strip(' ')+ '\"'
		print wu_str
		# if wu_str not in new_combined_list:
		# 	new_combined_list.append(wu_str)
		# 	print wu_str
		# 	location = geolocator.geocode(wu_str)
		# 	print wu_str, location.latitude, location.longitude

