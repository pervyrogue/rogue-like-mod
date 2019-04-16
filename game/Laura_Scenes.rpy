
# start LauraMeet//////////////////////////////////////////////////////////

default L_ScentTimer = 0

label LauraMeet(Topics=[],Loop=1):
    $ LauraName = "???"
    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("All",0,1)
    $ L_Loc = "bg dangerroom"  
    $ L_Love = 400        
    $ L_Obed = 0            
    $ L_Inbt = 200  
    call Shift_Focus("Laura")    
    $ L_SpriteLoc = StageCenter
    call Set_The_Scene(0)
    $ L_Petname = Playername   
    
    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."   
    call LauraFace("normal", 0) 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc)
    "When you come to, a girl pulls you up by your arm."     
    call LauraFace("surprised", 0, Eyes="squint",Brows="sad") 
    ch_u "Oh, good, you don't look too damaged." 
    call LauraFace("smile", 0, Brows="sad") 
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door." 
    call LauraFace("smile", 0) 
    while Loop:
        menu:
            extend ""
            "Who are you?" if LauraName == "???":
                    call LauraFace("normal", 0) 
                    ch_l "I go by \"X-23\" in the field."
                    $ LauraName = "X-23"        
            "X-23? Is that your real name?" if LauraName == "X-23" and "X23" not in Topics:
                    call LauraFace("confused", 0) 
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and "Laura" not in Topics:
                    call Statup("Laura", "Love", 70, 5) # Love
                    call LauraFace("normal", 0) 
                    ch_l "I also go by Laura. Laura Kinney."
                    call LauraFace("confused", 0, Mouth="normal") 
                    $ LauraName = "Laura"       
                    $ Topics.append("Laura")    
                    menu:
                        extend ""
                        "Nice to meet you Laura.": 
                            call Statup("Laura", "Love", 70, 5) # Love  
                            call LauraFace("normal", 0)                
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            call LauraFace("confused", 0,Mouth="sucking")   
                            ch_l "It's just-"
                            call LauraFace("smile", 0,Brows="surprised")   
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Inbt", 70, 2) # Inbt   
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            call LauraFace("angry", 1,Eyes="side") 
                            call Statup("Laura", "Love", 70, -2) # Love   
                            call Statup("Laura", "Obed", 70, 2) # Obed 
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if LauraName == "Laura" and "Laura" in Topics:
                            call Statup("Laura", "Love", 70, -2) # Love   
                            call Statup("Laura", "Obed", 70, 5) # Obed 
                            call LauraFace("sadside", 0,Brows="normal") 
                            ch_l "Suit yourself."        
                            $ L_History.append("X-23")   
                            $ LauraName = "X-23"     
            "My name is [Playername]" if LauraName != "???" and "player" not in Topics:
                    call LauraFace("normal", 0) 
                    ch_l "Ok."     
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            call Statup("Laura", "Love", 70, 1) # Love 
                            call LauraFace("confused", 0,Mouth="normal")   
                            ch_l "Yeah, you too." 
                        "So. . .[[moving on]":
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Obed", 70, 1) # Obed
                            call Statup("Laura", "Inbt", 70, 1) # Inbt  
                            
            "What are you doing here?" if "Training" not in Topics:
                    call Statup("Laura", "Obed", 70, -2) # Obed
                    call LauraFace("confused", 0) 
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                call Statup("Laura", "Obed", 70, 2) # Obed 
                        "Ok, that's fair.":
                                call LauraFace("normal", 0) 
                                ch_p "But are you new to this school?"
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 4) # Obed
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."   
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:  
                    call Statup("Laura", "Love", 70, 2) # Love   
                    call LauraFace("normal", 0,Eyes="side") 
                    ch_l "I'll be heading out again soon." 
                    call LauraFace("normal", 0) 
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")
                
                        
            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    call Statup("Laura", "Love", 70, -2) # Love   
                    call Statup("Laura", "Obed", 70, 8) # Obed  
                    call LauraFace("confused", 0) 
                    ch_l "It was a robot arm." 
                    call LauraFace("sad", 1,Eyes="leftside") 
                    ch_l "Like I said, sorry."                   
                    call Statup("Laura", "Obed", 70, -3) # Obed
                    call Statup("Laura", "Inbt", 70, 3) # Inbt  
                    call LauraFace("smile", 0,Brows="confused") 
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")
                
            "So what's your mutant power?" if LauraName != "???" and "claws" not in Topics:
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 1) # Obed                    
                    call LauraFace("normal", 0) 
                    ch_l "I can heal fast."
                    $ Laura_Arms = 2
                    ch_l "Also I have claws."
                    $ L_Claws = 1
                    call LauraFace("smile", 0,Brows="confused") 
                    "snikt"
                    $ Topics.append("claws")
                    menu:                        
                        "Those claws look pretty sharp.":
                                call Statup("Laura", "Inbt", 70, 3) # Inbt   
                                ch_l "Yeah, indestructible too." 
                        "Cool.":
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 2) # Obed
                                call Statup("Laura", "Inbt", 70, 1) # Inbt   
                                call LauraFace("smile", 0,Brows="surprised") 
                                ch_l "Yeah, indestructible too." 
                        "Ouch.": 
                                $ L_Claws = 0
                                call LauraFace("confused", 0) 
                                call Statup("Laura", "Love", 70, -2) # Love   
                                call Statup("Laura", "Obed", 70, -5) # Obed  
                                ch_l "Don't worry, I won't stab you." 
                                call LauraFace("confused", 0,Mouth="normal")      
                                call Statup("Laura", "Inbt", 70, 7) # Inbt   
                                ch_l "Probably."  
                    $ L_Claws = 0
                    $ Laura_Arms = 1
                            
            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if L_Love >= 405: 
                            call LauraFace("smile", 0,Brows="confused") 
                            ch_l "Yeah, I guess."
                    else:
                            call LauraFace("normal", 0) 
                            ch_l "Not really."
                    call Statup("Laura", "Inbt", 70, 3) # Inbt   
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off." 
                    call LauraFace("smile", 0,Brows="confused") 
                    call Statup("Laura", "Love", 70, 3) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed  
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."  
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust   
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    call LauraFace("confused", 0) 
                    ch_l "Huh." 
                    call LauraFace("sexy", 1,Eyes="closed") 
                    "You can feel her shudder a little." 
                    call LauraFace("sexy", 1) 
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    ch_l "That feels weird."  
                    call LauraFace("sexy", 1,Eyes="leftside") 
                    call Statup("Laura", "Obed", 70, 1) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust  
                    ch_l "-a little more \"alive\" than usual." 
                    call Statup("Laura", "Inbt", 70, 5) # Inbt  
                    call Statup("Laura", "Lust", 70, 5) # Lust 
                    call LauraFace("sexy", 1,Brows="confused")   
                    ch_l "Almost. . . dangerous."
                
            "Never mind that. . . [[moving on]" if LauraName != "???":
                    $ Loop = 0
            
        if len(Topics) >= 3 and LauraName == "???":
                call Statup("Laura", "Love", 70, -2) # Love   
                call Statup("Laura", "Obed", 70, 5) # Obed
                call Statup("Laura", "Inbt", 70, 5) # Inbt   
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ LauraName = "X-23"  
        if len(Topics) >= 8:
                $ Loop = 0
        
        
    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            call Statup("Laura", "Love", 70, 2) # Love   
            call Statup("Laura", "Lust", 70, 1) # Lust  
            call LauraFace("smile",0) 
            ch_l "Maybe I'll see you when I get back, [Playername]."
    else:
            call LauraFace("normal", 0) 
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            call Statup("Laura", "Obed", 70, 2) # Obed
            call Statup("Laura", "Inbt", 70, 2) # Inbt  
            call Statup("Laura", "Lust", 70, 3) # Lust   
            call LauraFace("smile", 1, Brows="confused") 
            ch_l "We should. . . spar."
         
    $ L_Loc = "bg laura"         
    call Set_The_Scene
    
    "She dashes out of the room, headed for the hanger."
    
    $ L_History.append("met")
    $ bg_current = "bg dangerroom"            
    $ Round -= 10      
    call Shift_Focus("Rogue")
    return

