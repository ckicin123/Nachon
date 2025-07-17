"""
right looking back at this code i'm realising a certain pattern
i may or may not have known of how pointers worked so and so
absoloute armies of if statements were used. 
as someone who now knows c++ and has actually worked on applications,
this hurts to look at.
ALSO DAMN HOW DID I HAVE THE PATIENCE TO WRITE SO MANY IF STATEMENTS?
"""


import time
class card:
    def __init__(self,name,at,de,spec,specinfo,hp,backround):
        self.at=at
        self.de=de
        self.spec=spec
        self.specinfo=specinfo
        self.hp=hp
        self.backround=backround
        self.name=name
def p(x):
    for i in x:
        print(i,end="")
        time.sleep(0.005)
    print("")
def hpdecheck(x):
    p(x.name+"\nHP: "+str(x.hp)+"\nDefense: "+str(x.de)+"\nAttack: "+str(x.at))
    print("")
def backcheck(x):
    pp=input(": ")
    if pp in x:
        if pp=="nightfury":
            p(str(nightfury.backround)+"\nattack: "+str(nightfury.at)+"\ndefense: "+str(nightfury.de)+"\nspecial count: "+str(nightfury.spec)+"\nspecial info: "+str(nightfury.specinfo)+"\nHP: "+str(nightfury.hp))
        elif pp=="firewall":
            p(str(firewall.backround)+"\nattack: "+str(firewall.at)+"\ndefense: "+str(firewall.de)+"\nspecial count: "+str(firewall.spec)+"\nspecial info: "+str(firewall.specinfo)+"\nHP: "+str(firewall.hp))
        elif pp=="cheater charles":
            p(str(cheater_charles.backround)+"\nattack: "+str(cheater_charles.at)+"\ndefense: "+str(cheater_charles.de)+"\nspecial count: "+str(cheater_charles.spec)+"\nspecial info: "+str(cheater_charles.specinfo)+"\nHP: "+str(cheater_charles.hp))
        elif pp=="rooster ron":
            p(str(rooster_ron.backround)+"\nattack: "+str(rooster_ron.at)+"\ndefense: "+str(rooster_ron.de)+"\nspecial count: "+str(rooster_ron.spec)+"\nspecial info: "+str(rooster_ron.specinfo)+"\nHP: "+str(rooster_ron.hp))
        elif pp=="ankle breaker":
            p(str(ankle_breaker.backround)+"\nattack: "+str(ankle_breaker.at)+"\ndefense: "+str(ankle_breaker.de)+"\nspecial count: "+str(ankle_breaker.spec)+"\nspecial info: "+str(ankle_breaker.specinfo)+"\nHP: "+str(ankle_breaker.hp))
        elif pp=="camo cat":
            p(str(camo_cat.backround)+"\nattack: "+str(camo_cat.at)+"\ndefense: "+str(camo_cat.de)+"\nspecial count: "+str(camo_cat.spec)+"\nspecial info: "+str(camo_cat.specinfo)+"\nHP: "+str(camo_cat.hp))
        return True
    return False
