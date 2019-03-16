import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_base_files_exist(host):
    working_dir =  host.run('cd && pwd').stdout
    files = [".digrc", ".netrc", ".curlrc", ".inputrc", ".pythonrc"]
    git_files = [".gitignore", ".gitconfig", ".gitmessage"]
    scripts = ["docker-rmstop-all.sh", "machine-diskutil.sh", "swap-usage.sh"]

    for f in files:
        assert host.file(f'{working_dir}/{f}').is_file
        assert host.file(f'{working_dir}/{f}').mode == 0o600

    for f in git_files:
        assert host.file(f'{working_dir}/{f}').is_file

    for f in scripts:
        assert host.file(f'{working_dir}/bin/{f}').is_file
        assert host.file(f'{working_dir}/bin/{f}').mode == 0o750

    assert host.file("/usr/local/bin/ktail").is_file
    assert host.file("/usr/local/bin/ktail").mode == 0o755
