# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ash = Character('Ash', color="#c8ffc8")

# The game starts here.

label start:
  scene bg day2
  play music "audio/debu.mp3" fadein 1.0
  with dissolve
  "{w=1.5}{cps=24} A year ago, I was a normal person. " 
  extend "\n{cps=24}Someone who lived in the present, who had no idea what the future held.{/cps}"
  pause 0.75
  "..."
  pause 0.75
  "{cps=18}Unfortunately, {/cps}{w=0.5}"
  extend "{cps=18}It was even worse than anything I could ever imagined.{/cps}" 
  "Ash" "{w=1.5}{cps=20} How long has it been since I ever went outside?{cps=20}"
  "Ash" "{cps=20}Well. It's a new dawn for me I suppose. This year, I'll make sure everything goes all right!{cps=20}" 
return
  
