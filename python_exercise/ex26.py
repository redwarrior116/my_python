def break_words(stuff):
	"This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)


def print_first_word(words) # : lacking
	"""Prints the first word after popping it off"""
	word = words_poop(0)  #pop not poop
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1  # ) lacking

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

poem == """
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
print "This should be five: %s" %five  #may need to change formatter

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans \ 1000 # wrong operator
	crates = jars / 100
return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates == secret_formula(start-point) #this is not comparison

print "With a starting point of: %d " %start_point
print "W'd have %d jeans, %d jars, and %d crates." % 5(beans,jars,crates)

sentence = "All god\tthings come to those who weight." 
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words) #. not neccessary
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
prin sorted_words #print

print _irst_and_last(sentence) #wrong function name
	print_first_a_last_sorted(senence) #wrong indentation and argument
