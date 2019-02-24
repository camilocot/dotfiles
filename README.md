dotfiles
========

Dot files

Scripts
--------------
- docker-rmstop-all.sh - remove ALL docker containers
- swap-usage.sh - get swap usage of running processes
- machine-diskutil.sh - Docker machine disk utility for mounting/unmounting shared folders


Install
--------------

```
ansible-galaxy install -r requirements.yaml
ansible-playbook playbook.yml -vvv --connection=local --ask-become-pass
```

Test
--------------

```
# There is a known issue Known with virtualenv and ansible on SELinux-enabled hosts, the workarround is to create the virtualenv with system packages enabled:
mkvirtualenv --system-site-packages molecule -p `which python3`
pip install -r requirements.txt

for role in $(ls -d ./*/)
do
    ( cd "$role" && molecule test)
done
```
