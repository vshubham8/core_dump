'''
/*
/* CoreDump: A file Segregation tool for cleaning up your Desktop in seconds !
/*		  Besides, it also displays user, the top 10 biggest files in his/her system !
/*
/* Author: Shubham Verma
/* (M.Tech, CSE, IIIT-Hyderabad)
/*
'''
from top10_final import top10
import os,errno
import glob
import shutil #to move files between disks
import platform
# arr=os.listdir('../../../../')
#arr=next(os.walk('/home/shubham/Desktop')) - tuple(location,all_folder_names_list,files_list)
#arr=glob.glob("*.py")
# print( arr

#/ = root directory
#./ = current directory

# pathname='files/'
# pathname='/home/shubham/Desktop/'

def common_utility(path_to_Desktop,all_files,different_extensions,all_files_names,files_with_extensions,all_folder_names):
	for i in all_files:
		file_name=i.split(path_to_Desktop)[-1]
		# print( file_name
		ext=file_name.split('.')
		# print( 'EXT=',ext
		if len(ext)==1 or ext[1]=='HIDDEN':
			all_folder_names.append(ext)
		else:
			all_files_names.append(file_name)
			ext=ext[-1].lower()
			different_extensions.append(ext)
			files_with_extensions[ext]=[]

	for i in all_files_names:
		# print( 'Processing file !'
		ext=i.split('.')[-1].lower()
		files_with_extensions[ext].append(i)
	# print( 'before: ',different_extensions
	different_extensions=list(set(different_extensions)-set(['url','lnk']))
	# print( 'after: ',different_extensions
	return [different_extensions,all_files_names,files_with_extensions,all_folder_names]

def move_files(path_to_Desktop,path_to_move,different_extensions,files_with_extensions,hidden_flag):
	########## making visible directories for different visible extesions ##########
	if hidden_flag==1:
		try:
			os.makedirs(path_to_move+'.HIDDEN')
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	for i in different_extensions:
		try:
			if hidden_flag==1:
				os.makedirs(path_to_move+'.HIDDEN/.'+i.upper())
			else:
				os.makedirs(path_to_move+i.upper())
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	#error will occur if not handled like above that directory exists
	#################################################################

	########### moving files to their respective category ###########
	#shutil.move(src,dstn)
	# shutil.move('./files/PDF_1.pdf','./files/pdfs')
	for i in different_extensions:
		files_to_move=files_with_extensions[i]
		flag = 0
		for j in files_to_move:
			if hidden_flag==1:
				try:
					shutil.move(path_to_Desktop+j,path_to_move+'.HIDDEN/.'+i.upper())
				except:
					if flag == 0:
						print( 'Moving file with same names !!')
						bahar_wali=path_to_Desktop+j
						andar_wali=path_to_move+'.HIDDEN/.'+i.upper()+'/'+j
						print( 'Original: ',j,'(',os.stat(andar_wali).st_size,'Bytes)')
						print( 'Replace With: ',j,'(',os.stat(bahar_wali).st_size,'Bytes)')
						print( '''
---------------------------------------------
|1.Replace?    |2.Skip?      |3.Skip All?   |
---------------------------------------------
						''')
						try:
							ch = input().lower()
						except:
							ch = raw_input().lower()
						if ch == '1':
							os.remove(andar_wali)
							shutil.move(bahar_wali,path_to_move+'.HIDDEN/.'+i.upper())
						elif ch == '2':
							continue
						elif ch == '3':
							flag = 1
			else:
				try:
					shutil.move(path_to_Desktop+j,path_to_move+i.upper())
				except:
					if flag == 0:
						bahar_wali=path_to_Desktop+j
						andar_wali=path_to_move+i.upper()+'/'+j
#						print('ANDAR_WALI:',andar_wali)
						print( 'Moving file with same name !')
						print( 'Original: ',j,'(',os.stat(andar_wali).st_size,'Bytes)')
						print( 'Replace With: ',j,'(',os.stat(bahar_wali).st_size,'Bytes)',)
						print( '''
---------------------------------------------
|1.Replace?    |2.Skip?      |3.Skip All?   |
---------------------------------------------
						''')
						try:
							ch = input().lower()
						except:
							ch = raw_input().lower()
						if ch == '1':
							os.remove(andar_wali)
							shutil.move(bahar_wali,path_to_move+i.upper())
						elif ch == '2':
							continue
						elif ch == '3':
							flag = 1
	# siz = os.stat('xyz.txt').st_size - size in Bytes

	#################################################################

