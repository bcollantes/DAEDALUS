import json
import os
import requests

CMDB_URL = os.getenv("CMDB_URL")
CMDB_TOKEN = os.getenv("CMDB_TOKEN")

headers = {
    "Authorization": f"Bearer {CMDB_TOKEN}",
    "Accept": "application/json"
}

response = requests.get(
    f"{CMDB_URL}/api/nodes?environment=prod&platform=openstack",
    headers=headers,
    timeout=30
)

response.raise_for_status()

nodes = response.json()

with open("inventory/raw/cmdb_nodes.json", "w") as f:
    json.dump(nodes, f, indent=2)

print(f"Imported {len(nodes)} nodes from CMDB")