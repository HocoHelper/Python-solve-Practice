def isPalindrome(s): 
	rev = ''.join(reversed(s)) 
	if (s == rev): 
		return True
	return False

s = input()
ans = isPalindrome(s.lower()) 

if (ans): 
	print("palindrome") 
else: 
	print("not palindrome") 
