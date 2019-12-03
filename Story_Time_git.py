print("I made a change")
print("Change")
import os
#all pictures from google
import winsound
#all sounds from freewave.org
def car (x):
  os.startfile('car_choice_one.jpg')
  #beginning of the story car, setting up the scene
  print ("Every weekend you drove down to a rarely used road just to walk and take in the scenery. You had taken the long route; a lazy day stretched before you and there was no need to rush.\n")
  winsound.PlaySound("car_walking_noise.wav", winsound.SND_ASYNC) #walking in the woods
  print("Summer homes along the river bank gave it a cozy feel; abundant flowers, fancy bird feeders, cheerful garden knickknacks and the charm of small houses kept you happily occupied as you walked the mile or two that connected this hidden back road to the main highway.\n")

  print("You see A walker approached in the distance. Normally no one is here, strange. You're suspicious.\n")

  reply = input("Do you ignore or head nod? \n").lower()

  if reply == "ignore":
    print("You don't see the person or where they go.\n")

  else:
    print("The person smiles and continues in the opposite direction of you. You are all alone again.\n")

  print("You start to walk towards the river. Your mind begins wander as you walked, one thought leading to the next going nowhere in particular. The soft clump of your sneakers on the pavement gives familiar comfort. If only this could last all week.\n")
  winsound.PlaySound("car_branchsnap.wav", winsound.SND_ASYNC) #branch cracking sound
  print("All of a sudden you hear a loud snap.\n")

  look = input("Do you check out what made that noise? (yes or no)\n").lower()

  if look == "yes":
    os.startfile('car_choice_two.jpg')
    winsound.PlaySound("car_branches_rusteling.wav", winsound.SND_ASYNC) #bush sound
    print("A squirrel jumped out of the bush, scaring you slightly.\n")
  elif look == "no":
    print("You continue on your way.\n")

  print("As you continue to walk you hear more and more rustling branches and crunching of leaves on your right, which is a forest lined with trees.\n")
  winsound.PlaySound("car_loud_branch.wav", winsound.SND_ASYNC) #branches cracking louder
  investigate = input("Do you go investigate the noise? (yes or no)\n").lower()

  if investigate == "yes":
    print("You get closer to the forest and start to hear voices.\n")
    investigation(investigate)

  elif investigate == "no":
    print("You continue on your way, walking faster. Eventually getting back to your car.\n")
    os.startfile('car_choice_safety.jpg')
    print("The End.")

def investigation(investigate):
    os.startfile('car_choice_investigate.jpg')
    #if this function is choosen the participant decided to continue and learn more about their environment
    winsound.PlaySound("car_clang.wav", winsound.SND_ASYNC) #clang 
    print("""You stopped walking and started to listen. The first voice was rough and deep, with a hint of an accent. “Hey, put it down here and cover it up. Make sure it’s covered good.  No, not there, over this way.” You couldn't hear the response from whoever he was speaking to. You heard a clang, like metal striking something, and then some curses from a different voice. “It’s too heavy to push over there. Let’s just cover it here and leave it.” This was a husky, cigarette-smoking voice. “Nah, can’t do that. Gotta get it out of here. It’s gotta go by the rest, into the pit. Come on, don’t be a slug, help me out here.” You heard grunting and groans and a lot of rustling.\n""")

    closer = input("Do you get closer to see what is going on? (yes or no) \n").lower()

    if closer == "yes":
      os.startfile('car_choice_throughthebushes.jpg')
      print("""You crept closer to the edge through a small space between some trees, where you could just catch a glimpse. What you saw caused you to freeze. Three big and burly men, pushing at a mound of something, you couldn’t tell what it was. The men were too close together for you to see it.  “Move!” you shouted in my head.  As if they heard me, they stepped aside for a moment. You could see part of something big and long being rolled up.\n""")

      print("You backed away. Not sure what you just saw. What were they trying to get rid of, way down by the river? You wanted to get a better look, but the fear had me wavering.\n")

    elif closer == "No":
      print("You slowly backed up, scared at what may happen next. Then you hear another crash. \n")
      winsound.PlaySound("car_clang.wav", winsound.SND_ASYNC) #clang
    print("You think about what happend, you're very curious about what is going on down there.\n")

    check = input("Should you walk away or stay to look closer?(stay or walk away) \n").lower()
    winsound.PlaySound("car_forest_walk.wav", winsound.SND_ASYNC) #walking away sound

    if check == "stay":
      os.startfile('car_choice_hiddenroad.jpg')
      print("""Curiosity is a strong force and you tended to favor to that side. You got even closer to the edge, holding onto a branch so you could get a better look. Just past where the men were gathered you saw the back end of a small truck, parked along a dirt road that leads down toward the river bank. You didn’t even know a road existed there and you've been walking this road for months. \n""")

      run(help)

    elif check == "walk away":
      os.startfile('car_choice_safety.jpg')
      print("You walk away, heading to your car. One your way back you see a truck drive quickly away. You ignore the eerie feeling and go back home.  \n")

