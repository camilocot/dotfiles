import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_find_snad_installed(host):
    snap_list_ran = host.run("snap list")

    assert 'spotify' in microk8s_ran.stdout
    assert 'microk8s' in microk8s_ran.stdout
