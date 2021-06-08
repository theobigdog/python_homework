
import Slayer_rolls
import random
import time
import colorama
from colorama import Fore, Back, Style, Cursor, win32, init
from colorama.winterm import WinTerm
from msvcrt import kbhit, getch


info_list = ["Magic Coin (Run Away, little girl)", "Sword (3-6 damage)", "Battle-Axe (2-8 damage)", "Halberd (1-10 damage)"]

def next():
    done = False
    while not done:
        if kbhit():
            key = ord(getch())
            if key == 13:
                print()
                done = True

def display_health(player, dragon):
    winterm.erase_screen(mode=2)
    fore = Fore.WHITE + Style.BRIGHT
    print((fore + Cursor.POS(name_x,name_y) + player.name).center(name_x + 2))
    if player.health <= (0.25 * player.starting_health):
        fore = Fore.RED + Style.BRIGHT
    print(fore + Cursor.POS(health_x,health_y) + "Health:  " + str(player.health) + "/" + str(player.starting_health))
    dragon_fore = Fore.WHITE + Style.BRIGHT
    print((dragon_fore + Cursor.POS(drag_name_x,drag_name_y) + dragon.name).center(drag_name_x))
    if dragon.health <= (0.25 * dragon.starting_health):
        dragon_fore = Fore.RED + Style.BRIGHT
    print(dragon_fore + Cursor.POS(drag_health_x,drag_health_y) + "Health:  " + str(dragon.health) + "/" + str(dragon.starting_health))
    print(Fore.WHITE)

def choose_your_weapon(player, dragon) -> str:
    print()
    print("Choose your weapon:")
    print()
    for choices in range(0, len(info_list)):
        print(info_list[choices])
    print()
    choice = input("Your choice?  ")
    counter = 1
    while choice not in player.inv_list:
        if choice == "Magic Coin":
            print()
            print("That's no longer listed as an option, now is it.  You used it up, remember?  Pick something else, and make it snappy!")
        if counter > 2:
            print()
            print("Having taken too long to decide what to do, " + dragon.name + " closes in, opening her ample maw to show rows of huge, razor-sharp teeth")
            print("Fear takes ahold of you, and you drop all weapons.  You might have a peed a little too.  We'll check later!")
            next()
            print()
            print("Suddenly, you feel a surge of strength and confidence; dodging the gaping mouth of " + dragon.name + ", you hop onto her back and start pounding her in the neck.")
            print("The scales, being highly protective, absorb every punch, leaving you with a fractured wrist on one side, and a very bruised hand on the other.")
            print('"Mierda," you grunt as ' + dragon.name + ' begins to buck.')
            print('"Time to improvise," you think to yourself.  Deftly, you untie your man-bun, reaching for ' + dragon.name + "'s neck.")
            return "Bare-Hands"
        if choice == "Sword" or choice == "Battle-Axe" or choice == "Halberd":
            print()
            print("Do you not remember what just happened?  The dragon shattered it.  It's broke and you ain't fixin' it right now.")
        print()
        if counter == 1:
            choice = input("You are, quite literally, playing with fire...  Please choose something from the list, or get eviscerated and burnt to a crisp:  ")
        elif counter == 2:
            choice = input("Seriously, she is closing in!  Choose something; anything!  Now!!!  ")
        counter += 1
    return choice  

def player_attack(player, dragon, weapon : str) -> int:
    if Slayer_rolls.multi_roll(1,10) > dragon.dodge:
        print("You missed her!  That was a poor choice.")
        return 0
    damage = player.inv_dict[weapon]
    crit = Slayer_rolls.multi_roll(1,20)
    if crit > player.crit_chance:
        damage = int(damage * player.crit_multiplier)
    if damage > dragon.health:
        damage = dragon.health
    if damage == 1:
        hp = "hitpoint"
    else:
        hp = "hitpoints"
    print()
    print("You swing your mighty " + weapon + ", striking " + dragon.name + ", for " + str(damage) + " " + hp + ".")
    if crit > player.crit_chance:
        print("Critical Hit!!")
    return damage

