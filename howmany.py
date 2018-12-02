#!/usr/bin/env python3

def Main():

    commands = {}
    file = open("/home/monepicor/.bash_history", "r")
    for line in file:
        #line = line[7:]
        try:
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
