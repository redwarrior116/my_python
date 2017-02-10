from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^c)."
print "If you do want that, hit RETURN."

raw_input("?")
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate() #not neccessary since we use w mode. it automatically truncateitself.

print "now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

all_lines = line1 + "\n" + line2 + "\n" + line3 #put every line in one line.
target.write(all_lines)
target.close()

#for some reasons, I have to close the the file which holds in target and open again to read the file. 
target_2 = open(filename)
print target_2.read()
print "And finally, we close it"
target_2.close()