def run (help):
    os.startfile('car_choice_scared.jpg')
    winsound.PlaySound("car_running.wav", winsound.SND_ASYNC) #walking away sound
      #third choice, you got caught and have to figure out what to do, stay in place or run away
    print("One of the men glanced up at you.  You are seized by fear. You jumped back and started walking away, inwardly cursing at yourself for being so stupid. Now what? They saw you. You tried to regain a calm nature by breathing slowly, in and out. Walk, breath, calm down. But they saw you! Or at least one man saw you, you think? You are now a witness to whatever they were doing. Oh, what a stupid idea, you think! This was supposed to be a nice morning walk and now look at what happened.\n")
    
    print("""Okay, think this through. The men could be doing some harmless thing, no big deal, you keep on walking to your car and all will be well. Or, they were trying to clean up from a crime, they saw you and you are in BIG trouble. Suddenly you hear, “Hey, go get her!” You start running, you are almost to your car, you can see it! You reach your car and hear footsteps getting incredibly close. You shakily put the key in the ignition and waited for it to start. It never did. You were planning on going to go to the mechanic next week because it had been acting up for months. The one time you needed it, it was broken. You started hitting the steering wheel and the dashboard willing it to start. You could feel your eyes beginning to flood, but needed to stay strong if you were going to survive.\n""")
    
    help = input("The men were 200 meters from you, and you had no idea what to do. Do you stay in the car and just lock the door or run into the forest? (stay or run) \n").lower()

    if help == "stay":
      os.startfile('car_brokenwindow.jpg')
      winsound.PlaySound("car_windowbreak.wav", winsound.SND_ASYNC) #window breaking sound
      print("The men run up to the car and break the window dragging you out.\n")

    elif help == "run":
      os.startfile('car_choice_purgatory.jpg')

      print("You run into the forest; however, you don't know how to navigate the forest and quickly get lost. You run for miles until you fall asleep.\n")

    print("You wake, walking around the forest, trying to figure out how to get out of here. But, you never did find your way out. You’ll be walking the forest and you will see those men again and again, but they never see you. You are like living in a sort of purgatory. Maybe you have purpose left on this earth, to save others from your fate. \n")

    print("The End.")

def dark(x):
    #beginning part of the story dark, the choices begin
  print ("""After the blackout, I awoke uncomfortably in pitch darkness on what felt like a metal table. I quickly check my arms and legs and begin to wiggle my limbs to make sure they all work. Besides the unfamiliar numbness that tickled my limbs, all I could feel was that sick chill in the air- oh God, that chill. Carefully, I felt around and attempted to sit upright on whatever I was laid out upon. Did they take me to jail, or was this an asylum, some solitary confinement facility where they’d torment me with mind games and medication for what would seem like decades? What is going on?""")

  stay_place = input("Should I stay in the corner or investigate how to get out of here? (stay or investigate?) \n").lower()

  if stay_place == "stay":
    print("You stay in the dark corner\n")

    how_about_now = input("Do you want to investigate now? (yes or no)\n").lower()

    if how_about_now == "yes":
      possibility(stay_place)
    elif how_about_now == "no":
      print("You die in the corner")
      
  elif stay_place == "investigate":
    possibility(stay_place)
    
