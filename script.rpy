# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
  
init python:
    def text_beep_callback_Male(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.music.play("audio/sfxblipmale.wav", channel="sound", loop=True)
        elif event in ("slow_done", "end"):
            renpy.music.stop(channel="sound")

init python:
    def text_beep_callback_Female(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.music.play("audio/sfxblipfemale.wav", channel="sound", loop=True)
        elif event in ("slow_done", "end"):
            renpy.music.stop(channel="sound")            


transform shake_side:
    subpixel True

    xoffset 0
    yoffset 0

    linear 0.07 xoffset -20 yoffset 10
    linear 0.07 xoffset  20 yoffset -10
    linear 0.07 xoffset -16 yoffset 9
    linear 0.07 xoffset 16  yoffset -9
    linear 0.07 xoffset -12 yoffset 7
    linear 0.07 xoffset 12  yoffset -7
    linear 0.07 xoffset -8
    linear 0.07 xoffset 8
    linear 0.00 xoffset 0 yoffset 0

    # Return to the original position so Ash doesn't stay offset
    linear 0.04 xoffset 0


init python:
    
    import math
    class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left'   : 0.0,
                'right'  : 1.0,
            }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

    Shake = renpy.curry(_Shake)
    #

#

            # How to call function >  init:
 #  $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
 
define sshake = Shaker((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

define Ash = Character('Ash', color="#004B49", callback=text_beep_callback_Male, window_left_padding=170, show_side_image=Transform(Image("images/Named Male/Ash/ash smile.png"), crop=(250, 250, 650, 650), zoom=0.15, xalign=0.0, xoffset=70, yalign=1.0, yoffset=-175)) 
define Ex = Character('???', color="#5C0120", callback=text_beep_callback_Male, window_left_padding=170, show_side_image=Transform(Image("images/extra/ex smile1.png"), crop=(250, 250, 650, 650), zoom=0.15, xalign=0.0, xoffset=70, yalign=1.0, yoffset=-175)) 
define G1 = Character('???', color="#00A86B", callback=text_beep_callback_Female, window_left_padding=170, show_side_image=Transform(Image("images/jess/jess pout.png"), crop=(195, 250, 650, 650), zoom=0.15, xalign=0.0, xoffset=70, yalign=1.0, yoffset=-175)) 
define Ms = Character('???', color="#00A86B", callback=text_beep_callback_Female, window_left_padding=170, show_side_image=Transform(Image("images/miho/Miho Winter Uniform/Miho smile.png"), crop=(195, 250, 650, 650), zoom=0.15, xalign=0.0, xoffset=70, yalign=1.0, yoffset=-175)) 
define M1 = Character('Miho', color="#00A86B", callback=text_beep_callback_Female, window_left_padding=170, show_side_image=Transform(Image("images/miho/Miho Winter Uniform/Miho smile.png"), crop=(195, 250, 650, 650), zoom=0.15, xalign=0.0, xoffset=70, yalign=1.0, yoffset=-175)) 
define SM = Character('Crowd', color="#F984EF", callback=text_beep_callback_Male)
define SW = Character('Crowd', color="#F984EF", callback=text_beep_callback_Female)

default G1Affection = 0
default G1Trust = 0
default G1Respect = 0
default G1Fear = 0
default G1Friendship = 0
default G1Love = 0
default G1Suspicion = 0
default G1Disgust = 0

default M1Affection = 0
default M1Trust = 0
default M1Respect = 0
default M1Fear = 0
default M1Friendship = 0
default M1Love = 0
default M1Suspicion = 0
default M1Disgust = 0

image ash normal:
    "images/Named Male/Ash/ash normal.png"
    zoom 0.5

image ash surprised:
    "images/Named Male/Ash/ash surprised.png"
    zoom 0.5

image ash smile:
    "images/Named Male/Ash/ash smile.png"
    zoom 0.5

image ash smirk:
    "images/Named Male/Ash/ash smirk.png"
    zoom 0.5

image ash angry1:
    "images/Named Male/Ash/ash angry1.png"
    zoom 0.5

image ash confused:
    "images/Named Male/Ash/ash confused.png"
    zoom 0.5

image ash weirded:
    "images/Named Male/Ash/ash weirded.png"
    zoom 0.5

image ex surprised: 
    "images/extra/ex surprised.png"
    zoom 0.5


image ex angry: 
    "images/extra/ex angry.png"
    zoom 0.5


image ex angry2: 
    "images/extra/ex angry2.png"
    zoom 0.5


image ex laughnerv: 
    "images/extra/ex laughnerv.png"
    zoom 0.5


 
image jess angry: 
    "images/jess/jess angry.png"
    zoom 0.5


image jess pout: 
    "images/jess/jess pout.png"
    zoom 0.5


image jess shocked: 
    "images/jess/jess shocked.png"
    zoom 0.5

image jess shocked: 
    "images/jess/jess shocked.png"
    zoom 0.5

image miho smile:
    "images/miho/Miho Winter Uniform/Miho smile.png"
    zoom 0.18

image miho smileblush:
    "images/miho/Miho Winter Uniform/Miho smileblush.png"
    zoom 0.18

image miho frown:
    "images/miho/Miho Winter Uniform/Miho frown.png"
    zoom 0.18

image miho frownblush:
    "images/miho/Miho Winter Uniform/Miho frownblush.png"
    zoom 0.18

image miho open:
    "images/miho/Miho Winter Uniform/Miho open.png"
    zoom 0.18

image miho openblush:
    "images/miho/Miho Winter Uniform/Miho openblush.png"
    zoom 0.18

# The game starts here.

label start:
  scene bg day2 with fade
  
  play music "audio/ontama_piano2_shiroihana.mp3"

  "{w=1.5}{cps=24} \"Time waits for no one.\ " 
  extend "\n{cps=24} It doesn't matter what you could've or should've done.\" "

  "{cps=24}{w=0.5} \"The only thing that matters is what you have done,\ "
  extend "\n{cps=24} And what you do now, in the present moment.\" "

  play sound "Air1k.mp3"

  pause 0.75   
  "..."


  "{w=1}{cps=24}In movies and anime, they always speak about dreams & purpose."
  extend " What is my purpose? My dream?"

  "{w=1}{cps=24}I don't think I can remember anything significant about my life."
  extend "{w=1}{cps=24} After all, I've done nothing but waste my years. "

  "{w=1}{cps=24} The people around me seem so joyful,"
  extend "\n{cps=24} so full of vigor and youth, yet I can't even dare to face myself"
  extend "\n{cps=24} ...especially my past. "
 
  play sound "Air2M.mp3"
  "{w=1}{cps=18}Unfortunately, {/cps}{w=0.5}"
  extend "{cps=18}{w=2}We all have only one life to live.{/cps}" 
  pause 3
  stop music fadeout 2.0
  
  play sound "ShinkaEND.mp3"
  scene bg shinm with dissolve

  "{w=1}{cps=24}As I look back on things,{/cps}"
  extend "\n{w=1}{cps=24}I realize life hasn't been as bad as I made it out to be.{/cps}"
  
  "{w=1}{cps=24}but it's also true that it hasn't been as good as I wanted it to be either.{/cps}"

  "{w=1}{cps=24}Though I still wanted to live my life to the fullest.{/cps}"
  extend "\n{w=1}{cps=24}yet due to my circumstances I really couldn't.{/cps}"

  play sound "shinkadoor.mp3"

  "{w=1}{cps=24}I guess I just have to accept that for now,{/cps}"
  extend "\n{w=1}{cps=24}since my stop is here.{/cps}"

  "{w=1}{cps=24}Afterall,{/cps}"
  pause 1
  extend "\n{w=0.25}{cps=26}I don't want to be late to my own place.{/cps}"

  play sound "stmwalk.mp3" volume 2
  pause 1.5
  
  scene bg stm with fade

  show ash normal at left with dissolve
  play audio "audio/packstation.mp3" volume 0.3
  Ash "{w=1.5}{cps=20} How long has it been since I ever went outside?{/cps}"
  play audio "audio/MetalAlert.mp3" volume 1
  
  show ash surprised at left with dissolve

  Ash "{cps=20}!!!{/cps}" 
  
  play music "audio/1/papercup.mp3" 
   
  show ash smile at left with dissolve

  Ash "{cps=20}I can't believe it!{/cps}"
  extend "\n{cps=20}This place is even better than what I Imagined.{/cps}"

  show ash smirk:
    zoom 2

  Ash "{cps=24}Well, I'll make sure I won't waste this opportunity!{/cps}"
  extend "\n{cps=24}I'll do my best and rise to the top!{/cps}"  

  Ash "{cps=24}Then they'll see!{/cps}"

  show ash angry1 at left with fade

  Ash "{w=1}{cps=24}But first. I'll have to deal with day to day life.{/cps}"

  show ash surprised at left, shake_side
  play audio "audio/fall2.mp3"
  Ash "{cps=24}?!?!?!?!{/cps}" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

  Ash "{w=1.5}{cps=24} what was that?{/cps}"

  pause 1.5 

  scene bg stm with dissolve

  # MultiCharacter Reference:
  #image ex surprised = "extra/ex surprised.png"
  #image ex angry = "extra/ex angry.png"
  #image ex angry2 = "extra/ex angry2.png"
  #image ex laughnerv = "extra/ex laughnerv.png"
 
  #image jess angry = "jess/jess angry.png"
  #image jess pout = "jess/jess pout.png"
  #image jess shocked = "jess/jess shocked.png"

  show jess angry:
      xpos 1.0 xanchor 1.0
      yalign 1.0 

  show ex surprised:
      xpos 0.7 xanchor 1.0
      yalign 1.0
  
  pause 0.75
   
  show ex angry:
      xpos 0.7 xanchor 1.0
      yalign 1.0
  
  pause 0.25

  show ex angry2:
      xpos 0.7 xanchor 1.0
      yalign 1.0
 
  play audio "Roxysen.mp3"

  Ex "{cps=33}WHY THE {b}####{/b} DID YOU PUNCH ME, YOU STUPID {b}##### !!!{/b}.{/cps}{w=1}{nw}"

  G1 "{w=1}{cps=27}Scum like you tend to harrass others,{/cps}{w=0.75}{nw}"
  extend "\n{cps=27}Then you dare ask why you get punished. How expectedly pitiful!{/cps}"

  # scene bg hnl
  # play audio "zeldaitem.mp3"
  # "Well, That's it for now folks! The demo is over!{nw}"
  # extend "\n{cps=27}Please feel free to rate us 5 stars and share with all your friends! Until we meet next time!{/cps}"

  Ex "{cps=33}THAT'S CRAZY FOR SOMEONE WHOSE GONNA GET HER LIGHTS KNOCKED OUT TO SAY!{/cps}"

  G1 "{cps=27}Sure, Go Ahead!"
  extend "\n{cps=27}I'd like to see you try!{cps=27}"

  Ex "{cps=33}YOU-{/cps}"

  SM "{cps=37}DUDE! YOU'RE GONNA REGRET PICKING A FIGHT WITH HER! SHE'S THE DAUGHTER OF A MEGACORPO.{/cps}" 
  SW "\n{cps=38} THAT'S THE LIKE THE YAKUZA WITH LEGAL PROTECTION YO!{/cps}" 
  SM "\n{cps=38} YEAH DUDE!, HER DAD'S GONNA KILL YOU!{/cps} "

  show ex surprised

  pause .5

  show ex laughnerv

  Ex "{cps=60}Really? I didn't know.{/cps}{w=0.5}{nw}"
  
  extend "{cps=99}\n Well, I gotta run byee, I'l fight you next time!!!{/cps}{nw}"
  extend "{cps=100}\n I'll fight you next time!!!{/cps}{nw}"

  play sound "Fullrun.mp3"

  hide ex laughnerv with moveoutleft

  pause 1.5

  stop sound fadeout 0.75 

  show jess pout

  pause 1

  G1 "{cps=27}Coward.{/cps}{nw}{w=1}"

  show ash weirded at left with dissolve

  Ash "{cps=24}Umm...{/cps}{w=1}"
  
  show ash surprised

  G1 "{cps=30}What.{w=1.0}{nw}{/cps}"
  extend "\n{cps=30}You here to pick a fight too?{/cps}{nw}{w=1.5}"
  
  show ash confused

  Ash "{cps=24}No! No! I just came here to see what all the commotion was about!{/cps}"

 #default G1Affection = 0
 #default G1Trust = 0
 #default G1Respect = 0
 #default G1Fear = 0
 #default G1Friendship = 0
 #default G1Love = 0
 #default G1Suspicion = 0
 #default G1Disgust = 0


label choices1:  
  G1 "{cps=44}Oh, I see.{/cps}"
  extend "\n{cps=44}You just happened to be in the right place at the right time, huh?{/cps}"
  extend "\n{cps=44}Do you take me for a fool?{/cps}"
menu: 
    "I think you misunderstood me. I really was just passing by.":
        jump choices1A
    "Woah, you're taking this a bit too far miss, I was curious and wanted to see what was going on.":
        jump choices1B
    "...":
        jump choices1C



label choices1A:

    $ G1Respect -= 1
    $ G1Trust += 1

    G1 "{cps=44}An idiot, just like everyone else.{/cps}"

    jump choices1common

label choices1B:
    $ G1Trust += 1
    $ G1Respect += 1

    G1 "{cps=44}I'll...{/cps}"
    extend "\n{cps=44}believe you for now.{/cps}"
    
    jump choices1common

label choices1C:
    $ G1Trust -= 1
    $ G1Respect -= 1

    G1 "{cps=44}Not so keen on conversation, huh?{/cps}"
    extend "\n{cps=44} I'll take that as a sign of your guilt.{/cps}"
    
    jump choices1common

label choices1common:

  if G1Trust == 1 and G1Respect == -1:
   G1 "{cps=44}It doesn't make much talking to someone like you.{/cps}{w=1.5}"
   jump result1common

  elif G1Trust == 1 and G1Respect == 1:
   G1 "{cps=44}I have to go.{/cps}{nw}"
   extend "\n{cps=44}My time is too precious to waste on someone like you.{/cps}{w=1.5}"
   jump result1common

  else: 
   G1 "{cps=44}I hope we never cross paths ever again.{/cps}{w=1.5}"
   jump result1common

label result1common:
 pause 1.0
 G1 "{cps=44}Farewell, peasant!{/cps}"

 hide jess pout with dissolve
 hide ash weirded with dissolve

 show bg stm: 
    blur 25
 with dissolve

 
 centered "{color=#F5BD02}{outlinecolor=#000000}{cps=45}{b}She moves towards the road gracefully.{/b}{w=1}{size=45}{/cps}{/color}{outlinecolor=#000000}{nw}"
 
 play sound "audio/CarDoor.mp3" volume 1 

 pause 2

 play sound "audio/CarStart.mp3" volume 0.25 fadeout 1.5

 centered "{color=#F5BD02}{outlinecolor=#000000}{cps=45}{b}A nice car with mens in suits shows up and the girl gets in, driving away without a second glance.{/b}{w=1.5}{size=45}{/cps}{/color}{outlinecolor=#000000}{nw}"
 
 pause 1.5

 


 show bg stm:
   blur 0

 show ash confused at left with dissolve
 
 pause 1.5
 
 Ash "{cps=24}Well, that was certainly interesting.{/cps}"

 Ash "{cps=24}I should probably head to my new place now though.{/cps}"

 show ash weirded at left with dissolve

 hide ash confused with moveoutright

 Ash "{cps=24}I'm on my way.{/cps}"
 
 centered "{color=#000000}{outlinecolor=#000000}{cps=45}{b}An hour and half of walking later...{/b}{w=1.5}{size=45}{/cps}{/color}{outlinecolor=#000000}{nw}"

 scene bg apcm with fade

 show ash normal at left with moveinleft

 Ash "{cps=24}I guess this is the place where I'll be living for the time being.{/cps}"

 Ash "{cps=24}I heard some weird voice.{/cps}{nw}{w=1}"
 extend "\n{cps=24}What even was that exactly?{/cps}{w=1}{nw}"
 extend "\n{cps=24}Sounded like some sort of brawl, then a squeak.{/cps}"

#add door sound effect
 play sound "audio/dooropen.mp3" volume 0.5

 pause 1.0

 Ash "{cps=25}I just hope the place is decent enough to live in.{/cps}{w=0.75}{nw}"
 extend "\n{cps=25}Well, I've dealt with worse before, but still would be nice.{/cps}"

 scene bg hem with dissolve

 show ash weirded at left with dissolve
 
 Ash "{cps=25}Judging from the corridor, this place seems decent enough.{/cps}{w=0.75}{nw}"
 extend "\n{cps=25}It's better than my old place, that's for sure.{/cps}"

 pause 1

 hide ash weireded at left with moveoutright 
 
 pause 1

 scene bg lrm with fade

 show ash surprised at left with moveinleft

 Ash "{cps=25}Woah, this place is even better than I could have imagined!{/cps}"

 Ash "{cps=25}But even considering the scholarship grant, isn't this place a bit too expensive for one person?{/cps}"

#add BoxesCrashing soundeffect
centered "INSERT NON COPYRIGHT BOXES CRASHING SFX"
#add then girl appearing and crashing into Mc effect
centered "INSERT NON COPYRIGHT GIRL CRASHING INTO MC EFFECT"

Ash "{cps=20}I think I spoke too soon...{/cps}"

Ms "{cps=7}Owww....!?{/cps}" 

Ash "{cps=25}Excuse me, are you okay?{/cps}"

Ash "{cps=25}And I don't mean to be rude, but who are you and what are you doing here?{/cps}"

show bg lrm:
   blur 25
with fade


centered "{color=#000000}{outlinecolor=#000000}{cps=45}{b}The girl with brown hair laying on the floor, notices your presence, turns her head and looks towards you.{/b}{w=1.5}{size=45}{/cps}{/color}{outlinecolor=#000000}{nw}"
 

show bg lrm:
   blur 0
with fade

show miho smile:
      xpos 0.7 xanchor 1.0
      yalign 1
      yoffset 500




Ms "{cps=5}....Huh?{/cps}"

show miho frown at right with dissolve

Ms "{cps=55}AHHHHHH!{/cps}{nw}"
extend "\n{cps=55}IT'S A PERVERT!! HELP ME!!! GET AWAY FROM ME!!!!!{/cps}{nw}{w=1}"

Ash "{cps=90}WAIT A MINUTE! I'M NOT A PERVERT!{/cps}{nw}{w=1}"

Ms "{cps=98}YEAH! THAT'S EXACTLY WHAT A PERV WHO SNEAKS INTO THE WOMEN'S DORMS LIKE A CLICHE ANIME WOULD SAY!{/cps}{nw}{w=1.45}"

Ash "{cps=101}YOU'VE GOT TO BELIEVE ME! I JUST GOT ASSIGNED THIS APARTMENT FOR XY ACADEMY OF N-LEARNING{/cps}{nw}{w=1.45}"

Ms "{cps=70}HAH NICE TRY BUT-{/cps}{nw}{w=2}"
extend "\n{cps=79}Wait what.{/cps}{nw}{w=1}"

Ms "{cps=57}Did you just say\"XY Academy of N-Learning\"?{/cps}{nw}{w=1.5}"
extend "\n{cps=57}But that's where I go to.....{/cps}{nw}{w=1.5}"

Ash "{cps=57}Look Miss, there's clearly been some sort of confusion.{/cps}{nw}{w=1.5}"
extend "\n{cps=57}This is supposed to be the room alloted to me.{/cps}{nw}{w=1.5}"

Ms "{cps=57}but this is my apartment!{/cps}{nw}{w=1}"
extend "\n{cps=57}See! It says that right here on my admission guide letter and pamphlet!{/cps}{nw}{w=1}"

show ash confused at left with dissolve

Ash "{cps=57}huh...It does...{/cps}{nw}{w=1.5}"
extend "\n{cps=57}but...So does mine?{/cps}{nw}{w=1.5}"

show ash weirded at left with dissolve

Ms "{cps=57}Something... is off...{/cps}{nw}{w=1.5}"
extend "\n{cps=57}Yeah...{/cps}{nw}{w=1.5}"

Ash "{cps=77}Wait, Check the fine print!{/cps}{nw}{w=1.6}"

Ms "{cps=77}You're right....{/cps}{nw}{w=1.5}"
extend "\n{cps=77}Partially.{/cps}{nw}{w=1.5}"

Ms "{cps=57}This apartment has indeed been allotted to the both of us.{/cps}{nw}{w=1.5}"
extend "\n{cps=57}But only some of the rooms are ours. We're supposed to have 4 more roommates.{/cps}{nw}{w=1.5}"

Ash "{cps=47}That...makes a lot more sense.{/cps}{nw}{w=1.5}"

show ash normal at left with dissolve

Ms "{cps=37}I'm very sorry for the way I behaved.{/cps}{nw}{w=1.5}"
extend "\n{cps=77}I was just very surprised and frigtened.{/cps}{nw}{w=1.5}."

show ash smirk at left with dissolve

Ash "{cps=37}Jeez, Am I really that scary?{/cps}{nw}{w=1.5}"

Ms "{cps=101}NO, I DIDN'T REALLY MEAN THAT IN THAT WAY!{/cps}{nw}{w=1.5}"

show ash smile at left with dissolve

Ash "{cps=35}I'm just kidding. Calm down miss.{/cps}{w=1.5}"

Ash "{cps=33}Anyways, We may have skipped the formalities but...{/cps}{w=1.5}"

Ash "{cps=32}My name is Ash. It's nice to meet you.{/cps}{nw}{w=1}"
extend "\n{cps=31}And to whom do I own the pleasure of conversing with?{/cps}{w=1}"

Ms "{cps=30}That's such an old, but gentlemenly and sweet way of asking.{/cps}{nw}{w=1}"
extend "\n{cps=30}Is that how you talk to all women?{/cps}{w=1}"

Ash "{cps=37}Only to the one's I've scared the soul out of.{/cps}{nw}{w=1.5}"

Ms "{cps=33}Jeez, You're never going to let that one go, are you?{/cps}{nw}{w=1.5}"
extend "\n{cps=57}And here I was being considerate of Mr Potential Stalker or perv.{/cps}{nw}{w=2}"

Ash "{cps=4}HEEEEY!{/cps}"

show miho open at right with dissolve

Ms "{cps=35}Anyways! It's nice to meet you too Ash.{/cps}"

M1 "{cps=35}I'm Miho Haruno. Please take good care of me.{/cps}"

centered "{cps=65}TAKE GOOD CARE OF HER? WHAT IS SHE IMPLYING?{/cps}{w=1}{nw}"
extend "\n{cps=20}Oh, Yeah. This is Japan.{/cps}{nw}{w=1}"
extend "\n{cps=20}She probably means she wishes for me to work smoothly and have a good roommate to roomate relationship with her.{/cps}{nw}{w=1}"

Ash "{cps=35}I'll do m-my best, Miss Miho Haruno.{/cps}"

show miho openblush at right with dissolve

M1 "{cps=37}S-SAME HERE!!!{/cps}{nw}{w=0.5}"
extend "\n{cps=25}I'll be...counting on you.{/cps}{w=0.5}"

centered "Insert the sound of a cat"

show ash surprised at left with dissolve
show miho frown at right with dissolve

Ash"{cps=30}Did you hear that?!{/cps}"

M1 "{cps=30}Yeah, It's what I was dealing wih earlier.{/cps}"
extend "\n{cps=30}It came from under the boxes{/cps}"

#Meow sound plays again

"{cps=30}A little orange ball, or what seems to be the head of a cat pops out of the cardboard{/cps}"

show miho smileblush at right with dissolve

M1 "{cps=70}KITTTYYYYYY!!!!!!!!!!! AWWWW!!!{/cps}{w=0.5}{nw}"
extend "\n{cps=30}Ash, look!!! It's so small and so friggin cute!"

default catfed = False

show ash confused at left with dissolve

Ash "{cps=30}Is that yours by chance?{/cps}"

M1 "{cps=30}No...{/cps}{w=0.75}{nw}"
extend "\n{cps=30}I spotted it, and I was trying to grab it when I tripped earlier.{/cps}"

show ash weirded at left with dissolve

Ash "{cps=30}I know you for like 5 minutes, but I already know that it's typical of you to trip and kill us both by accident.{/cps}"
extend "\n{cps=30}Just for the sake of, that thing.{/cps}"

M1 "{cps=30}Don't call it a thing! It's a Cat, It has feelings like us y'know!{/cps}"

menu:
    "Crouch down to offer it a hand":
     jump choice2hand
    "Look around the apartment for Catfood":
     jump choice2food
    "Tell Miho that we can't keep it":
     jump choice2nokeep

label choice2hand:

    $ M1Affection += 1
    $ catfed = False

    show ash smile at left with dissolve

    Ash "{cps=30}Hey there, Little guy..or girl. Sorry for scaring you.{/cps}"

    "{cps=30}The cat sniffs my fingers, and then rubs it's head against my open hand.{/cps}"

    M1 "{cps=30}It likes you, it seems...{/cps}{w=0.75}{nw}"
    extend "\n{cps=30}I'm a bit jealous...{/cps}"

    jump choice2common

label choice2food:

    $ M1Trust += 1
    $ catfed = True

    show ash normal at left with dissolve

    Ash "{cps=30}Give me a few seconds. There might be something in the kitchen.{/cps}"

    "{cps=30}Ash finds a few unopened cans of tuna in the cupboard. Looks like the people living here before left it behind.{/cps}"

    show miho open at right with dissolve
    
    M1 "{cps=30}Good thinking Ash!{/cps}{w=0.5}{nw}"
    extend "\n{cps=30}I've known {b}you{/b} for like five minutes, and you're already showing off.{/cps}"

    jump choice2common

label choice2nokeep:

    $ M1Affection -= 1
    $ catfed = False

    show  ash weirded at left with dissolve

    Ash "{cps=30}We don't even know if pets are allowed, what if someones allergic?{/cps}"

    show miho frownblush at right with dissolve

    M1 "{cps=30}You're so cold...{/cps}{w=0.75}{nw}"
    extend "\n{cps=30}Look at those eyes!!!!{/cps}"

    Ash "{cps=30}I'm not saying we should get rid of it! More like ask for permission first.{/cps}"

    M1 "{cps=30}...fine.{/cps}"

    jump choice2common

label choice2common:
  #Temporary/Unrefined story after this part
  #Doorbell sfx plays
   centered "#Doorbell sfx plays"

   centered "{cps=30}{b}Ding-Dong.{/b}{/cps}"

   show ash surprised at left with dissolve
   show miho frown at right with dissolve

   M1 "{cps=30}Another roommate maybe?{/cps}"

   Ash "{cps=30}Only one way to find out.{/cps}"

   scene bg hem with fade

   show ash normal at left with moveinleft

   pause 0.75

   #Door opening SFX
   centered "Insert Door opening SFX"

   show jess pout:
    xpos 1.0 xanchor 1.0
    yalign 1.0
   with dissolve

   pause 1.0

   show ash surprised at left with dissolve

   Ash "{cps=30}It's....You.{/cps}"

   G1 "{cps=30}You....Peasant!{/cps}{w=1}{nw}"
   extend "\n{cps=30}Of all the realms I could've ended up with in this accursed city!{/cps}"

   Ash "{cps=30}You're the girl from the station!{/cps}"

   G1 "{cps=30}And you are the unsightly peasant from the station.{/cps}"
   extend "\n{cps=30}Were you seriously following me all the way here?{/cps}"
    
   show ash confused at left with dissolve

   Ash "{cps=30}I think you're the one who showed up at {i}my{/i} door{/cps}"
   
   show jess angry:
    xpos 1.0 xanchor 1.0
    yalign 1.0

   G1 "{cps=30}{i}Your{/i} door? What utter nonsense!{/cps}{w=0.5}{nw}"
   extend "\n{cps=30}This is apartment 4 of dormitory F&M of the haruno allotment, and I have it written in my letter!"
    
   #miho steps in, animate it in the future when I have money

   show miho openblush at center with moveinright

   M1 "{cps=30}Umm...the Haruno you mentioned, is me. So that means...{/cps}{w=0.75}{nw}"
   extend "\n{cps=30}we're roommates? Tadaa...{/cps}"

   Ash "{cps=30}And when you finish reading the fine print, my name is just after hers.{/cps}"

   show jess shocked:
     xpos 1.0 xanchor 1.0
     yalign 1.0

   G1 "{cps=30}Roommates{/cps}{w=1}{nw}"
   extend "\n{cps=30}with {i}him{/i}.{/cps}"

menu:
    "Welcome her Warmly and politely":
      jump choice3welcome
    "Tell her you won't be a nuisance or cause trouble":
      jump choice3trouble
    "Tease her about 'Farewell, peasant!'":
      jump choice3tease

label choice3welcome:

    $ G1Respect += 1
    $ G1Trust += 1

    show ash smile at left with dissolve

    Ash "{cps=30}Well, welcome home. Come in mi'lady, I'll help with your bags.{/cps}"

    show jess pout:
        xpos 1.0 xanchor 1.0
        yalign 1.0

    G1 "{cps=30}...I did not ask for your help.{/cps}{w=1}{nw}"
    extend "\n{cps=30}However I will not refuse such treatment. Consider it my appreciation of your manners.{/cps}"

    jump choice3common

label choice3trouble:

    $ G1Trust +=1
    $ G1Suspicion +=1

    show ash normal at left with dissolve

    Ash "{cps=30}Look, I don't want to cause you any harm, Nor do I harbour any ill thoughts towards you.{/cps}"
    extend "{cps=30}\nI'm just trying to focus on my own studies and life!{/cps}"
    
    show jess pout:
     xpos 1.0 xanchor 1.0
     yalign 1.0

    G1 "{cps=30}Hmph. I'll be the judge of that.{/cps}"

    jump choice3common

label choice3tease:

    $ G1Respect -= 1
    $ G1Disgust += 1
    $ M1Affection += 1
    # Secret feelings(It will change the game)

    show ash smirk at left with dissolve

    Ash "{cps=30}Farewell, peasant, huh? How is my liege stooping so low to live amoung commoners now?{/cps}"

    show miho smile at center with dissolve

    M1 "{cps=30}Pffft-{/cps}"

    show jess angry:
      xpos 1.0 xanchor 1.0
      yalign 1.0

    G1 "{cps=60}DON'T LAUGH!{/cps}"

    jump choice3common
    
label choice3common:

Ash "MIHO Y'KNOW WHAT TIME IT IS?"

M1 "WHAT TIME IS IT ASH?"

G1 "YEAH! WHAT TIME IS IT PEASANT? WHY ARE WE SCREAMING?"

Ash "IT'S TIME FOR THE DEMO TO END AND FOR OUR CREATOR TO GET SOME ZZZ'S AND SLEEP!"

scene bg hnl

"Well Thanks for joining us once again, I need to sleep so I won't say much!"
"Also, the lack of music and effect placeholders is on purpose, the creator doesn't have/can't afford a drawing tab at the moment"
extend "\nNor can he pay you glorious fellows to do it so for now he's going to cry himself to sleep. Goodnight!! We'll work on Sound effects next time!!!"

























































  










  
