
def rem_vowel(string): 
	vowels = ('a', 'e', 'i', 'o', 'u') 
	for x in string.lower(): 
		if x in vowels: 
			string = string.replace(x, "") 
	return string.lower()
	 

string=input()
delete_sound=rem_vowel(string.lower())
for harf in delete_sound:
    print(''.join(('.',harf,'')),end='')
