from datetime import datetime


def find_string(txt, str1):
	return txt.find(str1, txt.find(str1)+1)

def filter_date(date):
	dateformat = r"%Y-%m-%d-%H:%M"
	date_string = date.replace("T", "-")
	last_index = find_string(date_string, ":")
	date_string = date_string[:last_index]
	print("-------------")
	print(date_string, dateformat)
	print("-------------")
	return datetime.strptime(date_string, dateformat)
