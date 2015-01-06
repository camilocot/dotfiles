#!/bin/bash

containsElement () {
  local e
  for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
  return 1
}

git submodule update --init --recursive

echo "Please enter your email: "
read email

copyFiles=("_gitconfig")
for f in `find ./ -maxdepth 1 -name _\* -printf '%f\n'`;
do
    dest=${f/_/.}

    if containsElement $f $copyFiles; then
        command="cp"
    else
        command="ln -s"
    fi

    if [[ -f ~/$dest || -d ~/$dest ]]; then
        mv ~/$dest ~/$dest.bak
    fi
    $command `pwd`/$f ~/$dest

done

sed -i "s/\(email =\).*/\1 ${email}/" ~/.gitconfig
