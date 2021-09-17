#!/usr/bin/expect -f
# exp_internal 1    ;# uncomment to turn on expect debugging

# usage: ./ahypersync.sh 8.30.204.204 "" root password /wks/kode/wksp/project/subprojects/db/build/ reports /mnt/
#        this will go to remote /wks/kode/wksp/project/subprojects/db/build/, compress folder reports to reports.tar.gz, then rsync it back as /mnt/reports.tar.gz
#       ./ahypersync.sh "" 8.30.204.204 root password /mnt/ reports /wks/kode/wksp/project/subprojects/db/build/
#        this will go to local /mnt/, compress folder reports to reports.tar.gz, then rsync it to remote as /wks/kode/wksp/project/subprojects/db/build/reports.tar.gz



set source_hostname [lindex $argv 0]
set destination_hostname [lindex $argv 1]
set username [lindex $argv 2]
set password [lindex $argv 3]
set source_folder_path [lindex $argv 4]
set source_folder_name [lindex $argv 5]
set destination_folder_path [lindex $argv 6]
puts "$source_folder_path"

set timeout -1

if { $source_hostname != "" } {
  spawn ssh $username@$source_hostname "pushd $source_folder_path && rm -rf ${source_folder_name}.tar.gz && tar -cvzf ${source_folder_name}.tar.gz $source_folder_name && popd"
} else {
  spawn bash
  send "pushd $source_folder_path && rm -rf ${source_folder_name}.tar.gz && tar -cvzf ${source_folder_name}.tar.gz $source_folder_name && popd && exit\r"
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
#expect EOF


if { $source_hostname != "" } {
  spawn rsync -av --progress $username@$source_hostname:$source_folder_path/${source_folder_name}.tar.gz $destination_folder_path
} else {
  spawn rsync -av --progress $source_folder_path/${source_folder_name}.tar.gz $username@$destination_hostname:$destination_folder_path
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
expect EOF
