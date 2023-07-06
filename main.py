from stix2 import *

ta505 = ThreatActor(name="TA505",
                    description="The creators of CL0P ransomware")

bundle = Bundle(ta505)
print(bundle.serialize(pretty=True))