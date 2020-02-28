
import paramiko

ssh = paramiko.SSHClient()
ssh.connect(hostname="10.211.55.6", port=22, username="root", password="4433")

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
ssh.close()
