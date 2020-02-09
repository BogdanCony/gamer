#game v1

import random
import time
time.sleep(3)
def rando():
	class inventory:
		axe = False
		gun = False
		life_centre = False
	life = 10
	b = random.randint(1, 6)
	if b == 1:
		print("today is nothing happend!")
	elif b == 3:
		print("Raders is here!")
		if inventory.axe == True:
			print("use axe?")
			axe1 = input("yes or no")
			if axe1 == yes:
				pass
		else:
			print("- 1 life")
			life -= 1
			print(life)

	elif b == 5:
		print("we watch for some eat!")
	elif b == 6:
		print("we find axe!")
		inventory.axe = True
	elif b == 2:
		print("we find life_centre")
		inventory.life_centre = True
	elif b == 4:
		print("we find gun!")
		inventory.gun = True



def gameplay():
	print("first day!")
	print("your player is Dan")
	print("we are going to go to another sity!")
	print("second day!")
	a = 5
	print("your lifes : ")
	print(a)
	rando()
	print("press '1' for continue....")
	con = input(" ")
	print("second day!")
	rando()
	print("press '1' for continue....")
	con = input(" ")
	print("third day!")
	rando()
	print("press '1' for continue....")
	con = input(" ")
	print("forth day!")
	print("press '1' for continue....")
	con = input(" ")
	rando()
	print("fifth day!")
	print("press '1' for continue....")
	con = input(" ")
	rando()
	print("sixth day!")
	print("press '1' for continue....")
	con = input(" ")
	rando()
	print("seventh day!")
	print("press '1' for continue....")
	con = input(" ")
	rando()
	print("last day!")
	print("we are at home!")
	


	





def main():
	print("Welcome!")
	print("1) Play! ")
	print("2) Creators")
	print("3) exit")
	mainq = input("choose: ")
	if mainq == 1:
		print("game")
		gameplay()


	

main()
gameplay()


