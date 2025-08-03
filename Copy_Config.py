import paramiko
import os
import time
from dotenv import load_dotenv
load_dotenv()
privatekey = os.getenv("PRIVATE_PATH")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
network='172.31.38.'
device_list = ['R0', 'R1', 'R2', 'S0', 'S1']
for i in range(1, 6):
    ssh.connect(hostname=network+str(i), 
                username='admin', 
                key_filename=privatekey,
                allow_agent=False,
                look_for_keys=False, 
                disabled_algorithms=dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256']))
    print("connected to "+network+str(i))
    stdin, stdout, stderr = ssh.exec_command("sh run")
    with open('{}_config'.format(device_list[i-1]), 'w') as file:
        file.write(stdout.read().decode())
    print("Saved {} running config file {}_config".format(device_list[i-1], device_list[i-1]))
    ssh.close()