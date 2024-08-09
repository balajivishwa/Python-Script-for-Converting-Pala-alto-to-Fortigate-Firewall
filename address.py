
import pandas as pd
import ipaddress


df = pd.read_csv('export_objects_addresses_08072024_115514gmt+5_30.csv')


def cidr_to_netmask(cidr):
    return str(ipaddress.IPv4Network(f'0.0.0.0/{cidr}', strict=False).netmask)

def generate_output(row):
    name = row['Name']
    type_ = row['Type']
    address = row['Address']

    if type_ == 'IP Netmask':
        if '/' in address:
            ip, cidr = address.split('/')
            netmask = cidr_to_netmask(cidr)
            return f'''
edit "{name}"
    set subnet {ip} {netmask}
next
'''
        else:
            return f'''
edit "{name}"
    set subnet {address} 255.255.255.255
next
'''

    return ''

outputs = df.apply(generate_output, axis=1)

with open('output_file.txt', 'w') as file:
    for output in outputs:
        file.write(output.strip() + '\n')
