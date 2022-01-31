import json
import pandas as pd
from collections import defaultdict
from collections import Counter


huge_json_file= "data-2021-05.txt"
with open(huge_json_file, "r") as f:
	#print(f.readlines())
	res=json.load(f)
	print(res)
	counts=[]
	for k,v in res.items():
		counts.append(len(res[k]))
		

	

	
	hist=Counter(counts)
	#print(hist)	
