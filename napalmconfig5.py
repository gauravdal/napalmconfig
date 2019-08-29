
import json
from napalm import get_network_driver

ip_addresses = ['192.168.10.10,'
                '192.168.10.1']

for each_ip in ip_addresses:
    print('\n\n')
    print('Accessing'+str(each_ip) +'...!')
    print('\n\n')
    driver = get_network_driver('ios')
    device = driver(each_ip,'gaurav','VIRL')
    device.open()


    device.load_merge_candidate(filename='ACL.cfg')


    diffs = device.compare_config()
    if len(diffs) > 0:
        print(diffs,'\n')
        device.commit_config()
    else:
        print('No changes in ACL configuration.')
        device.discard_config()

    device.load_merge_candidate(filename='ospf1.cfg')

    diff_ospf = device.compare_config()
    if len(diff_ospf) > 0:
        print(diff_ospf,'\n')
        device.commit_config()
    else:
        print('No changes in ospf configuration')
        device.discard_config()

    device.close()