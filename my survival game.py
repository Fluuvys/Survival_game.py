title = 'Welcome to my survival game. please type in all lower case for the answers.'
print(title.upper())
name = input("What is your name? ")
age = int(input("Enter your age: "))
health = 1

if age <= 18:
	print('You will now play the normal version of the game.')
	wannaplay = input('If you want to play type in yes: ').lower()
	pass

if wannaplay == 'yes':
	print('Health: ', health)
	left_or_right = input("First choice..... Left or Right? ")
	if left_or_right == "left":
		print("Your plane has crashed and you have landed on a deserted island naked with nothing but an axe and 2 bottles of water. ")
		scary_house = input("You see a house nearby but it looks creepy what do you do. 1.Go investigate 2.Walk away")
		if scary_house == "go investigate":
			investigate = input("You have entered the house but nobody is there. You see old pictured of people who seemed to have lived here, what do you do. 1.Look behind the pictures 2.Go outside")
		if investigate == 'look behind the pictures':
			key = input("You found a key. What do you do. 1.Go to the back room 2.Go outside. ")

		if key == "go to the back room":
			print("You have found a helicopter which uses the key you found. You used the helicopter to get out of the island")
			print("CONGRATULATIONS!!! You have escaped the island!!!")
			pass

		if investigate == "go outside":
			print("Health: ", health - 1)
			print("You tripped on the table and hit your head on the way out. Your skull is split in half. You Died!")


		if scary_house == "walk away":
			print("Health: ", health - 1)
			print("A tree fell on your head. You Died!")
			pass



	if left_or_right == "right":
		print("Your plane has crashed and you landed into a house of a serial killer.")
		run_fight = input("You are trying to get up and hide after the serial killer heard a noise and he found you what do you do?  1.Run or 2.Fight back: ")
		if run_fight == "run":
			print("Health: ", health-1)
			print("The serial killer was too strong for you injured body. You Died!!!")
			pass
		if run_fight == "fight back":
			print("Health: ",health-1)
			print("Who would've thought the killer had a gun. You Died!")
			pass
