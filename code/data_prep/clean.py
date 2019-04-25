import os

def clean(data):
	clean_data = ""
	count = 0
	for line in data.split("\n"):
		try:
			i, d, t = line.split("|", 2)
		except:
			print("==> ||" + line + "||\t", end='')
			print(line.split("|"))
			continue
		
		boolean = False
		if "|" in t:
			count += 1
			boolean = True
			# print(line)

		t = '.'.join(t.split("|"))
		line = '|'.join([i, d, t])
		clean_data += line + "\n"
		if boolean:
			# print("\t" + line)
			boolean = False
	
	print("Number of lines with Pipe symbols =", count)
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
