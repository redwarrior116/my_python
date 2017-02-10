def break_words(stuff):
	"This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)


def print_first_word(words): # : lacking (checked)
	"""Prints the first word after popping it off"""
	word = words.pop(0)  #pop not poop (checked)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)  # ) lacking (checked)

def sort_sentence(sentence):
	"""Tkaes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Prints the first words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"

five =10 - 2 + 3 - 5
print "This should be five: %d" %five  #may need to change formatter (checked)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000 # wrong operator (checked)
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) #this is not comparison and wrong name for argument (checked)

print "With a starting point of: %d " %start_point
print "W'd have %d jeans, %d jars, and %d crates." %(beans,jars,crates)

sentence = "All god\t things come to those who weight." 
words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #. not neccessary (checked)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words #print (checked)

print_first_and_last(sentence) #wrong function name (checked)
print_first_and_last_sorted(sentence) #wrong indentation and argument (checked)
