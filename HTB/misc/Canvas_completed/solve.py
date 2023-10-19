import re

js_script = open("deobjs.js","r") #reading deobfuscated version of 'login.js'

lastline = js_script.readlines()[-1].strip() # reads all lines from the js file and returns a list of lines.then selects the last line using [-1] and removes any leading or trailing whitespace with .strip()

chars_code = re.findall( r'\((.*?)\)' ,lastline)[0] # splits the chars_code string using ", " as the separator and converts each number to a character using chr(int(i)). The resulting characters are stored in a list

flag = [chr(int(i)) for i in chars_code.split(", ")] #converts each number to a character .The resulting characters are stored in a list

print("".join(flag)) #Finally,joins the characters in the flag list into a single string and prints the result
