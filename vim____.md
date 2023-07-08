

               <cmd>  <number>  <motion>

                c   <number>  <motion>
                d   <number>  <motion>
                



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


- instead of ctrl + 1,2,3,4 to go to tabs do this instead

            alt + 1 2 3 4 5 6 7 are much more easier and reachable

- move a block:- 

        
                9dd (so deletes next 9 lines and copies it the register)


- THIS IS GOLD !!!!!!


words, paragraphs , parenthesis are TEXT OBJECTS in vim
and you can do whatever you want over them (check out other TEXT OBJECTS IN VIM)

            daw  :  (around)  deletes enitre word including the spaces
            diw  :  (inside)  if in middle of a word and you wanna del that word without the spaces that it TRAILS 
            dap  :  if you are in the middle of paragraph, 
                    this deletes the entire paragraph

            di(  :  dels everything inside ()
            di{  :  dels everything inside {}
            di[  :  dels everything inside []

            da(  :  dels everything inside () INCLDUING THE BRACKETS
            da{  :  dels everything inside {} INCLDUING THE BRACKETS
            da[  :  dels everything inside [] INCLDUING THE BRACKETS


d   - del
i/a - (insert) (around) they are modifiers
p   - means paragraph
([{ - just paranthesis are also text objects



            this is a little bit wierd but anywhere in line if we have "" you
            don't even have to be inside the 


- THIS IS JUST GOLD !!!!!!!!!!!


:earlier 5m   ------- WE CAN GO BACK TO THE STATE WE WERE  5 MINUTES AGO 
:earlier 15m  ------- WE CAN GO BACK TO THE STATE WE WERE  15 MINUTES AGO 
:earlier 20m  ------- WE CAN GO BACK TO THE STATE WE WERE  20 MINUTES AGO
:later 20m    ------- WE CAN GO BACK TO THE STATE WE WILL BE IN 20 MIN (loll) kinda like REDO tbh


- 

        - b
        - e (end of next word)
        - w (begin of next word)

        -r (replace stuff)

        -c (ALL THE STUFF WE DO WITH d can be done with c, 
            c dels and put you in insert mode directly )

            caw  :  (around)  deletes enitre word including the spaces AND PUTS YOU IN INSERT MODE
            ciw  :  (inside)  if in middle of a word and you wanna del that word without the spaces that it TRAILS 
            cap  :  if you are in the middle of paragraph, 
                   this deletes the entire paragraph AND PUTS YOU IN INSERT MODE

            ci(  :  dels everything inside () AND PUTS YOU IN INSERT MODE
            ci{  :  dels everything inside {} AND PUTS YOU IN INSERT MODE
            ci[  :  dels everything inside [] AND PUTS YOU IN INSERT MODE

            ca(  :  dels everything inside () INCLDUING THE BRACKETS AND PUTS YOU IN INSERT MODE
            ca{  :  dels everything inside {} INCLDUING THE BRACKETS AND PUTS YOU IN INSERT MODE
            ca[  :  dels everything inside [] INCLDUING THE BRACKETS AND PUTS YOU IN INSERT MODE



            Delete the rest of the line :- d$ delete from cursor to EOL
            BETTER WAY :- D (del from cursor to EOL)

            WELL NOW YOU CAN DO  C and do whatever D does but go into insert mode less often



- after you had your fun with ci{ daa etc,
  you can jump to 20% of the file by --- 20%
  you can jump to 100% of the file by --- 100%
  you can jump to 50% of the file by --- 50%


-   search using /  (search forward)  

        n goes forward 
        N goes backward

    search using ?  (search backward)

        n goes forward 
        N goes backward


-   o makes a new paragraph below
    O makes a new paragraph ABOVE




                ' goes back to the position tht you were in a last time


- THIS IS VERYYYY USEFUL (you might need a lil regex to use it to it's full power)

            :s/lol/lollllll      replaces next occurance of lol with lollll
            :s/lol/lollllll/g    replaces ALL occurance of lol with lollll


- ctrl + a / ctrl +x ===> INCREASE NUM AND DECREASE NUM  



- You can DIRECTELY JUMP to the next occurance of a word by using :-

                            # <--- while over the word 


- Escape + tap on continue continously
- 