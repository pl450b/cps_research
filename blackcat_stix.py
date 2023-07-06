from stix2 import *

# Creates a full bundle and prints out the JSON content
# Pass each SDO/SRO to the `Bundle()` contructor
bundle = Bundle()
print(bundle.serialize(pretty=True))

# Send to a local json file to give to online viewer
with open('view.json', 'w') as json_file:
    json_file.write(bundle.serialize(pretty=True))