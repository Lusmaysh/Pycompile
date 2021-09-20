import base64,sys
print("[*] Python Encode By Lusmaysh")
filename = input("[*] Enter Filename: ")
enc = filename.replace(".py","_enc.py")
try:
	file = open(filename,"rb").read()
except FileNotFoundError:
	sys.exit(f'[*] File Not Exists!')
en = base64.b64encode(file)
en2 = en.decode()
with open(enc,"w") as en:
	en.write(f'import base64\nexec(base64.b64decode("{en2}"))')
try:
	level = int(input("[*] Security Level: "))
except:
	level = 0
for x in range(level):
	layer = open(enc,"rb").read()
	b64 = base64.b64encode(layer).decode()
	with open(enc,"w") as l:
		l.write(f"import base64\nexec(base64.b64decode('{b64}'))")
print(f"[*] Encode Success!\n[*] File Saved As {enc}")