def dragon_attack(player, dragon, weapon : str) -> int:
    attack = dragon.attack_type_list[0]
    if Slayer_rolls.multi_roll(1,10) > dragon.attack_type:
        attack = dragon.attack_type_list[1]
    if Slayer_rolls.multi_roll(1,10) > player.dodge:
        print()
        print("You evaded the attack.  Wow, I didn't think you had it in you!")
        return 0
    damage = dragon.attack_type_dict[attack]
    critical_hit = Slayer_rolls.multi_roll(1,20)
    crit = False
    if critical_hit > dragon.crit_chance:
        crit = True
        damage = int(damage * dragon.crit_multiplier)
    if attack == dragon.attack_type_list[0]:
        drag_weap = "wicked claws"
    else:
        drag_weap = "fireball-blast"
    if damage > player.health:
        damage = player.health
    if damage == 1:
        hp = "hitpoint"
    else:
        hp = "hitpoints"
    if drag_weap == "wicked claws":
        print(dragon.name + " swipes at you with her " + drag_weap + ", slicing you for " + str(damage) + " " + hp + ".")
    else:
        print(dragon.name + " opens her maw, showing rows of razor-sharp teeth, and shoots a " + drag_weap + " at you, spraying you in the face for " + str(damage) + " " + hp + ".")
    if crit:
        print("Critical Hit!!")
    if Slayer_rolls.multi_roll(1,20) > dragon.weapon_break:
        time.sleep(0.5)
        print()
        print("As you are assaulted by her attack, your " + weapon + " is shattered, leaving you standing there, mouth agape and even more terrified.")
        print(dragon.name + ' cackles with glee, as she begins to smack her gums together.')
        print('"She looks hungry," you think, as you stand there beginning to shudder.  At this point, you may have tinkled a little.  Don\'t judge!')
        matched = False
        counter = 0
        while matched == False:
            if player.inv_list[counter] == weapon:
                matched = True
            else:
                counter += 1
        player.item_broken(counter)
    return damage

