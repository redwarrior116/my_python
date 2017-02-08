# For most of the time formatter %r is used only at debugging
formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter % ("one","two","three","four")
print formatter %(True,False,False,False)
print formatter %(formatter,formatter,formatter,formatter) #In this case, "formatter" are print it out as string. 
print formatter %("I had this thing.",
		  "That you could type up right.",
		  "But it didn't sing.",
		  "So I said goodnight."
		 ) 
