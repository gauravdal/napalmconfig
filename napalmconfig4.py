
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.10.10', 'gaurav', 'VIRL')
device.open()

print('Accessing 192.168.10.10\n')
device.load_merge_candidate(filename='ACL.cfg')


diffs = device.compare_config()
if len(diffs) > 0:
    print(diffs)
    device.commit_config()
else:
    print('No changes in ACL configuration.')
    device.discard_config()

device.load_merge_candidate(filename='ospf1.cfg')

diff_ospf = device.compare_config()
if len(diff_ospf) > 0:
    print(diff_ospf)
    device.commit_config()
else:
    print('No changes in ospf configuration')
    device.discard_config()

device.close()