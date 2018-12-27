import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_kubectx_installed_successfully(host):
    assert host.file("/home/vagrant/bin/kubectx").is_symlink
    assert host.file("/home/vagrant/bin/kubectx").linked_to == "/home/vagrant/projects/kubectx/kubectx"
    assert host.file("/home/vagrant/bin/kubens").is_symlink
    assert host.file("/home/vagrant/bin/kubens").linked_to == "/home/vagrant/projects/kubectx/kubens"

