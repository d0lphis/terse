#! /usr/bin/python3
import webbrowser, sys

if len(sys.argv) < 3:
    print("Usage: openinbrowser.py ./urls.txt 20")
    quit()

f = open(sys.argv[1])
tabs = int(sys.argv[2])

#webbrowser.register('mychrome', None, webbrowser.MacOSXOSAScript('Google Chrome'), -1)
#browser = webbrowser.get('mychrome')

counter = 1
for url in f:
    if counter == 1:
        webbrowser.get('open -na /Applications/Google\ Chrome.app --args --new-window %s').open(url.rstrip())
    else:
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open(url.rstrip())
    counter += 1
    if counter == tabs:
        input("Press any key to continue...")
        counter = 1