def commence_battle(player, dragon):
    while player.health > 0 and dragon.health > 0:
        winterm.erase_screen(mode=2)
        display_health(player, dragon)
        weapon = choose_your_weapon(player, dragon)
        if weapon == "Magic Coin":
            print()
            print('As the Wise-Wizard instructed, before you had to.... nevermind, that\'s a tale for a different story.')
            print('You quickly rub the "Heads" side of the coin and flick it into the air.')
            print('The coin flips and spins into the air, beginning to sparkle and crackle, like lightning will shoot out of its arse.')
            next()
            escape = player.inv_dict[weapon]()
            if escape == "Heads":
                print()
                print('Rather than falling into your awaiting hand, the coin floats in the air, heading toward ' + dragon.name + '.')
                print('It is almost impossible for you to take your eyes off of the coin, mesmerizing as it is.')
                print(dragon.name + ' is not so lucky and remains transfixed by the coin, as electricity crackles all around it.')
                print('"This is my only chance for survival," you think to yourself, as you bolt for the tunnel exit.')
                next()
                if dragon.name == "The Ancient":
                    print('Having already forgotten about the first, destructive blast, you screech to a halt in front of the entrance, and begin to sob.')
                    print(dragon.name + " lifts up onto her hind legs, releasing a massive fireball in your direction as you stare at it stupidly.")
                    next()
                    dragon_damage = dragon.attack_type_dict[dragon.attack_type_list[1]] * 3
                    print()
                    print("The incoming bolt strikes you in the chest for " + str(dragon_damage) + " hitpoints.")
                    next()
                    player.set_health(dragon_damage)
                    if player.health < 1:
                        print()
                        print("Well I guess that's that.")
                        next()
                        print()
                        print("The End.")
                        print()
                        print()
                        exit()
                else:
                    print("You flee down the tunnel, muttering awful things about yourself.")
                    print('"I am such a wuss...  I\'ll never be a true warrior.  I\'ll never be anything." you curse as you continue down the tunnel, hearing endless, angry shrieks behind you.')
                    next()
                    print()
                    print('You may have survived, but your courage, your self-worth and your pride are all wounded beyond repair.')
                    next()
                    print()
                    print('You live a very long, very sad, lonely life.  As you die on your bed in your empty house, you sob uncontrollably.')
                    print('Then you die.  Alone.  And you poop yourself.  It\'s disgusting.')
                    next()
                    print()
                    print("The End")
                    print()
                    print()
                    exit()
            else:
                print()
                print("The sparkling fizzles, and the coin returns to your waiting hand, burning it terribly, as it is still white-freakin'-hot.")
                print("You quickly drop the coin, yelling obsenities, and stare at an incoming fireball from " + dragon.name + ".")
                dragon_damage = dragon.attack_type_dict[dragon.attack_type_list[1]] * 2
                player.set_health(dragon_damage)
                print("The projectile slams into your face, messing up your teeth, real bad, for " + str(dragon_damage) + " hitpoints of damage.")
                next()
                if player.health < 1:
                    next()
                    print()
                    print("You have been weighed.  You have been measured.  And you have been found wanting.")
                    print("You are slain.  Dead dead deadskies.")
                    print("It was inevitable.")
                    next()
                    print()
                    print("The End.")
                    print()
                    print()
            player.item_broken(0)
        elif weapon == "Bare-Hands":
            time.sleep(1)
            print()
            print("As you wrap your man-bun around her neck, " + dragon.name + " begins to buck and jump and twist and roar.")
            print("The agitation loosens up a few strands of your hair, which tickle against your nose, causing you to almost sneeze, and almost giggle.")
            attempt = player.inv_dict[weapon]
            if attempt > dragon.strangle:
                next()
                print()
                print(dragon.name + " continues to buck and writhe, but your grip is tight, and, eventually, her head slams down into the ground; a large fart escaping with her last breath.")
                print("She is dead.  You are victorious!!")
                dragon.health = 0
                next()
                print()
            else:
                next()
                print()
                print("You are no match for the brutal strength of this majestic creature, and you are bucked off almost immediately.")
                print('As you splat into a huge pile of dragon shit, apparently in ' + dragon.name + '\'s toity, you flail madly, but you are no match for the remaining digestive enzymes in the pile.')
                print('You sink further into the swamp of dragon poop, attempting to breathe, but only getting more poop in your mouth and lungs.')
                next()
                print()
                print('After a few seconds, you dissolve into the pile leaving only bones and teeth behind.')
                print('Your last thought:  "What the hell was I thi...."')
                print('"thinking"?  Not too much.  It\'s a goram dragon after all.')
                next()
                print()
                print("The End.")
                print()
                print()
                exit()
        else:
            dragon.health -= player_attack(player,dragon,weapon)
            next()
            if dragon.health > 0:
                dragon_damage = dragon_attack(player,dragon,weapon)
                if dragon_damage > player.health:
                    dragon_damage = player.health
                player.health -= dragon_damage
                next()

    if dragon.health == 0:
        print('You have survived!!!  You have slain the beast!  You are victorious and all should bow down before you, for you are the Dragonslayer!')
        next()
        print()
        print("You attempt to sever her head, hoping for a stunning trophy to mount upon your wall at home, but your weapons are all blunted from battle.")
        print("You bust out your only remaining tool, however, your safety scissors don't seem to do the trick, so you give up.")
        print("Why the hell are you carrying those anyway?  Are you in kindergarten or something?")
        if dragon.name == "The Ancient":
            next()
            print()
            print("You look around at the mounds of treasure, quite pleased with yourself and now filthy rich.")
            print("Then it hits you:  you have no way out of here!")
            print("You search everywhere but are unable to find any way out.")
            print('"How did the goram dragon get in and out?" you ponder.')
            next()
            print()
            print("Eventually, the gas released when " + dragon.name + " died, has diffused throughout the cave.")
            print("Unbeknownst to you, one of its primary components was sulfuric acid, which you have inhaled as you searched for an exit.")
            print("After a few torturous hours, you succomb to the lesions growing in your lungs, drowning on your own mucus.")
            print('Your last thought, "Well that sucked."')
            print("And it did.")
            next()
            print()
            print("The End.")
            print()
            print()
            exit()
        elif dragon.name == "Trogdor The Burninator" or dragon.name == "Skippy":
            next()
            print()
            print('After gathering all the treasure you can possibly carry, you head back down the entrance tunnel, and back home.')
            print("Upon your return, you are greeted with fanfare and applause from the citizens of your small town, which had been devastated by dragon attacks.")
            print('"I have been tested and found worthy," you think to yourself, as you pass out and fall off your horse onto your face, in front of everyone.')
            next()
            print()
            print('You wake, very sore, in a foreign bed, and realize you are in The Bubba\'s hut, the town cleric.')
            print('"What happened?" you ask, as you attempt to sit up.')
            print('"You goram fool," he says.  "You\'ve inhaled a significant amount of sulfuric acid, during your battle.')
            print('"The shit\'s as deadly as it gets.  You don\'t have long to live.  I hope it was worth it."')
            next()
            print()
            print('As you lay in Bubba\'s bed over the next few weeks, you cry yourself to sleep each night.')
            print('"I am such a greedy moron," you sob one morning.  These are your last words as you suffocate on your own mucus.')
            next()
            print()
            print("You have died.  I, too, hope it was worth it.")
            next()
            print()
            print("The End.")
            print()
            print()
            exit()
        if dragon.name == "Skippy":
            print()
            print('You have completed the adventure on "Regular" mode.')
            print('For any future attempts, use code "Kool-Aid" when prompted for readyness at the beginning of this story.')
            print('This will enable "Hard" mode, should you have the cajones to really test yourself.')
    if player.health == 0:
        print()        
        print("You have been slain.  You are terrible, and you deserved this.")
        next()
        print()
        print("The End.")
        print()
        print()
        exit()

