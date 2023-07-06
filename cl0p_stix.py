from stix2 import *

# SDO Creation
ta505 = ThreatActor(name="TA505",
                    description="Title given to this group by Proofpoint")

group_g0092 = ThreatActor(name="Group G0092",
                          description="Title given to this group by MITRE")

lace_tempest = ThreatActor(name="Lace Tempest",
                           description="Title given to this group by Microsoft")

graceful_spider = ThreatActor(name="Graceful Spider",
                              description="Title given to this group by Crowdstrike")

fin11_unc2546 = ThreatActor(name="FIN11, UNC2546",
                            description="Title given to this group by Mandiant")

hive0065 = ThreatActor(name="Hive0065",
                       description="Title given to this group by IBM X-Force")

dev0950 = ThreatActor(name="DEV0950",
                      description="Title given to this group by Microsoft (outdated)")

odinaff = ThreatActor(name="Odinaff",
                      description="Title given to this group by Symantec")


relationship = Relationship(relationship_type='BEEF',
                            source_ref=ta505.id,
                            target_ref=dev0950.id)

# Creates a full bundle and prints out the JSON content
# Pass each SDO/SRO to the `Bundle()` contructor
bundle = Bundle(ta505, group_g0092, graceful_spider, fin11_unc2546, hive0065, dev0950, odinaff, relationship)
print(bundle.serialize(pretty=True))

# Send to a local json file to give to online viewer
with open('view.json', 'w') as json_file:
    json_file.write(bundle.serialize(pretty=True))