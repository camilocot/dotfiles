import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_kubectx_installed_successfully(host):
    working_dir =  host.run('cd && pwd').stdout

    files = ["kubectx", "kubens"]

    for f in files:
        assert host.file(f'{working_dir}/bin/{f}').is_symlink
        assert host.file(f'{working_dir}/bin/{f}').linked_to == f'{working_dir}/projects/kubectx/{f}'

