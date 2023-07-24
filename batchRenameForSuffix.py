# 批量更改tif后缀为png
import os
import sys
os.chdir(r'./test/image')

# 列出当前目录下所有的文件
files = os.listdir('./')
print('files',files)

for fileName in files:
	portion = os.path.splitext(fileName)
	# 如果后缀是.dat 
	if portion[1] == ".tif":
		#把原文件后缀名改为 txt
		newName = portion[0] + ".png" 
		os.rename(fileName, newName)