name_x = 5
name_y = 3
health_x = name_x
health_y = 4
drag_name_x = 35
drag_name_y = 3
drag_health_x = drag_name_x
drag_health_y = 4
names_1 = ["Smug","Conceited","Silly","Happy","Sad","Amorphic","Petty","Pretty","Largish","Smelly","Farty","Tender","Kind","Jerky","Angry","Tumescent","Ridiculous","Stupid","Skanky","Master","Gassy","Broken"]
names_2 = ["Pussy-Willow","Monkey","Frog","Turtle","Fish","Dog","Tapir","Beaver","Kitten","Child","Worm","Gas","Tyrant","Giraffe","Fungus","Crab","Fart","Smegma","Warrior","Battle-Cat","Counselor","Magician","Bunghole","Baby","Doctor","Rock"]
names_3 = ["Smurf","Mouth","Lips","Fungus","Womanizer","Grass","Smegma","Clutz","Bunghole","Kitten","Baby","Doctor","Snarfblat","Hunter","Eater","Sniffer","Spanker","Robot","Trash-can","Ingestor","Hater","Player"]

class Player:  # Same for all modes

    def __init__ (self, name : str):
        self.name = name  # Update this to pick random funny descriptive names from three diff lists
        self.starting_health = Slayer_rolls.multi_roll(25,50)
        self.health = self.starting_health
        self.crit_chance = 15
        self.crit_multiplier = 3
        self.dodge = 8
        self.inv_list = ["Magic Coin", "Sword", "Battle-Axe", "Halberd"]
        self.inv_dict = {
            self.inv_list[0] : Slayer_rolls.get_coin_toss,
            self.inv_list[1] : Slayer_rolls.multi_roll(3,6),
            self.inv_list[2] : Slayer_rolls.multi_roll(2,8),
            self.inv_list[3] : Slayer_rolls.multi_roll(1,10),
            "Bare-Hands" : Slayer_rolls.multi_roll(1,100)   
            }
    
    def rename(self):
        random_first = names_1[random.randint(0,len(names_1)-1)]
        random_second = names_2[random.randint(0,len(names_2)-1)]
        random_third = names_3[random.randint(0,len(names_3)-1)]
        self.name = (random_first + " " + random_second + "-" + random_third)

    def set_health(self, damage : int):
        self.health -= damage

    def item_broken(self, item : int):
        self.inv_dict.pop(self.inv_list[item])
        self.inv_list.pop(item)
        info_list.pop(item)
        

