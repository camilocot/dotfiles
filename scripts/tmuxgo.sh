#!/bin/bash
SESSION=$USER

tmux -2 new-session -d -s $SESSION

# Setup a window for tailing log files
tmux new-window -t $SESSION:1 -n 'TMUX'
tmux split-window -h
tmux select-pane -t 0
tmux send-keys "vim" C-m
tmux select-pane -t 1
tmux split-window -v

# Attach to session
tmux -2 attach-session -t $SESSION
