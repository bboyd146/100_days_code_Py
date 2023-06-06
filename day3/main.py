print('''
                            ___
                          /~   ~\\
                         |_      |
                         |/     __-__
                          \   /~     ~~-_
                           ~~ -~~\       ~\\
                            /     |        \\
               ,           /     /          \\
             //   _ _---~~~    //-_          \\
           /  (/~~ )    _____/-__  ~-_       _-\             _________
         /  _-~\\0) ~~~~         ~~-_ \__--~~   `\  ___---~~~        /'
        /_-~                       _-/'          )~/               /'
        (___________/           _-~/'         _-~~/             _-~
     _ ----- _~-_\\\\        _-~ /'      __--~   (_ ______---~~~--_
  _-~         ~-_~\\\\      (   (     -_~          ~-_  |          ~-_
 /~~~~\          \ \~~       ~-_ ~-_    ~\            ~~--__-----_    \\
;    / \ ______-----\           ~-__~-~~~~~~--_             ~~--_ \    .
|   | \((*)~~~~~~~~~~|      __--~~             ~-_               ) |   |
|    \  |~|~---------)__--~~                      \_____________/ /    ,
 \    ~-----~    /  /~                             )  \    ~-----~    /
  ~-_         _-~ /_______________________________/    `-_         _-~
     ~ ----- ~                                            ~ ----- ~  -TX
''')
print('Welcome to Death Ride 😈🩼🚑\n\n')
print('Your mission is to get through the race at super high speed without any accidents.')
print("You're moving at high speeds, so there is no time to think! 🙀\n\n")

first_turn= input("The race has started - You've hit the first corner - Will you lean right or lean left?\n Type R or L.  ").upper()
if first_turn == 'R':
    print("Nice turn!\n You've got the lead")
    second_turn= input("There's a ramp ahead - Will you pop a wheelie or hold you weight down?\n Type W or D.  ").upper()
    if second_turn == 'D':
        print("Good Choice! You've made it over the ramp and pushing towards the final stretch!\n\n")
        print("You're going 200MPH and coming up on a curve!")
        third_turn = input("Do you want to hit your front brakes, back brakes, or both\n.Type F, B, ot BT.  ").upper()
        if third_turn == "B":
            print("You slide right into the finish line!!! Congrats")
        elif third_turn == "F":
            print("You stopped too hard and caused everyone to crash !!\n GAME OVER.")
        else:
            print("A bird flew right into your helmet visor, and you've crashed !! TERRIBLE\n\n GAME OVER")
    else:
        print("Terrible choice buddy.. Your wheelie caused you to do a flip mid-air - resulting your demise 🤕. The ambulance are on their way")
else: 
    print('OUCH 🤕!!\n You took a sketchy shortcut that led you over a cliff.\n YOU LOSE')