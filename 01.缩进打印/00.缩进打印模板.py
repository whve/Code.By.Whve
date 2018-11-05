# 缩进打印模板,打印列表到文本文件中.

import sys
''' print_lol()作用时打印列表,其中有可能包含(也有可能不包含)嵌套列表.'''
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
	''' the_list为该函数的位置参数,可以是任何的python列表.所指定的列表中的每一个数据项递归的打印到屏幕上,每个数据占一行.
	第2个参数indent:缩进,默认off(indent=False).
	第3个参数level用来遇到嵌套列表插入制表符.'''
	for each_item in the_list:
		# 判断是否为列表.
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1,fh)
		else:
			if indent:
				'''
				# end='':关闭print()自动换行.
				for tab_stop in range(level):
					print('\t',end='')
				'''
				# 等价于注释中的for循环.
				print('\t' *level,end='',file=fh)
			print(each_item,file=fh)

import os
# 路径设置,读取或保存的的修改路径.
# os.chdir(r'C:\Users\wz\Desktop\HeadFirstPython\chaphter3_4')

# 数据导入
ab=a&b
ac=a&c
bc=b&c
abc=a&b&c

# 保存到文本
try:
	with open('.ab.txt','w')as abfile,open('.bc.txt','w')as bcfile,open('.ac.txt','w')as acfile,open('.abc.txt','w')as abcfile:
		print_lol(ab,fh=abfile)
		print_lol(bc,fh=bcfile)
		print_lol(ac,fh=acfile)
		print_lol(abc,fh=abcfile)

except IOError as err:
	print('File,error' +str(err))