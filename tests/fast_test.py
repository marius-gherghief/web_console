import re

cmd = 'key 25'
cmd = cmd[cmd.find('key ') + 4:]
if cmd.isdigit():
    print("digit" + chr(int(cmd)) + "done" + str(int(cmd) == 25))


url = '<p>Hello World</p><a href="http://example.com">More Examples</a>' \
      '<a href="http://example2.com">Even More Examples</a><https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python>'

urls1 = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
urls2 = re.findall('<http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+>', url)
print(urls1)
print(urls2[0][1:-1])
