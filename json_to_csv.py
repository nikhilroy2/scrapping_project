import pandas as pd

# enter the json filename to be converted to json
JSON_FILE = 'result.json'

# enter the csv filename you wish to save it as
CSV_FILE = 'csf_file_result.csv'

with open(JSON_FILE, encoding = 'utf-8') as f :
	df = pd.read_json(f)
    
df.to_csv(CSV_FILE, encoding = 'utf-8', index = False)