class Trogdor_The_Burninator: # Easy Mode
    
    def __init__ (self):
        self.name = "Trogdor The Burninator"
        self.starting_health = Slayer_rolls.multi_roll(60,80) # modest health
        self.health = self.starting_health
        self.crit_chance = 18 # poor aim, so crits less likely
        self.crit_multiplier = 4 # brutal attacks, due to extra, beefy arm
        self.attack_type = 8 # chance for breath vs melee
        self.dodge = 10 # cannot dodge
        self.strangle = 70  # chance of death from strangulation
        self.weapon_break = 17 # reasonable chance of breaking weapons, due to brutality of attacks
        self.attack_type_list = ["melee","breath"]
        self.attack_type_dict = {
            self.attack_type_list[0] : Slayer_rolls.multi_roll(2,6),
            self.attack_type_list[1] : Slayer_rolls.multi_roll(3,8)
        }
    
    def intro(self):
        print()
        print('You continue to skip down the path, passing what look to have been a few bottles of mead.  Based on their smell, their contents have not been gone for terribly long.')
        print('Skipping (I said STOP) down the twisting route starts to make you feel dizzy, almost drunk.  If you\'re looking to battle a dragon, you\'d better start taking this more seriously.')
        next()
        print()
        print('A little further along, the smell of mead reaches your nostrils, once again, only this time, much more pungent and "fresh".  The further you go, the stronger the smell becomes.')
        print('You begin to hear a distant, rhythmic sound, almost like growling.  As you continue along your merry way, the growling gets louder and louder; the rumbling echoing through the tunnel.')
        print('Rounding yet another bend in the path, the tunnel begins to widen, and the rumbling has increased dramatically in volume; you\'ve finally reached the other side.')
        next()
        print()
        print('The tunnel continues to widen into a large cavern.  Conveniently spaced torches dot the ground, allowing you to see into the far reaches.')
        print('There, in the center of the cave, lies what looks like a very serpentine dragon, with a beefy arm growing out of its side?  One of the most bizarre creatures you\'ve ever come across.')
        print('It almost looks cartoonish.  You don\'t really know what a "cartoon" is, but it definitely looks like a character from one.')
        next()
        print()
        print('The rumbling appears to be coming from the dragon.  "Is it... snoring?" you ask yourself?  You see the dragon\'s chest rise and fall, in time with the rumbling.')
        print('"She\'s passed out?  What gives?" you wonder.  Being a noble warrior, not wanting to take advantage of the situation, you carefully walk up to the sleeping beast.  It does not stir.')
        next()
        print()
        print('"Hey," you quietly say.  Nothing.  "I said Hey", you speak a little louder.  Nothing.  "HEY!!" you scream in her face, as you poke her with the bottom of your torch.')
        print('Clearly still groggy, she rumbles, "Hmmmm what the...." She begins to stir when she sees you.  "Hi," she says.  "You need something?  Can\'t you see, I\'m trying to get some rest?"')
        print('"I\'m dead-tired and hung-over as shit" she mumbles, rubbing at her eyes with her clawed arm, "so I hope this is important."')
        print('"Are you serious?" you think to yourself.  "Are you the fierce beast who just attacked my neighbors, The Rodents?"')
        print('"Hmmmm.... I guess so," she mumbles.  "I don\'t much remember last night.  I was drunk as $hit."')
        next()
        print()
        print('Well this really chaps your hide.  She slaughtered your neighbors and friends, just because she got drunk?  How does a dragon get drunk, anyway?  You thought they were magical.')
        print('"Prepare to defend yourself, for I am ' + player.name + ', and I am here for the vengeance of my town, which you have repeatedly ravaged."')
        print('"Are you serious?  Do we have to do this right now?  I\'m very tired, and very sorry, ok?" she speaks, as if this will assuage anything.')
        print('"If you don\'t mind your p\'s and q\'s, you are in for it."')
        print('Enraged by her comments, you bust out your dagger, kept in its sheath around your neck.  It is an heirloom, and, having saved your ass many times, you know it is an excellent, deadly weapon.')
        print('As you attempt to strike her, her beefy arm grabs the dagger, mid-swipe, and shatters it on the cave floor.')
        print('As you look in shock at the broken pieces of your treasured weapon, she rears up, wobbling slightly.')
        next()
        print()
        print('She booms, "You dare to attack me?  I am ' + self.name + ', and with my beefy arm, I will crush you like a worm!"')
        print('And so it begins....')
        next()
    
    def set_health(self, damage : int):
        self.health -= damage


