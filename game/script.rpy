# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")


# The game starts here.

label start:
    scene bg grass field
    with fade
    play music "audio/neutral-theme.mp3"
    "You wake up in the middle of a grass field"
    "Your confused You Don't Remember going outside Infact You Dont Even Remember Anything at all"
    "You get up and look around still confused it seems that you are Lost" 
    "Dateball" "Where am I?"
    with fade
    "You notice in the distance a blue shaped ball and next to that blue ball is a red ball"
    label choices:
     "You get closer curious about those balls and notice they are sentient balls like you"
    menu:
        "uhm... Hello? Im a little lost Where am I?":
            show speed normal
            with fade
            "Speedball" "Hello Im Speedball and this is planet 8673"
            "DateBall" "huh what? What do you mean planet 8673 infact why are you so round and ballsy??"
            show speed angry
            "Speedball stares At you intensely  like he was about to rip your soul out for calling him round and ballsy even though you are literally a ball aswell"
            "Dateball" "My Bad Boss" 
            "Speedball still stares at you if I were you I would apologize PROPERLY"
            menu:
                "Apologize PROPERLY":
                  stop music
                  play music "audio/speedballs-theme.mp3"
                  show speed normal
                  "Speedball moves his hands towards you gesturing as if to try and do a thumbs up but he doesnt have fingers so he just raises his hands"
                  "Dateball""uhhhh right sooo where EXACTLY am i? Because telling me what planet im on doesnt exactly help me on my current situation"
                  "Speedball points his hand or should i saw his balls towards a specific direction"
                  "Dateball""Im going to guess that direction leads to a nearby city?"
                  "Speedball Nods almost as if to say… hes saying yes?"
                  "Dateball" "Thanks im gonna go now Bye!"
                  show speed blush
                  "Before you even moved speedball grabs your hand and says plz date"
                  hide speed blush
                  "unclemikey" "SPEEDBALL PLEASE DONT EXECUTE ME ITS JUST PART OF THE THE PLOT ITS VERY ESSENTIAL TO HAVE VERY MUCH"
                  "Jayisnotpro346" "Please Speed we need this"
                  "Barrel" "No yall Dont"
                  "Jayisnotpro346" "FUCK OFF Your not even real"
                  "After this whole whatever this is  you guys go to the park for a Date IN the demo build cuz we are so fucking lazy stupid fat chuds so were cutting the whole game short because we got lazy"

                 
                "Die":
                 "Dateball" "Fuck"
                 "Speedball" "Your going to die"
                 "Dashball" "SPEEDBALL STOP!!!!"
                 "Speedball Stares At DashBall and stops"
                 "Dashball Grabs you and flies away"
                 scene bg sky
                 with fade
                 hide speed angry
                 stop music
                 play music "audio/dashballtheme.mp3"
                 show dash normal
                 "Dashball" "You good?"
                 menu:
                    "Yeah":
                     "Dashball""Thats good"
                     "Dashball"  "Im Dashball By the way"
                     "Dashball" "and you are?"
                     "Dateball" "I… Don’t know?"
                     "Dashball"  "Ok ill call you Dateball"
                     "You stare at dashball and feel an odd feeling of nostalgia"
                     "Dateball" "Uhm… Alright sure you can call me Dateball I guess"
                     show dash blush
                     "Dashball" "cool cool anyways wanna go on a date"
                     "Dateball" "What?! I don’t even know you"
                     show dash cry
                     "Dashball" "PLEASEEE DATE ME PLEASEHHHEEEEE"
                     "Dateball"  "Okay Okay! Calm down jeez"
                     "Dashball from pure excitement his shoes explodes but his expression doesnt change"
                     hide dash cry
                     scene bg basket
                     "And after a few hours of planning the date and waiting for dashball in the Basketball court"
                     "Dashball" "Yo Dateball"
                     "unclemikey" "because we are lazy and this route will be on hold until full release"
                    

                    "Who are you?":
                     "Dashball" "Dashball."
                     "Dashball" "and you are?"
                     "Dateball" "I… Don’t know?"
                     "Dashball"  "Ok ill call you Dateball"
                     "You stare at dashball and feel an odd feeling of nostalgia"
                     "Dateball" "Uhm… Alright sure you can call me Dateball I guess"
                     show dash blush
                     "Dashball" "cool cool anyways wanna go on a date"
                     "Dateball" "What?! I don’t even know you"
                     show dash cry
                     "Dashball" "PLEASEEE DATE ME PLEASEHHHEEEEE"
                     "Dateball"  "Okay Okay! Calm down jeez"
                     "Dashball from pure excitement his shoes explodes but his expression doesnt change"
                     hide dash cry
                     scene bg basket
                     "And after a few hours of planning the date and waiting for dashball in the Basketball court"
                     "Dashball" "Yo Dateball"
                     "unclemikey" "because we are lazy and this route will be on hold until full release"





                

        "get far away as possible im not talking to sentient balls even if im one":
            "You Run away into the mountains infact you went so far that you reached dageastan and you are forgotten to 2 to 3 years"

        "truck":
            "a truck falls from the sky for no apparent reason and crushes the two balls"
            

    return
