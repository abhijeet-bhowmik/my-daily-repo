


def get_json(data, error):
	if data:
		json_object_list = []
		for snippet_dictionary in data:
			object_dictionary = {}
			for k,v in snippet_dictionary.items():
				object_dictionary[k] = v
			json_object_list.append(object_dictionary)
		print(json_object_list)
		json_response = {'data': json_object_list,
						 'success' : True,
						 'error' : None,
						 'status' : 200}
		return json_response

	elif error:
		json_response = {'data' : None,
						  'success' : False,
						  'error' : error,
						  'status' : 404}

		return json_response

	