nightfury=card("nightfury",200,200,100,"dash and blast: fly by every enemy quickly and shoot them all deals 100",300,"the dark bullet through the sky so fast you will\nnever see it coming but only the damage it inflicts")
firewall=card("firewall",0,400,100,"barbed wire: defends but also deals 100 damage on any attacking card",300,"a blockage in the way of all but can hurt others in the case that it is attacked")
cheater_charles=card("cheater charles",100,100,100,"cheat code: gives all of your cards an extra 100 damage",100,"the salty hacker of the team but will support it's friends")
rooster_ron=card("rooster ron",100,1,200,"sacrafical feeding: gives all of your\ncard 200 more HP but they do that by eating rooster ron",50,"shoots eggs at it's enemys with no remorse\nthough willing to sacrifice itself for the good of it's friends")
ankle_breaker=card("ankle breaker",200,200,100,"break quake: jumps and smashes the ground making a shockwave sending all it's enemys backwards dealing 100 damage",300,"a dinosoar with a mace for a tale and rock-hard skin")
camo_cat=card("camo cat",0,0,0,"copycat: takes the stats of 1 enemy card",50,"the outcast that really wants to fit in")
scard=["nightfury","firewall","cheater charles","rooster ron","ankle breaker","camo cat"]
p1card=[]
p2card=[]
p("welcome to Nachon\nthis is a card game I made because I had nothing to do\n")
time.sleep(1)
while len(scard)>0:
    p("player 1 pick a card:\n")
    for i in scard:
        p(i)
    while True:
        pp=input(": ")
        if pp in scard:
            p1card.append(pp)
            scard.remove(pp)
            break
        else:
            p("not a card")
    p("player 2 pick a card:\n")
    for i in scard:
        p(i)
    while True:
        pp=input(": ")
        if pp in scard:
            p2card.append(pp)
            scard.remove(pp)
            break
        else:
            p("not a card")
p("\nplayer 1 cards\n")
for i in p1card:
    p(i)
print("")
p("player 2 cards\n")
for i in p2card:
    p(i)
print("")
while True:
    p("player 1, would you like to see a discription of any of your cards?: y/n")
    if input("")=="y":
        p("pick a card\n")
        for i in p1card:
            p(i)
        while True:
            if backcheck(p1card):
                break
            else:
                p("not a card")
    else:
        break
while True:
    p("player 2, would you like to see a discription of any of your cards?: y/n")
    if input("")=="y":
        p("pick a card\n")
        for i in p2card:
            p(i)
        while True:
            if backcheck(p2card):
                break
            else:
                p("not a card")
    else:
        break
play=1
ma1=0
ma2=0
target1="None"
target2="None"
r1=True
r2=True
r3=True
r4=True
r5=True
p1cardspec=[]
p2cardspec=[]
r6=True
fw1=False
fw2=False
for i in p1card:
    p1cardspec.append(i)
for i in p2card:
    p2cardspec.append(i)
