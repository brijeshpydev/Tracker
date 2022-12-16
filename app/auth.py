import datetime, random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']
COMBINED_LIST = DIGITS  + LOCASE_CHARACTERS + UPCASE_CHARACTERS

def key(MAX_LEN):
	temp_key = ""
	for x in range(MAX_LEN):
		temp_key +=  random.choice(COMBINED_LIST)
	return str(temp_key)


def times():
    dt = str(datetime.datetime.now())[:19]
    return dt


    
