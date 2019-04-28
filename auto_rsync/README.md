# async

V0: spawn rsync from remote to current host
latest: spawn rsync from remote to current host, or current to remote host.

./async.sh 8.111.251.134 "" username password /mnt/a.txt /mnt/	#copy file 8.111.251.134:/mnt/a.txt to local:/mnt/a.txt
./async.sh "" 8.111.251.134 username password /mnt/a.txt /mnt/	#copy file local:/mnt/a.txt to 8.111.251.134:/mnt/a.txt
