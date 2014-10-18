import sys


def main():

	file = open(sys.argv[1], "r")
	content = file.read()
	num_arr = content.split(" ")
	suma = 0
	for i in num_arr:
		suma += int(i) #poluchava se whitespace nakraq v number.txt
	print(suma)
	file.close()

if __name__ == '__main__':
    main()