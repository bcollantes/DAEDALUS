import json
from collections import defaultdict

with open("inventory/raw/cmdb_nodes.json") as f:
    nodes = json.load(f)

active_nodes = [n for n in nodes if n["status"] == "active"]

groups = defaultdict(list)

for node in active_nodes:
    groups[node["role"]].append(node)

inventory = ""

for role, role_nodes in groups.items():
    inventory += f"[{role}s]\n"

    for node in role_nodes:
        inventory += (
            f"{node['hostname']} "
            f"ansible_host={node['mgmt_ip']} "
            f"az={node['az']} "
            f"storage_ip={node.get('storage_ip', '')} "
            f"tenant_ip={node.get('tenant_ip', '')}\n"
        )

    inventory += "\n"

with open("ansible/inventory.ini", "w") as f:
    f.write(inventory)

print("Generated ansible/inventory.ini from CMDB")