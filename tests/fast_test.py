cmd = 'key 25'
cmd = cmd[cmd.find('key ') + 4:]
if cmd.isdigit():
    print("digit" + chr(int(cmd)) + "done" + str(int(cmd) == 25))
