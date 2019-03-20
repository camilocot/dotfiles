import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_has_zsh_as_sh(host):
    username = host.run("whoami").stdout
    user = host.user(username)
    assert user.shell == "/usr/bin/zsh"

def test_oh_my_shell_is_installed_successfully(host):
    files = [".oh-my-zsh", ".zsh_nocorrect", ".zshrc"]
    working_dir = host.run("cd && pwd").stdout

    for f in files:
        assert host.file(f'{working_dir}/{f}').exists