class Skippy:  # Normal Mode

    def __init__ (self):
        self.name = "Skippy"
        self.starting_health = Slayer_rolls.multi_roll(80,100) # reasonable health, considering her youth
        self.health = self.starting_health
        self.crit_chance = 16 # reasonable aim, despite youth
        self.crit_multiplier = 2.25 # moderate crits, fairly young and not yet "strong"
        self.attack_type = 6 # chance for breath vs melee
        self.dodge = 6 # good dodge, with young, quick reflexes, and the ability to read minds
        self.strangle = 80  # chance of death from strangulation
        self.weapon_break = 18 # ok chance of breaking weapons - not yet experienced enough to be good at it
        self.attack_type_list = ["melee","breath"]
        self.attack_type_dict = {
            self.attack_type_list[0] : Slayer_rolls.multi_roll(3,8),
            self.attack_type_list[1] : Slayer_rolls.multi_roll(4,8)
        }
    
    def intro(self):
        print()
        print('You wander down the freshly-carved path, which appears to have been dug through completely solid rock.  There are very few curves and corners - it is mostly a straight path.')
        print('After a few minutes, the tunnel begins to widen, and brighten.  You peer down the length of the cavern, only to find a young, blue ridged-back dragon, apparently playing with human bones.')
        next()
        print()
        print('"I am the fiercestest warrior!", she grumbles, as she swings a femur towards a nearby skull.')
        print('"No, I am the fiercestest warrior!", she roars as she head-butts the femur with the skull.')
        print('This goes on for a few minutes and you wonder, "What the hell is the matter with this thing?  Does it not hear me breathing back here?"')
        print('"YES, I hear you breathing, and I can read your mind!", she roars, as she turns to face you.')
        print('"Do you not realize that I have been mocking you?  I am ' + dragon.name + ', and I demand your respect!"')
        next()
        print()
        print('"' + self.name + '?" you wonder.  "Isn\'t that a boys name?" you ask her.')
        print('Enraged by your question, she puffs out her chest and booms "I am ' + dragon.name + ', and you will now learn to respect a dragon as young as I!"')
        print('As she puffs up, you stare in horror as she appears to have doubled in size.  Her mouth opens showing modest, but very sharp teeth, drool running down her chin.')
        print('"Wow does she look hungry," you think as you begin to back away.  She begins to laugh hysterically.')
        print('"Shit."')
        next()
    
    def set_health(self, damage : int):
        self.health -= damage