def main():
	os_name = os.name
	platform_name = platform.system()
	print('OS Name  = ',os_name)
	print('Platform Name = ',platform_name)
	while(1):
		print('Do you want to specify path explicitly for \'Desktop\'?: (y/n)')
		try:
			ch = raw_input()
		except:
			ch = input()
		if ch.lower() == 'y':	
			print( '''------------------------------------------------
		/ = root directory
		./ = current directory
		FORMAT: (/path/subpath1/subpath2/.../Desktop/)
		------------------------------------------------
		Enter the path to your Desktop: (in above format)''')
			try:
				path_to_Desktop = input()
			except:
				path_to_Desktop = raw_input()
			break
		elif ch.lower() == 'n':
			try:
				if(platform_name != 'Windows'):
					path_to_Desktop = os.path.expanduser("~/Desktop/")
				else:
					path_to_Desktop = os.path.expanduser("~\Desktop/")
				print( 'Path fetched from the system:',path_to_Desktop)
				break
			except:
				print( 'Error in fetching Desktop path ! please run again the pgm and specify path...')
				break
		else:
			continue
	while(1):
		print( 'Do you want to specify path explicitly for \'Documents?: \'(y/n)')
		try:
			ch = raw_input()
		except:
			ch = input()
		# print( 'choice:',ch)
		if ch.lower() == 'y':	
			print( '''------------------------------------------------
		/ = root directory
		./ = current directory
		FORMAT: (/path/subpath1/subpath2/.../Documents/)
		------------------------------------------------
		Enter the path to your Documents: (in above format)''')
			try:
				path_to_move = input()
			except:
				path_to_move = raw_input()
			break
		elif ch.lower() == 'n':
			try:
				if(platform_name != 'Windows'):
					path_to_move = os.path.expanduser("~/Documents/")
				else:
					path_to_move = os.path.expanduser("~\Documents/")
				print( 'Path fetched from the system:',path_to_move)
				break
			except:
				print( 'Error in fetching Documents path ! please run again the pgm and specify path...')
				break
		else:
			continue

	print( '------------------------------------------------')
	########## getting filenames and extension names #########)
	all_files=glob.glob(path_to_Desktop+"*")
	# print( 'loading all visible files'
	all_hidden_files=glob.glob(path_to_Desktop+".*")
	# print( 'loading all hidden files'

	''' WORKING FOR VISIBLE FILES '''

	different_extensions=[]
	all_files_names=[]
	files_with_extensions={}
	all_folder_names=[]

	[different_extensions,all_files_names,files_with_extensions,all_folder_names]=common_utility(path_to_Desktop,all_files,[],[],{},[])

	# print( 'Files present in: ','\'',pathname,'\''
	# no_ext=len(different_extensions)
	# for i in xrange(0,no_ext):
	# 	values=files_with_extensions.values()[i]
	# 	for j in values:
	# 		print( j
	# 	if i != no_ext-1:
	# 		print(

	''' DONE VISIBLE '''

	''' WORKING FOR HIDDEN FILES '''

	different_hidden_extensions=[]
	all_hidden_files_names=[]
	hidden_files_with_extensions={}
	all_hidden_folder_names=[]

	[different_hidden_extensions,all_hidden_files_names,hidden_files_with_extensions,all_hidden_folder_names]=common_utility(path_to_Desktop,all_hidden_files,[],[],{},[])
	hidden_flag=len(all_hidden_files_names)
	#for windows skip all hidden files
	# print( '@@@@@@@@@@@',hidden_flag)

	''' DONE HIDDEN '''

	if len(all_files_names) == 0 and hidden_flag == 0:
		print( 'Your Desktop is already cleaned !')
		print( '------------------------------------------------')
	else:
		print( 'Moving files From: ',path_to_Desktop)
		print( 'Moving files To: ',path_to_move)

		print( 'WAIT !')
		if hidden_flag>0:
			move_files(path_to_Desktop,path_to_move,different_hidden_extensions,hidden_files_with_extensions,1)
			move_files(path_to_Desktop,path_to_move,different_extensions,files_with_extensions,0)
			#if we want to move visible files to hidden and ...
			#...hidden files in visible directories then swap 0 and 1 above
		else:
		#	print('fsd')
			if(platform_name!='Windows'):
				move_files(path_to_Desktop,path_to_move,different_extensions,files_with_extensions,0)
			else:
				move_files(path_to_Desktop,path_to_move,different_extensions,files_with_extensions,0)
		#########################################################
		print( 'MOVED !')
		print( '------------------------------------------------')
	top10()

if __name__=='__main__':
	try:
		main()
	except Exception as e:
		print( 'Error Occured Unxpectedly:',e)


