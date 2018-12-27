import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_base_packages_installed_successfully(host):

    assert host.package("build-essential").is_installed
    assert host.package("htop").is_installed
    assert host.package("git").is_installed
    assert host.package("python-pip").is_installed
    assert host.package("python3-pip").is_installed
    assert host.package("httpie").is_installed
    assert host.package("curl").is_installed
    assert host.package("most").is_installed

def test_base_directories_exists(host):
    assert host.file("/home/vagrant/projects").is_directory
    assert host.file("/home/vagrant/bin").is_directory
