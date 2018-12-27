import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_run_hello_world_container_successfully(host):
    hello_world_ran = host.run("docker run hello-world")

    assert 'Hello from Docker!' in hello_world_ran.stdout
