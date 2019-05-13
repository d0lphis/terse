#!/usr/bin/expect -f
# exp_internal 1    ;# uncomment to turn on expect debugging



#$ ssh 8.21.49.57 ls -l --time-style='+%Y%m%d' /source/file | awk '{print $6}'
#$ ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print $6}'
#$ ./aspawn.sh letmeOn321 "ssh 8.21.49.57 ls -l --time-style=+%Y%m%d /source/file | awk '{print \$6}'"
#$ ./aspawn.sh letmeOn321 "rsync -av --progress root@8.21.49.57:/source/file /destination/"
#$ ./aspawn.sh Letmein123 "rsync -av --progress /source/file root@9.111.254.192:/destination/"



set password [lindex $argv 0]
set command [lindex $argv 1]

set timeout -1

set esc_cmd [exec echo $command | sed s/\\$/\\\\\$/g]
eval "spawn $esc_cmd"

expect {
  "*continue connecting (yes/no)?*" {
    send "yes\r"
    expect {
      "*assword*" {
        send "$password\r"
      }
    }
  }
  "*assword*" {
    send "$password\r"
  }
}
#send "sudo -s\r"
#send "cd /data/logs\r"
#interact
expect EOF
