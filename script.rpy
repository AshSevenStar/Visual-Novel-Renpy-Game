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
define SM = Character('Crowd', color="#004B49", callback=text_beep_callback_Male)
define SW = Character('Crowd', color="#004B49", callback=text_beep_callback_Female)

default G1Affection = 0
default G1Trust = 0
default G1Respect = 0
default G1Fear = 0
default G1Friendship = 0
default G1Love = 0
default G1Suspicion = 0
default G1Disgust = 0

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

  G1 "{cps=27}Coward.{/cps}"

  show ash weirded at left with dissolve

  Ash "{cps=24}Umm...{/cps}"
  
  show ash surprised

  G1 "{cps=44}What.{/cps}"
  extend "{cps=44} You here to pick a fight too?{/cps}"
  
  show ash confused

  Ash "{cps=24}No!No! I just came here to see what all the commotion was about!{/cps}"

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
   G1 "{cps=44}It doesn't make much talking to someone like you.{/cps}"
   jump result1common

  elif G1Trust == 1 and G1Respect == 1:
   G1 "{cps=44}I have to go.{/cps}"
   extend "\n{cps=44}My time is too precious to waste on someone like you.{/cps}"
   jump result1common

  else: 
   G1 "{cps=44}I hope we never cross paths ever again.{/cps}"
   jump result1common

label result1common:
 G1 "{cps=44}Farewell, peasant!{/cps}"

 hide jess pout with dissolve
 hide ash weirded with dissolve

 show bg stm: 
    blur 25
 with dissolve

 
 centered "{color=#F5BD02}{outlinecolor=#000000}{cps=45}{b}She moves towards the road gracefully.{/b}{w=1}{size=45}{/cps}{/color}{outlinecolor=#000000}"
 
 play sound "audio/CarDoor.mp3" volume 1 

 pause 2

 play sound "audio/CarStart.mp3" volume 0.25 fadeout 1.5

 centered "{color=#F5BD02}{outlinecolor=#000000}{cps=45}{b}A nice car with mens in suits shows up and the girl gets in, driving away without a second glance.{/b}{w=1.5}{size=45}{/cps}{/color}{outlinecolor=#000000}"
 
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
 
scene bg apcm with fade

show ash normal at left with moveinleft

"{cps=24}I guess this is the place where I'll be living for the time being.{/cps}"

 



































































  










  
