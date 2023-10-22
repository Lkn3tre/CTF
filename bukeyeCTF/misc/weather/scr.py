import wave
import struct
wav = wave.open("challenge_nokia_pile.wav", mode='rb')
frame_bytes = bytearray(list(wav.readframes(wav.getnframes())))
shorts = struct.unpack('H'*(len(frame_bytes)//2), frame_bytes)
extracted_left = shorts[::2] 
extracted_right = shorts[1::2]
extractedLSB = ""
for i in range(0, len(extracted_left)):
	if i%2 == 0:
		print("a")
		extractedLSB += (str(extracted_left[i] & 1))
	else:
		extractedLSB += (str(extracted_right[i] & 1))
string_blocks = (extractedLSB[i:i+8] for i in range(0, len(extractedLSB), 8))
decoded = ''.join(chr(int(char, 2)) for char in string_blocks)
print(decoded[0:500])
wav.close()