class The_Ancient:  # "Beast" (lolz) Mode

    def __init__ (self):
        self.name = "The Ancient"
        self.starting_health = Slayer_rolls.multi_roll(80,120) # Beefy
        self.health = self.starting_health
        self.crit_chance = 15 # experience increases crit chance
        self.crit_multiplier = 2.75 # refined aim results in slightly increased crit damage
        self.attack_type = 7 # chance for breath vs melee
        self.dodge = 7 # experience increases evasion
        self.strangle = 90 # chance of death from strangulation
        self.weapon_break = 15 # strong attacks = more breakage
        self.attack_type_list = ["melee","breath"]
        self.attack_type_dict = {
            self.attack_type_list[0] : Slayer_rolls.multi_roll(4,8),
            self.attack_type_list[1] : Slayer_rolls.multi_roll(5,10)
        }
    
    def intro(self):
        print()
        print("The tunnel is in complete shambles.")
        print("You shimmy and crawl and squeeze your way through, deeply questioning your decision-making skills.")
        print("You reach multiple crevices which barely allow your passage, and it is clear that it would be nigh impossible to turn back.")
        print('"Geez...  I hope this tunnel has an exit!" you say to yourself.')
        next()
        print("As the tunnel comes to an end, a cave begins to appear, a thick layer of dust and detritus covering everything in sight.")
        print("A few dusty, rusty coins are scattered around, which you kick playfully.  And stupidly.")
        next()
        print("Suddenly, two white-hot slits appear in the distance, and there is rumbling of a voice, so deep, it rattles and shakes the very walls of the cave.")
        print()
        print("WHO DARES ENTER THE CAVE OF THE ANCIENT?!")
        print("ALL WHO ENTER SHALL DIE!!  COME NOW, FACE THE WRATH OF THE ANCIENT!!")
        next()
        print()
        print("A vision of unimaginable wealth appears as The Ancient releases a massive fireball towards you.")
        print("You deftly duck the blast, but quickly realize that the projectile is now headed for the tunnel exit.")
        print('"No!!" you yell, as the exit collapses.  "Well I sure do hope there is another way out of here."')
        next()
        print()
        print("As you turn back around, a second fireball flies at your face!")
        print("With your cat-like skills and reflexes, you parry the blast which ricochets towards the ceiling of the cave.")
        print("The massive blast lights up almost the entire cave, providing a vision of The Ancient.")
        print("You've heard (old-wives) tales of such a beast, but since a young age, you knew they were bullshit.  Nothing like that could exist.")
        print("She is gigantic.  A flame-crested, coal-black dragon; her irridescent scales covered in battle scars; her very presence demanding awe and disbelief.")
        print("Multiple arrows remain embedded in her impenetrable armor.")
        next()
        print("This is gonna suck.")
        next()
        print("This is it.  This is the battle for which you have been waiting your entire life!")
        time.sleep(2)
        print("Let's rock!")
        next()
    
    def set_health(self, damage : int):
        self.health -= damage

chunnel_list = ["Left","Right"]

chunnel_dict = {
    chunnel_list[0] : Trogdor_The_Burninator,
    chunnel_list[1] : Skippy
}

yes = ["Y","YES","YEP","YUP","YEAH"]

