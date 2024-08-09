import pandas as pd

df = pd.read_csv('export_objects_address_groups_08072024_125717gmt+5_30.csv')

def generate_output(df):
    outputs = []
    for name, group in df.groupby('Name'):
        addresses = group['Addresses'].str.split(';').explode().unique()  
        addresses = [address for address in addresses if address]  s
        
        if addresses:
            output = f'''
edit "{name}"
    set member {" ".join(f'"{address}"' for address in addresses)}
next
'''
            outputs.append(output)
    return ''.join(outputs)

output = generate_output(df)

with open('output_file.txt', 'w') as file:
    file.write(output.strip())
