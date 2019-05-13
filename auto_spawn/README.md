# async

V0: spawn rsync from remote to current host
latest: spawn rsync from remote to current host, or current to remote host.

./async.sh 8.111.251.134 "" username password /mnt/a.txt /mnt/	#copy file 8.111.251.134:/mnt/a.txt to local:/mnt/a.txt
./async.sh "" 8.111.251.134 username password /mnt/a.txt /mnt/	#copy file local:/mnt/a.txt to 8.111.251.134:/mnt/a.txt



# aspawn

#$ ssh 8.21.49.57 ls -l --time-style='+%Y%m%d' /source/file | awk '{print $6}'
#$ ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print $6}'
#$ ./aspawn.sh letmeOn321 "ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print \$6}'"
#$ ./aspawn.sh letmeOn321 "rsync -av --progress root@8.21.49.57:/source/file /destination/"
#$ ./aspawn.sh Letmein123 "rsync -av --progress /source/file root@9.111.254.192:/destination/"
