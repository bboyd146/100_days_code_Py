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

first_turn= input("The race has started - You've hit the first corner - Will you lean right or lean left?\n Type R or L.")
if first_turn == 'R':
    print("Nice turn!\n You've got the lead")
    
else: 
    print('OUCH 🤕!!\n You took a sketchy shortcut that led you over a cliff.\n YOU LOSE')