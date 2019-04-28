#!/bin/bash

if [ $# -ne 2 ] ; then
        echo "Usage: gint.sh keyfile passphrase"
        exit 1
fi

#if [ -z "$SSH_AUTH_SOCK" ]; then
        eval "$(ssh-agent -s)"
#fi

expect << EOF
        spawn ssh-add $1
        expect "Enter passphrase"
        send "$2\r"
        expect eof
EOF

