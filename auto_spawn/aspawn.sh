#!/usr/bin/expect -f
# exp_internal 1    ;# uncomment to turn on expect debugging



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
