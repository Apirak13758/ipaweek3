from netmiko import ConnectHandler
from dotenv import load_dotenv
import re
import os
def createdevice(ip):
    load_dotenv()
    privatekey = os.getenv("PRIVATE_PATH")
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'use_keys': True,
        'key_file': privatekey,
        "disabled_algorithms":dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256'])
    }
    return device

network = "172.31.35."
router = []
router.append(createdevice(network+"4"))
router.append(createdevice(network+"5"))

for i in range(2):
    router_connection = ConnectHandler(**router[i])
    int_br = router_connection.send_command("sh ip int br")
    acitve_interfaces = re.findall("(\\w*\\d\\/\\d)(?:.*up.*)", int_br)
    print("R"+str(i+1)+" active interfaces :\n", *acitve_interfaces)
    version = router_connection.send_command("sh version")
    match = re.search(" uptime is \\d+ hour, \\d+ minutes", version)
    print(match.group(0))
    router_connection.disconnect()