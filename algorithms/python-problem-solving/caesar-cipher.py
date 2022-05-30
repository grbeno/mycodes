# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

s = "6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr"  #"Always-Look-on-the-Bright-Side-of-Life" #"middle-Outz" #"6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr"
k = 87 #5 #2 #87


k = k % 26
A = 97  # ascii code of a
Z = 122 # ascii code of z

res = []

for i in range(len(s)):
    
    c = ord(s[i].lower())
    
    if s[i].isalpha():
        c = c + k
        if c > Z: # k overflowed
            c = A - 1 + k  - (Z - ord(s[i]))
    
    if s[i].isupper():
        cipher = chr(c).upper()
    else:
        cipher = chr(c)
    
    res.append(cipher)

print(''.join(res))