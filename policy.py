
import csv

def format_addresses(addresses):
    return ' '.join([f'"{addr.strip()}"' for addr in addresses.split(';')])

def format_interfaces(interfaces):
    return ' '.join([f'"{iface.strip()}"' for iface in interfaces.split(';')])

def generate_config(row, edit_number):
    name, srcintf, srcaddr, srcuser, srchip, dstintf, dstaddr, app, service, action, profile, options = row


    edit_suffix = f"{edit_number:02d}"[-2:]
    if len(name) > 35:
        name = name[:33] + edit_suffix

    
    services = [s.replace('tcp', 'tcp') for s in service.split(';')]
    services_str = ' '.join([f'"{s}"' for s in services])


    action = action.strip().replace('allow', 'accept')

    config = f"""edit {edit_number}
set name "{name.strip()}"
set srcintf {format_interfaces(srcintf.strip())}
set dstintf {format_interfaces(dstintf.strip())}
set srcaddr {format_addresses(srcaddr.strip())}
set dstaddr {format_addresses(dstaddr.strip())}
set action {action}
set service {services_str}
set schedule "always"
set logtraffic all
next
"""
    return config

def process_csv(input_csv, output_file):
    with open(input_csv, 'r') as csvfile, open(output_file, 'w') as outfile:
        reader = csv.reader(csvfile)
        next(reader)  
        edit_number = 100

        for row in reader:
            config = generate_config(row, edit_number)
            outfile.write(config)
            edit_number += 1

if __name__ == "__main__":
    input_csv = 'export_policies_security_rulebase_08062024_112531gmt+5_30.csv'
    output_file = 'generated_config.txt'
    process_csv(input_csv, output_file)
