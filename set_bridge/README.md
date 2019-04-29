# use expect style script
<pre><code>
$ ./tunnel_expect.sh 8.21.63.197 root Letmeon123 1234
spawn ssh -o StrictHostKeyChecking no -D 1234 -N -f root@8.21.63.197
parent: waiting for sync byte
parent: telling child to go ahead
parent: now unsynchronized from child
spawn: returns {20035}

expect: does "" (spawn_id exp4) match glob pattern "root@8.21.63.197*password:"? no
root@8.21.63.197's password: 
expect: does "root@8.21.63.197's password: " (spawn_id exp4) match glob pattern "root@8.21.63.197*password:"? yes
expect: set expect_out(0,string) "root@8.21.63.197's password:"
expect: set expect_out(spawn_id) "exp4"
expect: set expect_out(buffer) "root@8.21.63.197's password:"
send: sending "Letmeon123\r" to { exp4 }

expect: timed out

$ ps -ef|grep 1234
root     14071     1  0 16:09 ?        00:00:00 ssh -D 1234 -N -f root@8.21.63.197
</pre></code>






# use bash style script
<pre><code>
$ ./tunnel_bash.sh 8.21.63.197 root Letmeon123 1234
spawn ssh -o StrictHostKeyChecking no -D 1234 -N -f root@8.21.63.197
parent: waiting for sync byte
parent: telling child to go ahead
parent: now unsynchronized from child
spawn: returns {22752}

expect: does "" (spawn_id exp4) match glob pattern "*password*:"? no
root@8.21.63.197's password: 
expect: does "root@8.21.63.197's password: " (spawn_id exp4) match glob pattern "*password*:"? yes
expect: set expect_out(0,string) "root@8.21.63.197's password:"
expect: set expect_out(spawn_id) "exp4"
expect: set expect_out(buffer) "root@8.21.63.197's password:"
send: sending "Letmeon123\n" to { exp4 }

expect: timed out
argv[0] = expect  argv[1] = -c  argv[2] = exp_internal 1;spawn ssh -o "StrictHostKeyChecking no" -D 1234 -N -f root@8.21.63.197; expect *password*:; send "Letmeon123\n"; expect eof  
set argc 0
set argv0 "expect"
set argv ""

$ ps -ef|grep 1234
root     22798     1  0 17:54 ?        00:00:00 ssh -o StrictHostKeyChecking no -D 1234 -N -f root@8.21.63.197
</pre></code>






# start ssh agent and add ssh key
<pre><code>
$ . ginit.sh ~/.ssh/id_rsa_git passphrase
Agent pid 18224
spawn ssh-add /root/.ssh/id_rsa_git
Enter passphrase for /root/.ssh/id_rsa_git: 
Identity added: /root/.ssh/id_rsa_git (/root/.ssh/id_rsa_git)

$ ps -ef|grep ssh-agent
root     18224     1  0 20:54 ?        00:00:00 ssh-agent -s

$ ssh-add -l
4096 SHA256:5miowIOEWGkdf+M5WEFM/gewmosdf//amfdsIOFEWmdlsfsdaogefHDF /root/.ssh/id_rsa_git (RSA)
</pre></code>
