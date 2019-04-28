#!/usr/bin/expect -f
#!/bin/bash

exp_internal 1    ;# uncomment to turn on expect debugging



set h [lindex $argv 0]
set u [lindex $argv 1]
set s [lindex $argv 2]
set p [lindex $argv 3]

#set timeout -1

spawn ssh -o "StrictHostKeyChecking no" -D $p -N -f $u@$h

expect {
  "$u@$h*password:" { send "$s\r" }
  timeout { exit 5678 }
}
expect eof
