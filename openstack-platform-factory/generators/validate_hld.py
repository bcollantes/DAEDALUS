import yaml
import sys

with open("../hld-model/cloud.yaml") as f:
    hld = yaml.safe_load(f)

errors = []

if hld["control_plane"]["nodes"] < 3:
    errors.append("HA requires minimum 3 controllers")

if hld["storage"]["replication"] < 3:
    errors.append("Ceph replication should be >= 3")

if len(hld["availability_zones"]) < 2:
    errors.append("Production requires at least 2 AZs")

if errors:
    for e in errors:
        print(f"ERROR: {e}")
    sys.exit(1)

print("HLD validation successful")