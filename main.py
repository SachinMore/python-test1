# name = input("What is your name : ")
# for nme in range(5):
#     print(nme)

# a = 1
# while a < 5:
#     print(a)
#     a += 1


# print one sided pyramid
# for x in range(1,6):
#     print(x*"*")


# below code to print pyramid ########################
# floors=int(input("Enter no. of floors: "))
# j=0

# for x in range(1, floors+1):
#     print((floors-1)*" ", end="") ## this create/append space before *
#     if x==1:
#         print("*")
#     else:
#         print((x+j)*"*")
#     j+=1
#     floors-=1


# def initials(phrase):
#   words = phrase.split()
#   # print(words)
#   result = ""
#   for word in words:
#       result += word[0].upper()
#   return result
#
# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

"""
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for string_char in input_string.replace(" ","").lower():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if string_char != " ":
			new_string += string_char
			reverse_string = string_char + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
"""


"""
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
		i = sentence.rindex(old)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match
	return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
"""


"""
Q:The skip_elements function returns a list containing every other element from an input list,
starting with the first element. Complete this function to do that, using the for loop 
to iterate through the input list.

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for element in elements:
		# Does this element belong in the resulting list?
		if i%2 == 0:
			# Add this element to the resulting list
			new_list.append(element)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
"""

#######
"""
Question 3
The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner,
group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read,
2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
 For example:
 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
 Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
	result = ""
	value_letters = [(4, "r"), (2, "w"), (1, "x")]
	# Iterate over each of the digits in octal
	for digit in [int(n) for n in str(octal)]:
		# Check for each of the permissions values
		for value, letter in value_letters:
			if digit >= value:
				result += letter
				value -= value
			else:
				result = "-"
	return result
print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes in wardrobe.items():
	for cloth, color in clothes:
		print(clothes.value())
		# print("{} {}".format(cloth))
"""





# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for clothes, colors in wardrobe.items():
# 	for color in colors:
# 		print("{} {}".format(color,clothes))

"""
2.
Question 2
The groups_per_user function receives a dictionary, which contains group names with the list of users. 
Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)		
			# Now add the group to the the list of
			# 	listing = []
			# 	listing.append(group)
			# 	user_groups[user] = listing
			# else:
			# 	user_groups[user].append(group)
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
		
"""




