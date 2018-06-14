def get_json(data):
	json = {'data':[]}
	try:
		for dictionary in data:
			json['data'].append({})
			for k,v in dictionary.items():
				json['data'][-1][k] = v
		return json,None
	except Exception as e:
		return None,e




