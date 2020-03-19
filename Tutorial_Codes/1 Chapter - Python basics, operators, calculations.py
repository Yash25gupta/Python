# Tutorial 6 print()
print('Can use single comma (\' \')')
print("Can use inverted commas (\"  \")")
print("  ht  rtyu", end = " ")      # Dont go to next line


#Tutorial 7 Escape Sequence
# \'	'Print '
# \"	'Print "
# \\	'Print \
# \n	'Print in next line
# \t	'Tab
# \b	'Backspace
print("This is (\') comma\tThis is (\") inverted comma\tThis is (\\) backslash\nThis is in next line")


# Tutorial 8 Comments
# #		'Comments (Ctrl+/)

# Tutorial 09 Escape Sequence as Normal Text
# Output: "Line A \n Line B"    'Use double \\ to print Escape sequence
print("Line A \\n Line B")


# Tutorial 10 & 11 - Exercise 1 & solution
# **********Print these lines*************
# this is \\ double backlesh
# this is /\/\/\/\ mountain
# he is   awesome (use escape sequence instead of manual spaces)
# \" \n \t \' (print these as output)
print("this is \\\\ double backlesh")
print("this is /\\/\\/\\/\\ mountain")
print("he is\tawesome")
print("\\\" \\n \\t \\\'")


# Tutorial 12 - Raw Strings
print(r"Line A \n Line B")
print(r"\" \n \t \'")       # We dont use \\ instead we use 'r' to print as raw string


# Tutorial 13 - Print emoji
print("\U0001F602")    # "U+1F602" is code for emoji


# Tutorial 14 - Python as a Calculator
# Operation order : Bricket > Exponent(R-L) >   *,/,//,% (L-R)  >  +,- (L-R)
print(4/2) # Floating Point Devision
print(4//2) # Integer point Division
print(2**3) # Exponent


# Tutorial 15 - Variable in Python
# Rule 1: Number at 1st position cannot be used (eg 1var)
# Rule 2: letter,_ can be used at 1st posotion (var1, _name, etc)
# Rule 3: No special character cannot be used anywhere (@, #, $, etc)
user_one_name="Yash"        # Snake case writing
userOneName="Gupta"         # Camel case writing
var1=2
print(var1)
print(user_one_name)
print(userOneName)


# Tutorial 16 - Chapter 1 Summary
