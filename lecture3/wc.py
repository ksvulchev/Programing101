import sys
import re

def count (command, content):

	if command == "chars":
		return len(content)
	elif command == "words":
		return len(re.split(" |\n\n",content))
	elif command == "lines":
		return len(content.split("\n"))
	else:
		return "Invalid command. Try 'chars','words' or 'lines'"


def main():

	command = sys.argv[1]
	file = open(sys.argv[2], "r")
	content = file.read()
	print(count(command, content))
	file.close()

if __name__ == '__main__':
	main()	