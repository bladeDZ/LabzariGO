from math import*

sar1 = []

nam1 = str(input('Ievadiet jûsu spçles segvârdu: -  '))
Rwin = str(input('Ievadiet cik raundus jûsu komanda uzvarçja? -  '))
Rloss = str(input('Ievadiet cik raundus pretinieku komanda uzvarçja? -  '))

if Rwin > Rloss:
    result = 'uzvarçja'

elif Rwin < Rloss:
    result = 'zaudçja'

elif Rwin == Rloss:
    result = 'vienâdoja rezultâtu ar pretiniekiem'

kls1 = float(input('Cik pretinieku nâves tu dabûji? -  '))
dts1 = float(input('Cik reizes tu nomiri ? -  '))
kdr1 = round(kls1/dts1, 2)

sar1.append(nam1)

sar1.append(kls1)

sar1.append(dts1)

sar1.append(kdr1)

print('Spçles rezultâts ir ' + Rwin + ':' + Rloss + ' un jûsu komanda ' + str(result) + '.')

print('Ðajâ spçlç tu dabuji ' + str(sar1[1]) + ' pretinieku nâves, bet nomiri ' + str(sar1[2]) + ' reizes.')

print('Tavs KDR (Kills to Death Ratio) ir ' + str(sar1[3]) + '.')

trpn = str(input('Vai jûs vçlaties turpinât un ievadît savas komandas '
                 'citu spçlçtâju statistikas (Lûdzu atbildiet ar "Jâ/Nç")? -  '))

if trpn == "Nç":
    print('Statistikas piefiksçðana ir principâ pabeigta.')

