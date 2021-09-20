import marshal,sys
print("[*] Python Encode By Lusmaysh")
filename = input("[*] Enter Filename: ")
enc = filename.replace(".py","_enc.py")
try:
	file = open(filename,"rb").read()
except FileNotFoundError:
	sys.exit("[*] File Not Exists!")
try:
	code = compile(file,'<Lusmaysh>','exec')
	data = marshal.dumps(code)
except TypeError:
	sys.exit("[*] File Already Compile!")
with open(enc,"w") as res:
	res.write(f'import marshal\nexec(marshal.loads({repr(data)}))')
for x in range(1):
	layer = open(enc,"rb").read()
	code2 = compile(layer,'<Lusmaysh>','exec')
	data2 = marshal.dumps(code2)
	with open(enc,"w") as marshal:
		marshal.write(f'import marshal\nexec(marshal.loads({repr(data2)}))')
print(f"[*] Encode Success!\n[*] File Saved As {enc}")
