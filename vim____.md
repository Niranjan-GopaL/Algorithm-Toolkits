

                <number> <cmd> <motion>


## Quit

- ZQ (that easy, so don't use :q! this is wayyy faster) this is force exit
- ZZ (save and exit)

## Screen control

- zz (put that line in the middle of the screen)
- zz ( bring it to the top of the screen)


## cool stuff done in zsh prompt

- double tab and you can select from the menu list
- you can even see what all args and otpions can a command have ( after -- double tab)
- vi key bindings replaced the arrows in 
- ranger is awesome, check their config for much easier navigation

## cool stuff that I learned today

- compliment the rest of your folding addiction with NEW STUFF
- you can create your OWN FOLDING RANGES ( ctrl+k ctrl+, ) <== create fold range
- to remove the foling range ==> ( ctrl+k ctrl+. ) 
- pinning and unpinning tabs from Axle!!!


## New day new vim stuff 


- Understood :x :q can close tab and you can reopen them  by ctrl + shift + t 
- Played around 
- YP replicates entire line you can 4YP
- One way to "move" a line in vim is :-
           ddkp :=
        - dd will delete the line and add it to the default register.
        - k will move up a line (j would move down a line)
        - P will paste above the current line             

- ctrl + u / d move half a page up or down
- { and  } are super useful to move one paragraph up or down

-   $ : End of the line 
    ^ : Start of the line

so d$  d^ v$ v^ 

- 
    + A : appends stuff (wherever we are on the line, we'll start in insert mode at the END OF THE LINE )
    + I : prepends stuff   (wherever we are on the line, we'll start in insert mode at the START OF THE LINE)

    + a : insert on the RIGHT SIDE of the cursor
    + i : insert to the left of cursor

- Select entire file :- GVgg 

- Delete the rest of the line :- d$ delete from cursor to EOL

            BETTER WAY :- D (del from cursor to EOL)