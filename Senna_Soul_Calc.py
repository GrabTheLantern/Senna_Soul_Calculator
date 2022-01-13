##Senna Soul Calculator

souls=int(input('How many souls do you have? ' ))
souldmg = souls * .75
bonus = 'With ' + str(souls) + ' souls, you have gain the following bonuses: \n' + str(souldmg) + ' damage.\n'
if souls >= 20:
    soulmult = souls // 20
    soulrange = int(soulmult * 20)
    soulcrit = int(soulmult * 10)
    if soulcrit >= 100:
        lifesteal = (soulcrit -100) * .35
        soulcrit = 100
        bonus= bonus + str(soulcrit) + ' crit chance\n' + str(lifesteal)+ ' lifesteal \n'
        print(bonus)
    else:
        bonus = bonus + str(soulrange) + ' range \n' + str(soulcrit) + ' crit \n'
        print(bonus)
else:
    print(bonus)
