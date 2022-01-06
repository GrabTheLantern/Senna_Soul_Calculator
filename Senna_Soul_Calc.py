##Senna Soul Calculator

souls=int(input('How many souls do you have? ' ))
souldmg = souls * .75
if souls > 20:
    soulmult = souls / 20
    soulrange = int(soulmult * 20)
    soulcrit = int(soulmult * 10)
    print('You have at least 20 souls. In addition to ' + str(souldmg) + ' damage, you have an additional range of ' +
          str(soulrange) + ' and an extra ' + str(soulcrit) + ' crit chance.')
          
else:
    print('With ' + str(souls) + ' souls, you have an additional ' + str(souldmg) + ' damage.')