# end LauraMeet//////////////////////////////////////////////////////////

                       
label Laura_Key:
        call Set_The_Scene
        call LauraFace("bemused")
        ch_l "Hey, so... this isn't something I usually do but..."
        ch_l "Look, you've been sleeping over a lot and I was thinking..."
        ch_l "Just take it already."
        "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
        $ Keys.append("Laura")
        $ L_Event[0] = 1
        ch_p "Thanks."
        return
        


# Event Laura_Caught_Masturbating  /////////////////////////////////////////////////////  

#Not updated

label Laura_Caught_Masturbating:
            #This label is called from a Location
            call Shift_Focus("Laura")
            "You hear some odd noises coming from Laura's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call LauraOutfit(Changed=1)    
            $ L_Upskirt = 1
            $ L_PantiesDown = 1
            $ L_Loc = bg_current
            call Set_The_Scene(0)
            call Display_Laura(0)
            call LauraFace("sexy")
            $ L_Eyes = "closed"
            $ Laura_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ L_DailyActions.append("unseen")
            $ L_RecentActions.append("unseen")    
            call Laura_SexAct("masturbate")
            if "angry" in L_RecentActions:
                return
        
#After caught masturbating. . .
            $ L_Eyes = "sexy"
            $ L_Brows = "confused"
            $ L_Mouth = "smile"
            if L_Mast == 1:        
                    $ L_Mouth = "kiss"
                    ch_l "So what are you doing here? . ."
                    $ L_Eyes = "side"
                    $ L_Mouth = "lipbite"        
                    ch_l "not that I mind the company. . ."
                    $ L_Eyes = "sexy"
                    $ L_Brows = "normal"         
                    $ L_Mouth = "smile"
                    ch_l "But you know, give me a heads up first." 
            else:
                    ch_l "You're around a lot. . ."            
            $ Laura_Arms = 1  
            call LauraOutfit      
            return
    
