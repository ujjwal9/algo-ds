d={}
d1=d.copy()	#copy a dictionary
d.clear() #clears the dictionary 
for k,v in d.items()	#loop over dict
d[key]dict throws exception if the key is not present so use d.get() which returns None or d.get(x,0) which returns 0 in case of None