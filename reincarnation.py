"""
@author: ND
"""

import random
import sys


def end_game():
    print("Game over! See you next time!")
    sys.exit(0)


def scene1():
    print('''
  Enter 
    R for rules,
    S to start game or, 
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 's':
        start_game()
    elif user_input == 'r':
        print_rules()
    elif user_input == 'e':
        end_game()
    else:
        print("Invalid entry! Use only letters shown for each of the options")
        scene1()


def start_game():
    print('''
  You are a traveller trained in magic and swordplay. 
  You are on a quest to find a crown that is said to give a second life to the worthy. 
  On your travels, you encounter an inn that hopefully can give you a clue as to where it is. 
  As you walk in, you notice that the inn is empty, save for the bartender and an occasional mouse. 
  A sweet smell fills the air, leading you to the bartender. 
  You open your mouth to ask him-
  ''')
    print('''
  Enter 
    C to ask him about the crown
    D to ask for a drink or
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 'c':
        crown()

    elif user_input == 'd':
        drink()

    elif user_input == 'e':
        end_game()

    else:
        print("Invalid entry! Use only letters shown for each of the options")
        start_game()


def stone_room():
    print('''
  You are on the stone floor of a large room.  
  You see three doors around you. 
  They all look normal.
  The last one is locked with two locks. 
  You think that there might be a key behind the other doors. 
  You decide to go through one of the doors.
  ''')
    print('''
  Enter 
    F to see what's behind the first door
    S for the second door or
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 'f' or 's':
        rand_choice = random.randint(1, 3)
        if rand_choice == 1:
            claw_marks()
        else:
            water()

    elif user_input == 'e':
        end_game()

    else:
        print("Invalid entry! Use only letters shown for each of the options")
        stone_room()


def crown():
    print('''You ask the bartender about the crown of rebirth. \n“Sorry kid, I’ve never seen any kind of crown. But I 
    do know someone who might. First, have a drink. It’s on the house.”\n He hands you a shimmering cocktail.\n You 
    try to refuse, but your hand reaches out for the cup.\n You gaze into the depths of the drink as you ask him, 
    “Where can I find them?” \nYou bring the cup to your lips.\n I mean, a little sip never hurt, right? \n“You’ll 
    find out in a moment.” \nWhat does that mean?...\n
  ''')
    stone_room()


def drink():
    print('''
  You ask him for a drink. 
  He grins at you and hands you a shimmering cocktail. 
  You take a suspicious sip while eying him. 
  You frown and look at your drink. 
  “What’s in this?” you ask. 
  “Just a strong sedative.”
  ''')
    stone_room()


def claw_marks():
    print('''
  You decide to go through the door with claw marks. 
  You reach to grab your sword and find that it isn’t there. 
  Looking around, you see that there are a variety of swords behind you. 
  You grab the one that looks the strongest and prepare yourself. 
  You slowly turn the knob and what you see surprises you! 
  You can see a forest laid out in front of you. 
  The moonlight shines from between the leaves. 
  There are howls heard in the distance. 
  Are those werewolves? 
  You can just make out the other side of the forest. 
  Seems to be quite a small forest, or maybe just a fake one.
  The growls get louder as you walk to the other side of the forest. 
  Keeping your hand on the new sword you found, you slowly enter a clearing. 
  There is an entire pack of werewolves. 
  You decide that you should use your sword to get rid of the wolves.
  ''')
    for val in range(3):
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        print("What is", num1, " times ", num2, "?")
        user_input = int(input())
        if user_input == num1 * num2:
            if val == 2:
                print('''
          You defeat the wolves and look for the key to open the third door. 
          After 30 minutes of continuous searching, you still can not find the key. 
          You choose to use a locating spell and lo and behold, the key was in a tree. 
          It looked a little incomplete though, so you looked around to see if there was another part to it. 
          After searching with the locating spell, you found a keychain to put the key on. 
          You head back to the door to find nothing but forest. 
          You try to search around the area, but there seems to be an invisible wall blocking\
          you from passing through that point. 
          Walking along the ‘wall’ takes you in a circle, and you come back to the clearing, where there is a door\
          that looks like the locked door back in the stone room.
          You use the key to unlock it and enter the door.
          ''')
                door_three()
            else:
                print('Correct!')
        else:
            end_game()
            break


def water():
    print('''
  You sniff the air and find a wall with a lot of herbs and crystals to make spells behind you. 
  You pick a few that will help you breathe underwater and see in the dark, as those might be useful. 
  You go through the door with water. 
  The entire room is dark as you enter, the only light coming from a glowing object in the water. 
  You see large shapes moving underwater and they look like humanoids, so they are either sirens or mermaids. 
  Most likely sirens. 
  You sigh as their voices fill the room. It sounds so beautiful…
  You shake your head. 
  You quickly make a spell so you can’t hear their voices and one for breathing underwater and wait for them to \
  swim away.
  As you wait, you look around for any signs of a key. 
  To your disappointment, the area is a flat platform with no crevices and a smooth ceiling. 
  Nowhere to hide anything… Maybe the key is in the water? 
  You rush to the edge of the lake and peer down. 
  There are many rocks and seaweed down there, perfect for hiding small objects. 
  Looking around the lake, there is this one area where the sirens don't seem go. 
  That might be a safe area to go down. But it might also contain a more dangerous monster. 
  The area where you are has a lot of sirens, but you could probably fight them off. Maybe.
  ''')
    print('''
  Enter 
    Ns for the area without sirens
    S for the area with sirens or
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 'ns':
        without_sirens()

    elif user_input == 's':
        with_sirens()

    elif user_input == 'e':
        end_game()

    else:
        print("Invalid entry! Use only letters shown for each of the options")
        water()


def without_sirens():
    print('''
  You choose the area without sirens. 
  It should be safer, right? 
  The sirens seem to be trying to get you away from that area, but you ignore them. 
  You jump in the water, and your vision goes completely black. 
  You can still feel the water around you and you know you are awake, but you can’t see your own hand in front of you.
  You try to swim back to the surface, but you can’t  find and direction. 
  There is a low growl from behind you, and it steadily gets closer. 
  Suddenly, you feel sleepy as your eyes close… 
  Or maybe they are still open…
  ''')
    end_game()


def with_sirens():
    print('''
  You decide the area with the sirens is best. 
  You take a deep breath and jump in, prepared for a fight.
  ''')
    for val in range(3):
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        print("What is", num1, " times ", num2, "?")
        user_input = int(input())
        if user_input == num1 * num2:
            if val == 2:
                print('''
          The force of the fight takes you deeper, past the slowly disappearing bodies of the sirens. 
          You land in a rocky forest.
          You look around and find a key.
          It's made of silver, and looks like it was broken in half.
          You notice a seaweed forest next to you.
          Maybe it's there.
          ''')
                find_keys()
            else:
                print('Correct!')
        else:
            end_game()
            break


def find_keys():
    print('''
  Enter 
    Sw to see what's behind the seaweed or
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 'sw':
        seaweed()

    elif user_input == 'e':
        end_game()

    else:
        print("Invalid entry! Use only letters shown for each of the options")
        find_keys()


def seaweed():
    print('''
    You go to the seaweed. It would be harder to find something in this giant forest of seaweed. 
    Soon enough, a glint within the seaweed caught your eye. 
    It was a small bottle filled with-
    A tentacle pushed you back.
    Not another fight!
    ''')
    for val in range(3):
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        print("What is", num1, " times ", num2, "?")
        user_input = int(input())
        if user_input == num1 * num2:
            if val == 2:
                print('''
            You defeat the Kraken and find the other piece of the key in that tiny bottle.
            The piece of key looked like it was made of mother-of-pearl.
            Shouldn't the pieces be made of the same material?
            You swam to the surface before you ran out of breath.
            When you put them together, they glowed softly and changed the pattern.
            You wonder why magic obcets always glow.
            What is the point of that?
            ''')
                door_three()
            else:
                print('Correct!')
        else:
            end_game()
            break


def door_three():
    print('''
  You get back to the stone room feeling triumph. 
  The key was fixed in your hand, and you walked to the third door. 
  You unlocked the door and saw two paths ahead of you. 
  The first one had scorch marks on the ceiling and floor. 
  The second one had nothing except for what looked like snake skin on the floor.
  ''')
    print('''
  Enter 
    L for the first path
    R for the second path or
    E to end game
  ''')
    user_input = input().lower()
    if user_input == 'l':
        path_one()
    elif user_input == 'r':
        path_two()
    elif user_input == 'e':
        end_game()
    else:
        print("Invalid entry! Use only letters shown for each of the options")
        door_three()


def path_one():
    print('''
  You walk down the first path and hide behind the corners as a light grew at the end of the tunnel. 
  When you reach the end, there is a small opening. 
  There is a giant fire sprite in front of a seemingly empty pedestal. 
  You assume you have to fight the sprite in order to properly see what’s on that pedestal. 
  You run in, potions at the ready.
  ''')
    for val in range(3):
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        print("What is", num1, " times ", num2, "?")
        user_input = int(input())
        if user_input == num1 * num2:
            if val == 2:
                print('''
          You defeated the monster and now walk to the pedestal. 
          The crown of rebirth is standing there. 
          You take it off and put it on your head.
          You won. 
          ''')
                print('''
          Enter 
            B for the bonus scene or
            E to end game
          ''')
                user_input = input().lower()
                if user_input == 'b':
                    bonus()

                elif user_input == 'e':
                    end_game()
                    break
                else:
                    print("Invalid entry! Use only letters shown for each of the options")
            else:
                print('Correct!')
        else:
            print('''
            INCORRECT!
            Your body turns to ashes.
            You failed this time…
            ''')
            end_game()


def path_two():
    print('''
  You walk down the second path and hide behind the corners as a light grew at the end of the tunnel. 
  When you reach the end, there is a small opening. 
  There is a snake woman with snake hair surrounded by statues of other travellers who came here and failed. 
  Medusa is circling in front of a seemingly empty pedestal. 
  You assume you have to fight her in order to properly see what’s on that pedestal. 
  You run in, sword at the ready.
  ''')
    for val in range(3):
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        print("What is", num1, " times ", num2, "?")
        user_input = int(input())
        if user_input == num1 * num2:
            if val == 2:
                print('''
          You defeated the monster and now walk to the pedestal. 
          The crown of rebirth is standing there. 
          You take it off and put it on your head.
          You won. 
          ''')
                print('''
          Enter 
            B for the bonus scene or
            E to end game
          ''')
                while True:
                    user_input = input().lower()
                    if user_input == 'b':
                        bonus()
                        break

                    elif user_input == 'e':
                        end_game()
                        break
                    else:
                        print("Invalid entry! Use only letters shown for each of the options")
            else:
                print('Correct!')
        else:
            print('''
            INCORRECT!
            Your body slowly turns to stone.
            Now you’re no better than any of the other travelers who came here before you.
            ''')
            end_game()


def bonus():
    print('''
  You get woken up by the blaring sound of your alarm clock. 
  That was such a weird dream. 
  Mom calls you down for breakfast and tells you to get ready for school. 
  You quickly put on your favourite outfit and rush downstairs to grab your bag and lunch. 
  Your mom stuffs a samosa in your mouth and you run to the bus. 
  In your room, a crown glitters on your neatly made bed.
  Your cat judges it.
  It's hers now.
  ''')
    print('''
  Would you like to play again?
  Yes
  No
  ''')
    user_input = input().lower()
    if user_input == 'yes':
        scene1()
    elif user_input == 'no':
        end_game()
    else:
        print("Invalid entry! Use only letters shown for each of the options")
        bonus()


def print_rules():
    print('''
  You are a traveller on a journey to find the Crown of Rebirth.
  You must make different choices and fight monsters to get to the end.
  You will encounter many monsters on the way.
  Can you make it to the end?
  ''')
    print('''
  Enter
  Play if you want to start the game or
  E if you want to exit the game
  ''')
    user_input = input().lower()
    if user_input == 'play':
        start_game()
    elif user_input == 'e':
        end_game()
    else:
        print("Invalid entry! Use only letters shown for each of the options")
        print_rules()


scene1()
