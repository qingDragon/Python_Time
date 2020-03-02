import paramiko

private_key = paramiko.RSAKey.from_private_key_file("id_rsa122.txt")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.3.123',port = 22,username="yz",pkey=private_key)
stdin,stdout,stderr = ssh.exec_command("ip addr")
result = stdout.read()
print(result.decode())
ssh.close()
