import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_run_microk8s_successfully(host):
    microk8s_ran = host.run("/snap/bin/microk8s.status")

    assert 'microk8s is running' in microk8s_ran.stdout
