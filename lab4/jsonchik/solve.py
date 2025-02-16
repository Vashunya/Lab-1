import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")


with open("/Users/vashunya/Desktop/tets1/lab4/jsonchik/sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    
    print(f"{dn:<50}                      {speed:<8}  {mtu:<6}")