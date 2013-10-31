import string, sys

A_0, A_1 = 0, 1
ic = lambda text: sum(((text.count(l) * (text.count(l) - 1)) / float(len(text) * (len(text) - 1))) for l in string.uppercase)
normalize = lambda text: filter(lambda l: l in string.uppercase, text.upper())
ismatrice = lambda m: (m[0] * m[3] - m[1] * m[2]) % 2 and (m[0] * m[3] - m[1] * m[2]) % 13

def matriceinv(m):
	a, b, c, d = m
	k = (a * d - b * c)
	for x in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
		if k * x % 26 == 1:
			break
	return (d * x % 26, -b * x % 26, -c * x % 26, a * x % 26)

def decrypt(text, m, z):
	a, b, c, d = m
	letters = [ord(l) - 65 + z for l in text]
	decrypted = []
	i = 0
	while i < len(letters):
		j, k = letters[i], letters[i + 1]
		p = (a * j + b * k) % 26
		q = (c * j + d * k) % 26
		decrypted += [p, q]
		i += 2
	return ''.join(chr(65 + l - z) for l in decrypted)
	
def bruteforce(text, A = 0):
	print "[+] breakhill.py by Luxerails"
	print "[+] Starting ciphertext brute-force...\n"
	count = 0
	ICMIN = 0.07
	for a in range(26):
		for b in range(26):
			for c in range(26):
				for d in range(26):
					m = [a, b, c, d]
					if ismatrice(m):
						m = matriceinv(m)
						dec = decrypt(text, m, A)
						if ic(dec) >= ICMIN:
							print "[+] Possible text found -- Matrice inverse: %s -- IC = %s\n%s\n" % (repr(m), ic(dec), dec)
							count += 1
	print "\n[+] End of attack - %s possible plaintexts found" % count

def main():
	if len(sys.argv) != 2:
		print "[-] Usage: breakhill.py crypto.txt [> log.txt]"
		sys.exit()
	
	try:
		text = normalize(open(sys.argv[1], 'rb').read())
	
	except:
		print "[-] Error while trying to open file"
		sys.exit()
	
	bruteforce(text, A_1) # A_0 if A=0
	
if __name__ == "__main__":
	main()