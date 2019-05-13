# async

V0: spawn rsync from remote to current host
latest: spawn rsync from remote to current host, or current to remote host.

./async.sh 8.111.251.134 "" username password /mnt/a.txt /mnt/	#copy file 8.111.251.134:/mnt/a.txt to local:/mnt/a.txt
./async.sh "" 8.111.251.134 username password /mnt/a.txt /mnt/	#copy file local:/mnt/a.txt to 8.111.251.134:/mnt/a.txt



# aspawn

#$ ssh 8.21.49.57 ls -l --time-style='+%Y%m%d' /source/file | awk '{print $6}'
#$ ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print $6}'
#$ var=$(./aspawn.sh password "ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print \$6}'"|tail -1)
#$ ./aspawn.sh password "ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print \$6}'"
#$ ./aspawn.sh password "rsync -av --progress root@8.21.49.57:/source/file /destination"
#$ ./aspawn.sh password "rsync -av --progress /source/file root@8.111.254.192:/destination"
