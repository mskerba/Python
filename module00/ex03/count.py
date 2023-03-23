import sys
import string

def print_result(size, upper, lower, punct, space):
	print(f"The text contains {size} character(s):")
	print(f"- {upper} upper letter(s)")
	print(f"- {lower} lower letter(s)")
	print(f"- {punct} punctuation mark(s)")
	print(f"- {space} space(s)")

def text_analyzer(text=None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if text == None:
		print("What is the text to analyze?")
		text = input(">>")
	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
		return
	upper = 0
	lower = 0
	punct = 0
	space = 0
	for char in text:
		if char in string.punctuation:
			punct += 1
		elif char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		elif char == " ":
			space += 1
	print_result(len(text), upper, lower, punct, space)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])