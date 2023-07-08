

import pyperclip

text = pyperclip.paste()
# you can also try \ to / whatever works.
lines = text.replace('\\', '/')

print(lines)

pyperclip.copy(lines)
print("line copied to clipboard!")
