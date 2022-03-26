import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json
import sys


#converts a json file to dataframe object
def jsonToDf(fileName):
	with open(fileName) as f:
	    json_object = json.load(f)
	    json_dict = {}
	    i = 0
	    temp = []
	    res = []
	    for item in json_object:
	        
	        for attribute, value in item.items():
	            if(i == 6):
	                res.append(temp)
	                temp = [value]
	                i = 0
	            else:
	                temp.append(value)
	            i += 1
	                
	    json_df = pd.DataFrame(res, columns=['employer', 'mask', 'firstName', 'lastName', 'amountExpected', 'username'])
	    return json_df

#parses both csv files and returns a list of dictionaries used to build applied.json
def parse(json_df, csv_df):
	ans = []
	for index, row in json_df.iterrows():
	    temp = {'username': row['username']}
	    employer = row['employer']
	    first = row['firstName']
	    last = row['lastName']
	    mask = str(row['mask'])


	    for index1, row1 in csv_df.iterrows():
	    	#removes asteriks
	        mask1 = str(row1['mask']).replace("*",'')
	        amount = row1['amount']
	        #ensure that employer, first name, and last name match up
	        if(row1['employer'] == employer and row1['firstName'] == first and row1['lastName'] == last):
	            if(len(mask1) == 0):
	                temp['applied'] = amount
	                temp['owe'] = row['amountExpected'] - amount
	            else:
	                if(mask == mask1):
	                    temp['applied'] = amount
	                    temp['owe'] = row['amountExpected'] - amount
	    if(len(temp) == 3):
	        ans.append(temp)
	return ans

#scans in args and executes scripts
def main():
	input = sys.argv

	csv_file = input[1]
	json_file = input[2]
	applied_file = input[3]

	csv_df  = pd.read_csv(csv_file)
	json_df = jsonToDf(json_file)

	json_object = json.dumps((parse(json_df, csv_df)))

	with open(applied_file, "w") as outfile:
		outfile.write(json_object)

if __name__ == '__main__':
	main()