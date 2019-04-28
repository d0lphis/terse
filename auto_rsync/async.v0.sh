#!/usr/bin/expect -f
# exp_internal 1    ;# uncomment to turn on expect debugging



set hostname [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
set source  [lindex $argv 3]
set destination [lindex $argv 4]

set timeout -1

spawn rsync -av --progress $username@$hostname:$source $destination
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