def do_intro(hard_mode : bool):  #  Only Easy and Regular Modes available at first.  If Regular Mode is beaten, code "Kool-Aid" is provided
    print('After hours of hunting through the caves of The Dragon Cliffs, you have stumbled upon a tunnel, hidden between what look like a few stalagmites and stalactites.')
    print('As you get closer, the spikes look much more like teeth of some kind.  How had you never noticed these before?')
    print('A foul odor emanates from the tunnel.  Death.  Decay.  Dustmites.')
    print('Deep gouges, like those you would expect to come from something with awfully strong claws, line the tunnel, almost like the passageway had been dug out by a giant cougar.')
    next()
    print()
    print('You try not to get too excited, as, this is not likely the halls for which you have been searching.')
    print('But as you continue, you find large patches of stone which appear to have been burned straight through, scorch-marks still obvious on the surfaces; somehow still looking like fresh marks.')
    print('You begin to find small mounds of what appear to be the remnants of critters found in the nearby forests.')
    next()
    print()
    print('Scattered amongst these bits, you catch a patch of color in one of the heaps, and move closer to investigate.')
    print('You recognize the emblem on the shred of fabric you find in that heap:  2 mice, fighting over a hunk of bread as a trap begins to close on them; the family crest of your closest neighbors.  They are a silly family.')
    print('Well, they were.  These particular neighbors are the reason you are searching here, once again, for they are those, most recently devastated by what appears to have been a dragon attack.')
    print('"This must be it!" you say to yourself.  "I think I\'ve finally found it!!"')
    next()
    print()
    print('Having searched for the fabled Halls of the Wyrm since you were a young child, the thrill in this moment is unlike any you\'ve felt before.')
    print('Some would even say you are acting as giddy as a school-girl.  Stop skipping down the path already.  I can see you.')
    next()
    print()
    print('After an hour of trekking down the tunnel, you reach a fork in the road.')
    print('To the left veers a twisting, turning path along a cliffside with a sheer drop-off, the bottom of which is not in sight.')
    print('To the right, a path through what looks like freshly dug and melted solid rock, disappears after a bend, a few dozen feet in.')
    next()
    if hard_mode:
        print("Your veteran warrior intuition must catch ahold of some detail of a chunk of the floor that just doesn't seem right.")
        print("To the naked eye, it looks like just more tunnel floor.  However, when more closely inspected, underneath a mat of old cobwebs, it turns out there is a third fork extending downwards.")
        next()
    print()
    print('So all that remains is to choose;  which pathway will you take?')


init() # this makes sure the graphics work correctly in DOS windows
winterm = WinTerm()  # enables the next line
winterm.erase_screen(mode=2) # this clears the screen


player = Player(input("¿Como se llama?  "))
print("No.  No, that won't do at all.")
print("You need something with more pep.  More flavor!")
time.sleep(2)
player.rename()
print()
print("How about " + player.name + "?  Yes, I like that.")
print("Henceforth, you shall be known as " + player.name)
next()
print()
hard_mode = False
if input("Are you ready, " + player.name + "?  ") == "Kool-Aid":
    hard_mode = True
if hard_mode:
    chunnel_list.append("Lower")
    chunnel_dict[chunnel_list[2]] = The_Ancient
    print()
    print("Hard-mode enabled")
else:
    print("Alrighty then.  Like it or not, this bus ain't stoppin'.")
print()
intro = input("Intro (Y/N):  ").upper()
if intro in yes:
    winterm.erase_screen(mode=2)
    do_intro(hard_mode)
    print()
    for route in range(0,len(chunnel_list)):
        print(chunnel_list[route])
    print()
    choice = input("Which one?  ")
else:
    print()
    print("In a hurry, are we?  Death will come for you either way!!")
    choice = input("So which tunnel?  ")
while choice not in chunnel_list:
    if choice == "Lower":
        print()
        print("What makes you think there is a lower tunnel?  I gave you your options.")
    else:
        print("Fascinating.  Let's try one from the list, eh?")
    print()
    for route in range(0,len(chunnel_list)):
        print(chunnel_list[route])
    print()
    choice = input("Choose:  ")
if hard_mode and choice != "Lower":
    print()
    print("You entered the code for Hard Mode, and now you're not choosing it?  Chicken.")
    double_check = input("Are you sure you don't want to take the Lower path?  ").upper()
    if double_check not in yes:
        choice = "Lower"
dragon = chunnel_dict[choice]()
if intro in yes:
    dragon.intro()

commence_battle(player, dragon)