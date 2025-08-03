from netmiko import ConnectHandler
from dotenv import load_dotenv
import os
device_ip = '172.31.35.'
username = 'admin'
password = 'cisco'
load_dotenv()
privatekey = os.getenv("PRIVATE_PATH")
for i in range(1, 6):
    print("Start SSH to "+device_ip+str(i))
    device_params = {
        'device_type': 'cisco_ios',
        'host': device_ip+str(i),
        'username': 'admin',
        'use_keys': True,
        'key_file': privatekey,
        "disabled_algorithms":dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256']) 
        }
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_command("sh run | grep hostname")
        print(result.strip())