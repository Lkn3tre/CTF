from struct import unpack, pack

scrambled_png = open('scrambled.png', 'rb').read()

original = [b'\x89PNG\r\n\x1a\n']
i = 8

while i < len(scrambled_png):
    size = scrambled_png[i:i + 4]
    chunk_length = unpack('>I', size)[0]
    chunk = scrambled_png[i:i + 8 + chunk_length]
    original.append(chunk)
    i += 8 + chunk_length

with open('restored.png', 'wb') as restored_file:
    restored_file.write(b''.join(original))
