import sys


def main():

	file = open("MEGATRON.txt", "a") 
	for i in range(1, len(sys.argv)):
		concat_file = open(sys.argv[i], "r")
		content = concat_file.read()
		file.write(content)
		file.write("\n")
		file.write("\n")
		concat_file.close()
	file.close()

if __name__ == '__main__':
	main()	