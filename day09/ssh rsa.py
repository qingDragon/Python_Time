

import paramiko

private_key = paramiko.RSAKey.from_private_key_file("id_rsa.txt")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="10.211.55.7",port=22,username="yz",pkey=private_key)

stdin,stdout,stderr = ssh.exec_command("ifconfig")
result = stdout.read()

print(result.decode())
ssh.close()