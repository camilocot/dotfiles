import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_set_selinux_permissive_successfully(host):
    sestatus_ran = host.run("sestatus")

    assert  len(re.findall(r'^Current mode:\s+permissive$', sestatus_ran.stdout, flags=re.MULTILINE)) == 1
