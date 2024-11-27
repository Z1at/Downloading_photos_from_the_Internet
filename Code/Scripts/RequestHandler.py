def check_len(request, ln):
    return len(request) == ln


def command(cmd, request):
    if request[0] == "cd..":
        cmd.up()
    elif request[0] == "cd" and check_len(request, 2):
        cmd.down(request[1])
    elif request[0] == "get" and len(request) >= 3 and request[-1].isdigit():
        cmd.get_photos(request[1:-1], int(request[-1]))
    elif request[0] == "ls" and check_len(request, 1):
        return cmd.get_files()
    elif request[0] == "path" and check_len(request, 1):
        return cmd.get_path()
    elif request[0] == "del" and check_len(request, 1):
        cmd.delete()
    elif request != ["exit"]:
        return "I do not know this command"
    return "Complete"
