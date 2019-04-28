#!/usr/bin/expect -f
# exp_internal 1    ;# uncomment to turn on expect debugging



set source_hostname [lindex $argv 0]
set destination_hostname [lindex $argv 1]
set username [lindex $argv 2]
set password [lindex $argv 3]
set source_file [lindex $argv 4]
set destination_file [lindex $argv 5]

set timeout -1

if { $source_hostname != "" } {
  spawn rsync -av --progress $username@$source_hostname:$source_file $destination_file
} else {
  spawn rsync -av --progress $source_file $username@$destination_hostname:$destination_file
}

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
