import re

pattern_to_search = b'\x01\x02\x03'
replacement_pattern = b'\x0A\x0B\x0C'

binary_data = b'\x00\x01\x02\x03\x04\x01\x02\x03\x05\x06'

modified_binary_data = re.sub(pattern_to_search, replacement_pattern, binary_data)

print("Original Binary Data:", binary_data)
print("Modified Binary Data:", modified_binary_data)
