import pandas as pd
import json
import numpy as np
from collections import defaultdict
from datetime import datetime




huge_json_file= "RS_2018-12"
d = defaultdict(list)
print(d)

with open(huge_json_file, "r") as f:
#print(f.readline())
	#for i in range(2):
	one_block = f.readline()
	res = json.loads(one_block)
		#print (res)
	count=0	
	while one_block:
		one_block = f.readline()
		if one_block=="":
			break
		res = json.loads(one_block)
		if res['media']==None:
			continue
		YouTube_Check = res.get('media', {}).get('oembed', {}).get('provider_name',"")
		if YouTube_Check== "YouTube":
			author=res['author']
			url=res['url']
			time_unix=int(res['created_utc'])
			time_real=datetime.utcfromtimestamp(time_unix).strftime('%Y-%m-%d %H:%M:%S')
			packet=[]
			packet.append(url)
			packet.append(time_real)
			#print(packet)
			temp=1
			for items in d[author]:
				if url==items[0]:
					temp=0
					break
				else:
					continue	
		
			if temp==1:
				d[author].append(packet)	
			
			count=count+1
			print(count)
		else:
			continue	
		
with open('data-2018-12.txt', 'a') as convert_file:
				convert_file.write(json.dumps(d)) 


