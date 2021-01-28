#! /usr/bin/python3
import os, sys, re



#usage:
#1. drag similar topic of tabs to one window
#2. bookmark all tabs in the window
#3. go to bookmark management page, select all and copy, the urls are copied
#4. go to surls.txt, add ______name, and paste in surls.txt
#______surfing
#https://www.sina.com
#https://www.google.com
#https://www.baidu.com
#______studying
#https://stackoverflow.com
#https://reddit.com
#5. try restore from surls.txt, topic related urls are opened in a new window as specified browser type
# python opentabs.py firefox surls.txt ______routine_affair_a
# python opentabs.py firefoxd surls.txt ______org_project_a
# python opentabs.py chromium surls.txt ______patent_topic_a
# python opentabs.py chrome surls.txt ______global_topic_a
# python opentabs.py surls.txt vivaldi ______life_topic_a
#6. clean up bookmarks generated in step 3 from browser



#with open(sys.argv[2], 'r') as file:
#    urls = file.read().replace('\r', ' ').replace('\n', ' ')

#with open(sys.argv[2], 'r') as file:
#   for line in file:
#       if sys.argv[3] in line:
#            urls += line + " "
#            break

inRecordingMode = False
urls = ""
with open(sys.argv[2], 'r') as file:
    for line in file:
        line = line.split(' ', 1)[0].split("\t", 1)[0]
        if not inRecordingMode:
            if line.startswith(sys.argv[3]):
                inRecordingMode = True
        elif line.startswith('______'):
            inRecodingMode = False
            break
        else:
            urls += " '" + line.replace('\r', ' ').replace('\n', ' ').rstrip() + "' "

urls = re.sub(' +', ' ', urls).rstrip().replace(' ', ' -url ')
print urls
exit()



browserTypes = {
    "firefox": "/Applications/Firefox.app",
    "firefoxd": "/Applications/Firefox\ Developer\ Edition.app",
    "chrome": "/Applications/Google\ Chrome.app",
    "chromium": "/Applications/Chromium.app",
    "vivaldi": "/Applications/Vivaldi.app"
}



os.system("open -na " + browserTypes[sys.argv[1]] + " --args --new-window " + urls)
