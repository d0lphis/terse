import os, sys

folder_path = sys.argv[1]
files = os.listdir(folder_path)
keyword = 'URL='
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        f = open(os.path.join(folder_path, file),'r')
        url = None
        for x in f:
            if keyword in x:
                url = x.replace(keyword, "").replace("\n", "")
                break
        f.close()
        sys.stdout.write(url + '\t' + file + '\n')