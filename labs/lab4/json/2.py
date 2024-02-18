import json

# Load JSON data from file
with open('vscode/kbtu/pp2/labs/lab4/json/sample-data.json') as f:
    data = json.load(f)

# Extract interface status information
interface_status = []
for item in data['imdata']:
    if 'l1PhysIf' in item:
        attributes = item['l1PhysIf']['attributes']
        interface_status.append({
            'DN': attributes.get('dn', ''),
            'Description': attributes.get('descr', ''),
            'Speed': attributes.get('speed', ''),
            'MTU': attributes.get('mtu', '')
        })

# Print output header
print("Interface Status")
print("=" * 80)
print("{:<50}{:<25}{:<10}{:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface status data
for interface in interface_status:
    print("{:<50}{:<25}{:<10}{:<10}".format(interface['DN'], interface['Description'], interface['Speed'], interface['MTU']))
