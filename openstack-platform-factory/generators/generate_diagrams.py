import yaml

with open("../hld-model/cloud.yaml") as f:
    hld = yaml.safe_load(f)

diagram = f"""
flowchart TB

VIP[API VIP]

CTRL1[controller-01]
CTRL2[controller-02]
CTRL3[controller-03]

VIP --> CTRL1
VIP --> CTRL2
VIP --> CTRL3

CEPH[(Ceph Cluster)]

CTRL1 --> CEPH
CTRL2 --> CEPH
CTRL3 --> CEPH
"""

with open("../diagrams/openstack-ha.mmd", "w") as f:
    f.write(diagram)