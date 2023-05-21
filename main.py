import os
from time import sleep
import random
from termcolor import cprint 
from pyfiglet import figlet_format

text = "             WELCOME TO\n         DIAMOND RISK"
cprint(figlet_format(text, font = "bubble"), "green", attrs=['bold'])
weapons = ["lightsabre", "gun", "sword", "dagger", "metal stick"]
White = "\033[0;37m"
Cyan="\033[1;36m" 
Green="\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"
Blue="\033[0;34m"
diamonds = 0
jailtime = 5
gun = 0
vault = 0
goojfc = 0
health = 50
sleep(5)
weapon = "fist"
def demo():
  input(Orange + "\nPress enter whenever you see this sign " + Cyan + "-->")
  print(Orange + "\nYou are a very advanced robber. But even advanced robbers have a chance of going to jail.")
  print(Orange + "\nYou have 50 health at the beginning out the game, and the maximum amount of health is 100. You can get health by sleeping.")
  print(Orange + "\nTo win the game, you have to get to as many diamonds as you can without dying. You actually need to be the biggest robber in the world. But if you get caught by the police, you lose all your diamonds and go to jail (have a 10 second time out), unless you have some kind of vault where you keep your diamond or have a weapon that will knock the police out. \nBut if you get caught by the MI6, which is the fifth time you get caught, you get beheaded, which officially marks the end of your robbing career.")
  input(Cyan + "\n-->")
os.system("clear")
demoornot = input("Do you want to see the rules and the demo? (y,n)")
if demoornot == "y":
  demo()
