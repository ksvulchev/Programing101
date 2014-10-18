import sys
from random import randint

def main():

		file = open(sys.argv[1], "w") 
		for i in range(int(sys.argv[2])):
			contents = str(randint(1, 1000))
			file.write(contents + " ")
		file.close()

if __name__ == '__main__':
	main()