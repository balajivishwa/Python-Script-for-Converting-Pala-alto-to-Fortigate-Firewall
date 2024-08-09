import csv

def format_entry(count, destination, nexthop, interface):
    return f'''
edit {count}
    set dst {destination}
    set gateway {nexthop}
    set device "{interface}"
next
    '''

def generate_output(csv_filename, output_filename):
    with open(csv_filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = []
        count = 4  # Starting count value
        for row in reader:
            destination = row['destination']
            nexthop = row['nexthop']
            interface = row['Interface']
            entries.append(format_entry(count, destination, nexthop, interface))
            count += 1

    with open(output_filename, mode='w') as outfile:
        outfile.write("\n".join(entries))

generate_output('PA_Route_List.csv', 'output.txt')
