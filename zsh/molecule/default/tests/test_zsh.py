import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vagrant_user_has_zsh_as_sh(host):
    vagrant = host.user("vagrant")
    assert vagrant.shell == "/usr/bin/zsh"

def test_oh_my_shell_is_installed_successfully(host):
    assert host.file("/home/vagrant/.oh-my-zsh").exists
    assert host.file("/home/vagrant/.zsh_nocorrect").exists
    assert host.file("/home/vagrant/.zshrc").is_symlink
    assert host.file("/home/vagrant/.zshrc").linked_to == "/home/vagrant/.oh-my-zsh/templates/zshrc.zsh-template"

