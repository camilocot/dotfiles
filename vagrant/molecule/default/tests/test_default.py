import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vagrant_package_installed_successfully(host):
    packages = ["vagrant"]

    for package in packages:
        assert host.package(f'{package}').is_installed
