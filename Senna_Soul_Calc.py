##Senna Soul Calculator

souls=int(input('How many souls do you have? ' ))
souldmg = souls * .75
if souls >= 20:
    soulmult = souls // 20
    soulrange = int(soulmult * 20)
    soulcrit = int(soulmult * 10)
    if soulcrit >= 100:
        lifesteal = (soulcrit -100) * .35
        soulcrit = 100
        print('With ' + str(souls) + ' souls, you have gain the following bonuses:\n' + str(souldmg)+' damage\n'+ str(soulrange) + ' range\n' + str(soulcrit) + ' crit chance\n' + str(lifesteal)+ ' lifesteal \n')
    else:
        print('With ' + str(souls) + ' souls, you have gain the following bonuses:\n' + str(souldmg)+' damage\n'+ str(soulrange) + ' range\n' + str(soulcrit) + ' crit chance\n')
else:
    print('With ' + str(souls) + ' souls, you have an additional ' + str(souldmg) + ' damage.')
