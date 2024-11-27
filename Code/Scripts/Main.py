from CommandLine import CommandLine
from RequestHandler import command

cmd = CommandLine()
request = ""
print("The program has started")
while request != ["exit"]:
    request = input().strip().split()
    print(command(cmd, request))
