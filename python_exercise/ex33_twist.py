def make_a_list(index,increment):
	i = 0
	numbers = []

	while i < index:
		print "At the top i is %d." %i
		numbers.append(i)

		i = i + increment
		print "Numbers now: ",numbers
		print "At the bottom i is %d." %i

	print "The numbers: "

	for num in numbers: 
		print num

index_input = int(raw_input("Give me index number: "))
increment_input = int(raw_input("Give me increment number: "))
make_a_list(index_input,increment_input)