while True:
    p("\n\n\n\nplayer 1 cards:\n")
    for pp in p1card:
        if pp=="nightfury":
            hpdecheck(nightfury)
        elif pp=="firewall":
            hpdecheck(firewall)
        elif pp=="cheater charles":
            hpdecheck(cheater_charles)
        elif pp=="rooster ron":
            hpdecheck(rooster_ron)
        elif pp=="ankle breaker":
            hpdecheck(ankle_breaker)
        elif pp=="camo cat":
            hpdecheck(camo_cat)
    p("\n\n\nplayer 2 cards:\n")
    for pp in p2card:
        if pp=="nightfury":
            hpdecheck(nightfury)
        elif pp=="firewall":
            hpdecheck(firewall)
        elif pp=="cheater charles":
            hpdecheck(cheater_charles)
        elif pp=="rooster ron":
            hpdecheck(rooster_ron)
        elif pp=="ankle breaker":
            hpdecheck(ankle_breaker)
        elif pp=="camo cat":
            hpdecheck(camo_cat)
    if nightfury.hp<=0 and r1:
        try:
            p1card.remove("nightfury")
            if "nightfury" in p1cardspec:
                p1cardspec.remove("nightfuryt")
        except:
            p2card.remove("nightfury")
            if "nightfury" in p2cardspec:
                p2cardspec.remove("nightfury")
        r1=False
        p("the nightfury is now dead")
    if firewall.hp<=0 and r2:
        try:
            p1card.remove("firewall")
            if "firewall" in p1cardspec:
                p1cardspec.remove("firewall")
        except:
            p2card.remove("firewall")
            if "firewall" in p2cardspec:
                p2cardspec.remove("firewall")
        r2=False
        p("the firewall is now dead")
    if cheater_charles.hp<=0 and r3:
        try:
            p1card.remove("cheater charles")
            if "cheater charles" in p1cardspec:
                p1cardspec.remove("cheater charles")
        except:
            p2card.remove("cheater charles")
            if "cheater charles" in p2cardspec:
                p2cardspec.remove("cheater charles")
        r3=False
        p("cheater charles is now dead")
    if rooster_ron.hp<=0 and r4:
        try:
            p1card.remove("rooster ron")
        except:
            p2card.remove("rooster ron")
        r4=False
        p("rooster ron is now dead")
    if ankle_breaker.hp<=0 and r5:
        try:
            p1card.remove("ankle breaker")
            if "ankle breaker" in p1cardspec:
                p1cardspec.remove("ankle breaker")
        except:
            p2card.remove("ankle breaker")
            if "ankle breaker" in p2cardspec:
                p2cardspec.remove("ankle breaker")
        r5=False
        p("the ankle breaker is now dead")
    if camo_cat.hp<=0 and r6:
        try:
            p1card.remove("camo cat")
            if "camo cat" in p1cardspec:
                p1cardspec.remove("camo cat")
        except:
            p2card.remove("camo cat")
            if "camo cat" in p2cardspec:
                p2cardspec.remove("camo cat")
        r6=False
        p("camo cat is now dead")
    if len(p1card)<=0:
        p("player 2 wins")
        break
    elif len(p2card)<=0:
        p("player 1 wins")
        break
    if play==1:
        play=0
        p("\nplayer 1 your move\n1 for attack\n2 for defend\n3 for special")
        while True:
            pp=(input(": "))
            if pp=="1":#attack p1
                ma1=0
                p("pick a card to attack with\n")
                for i in p1card:
                    p(i)
                while True:
                    pp=input(": ")
                    if pp in p1card:
                        if pp=="nightfury":
                            attack=nightfury.at
                            attacker=nightfury
                        elif pp=="firewall":
                            attack=firewall.at
                            attacker=firewall
                        elif pp=="cheater charles":
                            attack=cheater_charles.at
                            attacker=cheater_charles
                        elif pp=="rooster ron":
                            attack=rooster_ron.at
                            attacker=rooster_ron
                        elif pp=="ankle breaker":
                            attack=ankle_breaker.at
                            attacker=ankle_breaker
                        elif pp=="camo cat":
                            attack=camo_cat.at
                            attacker=camo_cat
                        break
                    else:
                        p("not a card")
                if ma2==0:
                    p("\npick an enemy card to attack\n")
                    for i in p2card:
                        p(i)
                    while True:
                        pp=input(": ")
                        if pp in p2card:
                            if pp=="nightfury":
                                nightfury.hp-=attack
                                p("the nightfury is now on "+str(nightfury.hp))
                            elif pp=="firewall":
                                firewall.hp-=attack
                                p("the firewall is now on "+str(firewall.hp))
                            elif pp=="cheater charles":
                                cheater_charles.hp-=attack
                                p("the cheater charles is now on "+str(cheater_charles.hp))
                            elif pp=="rooster ron":
                                rooster_ron.hp-=attack
                                p("the rooster ron is now on "+str(rooster_ron.hp))
                            elif pp=="ankle breaker":
                                ankle_breaker.hp-=attack
                                p("the ankle breaker is now on "+str(ankle_breaker.hp))
                            elif pp=="camo cat":
                                camo_cat.hp-=attack
                                p("the camo cat is now on "+str(camo_cat.hp))
                            break
                        else:
                            p("not a card")
                else:
                    target.de-=attack
                    if target.de<0:
                        target.hp+=target.de
                        target.de=0
                    p("\nthe "+target.name+" is now on "+str(target.de)+" Defense")
                    if target.de==0:
                        p("the "+target.name+" is now on "+str(target.hp)+" HP")
                    if fw2:
                        fw2=False
                        attacker.hp-=50
                        p("firewall's special has left "+attacker.name+" on "+str(attacker.hp))
                ma2=0
                break
            elif pp=="2":#defense p1
                p("pick a card to defend with\n")
                for i in p1card:
                    p(i)
                while True:
                    pp=input(": ")
                    if pp in p1card:
                        if pp=="nightfury":
                            target=nightfury
                            p("nightfury is now defending with "+str(nightfury.de))
                        elif pp=="firewall":
                            target=firewall
                            p("firewall is now defending with "+str(firewall.de))
                        elif pp=="cheater charles":
                            target=cheater_charles
                            p("cheater charles is now defending with "+str(cheater_charles.de))
                        elif pp=="rooster ron":
                            target=rooster_ron
                            p("rooster ron is now defending with "+str(rooster_ron.de))
                        elif pp=="ankle breaker":
                            target=ankle_breaker
                            p("ankle breaker is now defending with "+str(ankle_breaker.de))
                        elif pp=="camo cat":
                            target=camo_cat
                            p("camo cat is now defending with "+str(camo_cat.de))
                        break
                    else:
                        p("not a card")
                ma1=1
                break
            elif pp=="3": #special 1
               
                p("pick a card to use it's special\n")
                for i in p1cardspec:
                    p(i)
                while True:
                    if len(p1cardspec)<=0:
                        p("no specials left\n")
                        break
                    pp=input(": ")
                    if pp in p1cardspec:
                        if pp=="nightfury":
                            p1cardspec.remove("nightfury")
                            for pp in p2card:
                                   attack=nightfury.spec
                                   if pp=="firewall":
                                       firewall.hp-=attack
                                       p("the firewall is now on "+str(firewall.hp))
                                   elif pp=="cheater charles":
                                       cheater_charles.hp-=attack
                                       p("the cheater charles is now on "+str(cheater_charles.hp))
                                   elif pp=="rooster ron":
                                        rooster_ron.hp-=attack
                                        p("the rooster ron is now on "+str(rooster_ron.hp))
                                   elif pp=="ankle breaker":
                                        ankle_breaker.hp-=attack
                                        p("the ankle breaker is now on "+str(ankle_breaker.hp))
                                   elif pp=="camo cat":
                                        camo_cat.hp-=attack
                                        p("the camo cat is now on "+str(camo_cat.hp))
                        elif pp=="firewall":
                            p1cardspec.remove("firewall")
                            ma1=1
                            target=firewall
                            fw1=True
                            p("firewall is now defending with "+str(firewall.de))
                        elif pp=="cheater charles":
                            p1cardspec.remove("cheater charles")
                            for pp in p1card:
                                if pp=="nightfury":
                                    nightfury.at+=cheater_charles.spec
                                    p("nightfury's new attack is "+str(nightfury.at))
                                elif pp=="firewall":
                                    firewall.at+=cheater_charles.spec
                                    p("firewall's new attack is "+str(firewall.at))
                                elif pp=="cheater charles":
                                    cheater_charles.at+=cheater_charles.spec
                                    p("cheater_charles' new attack is "+str(cheater_charles.at))
                                elif pp=="rooster ron":
                                    rooster_ron.at+=cheater_charles.spec
                                    p("rooster ron's new attack is "+str(rooster_ron.at))
                                elif pp=="ankle breaker":
                                    ankle_breaker.at+=cheater_charles.spec
                                    p("ankle breaker's new attack is "+str(ankle_breaker.at))
                                elif pp=="camo cat":
                                    camo_cat.at+=cheater_charles.spec
                                    p("camo cat's new attack is "+str(camo_cat.at))
                        elif pp=="rooster ron":
                            p1cardspec.remove("rooster ron")
                            rooster_ron.hp=0
                            for pp in p1card:
                                if pp=="nightfury":
                                    nightfury.hp+=rooster_ron.spec
                                    p("nightfury's new HP is "+str(nightfury.hp))
                                elif pp=="firewall":
                                    firewall.hp+=rooster_ron.spec
                                    p("firewall's new HP is "+str(firewall.hp))
                                elif pp=="cheater charles":
                                    cheater_charles.hp+=rooster_ron.spec
                                    p("cheater charles's new health is "+str(cheater_charles.hp))
                                elif pp=="ankle breaker":
                                    ankle_breaker.hp+=rooster_ron.spec
                                    p("ankle breaker's new health is "+str(ankle_breaker.hp))
                                elif pp=="camo cat":
                                    camo_cat.hp+=rooster_ron.spec
                                    p("camo cat's new health is "+str(camo_cat.hp))
                        elif pp=="ankle breaker":
                            p1cardspec.remove("ankle breaker")
                            for pp in p2card:
                                attack=ankle_breaker.spec
                                if pp=="nightfury":
                                    nightfury.hp-=attack
                                    p("the nightfury is now on "+str(nightfury.hp))
                                elif pp=="firewall":
                                    firewall.hp-=attack
                                    p("the firewall is now on "+str(firewall.hp))
                                elif pp=="cheater charles":
                                    cheater_charles.hp-=attack
                                    p("the cheater charles is now on "+str(cheater_charles.hp))
                                elif pp=="rooster ron":
                                    rooster_ron.hp-=attack
                                    p("the rooster ron is now on "+str(rooster_ron.hp))
                                elif pp=="ankle breaker":
                                    ankle_breaker.hp-=attack
                                    p("the ankle breaker is now on "+str(ankle_breaker.hp))
                                elif pp=="camo cat":
                                    camo_cat.hp-=attack
                                    p("the camo cat is now on "+str(camo_cat.hp))
                        elif pp=="camo cat":
                            p1cardspec.remove("camo cat")
                            p("pick an enemy card to copy\n")
                            for i in p2card:
                                p(i)
                            while True:
                                pp=input(": ")
                                if pp in p2card:
                                    if pp=="nightfury":
                                        cc=nightfury
                                    elif pp=="firewall":
                                        cc=firewall
                                    elif pp=="cheater charles":
                                        cc=cheater_charles
                                    elif pp=="rooster ron":
                                        cc=rooster_ron
                                    elif pp=="ankle breaker":
                                        cc=ankle_breaker
                                    elif pp=="camo cat":
                                        cc=camo_cat
                                    break
                                else:
                                    p("not an option")
                            p("camo cat now has all the stats of the "+cc.name)
                            camo_cat.hp=cc.hp
                            camo_cat.at=cc.at
                            camo_cat.de=cc.de
                        break
                    else:
                        p("not a card")
                break    
            else:
                p("not an option")
    else:
        play=1
        p("\nplayer 2 your move\n1 for attack\n2 for defend\n3 for special")
        while True:
            pp=(input(": "))
            if pp=="1":#attack p2
                ma2=0
                p("\npick a card to attack with\n")
                for i in p2card:
                    p(i)
                while True:
                    pp=input(": ")
                    if pp in p2card:
                        if pp=="nightfury":
                            attack=nightfury.at
                            attacker=nightfury
                        elif pp=="firewall":
                            attack=firewall.at
                            attacker=firewall
                        elif pp=="cheater charles":
                            attack=cheater_charles.at
                            attacker=cheater_charles
                        elif pp=="rooster ron":
                            attack=rooster_ron.at
                            attacker=rooster_ron
                        elif pp=="ankle breaker":
                            attack=ankle_breaker.at
                            attacker=ankle_breaker
                        elif pp=="camo cat":
                            attack=camo_cat.at
                            attacker=camo_cat
                        break
                    else:
                        p("not a card")
                if ma1==0:
                    p("\npick an enemy card to attack\n")
                    for i in p1card:
                        p(i)
                    while True:
                        pp=input(": ")
                        if pp in p1card:
                            if pp=="nightfury":
                                nightfury.hp-=attack
                                p("the nightfury is now on "+str(nightfury.hp))
                            elif pp=="firewall":
                                firewall.hp-=attack
                                p("the firewall is now on "+str(firewall.hp))
                            elif pp=="cheater charles":
                                cheater_charles.hp-=attack
                                p("the cheater charles is now on "+str(cheater_charles.hp))
                            elif pp=="rooster ron":
                                rooster_ron.hp-=attack
                                p("the rooster ron is now on "+str(rooster_ron.hp))
                            elif pp=="ankle breaker":
                                ankle_breaker.hp-=attack
                                p("the ankle breaker is now on "+str(ankle_breaker.hp))
                            elif pp=="camo cat":
                                camo_cat.hp-=attack
                                p("the camo cat is now on "+str(camo_cat.hp))
                            break
                        else:
                            p("not a card")
                else:
                    target.de-=attack
                    if target.de<0:
                        target.hp+=target.de
                        target.de=0
                    p("\nthe "+target.name+" is now on "+str(target.de)+" Defense")
                    if target.de==0:
                        p("the "+target.name+" is now on "+str(target.hp)+" HP")
                    if fw1:
                        fw1=False
                        attacker.hp-=50
                        p("firewall's special has left "+attacker.name+" on "+str(attacker.hp))
                ma1=0
                break
            elif pp=="2":#defend p2
                p("pick a card to defend with\n")
                for i in p2card:
                    p(i)
                while True:
                    pp=input(": ")
                    if pp in p2card:
                        if pp=="nightfury":
                            target=nightfury
                            p("nightfury is now defending with "+str(nightfury.de))
                        elif pp=="firewall":
                            target=firewall
                            p("firewall is now defending with "+str(firewall.de))
                        elif pp=="cheater charles":
                            target=cheater_charles
                            p("cheater charles is now defending with "+str(cheater_charles.de))
                        elif pp=="rooster ron":
                            target=rooster_ron
                            p("rooster ron is now defending with "+str(rooster_ron.de))
                        elif pp=="ankle breaker":
                            target=ankle_breaker
                            p("ankle breaker is now defending with "+str(ankle_breaker.de))
                        elif pp=="camo cat":
                            target=camo_cat
                            p("camo cat is now defending with "+str(camo_cat.de))
                        break
                    else:
                        p("not a card")
                ma2=1
                break
            elif pp=="3": #special p2
                p("pick a card to use it's special\n")
                for i in p2cardspec:
                    p(i)
                while True:
                    if len(p2cardspec)<=0:
                        p("no specials left\n")
                        break
                    pp=input(": ")
                    if pp in p2cardspec:
                        if pp=="nightfury":
                            p2cardspec.remove("nightfury")
                            for pp in p1card:
                                attack=nightfury.spec
                                if pp=="nightfury":
                                    nightfury.hp-=attack
                                    p("the nightfury is now on "+str(nightfury.hp))
                                elif pp=="firewall":
                                    firewall.hp-=attack
                                    p("the firewall is now on "+str(firewall.hp))
                                elif pp=="cheater charles":
                                    cheater_charles.hp-=attack
                                    p("the cheater charles is now on "+str(cheater_charles.hp))
                                elif pp=="rooster ron":
                                    rooster_ron.hp-=attack
                                    p("the rooster ron is now on "+str(rooster_ron.hp))
                                elif pp=="ankle breaker":
                                    ankle_breaker.hp-=attack
                                    p("the ankle breaker is now on "+str(ankle_breaker.hp))
                                elif pp=="camo cat":
                                    camo_cat.hp-=attack
                                    p("the camo cat is now on "+str(camo_cat.hp))
                        elif pp=="firewall":
                            p2cardspec.remove("firewall")
                            ma2=1
                            target=firewall
                            fw2=True
                        elif pp=="cheater charles":
                            p2cardspec.remove("cheater charles")
                            for pp in p2card:
                                if pp=="nightfury":
                                    nightfury.at+=cheater_charles.spec
                                    p("nightfury's new attack is "+str(nightfury.at))
                                elif pp=="firewall":
                                    firewall.at+=cheater_charles.spec
                                    p("firewall's new attack is "+str(firewall.at))
                                elif pp=="cheater charles":
                                    cheater_charles.at+=cheater_charles.spec
                                    p("cheater_charles' new attack is "+str(cheater_charles.at))
                                elif pp=="rooster ron":
                                    rooster_ron.at+=cheater_charles.spec
                                    p("rooster ron's new attack is "+str(rooster_ron.at))
                                elif pp=="ankle breaker":
                                    ankle_breaker.at+=cheater_charles.spec
                                    p("ankle breaker's new attack is "+str(ankle_breaker.at))
                                elif pp=="camo cat":
                                    camo_cat.at+=cheater_charles.spec
                                    p("camo cat's new attack is "+str(camo_cat.at))
                        elif pp=="rooster ron":
                            p2cardspec.remove("rooster ron")
                            rooster_ron.hp=0
                            for pp in p2card:
                                if pp=="nightfury":
                                    nightfury.hp+=rooster_ron.spec
                                    p("nightfury's new HP is "+str(nightfury.hp))
                                elif pp=="firewall":
                                    firewall.hp+=rooster_ron.spec
                                    p("firewall's new HP is "+str(firewall.hp))
                                elif pp=="cheater charles":
                                    cheater_charles.hp+=rooster_ron.spec
                                    p("cheater charles's new health is "+str(cheater_charles.hp))
                                elif pp=="ankle breaker":
                                    ankle_breaker.hp+=rooster_ron.spec
                                    p("ankle breaker's new health is "+str(ankle_breaker.hp))
                                elif pp=="camo cat":
                                    camo_cat.hp+=rooster_ron.spec
                                    p("camo cat's new health is "+str(camo_cat.hp))
                        elif pp=="ankle breaker":
                            p2cardspec.remove("ankle breaker")
                            for pp in p1card:
                                attack=ankle_breaker.spec
                                if pp=="nightfury":
                                    nightfury.hp-=attack
                                    p("the nightfury is now on "+str(nightfury.hp))
                                elif pp=="firewall":
                                    firewall.hp-=attack
                                    p("the firewall is now on "+str(firewall.hp))
                                elif pp=="cheater charles":
                                    cheater_charles.hp-=attack
                                    p("the cheater charles is now on "+str(cheater_charles.hp))
                                elif pp=="rooster ron":
                                    rooster_ron.hp-=attack
                                    p("the rooster ron is now on "+str(rooster_ron.hp))
                                elif pp=="ankle breaker":
                                    ankle_breaker.hp-=attack
                                    p("the ankle breaker is now on "+str(ankle_breaker.hp))
                                elif pp=="camo cat":
                                    camo_cat.hp-=attack
                                    p("the camo cat is now on "+str(camo_cat.hp))
                        elif pp=="camo cat":
                            p2cardspec.remove("camo cat")
                            p("pick an enemy card to copy\n")
                            for i in p1card:
                                p(i)
                            while True:
                                pp=input(": ")
                                if pp in p1card:
                                    if pp=="nightfury":
                                        cc=nightfury
                                    elif pp=="firewall":
                                        cc=firewall
                                    elif pp=="cheater charles":
                                        cc=cheater_charles
                                    elif pp=="rooster ron":
                                        cc=rooster_ron
                                    elif pp=="ankle breaker":
                                        cc=ankle_breaker
                                    elif pp=="camo cat":
                                        cc=camo_cat
                                    break
                                else:
                                    p("not a card")
                            p("camo cat now has all the stats of the "+cc.name)
                            camo_cat.hp=cc.hp
                            camo_cat.at=cc.at
                            camo_cat.de=cc.de
                        break
                    else:
                        p("not a card")
                break
            else:
                p("not an option")
