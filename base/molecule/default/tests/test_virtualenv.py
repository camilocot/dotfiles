import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_virtualenv_packages_installed_successfully(host):
    if host.system_info.distribution == 'ubuntu' or host.system_info.distribution == 'debian':
        assert host.package("python-virtualenv").is_installed
        assert host.package("virtualenvwrapper").is_installed
    elif host.system_info.distribution == 'fedora' or host.system_info.distribution == 'centos':
        assert host.package("python2-virtualenv").is_installed
        assert host.package("python2-virtualenvwrapper").is_installed
        assert host.package("python3-virtualenv").is_installed
        assert host.package("python3-virtualenvwrapper").is_installed
    else:
        assert host.package("python2-virtualenv").is_installed
