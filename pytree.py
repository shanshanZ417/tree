#!/usr/bin/env python3
import sys
import os
import string
directNum = 0
fileNum = 0
names = []


def sortedTree(dir):
	files = []
	for files1 in os.listdir(dir):
		if not files1.startswith("."):
			files.append(files1)
	return files


def buildTree(dir,front):
	itemOrder = 0
	list = []
	global names
	global directNum
	global fileNum
	symbol1 = "    "
	symbol2 = "│   "
	files = sortedTree(dir)
	for path in sorted(files,key=str.lower):
		curDir = dir + "/" + path
		itemOrder = itemOrder + 1
		if os.path.isdir(curDir):
			directNum = directNum + 1
			if(itemOrder != len(files)):
				name = front + "├── "+ path
				names.append(name)
				buildTree(curDir,front + symbol2)
			else:
				name = front + "└── " + path
				names.append(name)
				buildTree(curDir,front + symbol1)
		else:
			fileNum = fileNum + 1
			if (itemOrder != len(files)):
				name = front + "├── "+ path
				names.append(name)
			else:
				name = front + "└── " + path
				names.append(name)
if __name__ == '__main__':
	dir = None
	if (len(sys.argv)!=1 and len(sys.argv)!=2):
		print("Your enter is not valid!")
	else:
		
		if len(sys.argv) == 2:
			dir = sys.argv[1]
		if len(sys.argv) == 1:
			dir = "."
		buildTree(dir,"")
		print(dir)
		for i in range(0,len(names)):
			print(names[i])
		print("")
		directories = "directories"
		files = "files"
		if(directNum == 1):
			directories = "directory"
		else:
			pass
		if(files == 1):
			files = "file"
		else:
			pass
		print(str(directNum) + " " + directories + ", " + str(fileNum) + " " + files) 		
