
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.10.10', 'gaurav', 'VIRL')
device.open()

print('Accessing 192.168.10.10\n')
device.load_merge_candidate(filename='ACL.cfg')
device.commit_config()
device.close()