# end Laura_Caught_Masturbating/////////////////////////////////////////////////////


# Event Laura_Caught /////////////////////////////////////////////////////  


label Laura_Caught(TotalCaught=0):
    $ TotalCaught = R_Caught + K_Caught + E_Caught + L_Caught
    call Shift_Focus("Laura")
    call Checkout
    ch_l "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call LauraOutfit
    if R_Loc == bg_current:         
        $ R_Loc = "bg study"
    if K_Loc == bg_current:                
        $ K_Loc = "bg study" 
    if E_Loc == bg_current:                
        $ E_Loc = "bg study"        
    $ bg_current = "bg study"  
    $ L_Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    show Laura_Sprite at SpriteLoc(StageRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if E_Loc == bg_current:         
        show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call LauraFace("sad")
    ch_x "I'm very disappointed in your behavior, the both of you."
    
    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"
    
    if L_Shame >= 40:
        ch_x "Laura, my dear, you're practically naked! At least throw a towel on!"
        "He throws Laura the towel."
        show blackscreen onlayer black 
        $ L_Over = "towel"         
        hide blackscreen onlayer black
    elif L_Shame >= 20:
        ch_x "Laura, my dear, that attire is positively scandalous."
    
    if L_Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        if "Rogue" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1, Eyes="side")
    elif K_Loc == bg_current:             #fix, might not currently work?
        call KittyFace("surprised",2)
        if "Kitty" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Kitty, you were just watching this occur!"        
        call KittyFace("bemused",1,Eyes="side")
    elif E_Loc == bg_current:             #fix, might not currently work?
        call EmmaFace("surprised",2)
        if "Emma" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Emma, you were just watching this occur!" 
            ch_x "Unacceptable. . ."        
        call EmmaFace("bemused",1, Eyes="side")
        
    if "rules" in Rules: #if the rules had been removed in a previous game
            call XavierFace("hypno")
            ch_x ". . ."
            ch_x "Hmm, I seem to be having a bit of deja vu here. . ."
            ch_x "I could swear that we've had a conversation like this before, but I cannot recall when. . ."
            call XavierFace("angry")
            ch_x "Regardless, this is a serious issue."
            $ Rules.remove("rules")
            
    $ Count = L_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if L_Caught < 5:
                call Statup("Laura", "Inbt", 30, -20)            
                call Statup("Laura", "Inbt", 50, -10) 
            call XavierFace("happy")  
            if L_Caught:
                ch_x "But you know you've done this before. . . at least [L_Caught] times. . ." 
            elif TotalCaught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [L_Pet]?":
            call Laura_Namecheck
            call LauraFace("bemused")         
            call Statup("Laura", "Lust", 90, 5) 
            if L_Caught < 5:            
                call Statup("Laura", "Inbt", 90, 10)   
                call Statup("Laura", "Love", 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."    
            if L_Caught < 5:            
                call Statup("Laura", "Obed", 50, 20)
                call Statup("Laura", "Obed", 90, 20)
                call Statup("Laura", "Inbt", 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Chi, Laura!" if P_Lvl >= 5:
            if L_Lvl >= 5 and ApprovalCheck("Laura", 1500, TabM=1, Loc="No") and ApprovalCheck("Laura", 750, "I"):                   
                    jump Plan_Chi
            elif ApprovalCheck("Laura", 1000, TabM=1, Loc="No"):
                    call LauraFace("angry",Eyes="side") 
                    $ L_Brows = "angry"
                    ch_l "I told you that was a stupid idea. . ."
                    menu:
                        "Dammit Laura. . .":
                                call LauraFace("angry")
                                call Statup("Laura", "Obed", 50, 5)
                                call Statup("Laura", "Love", 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call LauraFace("bemused") 
                                call Statup("Laura", "Love", 90, 5) 
            else:
                    call LauraFace("confused") 
                    ch_l "Yeah!"
                    ch_l ". . ."
                    ch_l "Wait, plan \"key,\" what??"
                    ch_p "Plan {i}Chi!{/i} . . you know. . ."
                    ch_l "Um. No?"
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call LauraFace("bemused") 
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."  
            if L_Caught < 5:              
                call Statup("Laura", "Obed", 50, 10)
                call Statup("Laura", "Obed", 90, 10)
                call Statup("Laura", "Inbt", 30, -10)
                call Statup("Laura", "Inbt", 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call LauraFace("surprised")
            call Statup("Laura", "Lust", 90, 10)
            if L_Caught < 5:
                call Statup("Laura", "Obed", 50, 25)
                call Statup("Laura", "Obed", 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if L_Caught < 5:
                if L_Inbt > 50:
                    call Statup("Laura", "Inbt", 90, 15)             
                call Statup("Laura", "Inbt", 30, -15)
                call Statup("Laura", "Inbt", 50, -10)    
            ch_x "Now get out of my sight."
    
    if "Xavier's photo" not in P_Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            "There probably isn't a way available right now though. . ."
#            if L_Caught > 1: 
#                "Maybe I should try searching the office when he's not around."
#            if L_Caught > 2:
#                "I bet Laura could help me get in."
    $ PunishmentX += Count            
    $ L_Caught += 1
    $ L_RecentActions.append("caught")
    $ L_DailyActions.append("caught") 
    call Remove_Girl("All")  
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Chi:
    call LauraFace("sly")         
    "As you say this, a sly grin crosses Laura's face."
    $ Laura_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."   
    show Laura_Sprite at SpriteLoc(StageLeft+100,150) with ease
    $ L_SpriteLoc = StageCenter
    "Laura moves in sits on his lap, placing one hand on his."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    elif K_Loc == bg_current and "Kappa" not in P_Traits:        
        call KittyFace("surprised")      
        "Kitty looks a bit caught off guard, but goes along with the idea."        
        call KittyFace("sly")
    elif E_Loc == bg_current and "Psi" not in P_Traits:        
        call EmmaFace("surprised")      
        "Emma looks a bit caught off guard, but goes along with the idea."        
        call EmmaFace("sly")
    call XavierFace("angry")
    
    if "Chi" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            call Statup("Laura", "Obed", 80, 3)
            call Statup("Laura", "Inbt", 80, 1)   
    else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "Laura and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [L_Pet] here has a very particular set of skills, you know. . ."
            call Laura_Namecheck
            $ L_Claws = 1
            call LauraFace("sly")     
            ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
            "Laura draws her claws along the arm of the Professor's chair, tracing fine lines into the metal." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            call Statup("Laura", "Obed", 50, 40)
            call Statup("Laura", "Inbt", 80, 30)
            call Statup("Laura", "Obed", 200, 30)
            call Statup("Laura", "Inbt", 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_l "Well, [L_Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if "Laura" not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append("Laura")
            "You know, it's kinda fun dodging you, catch us if you can." if "Laura" in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove("Laura")
            "Raise my stipend." if P_Income < 30 and "Chi" not in P_Traits:    
                    ch_x "Very well. . . but I can only raise it by so much. . ."        
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Chi" in P_Traits:           
                    pass
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, take it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Laura's room." if "Laura" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Laura")
                    "Give me the key to Laura's room.[[Owned] (locked)" if "Laura" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conclude our business. Please leave." 
    if "Chi" not in P_Traits:
        call Statup("Laura", "Lust", 90, 10)
        call Statup("Laura", "Inbt", 80, 10)
        call Statup("Laura", "Love", 70, 10)
        call Statup("Laura", "Love", 200, 20)
        $ P_Traits.append("Chi")
    $ Laura_Arms = 1
    $ L_Claws = 0
    "You return to your room"
    jump Player_Room
                              
# end Laura_Caught/////////////////////////////////////////////////////


label Gwentro:
        if Taboo > 5 or R_Loc == bg_current or K_Loc == bg_current or E_Loc == bg_current:
            #returns if other girls are present, this is a one on one thing. 
            return
        $ L_History.append("Gwentro")
        $ GwenName = "???"
        ch_g "Where is the exit to this place?!" 
        call GwenFace("angry")
        show Gwen_Sprite at SpriteLoc(1500) zorder 25:
                xzoom -1 
        show Gwen_Sprite at SpriteLoc(100) zorder 25 with easeinright #call Display_Gwen
        pause .1
        call GwenFace("surprised")
        $ Speed = 0
        call LauraFace("surprised",2,Eyes="side")
        show Gwen_Sprite at SpriteLoc(200) zorder 25 with vpunch #call Display_Gwen
        ch_g "Ouch!" 
        call GwenFace("angry")
        ch_g "Ok, that's a wall. . . apparently." 
        call GwenFace("surprised")
        ch_g "Oh, hey you tw-"
        call GwenFace("surprised",1,Mouth="kiss")
        ch_g "Um. . ."
        call GwenFace("shocked",1)
        ch_g "Sorry! My bad, I was just. . ." 
        call LauraFace("confused",2,Eyes="side")
        call GwenFace("surprised",1,Mouth="kiss")
        extend "\n looking for an exit. . ." 
        call GwenFace("smile",1)
        extend "\n but you two. . . seem to be working on something. . ." 
        call GwenFace("sad",1)
        extend "\n and now I can't see because of this stupid word balloon. . ." 
        show Gwen_Sprite:
            ease 1 ypos 150 
        call GwenFace("smile",1)
        extend ""
        ch_g "Better. . ."
        show Gwen_Sprite:
            ease 1 ypos 50 
        ch_g "So now that we've got that taken care of, what's your name?"
        call LauraFace("angry",1,Eyes="side")
        show Gwen_Sprite:
            ypos 50
        ch_g "So now that we've got that taken care of, what's your name?{w=0.2}{nw}"                            
        call GwenFace("shocked",0)
        menu:
            ch_g "So now that we've got that taken care of, what's your name?{nw}"
            "[Playername]":
                pass
            "Zero":
                pass
            "None of your buisiness":
                pass
            "Who are you?":
                pass
        ch_g "Whoa!" with vpunch
        menu:
            ch_g "Whoa!"
            "What?":
                pass                            
        call GwenFace("surprised")
        ch_g "Sorry, it's just that menu popping up caught me by surprise."                            
        call GwenFace("smile")
        ch_g "That's how you talk around here? Menus?"
        menu:
            extend ""
            "Yes?":
                    ch_g "That's ok, no judgement. . ."
                    ch_g "I guess that's not the most important thing at the moment. . ."
            "What are you talking about?":
                    ch_g "The floating blocks from earlier? I guess you can't see those. . ."
                    ch_g "Unless you're roleplaying right now." 
        ch_g "Anyway, back to you, what's your name?"
        menu:
            extend ""
            "[Playername]":
                ch_p "It's [Playername]."
                ch_g "Hi, [Playername], my name's Gwen!"
                $ GwenName = "Gwen"
            "None of your buisiness":
                ch_p "It's none of your business."
                ch_g "Well, it looks like your name is [Playername]."
                ch_g "I could tell from the menu."
                ch_g "Mine's Gwen, b-t-dubs."
            "Who are you?":
                ch_p "Never mind me, who are you?!" 
                ch_g "Oh! That's fair, I'm new around here. My name's Gwen!"
                ch_g "And it looks like your name is [Playername]."
                ch_g "I could tell from the menu."
        if GwenName != "Gwen":
            $ GwenName = "Gwen"
            menu:
                extend ""
                "What menu?!":
                    ch_g "Don't worry about it."                                
                "Riiiight. . .":
                    pass
        ch_g "It is kinda crowded over here though, so if you don't mind. . ."
        show Gwen_Sprite:
            easeout 1 xpos 300 
            xzoom 1
            easein .5 xpos 900 
        ch_g "Ah, yes, room to breathe!"
        call LauraFace("angry",Eyes="leftside")
        ch_g "Sorry, I should have said hello earlier, hey Laura!"
        call LauraFace("confused",Eyes="leftside")
        ch_l "How do you know my name!"
        ch_g "I've read all about you! Or do you prefer \"X-23?\""
        ch_g "Or \"Wolverine?\""                            
        call GwenFace("surprised",Mouth="kiss")
        ch_g "God, it's not \"Talon,\" is it?"                       
        call GwenFace("smile")
        ch_l "[LauraName] - is - fine."                            
        call GwenFace("smile",Mouth="kiss")
        ch_g "Cool, so. . ."
        menu:
            "What are you doing here?":
                ch_p "What are you doing here?" 
                ch_g "I had a feeling you would ask that."
            "Some other irrelvant option.":
                ch_p "What are you doing here?" 
                ch_g "Man, determinism, am I right?"
        call LauraFace("confused",Eyes="leftside")
        ch_g "Why are any of us here, really?"
        ch_g "Oh! You mean \"why am I {i}here{/i}\" in this game?"                            
        call GwenFace("sad")
        ch_g "Honestly? No idea. One minute I had an ongoing, then I was on a team book, guess that's cancelled now?"                            
        call GwenFace("smile")
        ch_g "Yeah, your guess is as good as mine. Maybe whoever made it's a fan?"
        call GwenFace("smile",1)
        ch_g "Judging by what you two have cooking over there, looks like some kind of hentai game."
        ch_g "Well, \"When in Rome. . .\""
        show Gwen_Sprite:
            easeout .2 xpos 890 
            easeout .2 xpos 900 
            pause .5
            easeout .15 xpos 880 
            easeout .15 xpos 910 
            easeout .15 xpos 880 
            easeout .15 xpos 900 
        ch_g "Well, \"When in Rome. . .\"{w=1.8}{nw}"                            
        call GwenFace("angry",1)
        ch_g "Huh."
        ch_g "Apparently I can't get my clothes off here."                            
        call GwenFace("sad",1)
        ch_g "That's unfortunate."                             
        call GwenFace("angry",1,Mouth="smile")
        ch_g "I could just stay and watch for a bit. . ."
        call LauraFace("angry",Eyes="leftside")                            
        call GwenFace("surprised",1)
        ch_l "NO!"
        ch_g "Right, right. Don't poke the wolverine. . ."                            
        call GwenFace("smile",1)
        ch_g "Except you, of course -wink-."       
        call GwenFace("sad",0)
        show Gwen_Sprite:
            ease .5 xpos 950                      
        ch_g "I should probably get going then. . ."
        show Gwen_Sprite:
            ease .5 xpos 1050 
        ch_g "Don't know when I'll be back. . ."
        show Gwen_Sprite:
            ease .5 xpos 1200 
        ch_g "If ever. . ."
        show Gwen_Sprite:
            ease .5 xpos 1000        
        call GwenFace("sad",1,Eyes="surprised")
        ch_g "Maybe never, we won't know."
        show Gwen_Sprite:
            ease .2 xpos 1500                                    
        call GwenFace("surprised")
        ch_l "Get out!"
        ch_g "Right! I'm gone, sorry!"
        hide Gwen_Sprite                        
        call LauraFace("bemused",Eyes="sexy")
        ch_l "Now, what were were doing. . ."
        
        return
    