os.system("clear")
while jailtime != 0 and health > 0:
  text = "                   DIAMOND RISK"
  cprint(figlet_format(text, font = "bubble"), "green", attrs=['bold'])
  print()
  print(Orange + "Diamonds: " + White + str(diamonds))
  print(Orange + "Health: " + White + str(health))
  print(Orange + "Times in jail left: " + White + str(jailtime))
  print(Orange + "Get out of jail free cards: " + White + str(goojfc))
  print(Orange + "Vaults: " + White + str(vault))
  print(Orange + "Gun: " + White + str(gun))
  print(Orange + "Weapon:" + White + str(weapon))
  print(Green + "You can choose one of these options.")
  print(Cyan + "a." + Green + "Rob a bank with 1 diamond." + Pink + "Here you have a 1/100 chance of getting caught.")
  print(Cyan + "b." + Green + "Rob a bank with 5 diamonds." + Pink + "Here you have a 1/20 chance of getting caught.")
  print(Cyan + "c." + Green + "Rob a bank with 10 diamonds." + Pink + "Here you have a 1/10 chance of getting caught.")
  print(Cyan + "d." + Green + "Rob a bank with 20 diamonds." + Pink + "Here you have a 1/5 chance of getting caught.")
  print(Cyan + "e." + Green + "Rob a bank with 50 diamonds." + Pink + "Here you have a 1/2 chance of getting caught.")
  print(Cyan + "f." + Green + "Steal a get out of jail free card." + White + "If you steal that, you are allowed to escape.the punishment of jail, but the police still take your diamonds." + Pink + "Here you have a 1/2 chance of getting caught.")
  print(Cyan + "g." + Green + "Steal a vault from the bank." + White + "If you steal that, all the diamonds you steal successfully, go into your vault. There is a chance of somebody stealing from your vault though." + Pink + "Here you have a 999/1000 chance of losing of getting caught.")
  print(Cyan + "h." + Green + "Steal a weapon." + White + "You can get different weapons. If you steal a gun, you will be able to escape the punishment of jail and rescue your diamonds. You can only use the gun once though. The other weapons will be used to fight the people on the road." + Pink + "Here you have a 97/100 chance of getting caught.")
  print(Cyan + "i." + Green + "Sleep." + White + "By sleeping, you might get a some health. You will sleep for 5 seconds.")
  print(Cyan + "j." + Green + "The casino." + White + "Here you will be able to gamble your diamonds." + Pink + "You have a risk of losing and winning diamonds.")
  print(Cyan + "k." + Green + "Highwaymaning." + White + "Here you will try to steal diamonds from random people on the road." + Pink + "There isn't a calculated risk.")
  print(Cyan + "l." + Green + "The leaderboard." + White + "Here you will be able to see if you are the biggest robber in the world. Write your highscores in the comments (if they are over 500, send a screenshot as well) so I can put them on the leaderboard.")
  print(Cyan + "m." + Green + "Jobs." + White + "Here random people will ask you to get random things for them for diamonds." + Pink + "There is a 3/100 chance of getting caught.")
  print(Cyan + "n." + Green + "Fake Calling." + White + "Here you will call random people, trying to get their bank account number, so you can hack into their account." + Pink + "Here you have a 1/10 chance of getting caught.")
  chance1 = input(Orange + "What do you want to do?")
  chance = chance1.lower()
  if chance == "a":
    number = random.randint(1,100)
    if number == 1:          
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        #### if caught
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        ########
        sleep(2)
    if number == 2:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      health = health - shoot
    if number != 1 and number != 2:
      input("You successfully stole the diamond. " + Cyan + "-->")
      diamonds = diamonds + 1
  ###### all of a
  if chance == "b":
    number = random.randint(1,20)
    if number == 1:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
        goojfc = goojfc - 1
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number == 2:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      health = health - shoot
    if number != 1 and number != 2:
      input("You successfully stole 5 diamonds. " + Cyan + "-->")
      diamonds = diamonds + 5
  if chance == "c":
    number = random.randint(1,20)
    if number == 1:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number == 2:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      health = health - shoot
    if number != 1 and number != 2:
      input("You successfully stole 10 diamonds. " + Cyan + "-->")
      diamonds = diamonds + 10
  if chance == "d":
    number = random.randint(1,5)
    if number == 1:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number == 2:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      health = health - shoot
    if number != 1 and number != 2:
      input("You successfully stole 20 diamonds. " + Cyan + "-->")
      diamonds = diamonds + 20
  if chance == "e":
    number = random.randint(1,2)
    if number == 1:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number != 1:
      input("You successfully stole 50 diamonds. " + Cyan + "-->")
      diamonds = diamonds + 50
  if chance == "i":
    poster = random.randint(1,2)
    if poster == 1:
      healths = random.randint(1,20)
      input(Orange + "Start your sleep. " + Cyan + "-->")
      sleep(5)
      input(Green + "You got " + White + str(healths) + Green + " health." + Cyan + "-->")
      health = health + healths
      if health > 100:
        health = 100
    if poster == 2:
      input(Pink + "You see a wanted poster of yourself" + Cyan + "-->")
      sleepornot = input("Do you sleep or not? (y,n)")
      if sleepornot == "n":
        input(Blue + "You decide that it isn't safe to sleep" + Cyan + "-->")
        input(Blue + "And don't sleep" + Cyan + "-->")
      if sleepornot != "n":
        input(Orange + "Start your sleep. " + Cyan + "-->")
        sleep(5)
        print(Pink + "You were very unfortunate and got caught by the police while you were sleeping.")
        if goojfc > 0:
          print(Green + "You have a get out of jail card. You are using it.")
          goojfc = goojfc - 1
          if vault == 1:
            print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          elif gun == 1:
            print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
            gun = 0
          else:
            diamonds = 0
          sleep(2)
        if goojfc < 1:
          input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
  if chance == "f":
    number = random.randint(1,4)
    if number == 1 or number == 2:
      print("You got a get out of jail free card. Now every time you go to jail, you will use the card.")
      goojfc = goojfc + 1
      sleep(2)
    if number == 3:
      print(Pink + "You were very unfortunate and got caught by the police while you were sleeping.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number == 4:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      health = health - shoot
  if chance == "g":
    number = random.randint(1,1000)
    if number == 1:
      if vault == 1:
        print(Pink + "You have already got a vault" + Cyan + "-->")
        sleep(2)
      else:
        print(Green + "You got a vault. Now you can't get another vault. From now on, all the diamonds you steal will be stored here if you return from your heist successfully.")
        vault = vault + 1
        sleep(2)
    if number == 2:
      shoot = random.randint(1,50)
      input(Pink + "The police shot you. You lose " +  str(shoot) + " health. " + Cyan + "-->")
      sleep(2)
      health = health - shoot
    if number != 1 and number != 2:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
  if chance == "h":
    number = random.randint(1,100)
    if number != 1 and number != 2 and number != 3:
      print(Pink + "You were very unfortunate and got caught by the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        sleep(2)
    if number == 1:
      if gun == 1:
        print(Pink + "You have already stolen a gun!")
        sleep(2)
      else:
        input(Green + "You successfully stole the gun. " + Cyan + "-->")
        weapon = "gun"
        sleep(2)
        gun = gun + 1
    if number == 2:
      print(Green + "You got a sword.")
      weapon = "sword"
    if number == 3:
      print(Green + "You got a lightsabre.")
      weapon = "lightsabre"
  if chance == "j":
    os.system("clear")
    text = "THE CASIN0"
    cprint(figlet_format(text, font = "bubble"), "green", attrs=['bold'])
    print(Blue + "\nWelcome to the casino. Here you can do lots of betting with your diamonds. Be careful, you could lose or gain diamonds.")
    input(Cyan + "-->")
    if diamonds < 1:
      input(Pink + "You don't have enough diamonds." + Cyan + "-->")
    else:
      print(Blue + "You can choose one of these options:")
      print(Cyan + "a." + Green + "Dice = Diamond")
      print(Cyan + "b." + Green + "Slot Machine")
      gameletter = input("Type in the letter of the game you  want to play: ")
      if gameletter == "a":
        print(Green + "Welcome to Dice = Diamond. You will roll a ten-sided dice and whatever number on the dice, that many diamonds you will get. If you want to play you must pay 5 diamonds.")
        pay1 = input(Orange + "Do you want to play? (y,n)")
        pay = pay1.lower()
        if pay == "y":
          if diamonds >= 5:
            diamonds = diamonds - 5
            input(Blue + "Roll the dice." + Cyan + "-->")
            dice = random.randint(1,10)
            dice1 = str(dice)
            print(Green + "The dice got", dice1, "\nYou get",dice1,"diamonds.")
            input("Collect the diamonds. " + Cyan + "-->")
            diamonds = diamonds + dice
          else:
            print(Pink + "You do not have enough diamonds")
            sleep(2)
      if gameletter == "b":
        slots = "apple", "orange", "pear", "peach", "grapes", "watermelon"
        print(Green + "Welcome to the slot machine. Here will spin the slots. If you get 2 fruits matching, you get 5 diamonds. If you get 3 fruits matching, you get 10 diamonds. You have to pay 5 diamond to play.")
        pay1 = input(Orange + "Do you want to play? (y,n)")
        pay = pay1.lower()
        if pay == "y":
          if diamonds >= 5:
            diamonds = diamonds - 5
            slot1 = random.choice(slots)
            slot2 = random.choice(slots)
            slot3 = random.choice(slots)
            input(Orange + "Spin " + Cyan + "-->")
            print(Cyan + "Your three slots were:", slot1, ",",slot2, "and", slot3)
            if slot1 == slot2 and slot2 == slot3:
              print(Green + "You got all the of the slots the same.")
              input(Orange + "Collect your diamonds. " + Cyan + "-->")
              diamonds = diamonds + 10
            else:
              if slot1 == slot2 or slot2 == slot3 or slot3 == slot1:
                print(Green + "You got 2 of the slots the same.")
                input(Orange + "Collect your diamonds. " + Cyan + "-->")
                diamonds = diamonds + 5
              else:
                input("You didn't get any of the slots match. " + Cyan + "-->")
          else:
            print(Pink + "You do not have enough diamonds")
            sleep(2)
  if chance == "k":
    print(Blue + "You have agreed to attack some random guy on the street.")
    enemyweapon = random.choice(weapons)
    fightorrun = input(Orange + "Do you want to fight(f) or run(r)?")
    enemyhealth = random.randint(30,70)
    print(Pink + "The enemy has ", White + str(enemyhealth) + " health and has a ", White + enemyweapon + " as a weapon.")
    while fightorrun != "r" and fightorrun != "d":
      os.system("clear")
      print(Cyan + "Health:" + White + str(health))
      print(Cyan + "Enemy Health:" + White + str(enemyhealth))
      losehealth = random.randint(1,20)
      enemylosehealth = random.randint(1,20)
      print(Green + "You hit the enemy, which made them lose", enemylosehealth, "health, but the enemy hit you which made you lose", losehealth, "health.")
      enemyhealth = enemyhealth - enemylosehealth
      health = health - losehealth
      if enemyhealth < 1:
        os.system("clear")
        stolendi = random.randint(1,50)
        fightorrun = "d"
        print(Cyan + "Health:" + White + str(health))
        print(Cyan + "Enemy Health:" + White + str(enemyhealth))
        diamonds = stolendi + diamonds
        print(Green + "You killed the enemy and stole", str(stolendi), "diamonds from them.")
        input(Cyan + "-->")
      if health < 1:
        os.system("clear")
        fightorrun = "d"
        print(Cyan + "Health:" + White + str(health))
        print(Cyan + "Enemy Health:" + White + str(enemyhealth))
        print(Pink + "The enemy killed you and stole all your diamonds.")
        diamonds = 0
        input(Cyan + "-->")
      if enemyhealth > 0 and health > 0:
        fightorrun = input(Orange + "Do you want to fight(f) or run(r)?")
    if fightorrun == "r":
      losehealth = random.randint(1,20)
      print(Pink + "As you ran away, the enemy attacked you, making you lose",losehealth, "health." )
      input(Cyan + "-->")
      health = health - losehealth
  if chance == "l":
    os.system("clear")
    text = "THE LEADERBOARD"
    cprint(figlet_format(text, font = "bubble"), "green", attrs=['bold'])
    print(Green + "1) Name12: 1025")
    print(Green + "2) awesome10: 986")
    print(Green + "3) Twitchmmanikan: 813")
    print(Green + "4) kacperox1224: 606")
    print(Green + "5) medcho: 240")
    print(Green + "6) AbhayBhat: 201")
    print(Green + "7) DigitCommander: 200")
    print(Green + "8) SeanXiao: 187")
    print(Green + "9) CoolJames1610: 170")
    input(Cyan + "-->")
  if chance == "m":
    print(Blue + "You have agreed to do stuff for people for diamonds.")
    names = "Bob", "Billy", "Nathaniel", "Liam", "Noah", "William", "Alex", "James", "Lucas", "Luke", "Percy", "Harry", "Oliver", "Grover", "Ronald"
    name = random.choice(names)
    aod = random.randint(1,20)
    print(Cyan + "A man called", name, "asks you to steal a bomb from the bank. He tells you that he will give you", str(aod), "diamonds if you do it for him.")
    yorn1 = input(Orange + "Do you want to do it?(y,n)")
    yorn = yorn1.lower()
    if yorn == "y":
      number = random.randint(1,100)
      if number == 1 or number == 2 or number == 3:
        print(Pink + "You were very unfortunate and got caught by the police.")
        if goojfc > 0:
          print(Green + "You have a get out of jail card. You are using it.")
          goojfc = goojfc - 1
          if vault == 1:
            print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          elif gun == 1:
            print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
            gun = 0
          else:
            diamonds = 0
          sleep(2)
        if goojfc < 1:
          input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
          if vault == 1:
            print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
            sleep(2)
            jailtime = jailtime - 1
            sleep(10)
            input(Orange + "You got released. Continue the game. " + Cyan + "-->")
          elif gun == 1:
            print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
            gun = 0
          else: 
            sleep(2)
            jailtime = jailtime - 1
            sleep(10)
            diamonds = 0
            input(Orange + "You got released. Continue the game. " + Cyan + "-->")
          sleep(2)
        losehealth = random.randint(1,20)
        print(Pink + "You meet", name, "and tell him that you didn't get the bomb. He gets mad and attacks you, so you lose", str(losehealth), "health. You run away before he attacks again.")
        input(Cyan + "-->")
        health = health - losehealth
      if number != 1 and number != 2 and number != 3:
        print(Green + "You got the bomb for", name)
        print(name + " gives you", str(aod), "diamonds.")
        diamonds = aod + diamonds
        input(Cyan + "-->")
    else:
      losehealth = random.randint(1,20)
      print(Pink + "You tell", name, "that you don't want to get the bomb. He gets mad and attacks you, so you lose", str(losehealth), "health. You run away before he attacks again.")
      health = health - losehealth
      input(Cyan + "-->")
  if chance == "n":
    print(Blue + "You have decided to do fake calling.")
    names = "Bob", "Billy", "Nathaniel", "Liam", "Noah", "William", "Alex", "James", "Lucas", "Luke", "Percy", "Harry", "Oliver", "Grover", "Ronald"
    name = random.choice(names)
    ideas = "getting free pizzas", "won the lottery", "won a free holiday", "won a free car"
    idea = random.choice(ideas)
    print(Cyan + "You decide to call a random guy called", name, "saying that he's", idea)
    input(Orange + "Call." + Cyan + "-->")
    number = random.randint(1,10)
    if number == 1:
      print(Pink + "You were very unfortunate and got caught by the police, as the person you called was the police.")
      if goojfc > 0:
        print(Green + "You have a get out of jail card. You are using it.")
        goojfc = goojfc - 1
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else:
          diamonds = 0
        sleep(2)
      if goojfc < 1:
        input(Pink + "You have to have a 10 second time out." + Cyan + "-->")
        if vault == 1:
          print(Green + "You quickly stashed your diamonds in your vault and so the police didn't find anything!")
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
        elif gun == 1:
          print(Green + "You used your gun to scare the guards and you ran off with your diamonds! But you dropped it as you ran away :(")
          gun = 0
        else: 
          sleep(2)
          jailtime = jailtime - 1
          sleep(10)
          diamonds = 0
          input(Orange + "You got released. Continue the game. " + Cyan + "-->")
    else:
      print(Green + "You ask", name, "for his bank account number. He gives it to you. Then you cut the phone.")
      print(Blue + "You decide to hack into", name,"'s bank account.")
      input(Orange + "Hack." + Cyan + "-->")
      aod = random.randint(1,50)
      print(Green + "You hack into", name,"'s bank account and steal", str(aod), "diamonds from it.")
      diamonds = diamonds + aod
      input(Cyan + "-->")
  os.system("clear")
if jailtime == 0:
  print(Pink + "MI6 beheaded you. That ended your criminal career.")
  print(Pink + "You ended up with 0 diamonds.")
if health < 1:
  print("You died because you lost all your health. You give your amount of", diamonds, "diamonds to your friend.")
