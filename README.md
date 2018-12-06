dotfiles
========

Dot files

Scripts
--------------
- download_jdk_8u60.sh - download jdk 8_60 from Oracle web
- supercat.sh - pygmentize file
- tmuxgo.sh - default layout for tmux
- wine-smooth-fonts.sh - set wine smooth font

tmux (> 2.4) install
------------

1. Install Tmux Plugin Manager
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
2. Install plugins
Press prefix + I (capital I, as in Install) to fetch the plugin.

kubectx / kube-ps1
------------
git clone https://github.com/ahmetb/kubectx ~/kubectx
git clone https://github.com/jonmosco/kube-ps1 ~/kube-ps1
ln -s ~/kubectx/kubens ~/bin/
ln -s ~/kubectx/kubectx ~/bin/



Requirements
--------------
- tmux > 2.4
- [highlight](http://www.andre-simon.de/doku/highlight/en/highlight.php)
- [fzf](https://github.com/junegunn/fzf)
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
- [kube-ps1](https://github.com/jonmosco/kube-ps1/)
- [kubectx](https://github.com/ahmetb/kubectx)
- [tmux-xpanes](https://github.com/greymd/tmux-xpanes)
