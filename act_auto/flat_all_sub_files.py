import os, sys, shutil

# python flat_all_sub_files.py C:\Users\Will\Desktop\sort\0b0d4006cfac9fef4d061ba98c7bce18\image2 C:\Users\Will\Desktop\sort\0b0d4006cfac9fef4d061ba98c7bce18\image2jpg

src_path = sys.argv[1]	#folder contains many sub folders with pictures
des_path = sys.argv[2]	#destination folder to contain all pictures in sub folders
print(len(sys.argv))
if len(sys.argv) == 4:
    suffix = sys.argv[3]
else:
    suffix = ''

def get_file_list(path):
    file_list = []
    i = 0
    for root, dirs, files in os.walk(path):
        #print('root_dir:', root)
        #print('sub_dirs:', dirs)
        #print('files:', files)
        for file in files:
            file_full_name = os.path.join(root, file)
            file_list.append(file_full_name)
            sys.stdout.write("\rFiles traversed 0 -> {:d}.".format(i))
            i += 1
    return file_list
file_list = get_file_list(src_path)

os.makedirs(des_path)
for file_full_name in file_list:
    print(file_full_name)
    shutil.copy(file_full_name, os.path.join(des_path, os.path.basename(file_full_name) + suffix))