elif trpn == "Jâ":

    sar2 = []

    nam2 = str(input('Ievadiet jûsu otrâ komandas biedra segvârdu: -  '))
    kls2 = float(input('Cik pretinieku nâves ' + nam2 + ' dabûja? -  '))
    dts2 = float(input('Cik reizes ' + nam2 + ' nomira? -  '))
    kdr2 = round(kls2 / dts2, 2)

    sar2.append(nam2)
    sar2.append(kls2)
    sar2.append(dts2)
    sar2.append(kdr2)

    print('Ðajâ spçlç ' + nam2 + ' dabuja ' + str(sar2[1]) + ' pretinieku nâves, bet nomira ' + str(sar2[2]) +
          ' reizes.')

    print(nam2 + ' KDR (Kills to Death Ratio) ir ' + str(sar2[3]) + '.')

    sar3 = []

    nam3 = str(input('Ievadiet jûsu treðâ komandas biedra segvârdu: -  '))
    kls3 = float(input('Cik pretinieku nâves ' + nam3 + ' dabûja? -  '))
    dts3 = float(input('Cik reizes ' + nam3 + ' nomira? -  '))
    kdr3 = round(kls3 / dts3, 2)

    sar3.append(nam3)
    sar3.append(kls3)
    sar3.append(dts3)
    sar3.append(kdr3)

    print('Ðajâ spçlç ' + nam3 + ' dabuja ' + str(sar3[1]) + ' pretinieku nâves, bet nomira ' + str(sar3[2]) +
          ' reizes.')

    print(nam3 + ' KDR (Kills to Death Ratio) ir ' + str(sar3[3]) + '.')

    sar4 = []

    nam4 = str(input('Ievadiet jûsu ceturtâ komandas biedra segvârdu: -  '))
    kls4 = float(input('Cik pretinieku nâves ' + nam4 + ' dabûja? -  '))
    dts4 = float(input('Cik reizes ' + nam4 + ' nomira? -  '))
    kdr4 = round(kls4 / dts4, 2)

    sar4.append(nam4)
    sar4.append(kls4)
    sar4.append(dts4)
    sar4.append(kdr4)

    print('Ðajâ spçlç ' + nam4 + ' dabuja ' + str(sar4[1]) + ' pretinieku nâves, bet nomira ' + str(sar4[2]) +
          ' reizes.')

    print(nam4 + ' KDR (Kills to Death Ratio) ir ' + str(sar4[3]) + '.')

    sar5 = []

    nam5 = str(input('Ievadiet jûsu piektâ komandas biedra segvârdu: -  '))
    kls5 = float(input('Cik pretinieku nâves ' + nam5 + ' dabûja? -  '))
    dts5 = float(input('Cik reizes ' + nam5 + ' nomira? -  '))
    kdr5 = round(kls5 / dts5, 2)

    sar5.append(nam5)
    sar5.append(kls5)
    sar5.append(dts5)
    sar5.append(kdr5)

    print('Ðajâ spçlç ' + nam5 + ' dabuja ' + str(sar5[1]) + ' pretinieku nâves, bet nomira ' + str(sar5[2]) +
          ' reizes.')

    print(nam5 + ' KDR (Kills to Death Ratio) ir ' + str(sar5[3]) + '.')
    
    print("Tava komanda sastâvçja no " + str(nam1) + " ; " + str(nam2) + " ; " + str(nam3) + " ; " + str(nam4) + " ; "
          + str(nam5) + " ;     ")

    if float(kls1) > float(kls2) > float(kls3) > float(kls4) > float(kls5):
        print('Visvairâk pretinieku nâves dabûja ' + str(nam1) + '.' + str(kls1));
    elif float(kls2) > float(kls1) > float(kls3) > float(kls4) > float(kls5):
        print('Visvairâk pretinieku nâves dabûja ' + str(nam2) + '.' + str(kls2));
    elif float(kls3) > float(kls1) > float(kls2) > float(kls4) > float(kls5):
        print('Visvairâk pretinieku nâves dabûja ' + str(nam3) + '.' + str(kls3));
    elif float(kls4) > float(kls1) > float(kls2) > float(kls3) > float(kls5):
        print('Visvairâk pretinieku nâves dabûja ' + str(nam4) + '.' + str(kls4));
    elif float(kls5) > float(kls1) > float(kls2) > float(kls3) > float(kls4):
        print('Visvairâk pretinieku nâves dabûja ' + str(nam5) + '.' + str(kls5));
        

    if float(dts1) > float(dts2) > float(dts3) > float(dts4) > float(dts5):
        print('Visvairâk nomira ' + str(nam1) + '.')
    elif float(dts2) > float(dts1) > float(dts3) > float(dts4) > float(dts5):
        print('Visvairâk nomira ' + str(nam2) + '.')
    elif float(dts3) > float(dts1) > float(dts2) > float(dts4) > float(dts5):
        print('Visvairâk nomira ' + str(nam3) + '.')
    elif float(dts4) > float(dts1) > float(dts2) > float(dts3) > float(dts5):
        print('Visvairâk nomira ' + str(nam4) + '.')
    elif float(dts5) > float(dts1) > float(dts2) > float(dts3) > float(dts4):
        print('Visvairâk nomira ' + str(nam5) + '.')
        

    if float(kdr1) > float(kdr2) > float(kdr3) > float(kdr4) > float(kdr5):
        print('Vislabâkais KDR bija ' + str(nam1) + '.')
    elif float(kdr2) > float(kdr1) > float(kdr3) > float(kdr4) > float(kdr5):
        print('Vislabâkais KDR bija ' + str(nam2) + '.')
    elif float(kls3) > float(kdr1) > float(kdr2) > float(kdr4) > float(kdr5):
        print('Vislabâkais KDR bija ' + str(nam3) + '.')
    elif float(kdr4) > float(kdr1) > float(kdr2) > float(kdr3) > float(kdr5):
        print('Vislabâkais KDR bija ' + str(nam4) + '.')
    elif float(kdr5) > float(kdr1) > float(kdr2) > float(kdr3) > float(kdr4):
        print('Vislabâkais KDR bija ' + str(nam5) + '.')
        

    
