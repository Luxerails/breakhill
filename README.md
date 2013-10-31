breakhill
=========

Tool to break Hill ciphers. Only breaks 2x2 hill matrices. For the moment.
Usage: breakhill.py ciphertext.txt.
The script will output possible plaintexts with their matrices based on their index of coincidence (here hardcoded as a minimal value of 0.07 for french plaintexts, you might adjust this value to ~0.65 for english).
The attack on the ciphertext only lasts a few seconds.
