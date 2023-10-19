import re

with open("behindthescenes","rb") as f:
    content = f.read()

print(content)
re.sub(b'\x0f\x0b', b'\x90\x90', content)

with open("flag2","wb") as f:
    f.write(content)
    