import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tmux_files_exist(host):
    working_dir =  host.run('cd && pwd').stdout
    assert host.file(f'{working_dir}/.tmux.conf').exists
    assert host.file("/usr/local/bin/xpane").exists

def test_tmux_packages_installed_successfully(host):
    assert host.package("tmux").is_installed

def test_plugins_installed_successfully(host):
    plugins = ["tmux-continuum", "tmux-copycat", "tmux-open", "tmux-resurrect", "tmux-sensible", "tmux-yank", "tpm"]
    working_dir =  host.run('cd && pwd').stdout

    for plugin in plugins:
        assert host.file(f'{working_dir}/.tmux/plugins/{plugin}/').is_directory

