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
        print("%-8s  : %4d" % (key, commands[key]))
        i +=1

def get_command_list():
    command_number = 0
    commands = {}
    file = open(os.path.expanduser('~') + "/.bash_history", "r")
    command_number += 1
    # debug file
    #file = open(os.path.expanduser('~') + "/Projects/Python/howmany/tests/test.txt", "r")
    for line in file:
        command = get_command(line)

        # if command is sudo, ignore it and take the next word
        if command == "sudo":
            line = line[5:]
            command = get_command(line)

        if command not in commands:
            commands[command] = 1
        else:
            commands[command] += 1

    file.close()
    return commands;

def get_command(line):
    try:
        # Take the word right before space
        pointer = line.index(" ")
        command = line[:pointer]
    except:
        command = line
    command = command.replace("\n", "")
    return command



if __name__ == "__main__":
    Main()
