import yaml

with open("../hld-model/cloud.yaml") as f:
    hld = yaml.safe_load(f)

doc = f"""
# OpenStack HLD

## Región
{hld['region']}

## Availability Zones
{", ".join(hld['availability_zones'])}

## Compute
Hypervisor: {hld['compute']['hypervisor']}

## Networking
Backend: {hld['network']['backend']}

## Storage
Backend: {hld['storage']['backend']}
Replication: {hld['storage']['replication']}
"""

with open("../docs/index.md", "w") as f:
    f.write(doc)