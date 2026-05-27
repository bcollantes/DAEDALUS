import yaml
from jinja2 import Template

with open("../hld-model/cloud.yaml") as f:
    hld = yaml.safe_load(f)

network_template = """
resource "openstack_networking_network_v2" "provider" {
  name = "{{ provider.name }}"
}

resource "openstack_networking_subnet_v2" "tenant" {
  name       = "tenant-subnet"
  cidr       = "10.0.0.0/24"
  ip_version = 4
}
"""

template = Template(network_template)

rendered = template.render(
    provider=hld["network"]["provider_networks"][0]
)

with open("../terraform/networks.tf", "w") as f:
    f.write(rendered)