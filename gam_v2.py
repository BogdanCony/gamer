#game v2

import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
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
		if inventory.gun == True:
			print("use gun?")
			gun1 = input("yes or no")
			if gun1 == yes:
				pass
			if inventory.gun == True:
				inventory.gun = False
				print("- 1 axe")
			elif inventory.gun == True:
				inventory.gun = False
				print("- 1 gun")
		else:
			print(" - 1 life")


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
	print(Back.GREEN + "Welcome!")
	print(Back.BLUE + "1) Play! ")
	print(Style.RESET_ALL)

	print(Back.YELLOW + "2) Creators")
	print(Style.RESET_ALL)

	print(Back.RED + "3) exit")
	print(Style.RESET_ALL)

	mainq = input("choose: ")
	if mainq == 1:
		print("game")
		gameplay()


	

main()
gameplay()


