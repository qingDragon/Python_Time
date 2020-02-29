
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="10.211.55.6", port=22, username="root", password="4433")

stdin, stdout, stderr = ssh.exec_command('ls')
result = stdout.read()
print(result.decode())
ssh.close()
