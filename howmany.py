#!/usr/bin/env python3

import os
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description="See your favorite bash commands!")
parser.add_argument("-n", "--number", type=int, default=10, help="The number of commands to print")

args = parser.parse_args()

def Main():
    # print the commands
    commands = get_command_list()
    number = args.number
    i = 0
    for key in sorted(commands, key=commands.__getitem__, reverse=True):
        if i == number:
            break
        print(key + ": " + str(commands[key]))
        i +=1

def get_command_list():
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
    return commands;

if __name__ == "__main__":
    Main()
