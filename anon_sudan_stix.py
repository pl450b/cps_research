from stix2 import *

# ----- Threat Actors -----
anonSu = ThreatActor(name="Anoymous Sudan",
                    description="Hacktivist group")

killnet = ThreatActor(name="KILLNET",
                      description="Russia-aligned hacktivist group, specialized in DDoS attacks")

revil = ThreatActor(name="REvil",
                      description="Russian based RaaS operation. Would post the contents of attack \
                      on their \"Happy Blog\" site. Russian Federal Security Service says they dismantled \
                        the group and charged several of it's members")


# ----- Campaigns -----
microsoft = Campaign(name="Microsoft Office Attack",
                     description="Anonymous Sudan attacks microsoft servers with a DDoS attack",
                     aliases="Storm-1359")
# russia_ukraine = Campaign()

# ----- Attack Patterns -----

# ----- Object Lists -----
threat_list = [anonSu, killnet, revil]
campaign_list = [microsoft]
pattern_list = []

# Creates a full bundle and prints out the JSON content
# Pass each SDO/SRO to the `Bundle()` contructor
bundle = Bundle(threat_list, campaign_list, pattern_list)
print(bundle.serialize(pretty=True))

# Send to a local json file to give to online viewer
with open('view.json', 'w') as json_file:
    json_file.write(bundle.serialize(pretty=True))