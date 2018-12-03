#!/usr/bin/env python3

import os
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description="See your favorite bash commands!")
parser.add_argument("-n", "--number", type=int, default=10, help="The number of commands to print")

args = parser.parse_args()

command_number = 0

def Main():
    # print the commands
    file = open(os.path.expanduser('~') + "/.bash_history", "r")
    commands = get_command_list(file)

    number = args.number
    i = 0
    for key in sorted(commands, key=commands.__getitem__, reverse=True):
        if i == number:
            break
        print("%-12s  : %4d |  %%%6f" % (key, commands[key], 100*(commands[key] / command_number)))
        i +=1

def get_command_list(file):
    global command_number
    commands = {}
    # debug file
    #file = open(os.path.expanduser('~') + "/Projects/Python/howmany/tests/test.txt", "r")
    for line in file:
        command = get_command(line)
        command_number += 1
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
