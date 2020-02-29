

import paramiko
transport = paramiko.Transport(('10.211.55.6',22))
transport.connect(username='root',password='4433')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('location.txt','location.txt')
sftp.get('test.dd','test.dd')

transport.close()