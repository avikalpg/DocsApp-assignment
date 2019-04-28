import os
import re

def remove_pipes(sentence):
	sentence = '.'.join(sentence.split("|"))
	return sentence

def remove_urls(sentence):
	# ref: https://www.geeksforgeeks.org/python-check-url-string/
	sentence = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "", sentence)
	return sentence

def remove_numbers(sentence):
	sentence = re.sub(r'\d+', "", sentence)
	return sentence

def remove_symbols(sentence):
	sentence = re.sub(r'[^\w]', ' ', sentence)
	return sentence

def remove_special_chars(sentence):
	sentence = re.sub(r'[^A-Za-z0-9 ]', ' ', sentence)
	return sentence

def clean(data):
	clean_data = ""
	for line in data.split("\n"):
		try:
			i, d, t = line.split("|", 2)
		except:
			print("==> ||" + line + "||\t", end='')
			print(line.split("|"))
			continue

		# t = remove_pipes(t)
		t = remove_urls(t)
		t = remove_numbers(t)
		# t = remove_symbols(t)
		t = remove_special_chars(t)
		
		line = '|'.join([i, d, t])
		clean_data += line + "\n"
	
	return clean_data
		

def clean_file(data_file, source, target):
	with open(source + data_file, 'r+', errors='ignore') as f:
		data = f.read()

	data = clean(data)
	with open(target + data_file, 'w+') as f:
		f.write(data)

def main():
	raw_data_location = "../../data/raw/Health-Tweets/"
	target_data_location = "../../data/processed/Health-Tweets/"

	for data_file in os.listdir(raw_data_location):
		print(data_file)
		clean_file(data_file, raw_data_location, target_data_location)

if __name__ == '__main__':
	main()
