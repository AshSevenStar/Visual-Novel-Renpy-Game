# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

define Ash = Character('Ash', color="#c8ffc8")

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

  "Ash" "{w=1.5}{cps=20} How long has it been since I ever went outside?{/cps}"
  play sound "audio/MetalAlert.mp3" volume 1
  
  show ash surprised at left with dissolve

  "Ash" "{cps=20}!!!{/cps}" 

  play music "audio/1/papercup.mp3"
   
  show ash smile at left with dissolve

  "Ash" "{cps=20}I can't believe it!{/cps}"
  extend "\n{cps=20}This place is even better than what I Imagined.{/cps}"

  show ash smirk:
    zoom 2

  "Ash" "{cps=24}Well, I'll make sure I won't waste this opportunity!{/cps}"
  extend "\n{cps=24}I'll do my best and rise to the top!{/cps}"  

  "Ash" "{cps=24}Then they'll see!{/cps}"

  show ash angry1 at left with fade

  "Ash" "{w=1}{cps=24}But first. I'll have to deal with day to day life.{/cps}"


show ash surprised at left 
"Ash" "{cps=24}?!?!?!?!{/cps}" with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

"Ash" "{w=1.5}{cps=24} what was that?{/cps}"
    
  





return
  
