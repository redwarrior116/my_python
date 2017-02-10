#import module which we can use argv
from sys import argv

#store information from argv into variable script and filename. script is a special variable which stores the python file name that we are running now.
scirpt, filename = argv

#open the file.
txt = open(filename)

#put the file on display using read function
print "Here is your file %r." %filename
print txt.read()
txt.close() #close the file when its done
#simply do it what's done above but using raw_input to get the file name instead.
print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close() #close the file when its done 
