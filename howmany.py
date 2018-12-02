#!/usr/bin/env python3

import os

def Main():

    commands = {}
    file = open(os.path.expanduser('~') + "/.bash_history", "r")
    for line in file:
        try:
            # In case if there is a space before the command
            pointer = line.index(" ")
            command = line[:pointer]
        except:
            command = line
        command = command.replace("\n", " ")
        if command not in commands:
            commands[command] = 1
        else:
            commands[command] += 1

    file.close()
    i = 0
    for key in sorted(commands, key=commands.__getitem__, reverse=True):
        if i == 10:
            break
        print(key + ": " + str(commands[key]))
        i +=1

if __name__ == "__main__":
    Main()
