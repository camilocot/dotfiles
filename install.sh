#!/bin/bash

containsElement () {
  local e
  for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
  return 1
}

git submodule update --init --recursive

copyFiles=("_gitconfig")
for f in `find ./ -maxdepth 1 -name _\* -printf '%f\n'`;
do
    if containsElement $f $copyFiles; then
        command="cp"
    else
        command="ln -s"
    fi
    echo $command `pwd`/$f ~/${f/_/.}
done

