import os

#my_results = os.walk('/home/marcathian/try_walk')
source_directory = '/home/marcathian/OneDrive/ITOfficer/Physdev_GIS/LRTP/WholeIsland_try1'
len_source_directory = len(source_directory)
Target_directory = '/home/marcathian/OneDrive/ITOfficer/Physdev_GIS/LRTP/WholeIsland_shps_trial'
my_results = os.walk('/home/marcathian/OneDrive/ITOfficer/Physdev_GIS/LRTP/WholeIsland_try1')
print('My Results is of type: ',type(my_results))
print(my_results)

for root, dirs, files in my_results:
#for root, dirs in my_results:
    #print('This is root: ', root)
    #print('it has', len(dirs), ' Directories')
    #print('this is dirs: ', dirs)
    #print('this is files: ', files)
    for file in files:
        file_and_path =os.path.join(root,file) 
        isFile = os.path.isfile(file_and_path)
        file_extension = file_and_path[-3:]
        file_directory_path = os.path.dirname(file_and_path)
        len_file_directory_path = len(file_directory_path)
        len_file_directories = len_file_directory_path -len_source_directory
        if len_file_directories >0:
            file_directories = file_directory_path[-len_file_directories:]
        else:
            file_directories = ""
        file_target_path = os.path.join(Target_directory,file_directories.strip('/\\'))
        print(file)
        print('for', file,'at', os.path.join(root,file), 'isfile = ', isFile, 'its extension is: ',
              file_extension, 'its target folder is: ', file_target_path)
        #print('for', file,'at', os.path.join(root,file), 'isfile = ', isFile, 'its extension is: ',
              #file_extension, 'its parent folder is: ', file_directories)
        #print('for', file,'at', os.path.join(root,file), 'isfile = ', isFile, 'its extension is: ',
              #file_extension, 'its parent folder is: ', os.path.dirname(file_and_path))
        #print('for', file,'at', os.path.join(root,file), 'isfile = ', isFile, 'its extension is: ', 
              #file_extension, 'its parent folder is: ', os.path.splitext(os.path.dirname(file_and_path)))
        if os.path.isdir(file_target_path)== False:
            os.makedirs(file_target_path, 0o771, True)
        
    