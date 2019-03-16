import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_base_packages_installed_successfully(host):
    packages = ["make", "htop", "git", "httpie", "curl", "most", "jq", "wireshark", "highlight", "snapd", "socat", "mtr", "socat", "ngrep"]
    bin_files = ["pip2", "pip3", "ruby"]

    for package in packages:
        assert host.package(f'{package}').is_installed

    for f in bin_files:
        assert host.file(f'/usr/bin/{f}').is_file

def test_base_directories_exists(host):
    working_dir =  host.run('cd && pwd').stdout
    directories = ["projects", "bin"]

    for directory in directories:
        assert host.file(f'{working_dir}/{directory}').is_directory
