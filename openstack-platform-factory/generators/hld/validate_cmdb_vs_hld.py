import json
import yaml
import sys
from collections import Counter

with open("hld-model/cloud.yaml") as f:
    hld = yaml.safe_load(f)

with open("inventory/raw/cmdb_nodes.json") as f:
    nodes = json.load(f)

active_nodes = [n for n in nodes if n["status"] == "active"]

errors = []

roles = Counter(n["role"] for n in active_nodes)

if roles["controller"] != hld["control_plane"]["nodes"]:
    errors.append(
        f"Controller mismatch: HLD={hld['control_plane']['nodes']} CMDB={roles['controller']}"
    )

for az, expected_count in hld["compute"]["nodes"].items():
    actual_count = len([
        n for n in active_nodes
        if n["role"] == "compute" and n["az"] == az
    ])

    if actual_count != expected_count:
        errors.append(
            f"Compute mismatch in {az}: HLD={expected_count} CMDB={actual_count}"
        )

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("CMDB inventory matches HLD")