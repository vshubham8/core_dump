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

def top10():
	try:
		while(1):
			print '------------------------------------------------'
			print 'Do you want:\n\t1.Deep Scan?\n\tor\n\t2.Normal Scan ?\n',
			print '''
	  1. Deep Scan will scan all the
	  files in your system
	  (system files, media files, etc.)
	\n
	  2. Normal Scan will scan all
	  the files excluding sensitive
	   files like system files,etc.
	\n
	  3. Quit
	'''
			print '------------------------------------------------'
			choice = raw_input()
			if choice == '1':
				flag = 1
				directory = '/'
				break
			elif choice == '2':
				flag = 0
				directory = '/home/'
				break
			elif choice == '3':
				return
			else:
				print '\tWrong Choice entered ! Try again !\n'
		# directory = '/home/shubham/Desktop/BMB/'
		excluded_extensions = ['svg','SingletonCookie','SingletonLock','page']
		excluded_paths = ['/usr','/proc','/var','/run','/bin/','/boot/','/sys/','/root/','/var/','/sbin/','/snap/','/srv/','/etc/','/lib/','/mnt/']#'/usr/share/help/','/usr/share/qemu/','/usr/share/omf/','/usr/share/qemu/man/']
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
		while(1):
			print 'Oh, yes!\nDo you want to delete some of above files?? (Y/N)'
			wanting = raw_input()
			if wanting.lower() == 'y':
				# print 'List of 10 biggest files:\n'
				# for i in xrange(0,10):
				# 	print i+1,')',top_10_files[i]
				nos = ['1','2','3','4','5','6','7','8','9','10']
				file_no = raw_input('Enter the no. of file you want to delete: ')
				if file_no in nos:
					file_to_delete = top_10_files[int(file_no)-1][0]
					# print file_to_delete
					sys_file = 0
					for j in excluded_paths:
						if j in file_to_delete:
							sys_file = 1

					if sys_file == 1:
						print 'You are trying to delete a System File: ',file_to_delete.split('/')[-1]
						print 'Still want to delete it?? (y/n)'
						while(1):
							ch = raw_input()
							if ch.lower() == 'y':
								os.remove(file_to_delete)
								entry = [file_to_delete,top_10_files[int(file_no)-1][1]]
								top_10_files.remove(entry)
								print 'File Deleted !'
								break
							elif ch.lower() == 'n':
								break
							else:
								print 'Enter correct choice !'
					else:
						print 'Do you really want to delete the file: ',file_to_delete.split('/')[-1]
						print '(y/n)'
						while(1):
							ch = raw_input()
							if ch.lower() == 'y':
								os.remove(file_to_delete)
								entry = [file_to_delete,top_10_files[int(file_no)-1][1]]
								top_10_files.remove(entry)
								print 'File Deleted !'
								break
							elif ch.lower() == 'n':
								break
							else:
								print 'Enter correct choice !'
				else:
					print 'Enter correct file no. !'
					continue
			
			elif wanting.lower() == 'n':
				break
			else:
				print 'Wrong Choice ! Please Try again !'
				continue
			print '------------------------------------------------'
			for i in xrange(0,len(top_10_files)):
				print i+1,')',top_10_files[i][1],'MB :',top_10_files[i][0]

		print 'Good Bye !'
		print '-----------x-----------x-----------x------------'

	except:
		print 'Error Occured Unxpectedly !'

# top10('/home/shubham/Desktop')
