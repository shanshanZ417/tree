#!/usr/bin/env python3
import subprocess
import sys
import os
import string
class XXTree:
<<<<<<< HEAD
		def __init__(self): 		
				pass

		def getTree(self, dir): 		
				directNum = 0
				filesNum = 0
				judge = 0
				list = self.getList(dir, 0)
				length = len(list)
				treelist = [] 	
				for i in range(0, len(list)):
						final = 0
						judge = judge + 1
						fullpath = list[i] 
						parpath = os.path.dirname(list[i])
						filename = os.path.basename(list[i])
						if(fullpath == dir):
								treelist.append(fullpath) 
								continue
						if os.path.isdir(fullpath):
								directNum = directNum + 1
						else:
								filesNum = filesNum + 1
								temp = fullpath.replace(dir, "")
								temp2 = temp.split("/")
								print("iiiiiiiiiiiiiii")
								print(temp2)
								if(len(temp2)==1):
										pass
								else:
										final = 1
						path = fullpath.replace(dir, "")
						names = path.split("/")
						print("namessssss")
						print(names)
						print(len(names))
						if (final == 0):
								name = "├-- " + names[len(names) - 1]
						else:
								name = "└" + names[len(names)-1]
						for j in range(1, len(names)):
								print("iamhererererer")
								name = "|    " + name						
						treelist.append(name)
				for i in range(0, len(treelist)):
						print (treelist[i])
				print("")
				print(directNum,"directories,",filesNum,"files")
		def getList(self, dir, layer):
				list = []
				if layer == 0: 
						list.append(dir)
				files = os.listdir(dir)
				for file in files:
						if not file.startswith("."):
								file = os.path.join(dir, file)
								if os.path.isdir(file):
										list.append(file)
										list += self.getList(file, layer + 1)
								else:
										list.append(file)
				return list
=======
	def __init__(self):
		pass
	def getTree(self, dir):
		directNum = 0
		filesNum = 0
		judge = 0
		list = self.getList(dir, 0)
		treelist = []
		for i in range(0, len(list)):
			final = 0
			judge = judge + 1
			fullpath = list[i]
			parpath = os.path.dirname(list[i])
			filename = os.path.basename(list[i])
			if(fullpath == dir):
				treelist.append(fullpath)
				continue
			if os.path.isdir(fullpath):
				directNum = directNum + 1
			else:
				filesNum = filesNum + 1
				temp = fullpath.replace(dir, "")
				temp2 = temp.split("/")
				if(len(temp2)==2):
					pass
				else:
					final = 1
			path = fullpath.replace(dir, "")
			names = path.split("/")
			if(judge != len(list)):
				if (final == 0):
					name = "├── " + names[len(names) - 1]
				else:
					name = "└── " + names[len(names)-1]
				for j in range(1, len(names) - 1):
					name = "|    " + name
					treelist.append(name)
			else:
				name = "└── " + names[len(names)-1]
				treelist.append(name)
		for i in range(0, len(treelist)):
			print (treelist[i])
		print("")
		print(directNum,"directories,",filesNum,"files")
		
	def getList(self, dir, layer):
		list = []
		if layer == 0:
			list.append(dir)
		files = os.listdir(dir)
		for file in files:
			if not file.startswith("."):
				file = os.path.join(dir, file)
				if os.path.isdir(file):
					list.append(file)
					list += self.getList(file, layer + 1)
				else:
					list.append(file)
		return list
>>>>>>> b1a952da7cba870f84c5820ad484234ed425890a
if __name__ == '__main__':
	t = XXTree()
	dir = None
	if len(sys.argv) == 2:
		dir = sys.argv[1]
	if len(sys.argv) == 1:
		dir = "."
	t.getTree(dir)
