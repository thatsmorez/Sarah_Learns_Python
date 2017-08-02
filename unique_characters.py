#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#With additional data structures
def unique_characters_data(s):
	my_dict = {}
	for c in s:
		if c in my_dict:
			return False
		else:
			my_dict[c] = 1
	return True

#Without additional data structures
def unique_characters(s):
	while(len(s) > 0):
		character = s[0:1]
		s = s[1:len(s)]
		for c in s:
			if character == c:
				return False
	return True
		

string = raw_input("Please enter in a string: ")
print unique_characters_data(string)
print unique_characters(string)
