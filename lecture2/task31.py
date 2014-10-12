#!/usr/bin/python


def reduce_file_path(path):

	arr = path.split("/")
	new_path_arr = []
	for i in arr:
		if i == "":
			continue
		new_path_arr.append(i)
		if i == "..":
			new_path_arr.pop()
			new_path_arr.pop()
		if i == ".":
			new_path_arr.pop()




	return "/" + "/".join(new_path_arr)

print(reduce_file_path("//////////////"))