def possibility(stay_place):
    #second choice in the story dark, begin to explore your surrounding
  print("""Every possibility running through my frantic mind, I blindly stumbled throughout the blackened room as I felt around for a light switch somewhere. Finally, with my hand shaking, I grazed what felt like a switch of some sort, and six flickering LED lights brightened up the room with a pale, disgusting glow. Gasping, I staggered back against the wall in horror as my eyes darted around the room, witnessing the other stretchers, the table of equipment, the cement walls. This had to be some sort of hospital, I think? \n""")

  print("""The tables were humongous in this room and there were six of them, but I was the only one here. I couldn’t understand why I’m here I’m not dead, am I? I couldn’t be dead, even if I were, why would I be stuck here? I was a good person, held the doors open for others, listened to my parents, I did everything I was told! So, why was I here! \n""")

  print("""Just the sight of this room and what might or will happen here makes me want to vomit, not to mention the sick smell of formaldehyde lingering in the air, creating an atmosphere equivalent to the inside of a just-fed carnivore’s mouth. Murder was always something I heard about happening, but I never thought it would happen to me. Long metal doors stood at the end of the room and I began to make my way to them, quickly but quietly going to my escape, all the while avoiding the unidentified stains around the room. \n""")

  print("I couldn’t help but get the feeling that I was being watched. \n")

  open_door = input("Do I dare open the door? (yes or no) \n").lower()

  if open_door == "no":
    print("You stay in the room and look around. \n")
    print("You continue looking around until you fall asleep. You never did wake up from that slumber. \n")
    print("The End.")
  elif open_door == "yes":
    squeeze_through(open_door)

def squeeze_through(open_door):
    #third choice, deciding to leave the original room and find a way out
  print("Moving one door open enough to where I could squeeze through and enter a long hallway, I noticed that this hospital looked as though it hadn’t been maintained, let alone inhabited in decades. No one seemed to be here, so I think I’m alone, but how did I get here? The walls of the abandoned building were rusty and decayed, and the fluorescent lights flickered on one by one as I slowly made my way down the hallway, searching for somebody, anybody, to explain why I was here… and where “here” was. Passing all of the windowless doors, my nose picked up a horrible odor wafting in my direction. \n")
  
  print("Questioning my own sanity had become a lost cause long ago, but somehow this place felt different…like I was insane, like I was imagining this horrible place like this was some terrible nightmare in my own subconscious had conjured up in my endless mind. Roars of rage billowed suddenly from behind me, and I whipped around in the direction of the place I came from to see some shadow progressing towards me. \n")

  shadow_progressing = input("What do I do? Run the opposite way or it is not real and I just have to face it (run or face it). \n").lower()

  if shadow_progressing == "face it":
    print("The shadow got closer and closer. I began to feel its breath right infront of me and then it all goes black. \n")

    print("The End.")

  elif shadow_progressing == "run":
    run_away(shadow_progressing)

def run_away(shadow_progressing):
    #last choice in the story dark, there was no monster, just the participants imagination
  print("Swiftly, I instinctively darted in the opposite direction away from it, wondering what it wanted from me - suddenly I was stopped in my tracks, my locket on the ground, broken. I never took it off how did it end up there? I quickly picked it up and continued to run away from the shadow creature. \n")

  print("How long have I been here, how long have I been running, what time is it even? Ultimately, I have to stop and take a breath, I turn around but it’s not there anymore I must have lost it. There’s nothing but a void around me anymore, I’m in a dark room and it’s all black, I don’t even remember going through a door. All I remember was only running through hallways, nothing is making any sense anymore! \n")

  print("Whoever is doing this to me is pure evil, they have set up the perfect murder. Nobody will ever find me. I’m am lost both physically and mentally now. That thing will find me soon. \n")

  print("I can’t hide, I would just end up making to much noise because I can’t see. I can hear it coming closer. \n")

  print("Once I know it’s in the hallway, I start slowly sliding back until I’m against the wall in a corner, waiting for my impending doom. \n")

  print("My head is in my hands, I’m in a little ball when I see one little light in the room. All of a sudden the lights go on, and I finally can see the room I’m in. \n")

  print("The whole room mirrors, all I see is...me. There’s no noise anymore, no monster, nothing but me. \n")

  print("The End.")

#opening message of the program. Welcoming and the first choice awaits the participant
print("Hello, welcome to Lost. This is an adventure game in which you choose the path. Maybe you'll survive....maybe not. \n")

print("First things first, you pick the story.\n")

x = input("Choose car or dark: \n").lower()
if x == "car":
  car(x)
elif x == "dark":
  dark(x)
