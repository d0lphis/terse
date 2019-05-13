#!/usr/bin/expect -f
#!/bin/bash

# exp_internal 1    ;# uncomment to turn on expect debugging

set timeout -1



set password [lindex $argv 0]
set command [lindex $argv 1]

#log_user 0

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

#log_user 1

expect EOF

#expect -re \"*\"
#set var $expect_out(1,string)
#set val $expect_out(buffer)
#puts $var

#set var [lindex [split $::expect_out(buffer) \n] 0]
