from random import choice, randint
from json import dumps

def generate_list_JSON(num_of_records,feature_0,feature_1,):
	data = []
	for i in range(num_of_records):
			data.append([choice(feature_0), choice(feature_1), randint(1,5)])
	return(data)

def generate_dict_JSON(num_of_records,feature_0,feature_1,):
	data = []
	feature_0_name = 'flavor'
	feature_1_name = 'meal'
	for i in range(num_of_records):
		data.append(
		[
		{feature_0_name:choice(feature_0)},
		{feature_1_name:choice(feature_1)},
		{'score':randint(1,5)}
		])
	return(data)

flavor = ['American','Italian','French','Mexican',]
meal  = ['chicken','fish','nachos','pasta','potpie','vegan','vegetarian',]
records = 10000
fname = 'test.json'
meal_data = generate_dict_JSON(records,flavor,meal)

f = open(fname,'w')
f.write(dumps(meal_data))
f.close()
