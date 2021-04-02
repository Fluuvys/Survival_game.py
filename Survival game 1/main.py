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
		if scary_house == "1":
			investigate = input(
				"You have entered the house but nobody is there. You see old pictured of people who seemed to have lived here, what do you do. 1.Look behind the pictures 2.Go outside")
			if investigate == "1":
				key = input("You found a key. What do you do. 1.Go to the back room 2.Go outside. ")
				if key == "1":
					print(
						"You have found a helicopter which uses the key you found. You used the helicopter to get out of the island")
					print("CONGRATULATIONS!!! You have escaped the island!!!")
			else:
				print("Health: ", health - 1)
				print("You tripped on the table and hit your head on the way out. Your skull is split in half. You Died!")
		pass




		if scary_house == "2":
			print("Health: ", health - 1)
			print("A tree fell on your head. You Died!")
			pass
