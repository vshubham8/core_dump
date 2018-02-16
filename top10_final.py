'''
/*
/* This module will scan through all the drives and directories in your system and
/* find the top 10 Biggest files on your system
/* Author: Shubham Verma
/* (M.Tech, CSE, IIIT - Hydearbad)
/*
'''

import heapq
import sys
import operator
import os, os.path


# directory = "/"


def top10(directory):
	try:
		excluded_extensions = ['svg','SingletonCookie','SingletonLock','page']
		excluded_paths = ['/usr','/proc','/var','/run']#'/usr/share/help/','/usr/share/qemu/','/usr/share/omf/','/usr/share/qemu/man/']
		filenames = (os.path.join(p, n) for p, _,f in os.walk(directory) for n in f)
		print 'Started scanning files in your system !'
		actual_filenames = []
		no_of_files=0
		_exhausted = object()

		top_10_files = []
		for i in xrange(0,10):
			file = next(filenames,_exhausted)
			if file == _exhausted:
				break
			else:
				ext = file.split('.')[-1]
				if ext not in excluded_extensions:
					size = round(os.stat(file).st_size/(1024*1024.0),2)
					top_10_files.append([file,size])

		sno = 1
		no_of_files = len(top_10_files)
		print 'WAIT ! \(^u^)/'
		while 1:
			file = next(filenames,_exhausted)
			#file = str is returned
			#for empty generator = object is returned
			if file == _exhausted:
				# print 'Generator is empty now !'
				break
			else:
				# print sno,')',file
				sno+=1
				no_of_files+=1
				if no_of_files == 100000:
					print 'WAIT more ! \(^_^)/'
				elif no_of_files == 300000:
					print 'WAIT a little more ! \(0_0)/'
				elif no_of_files == 500000:
					print 'Yr system has too many files, still scanning ! \(z_z)/'
				elif no_of_files == 600000:
					print 'Indeed a lot of files ! \(*_*)/'
				elif no_of_files == 800000:
					print '\t\t\t   $$$'
					print 'Get a Coffee for a while: (___)0'
					print 'Just about to display the results !!!'
				# print 'EXT: ',ext
				if file[0:4] == '/usr' or file[0:5] == '/proc' or file[0:4] == '/var' or file[0:4] == '/run': #usr contains shareable things so don't touch it
					continue
				ext1 = file.split('.')[-1]
				ext2 = file.split('/')[-1]
				if ext1 not in excluded_extensions and ext2 not in excluded_extensions:
					size = round(os.stat(file).st_size/(1024*1024.0),2)
					top_10_files.append([file,size])
					top_10_files.sort(key=lambda x: x[1])
					top_10_files = top_10_files[::-1][0:10]

		print 'Done Scanning files in your system !\n'
		print 'Total files in your system: ',no_of_files,'\n'
		print 'Top 10 biggest files in your system:','\n'
		for i in xrange(0,10):
			print i+1,')',top_10_files[i][1],'MB :',top_10_files[i][0]
		print '------------------------------------------------'
	except:
		print 'Error Occured Unxpectedly !'

# top10('/home/shubham/Desktop')