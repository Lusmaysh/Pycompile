import base64,zlib,marshal,sys,os
os.system("cls" if os.name=="nt" else "clear")
print("""
_______ ___ ___ _______ ______  _______
|   _   |   Y   |   _   |   _  \|   _   |
|.  1   |   1   |.  1___|.  |   |.  1___|  [*] Support Python2 And Python3
|.  ____|\_   _/|.  __)_|.  |   |.  |___   [*] Python Encode By Lusmaysh
|:  |     |:  | |:  1   |:  |   |:  1   |  [*] Encode Available: base64,zlib,marshal
|::.|     |::.| |::.. . |::.|   |::.. . |
`---'     `---' `-------`--- ---`-------'
""")
try:
	filename = raw_input("[*] Enter Filename: ")
except:
	filename = input("[*] Enter Filename: ")
enc = filename.replace(".py","_enc.py")
try:
	file = open(filename,"rb").read()
except IOError:
	sys.exit('[*] File Not Exists!')
try:
	type = raw_input("[*] Encode Type [base64/zlib/marshal]: ")
except:
	type = input("[*] Encode Type [base64/zlib/marshal]: ")
if type=="b64" or type=="base64":
	en = base64.b64encode(file)
	en2 = en.decode()
	with open(enc,"w") as en:
		en.write("import base64\nexec(base64.b64decode(\'"+en2+"\'))")
	try:
		try:
			level = raw_input("[*] Security Level: ")
			level = int(level)
		except:
			level = int(input("[*] Security Level: "))
	except:
		level = 0
	for x in range(level):
		layer = open(enc,"rb").read()
		b64 = base64.b64encode(layer).decode()
		with open(enc,"w") as l:
			l.write("import base64\nexec(base64.b64decode(\'"+b64+"\'))")
	print("[*] Encode Success!\n[*] File Saved As "+enc)
elif type=="zlib":
	data = zlib.compress(file)
	with open(enc,"w") as zl:
		zl.write("import zlib\nexec(zlib.decompress("+str(data)+"))")
	try:
		try:
			level = raw_input("[*] Security Level: ")
			level = int(level)
		except:
			level = int(input("[*] Security Level: "))
	except:
		level = 0
	for x in range(level):
		layer = open(enc,"rb").read()
		data2 = zlib.compress(layer)
		with open(enc,"w") as zz:
			zz.write("import zlib\nexec(zlib.decompress("+str(data2)+"))")
	print("[*] Encode Success!\n[*] File Saved As "+enc)
elif type=="marshal":
	try:
		code = compile(file,'<Lusmaysh>','exec')
		data = marshal.dumps(code)
	except TypeError:
		sys.exit("[*] The File Is Already Compiled!")
	with open(enc,"w") as mars:
		mars.write("import marshal\nexec(marshal.loads("+repr(data)+"))")
	try:
		try:
			level = raw_input("[*] Security Level: ")
			level = int(level)
		except:
			level = int(input("[*] Security Level: "))
	except:
		level = 0
	for x in range(level):
		layer = open(enc,"rb").read()
		code2 = compile(layer,'<Lusmaysh>','exec')
		data2 = marshal.dumps(code2)
		with open(enc,"w") as mars2:
			mars2.write("import marshal\nexec(marshal.loads("+repr(data2)+"))")
	print("[*] Encode Success!\n[*] File Saved As "+enc)
elif type=="all":
	m = compile(file,'<Lusmaysh>','exec')
	m2 = marshal.dumps(m)
	with open(enc,"w") as ms:
		ms.write("import marshal\nexec(marshal.loads("+repr(m2)+"))")
	file = open(enc,"rb").read()
	z = zlib.compress(file)
	with open(enc,"w") as zl:
		zl.write("import zlib\nexec(zlib.decompress("+str(z)+"))")
	b64 = base64.b64encode(file).decode()
	with open(enc,"w") as b6:
		b6.write("import base64\nexec(base64.b64decode(\'"+b64+"\'))")
	print("[*] Encode Success!\n[*] File Saved As "+enc)
else:
	sys.exit("[*] Exiting Program!")
