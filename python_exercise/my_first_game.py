from sys import exit
def start():
	my_journey = []
	print """
		Here You are. standing in a room with three doors.
		1. door of heaven
		2. door of world
		3. door of hell
		which will you choose?"""
	my_choice = raw_input("> ")
	
	if my_choice == "1":
		print my_choice
		#room_heaven()
		exit(0)
	elif my_choice == "2":
		print my_choice
		#room_world()
		exit(0)
	elif my_choice == "3":
		print my_choice
		#room_hell()
		exit(0)
	else: 
		print "\ntake your time, you only need to type the number 1,2,3."
		start()

def room_heaven():
	
	room_tracker = "heaven"
	print """Welcome to Heaven. your decision from now will be crucial. Thin		 k your decision twice.
		 There is God almighty standing in front of you. what will you d		 o?
		 1. bow down and repent
		 2. worship and brag about your accomplishment."""
	my_choice = raw_input("> ")
	
	if my_choice == 1 j

#start()
