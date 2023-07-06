from stix2 import *

# Creates a full bundle and prints out the JSON content
# Pass each SDO/SRO to the `Bundle()` contructor
bundle = Bundle()
print(bundle.serialize(pretty=True))