from stix2 import *

# SDO Creation
ta505 = ThreatActor(name="TA505",
                    description="The creators of CL0P ransomware")

# Creates a full bundle and prints out the JSON content
# Pass each SDO/SRO to the `Bundle()` contructor
bundle = Bundle(ta505)
print(bundle.serialize(pretty=True))