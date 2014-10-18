import sys


def main():

	for i in range(1, len(sys.argv)):
		file = open(sys.argv[i], "r")
		content = file.read()
		print(content)
		file.close()
		print("\n")

if __name__ == '__main__':
    main()