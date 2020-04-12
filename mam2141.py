dados = {'MightySwing': ['fisico', 270, 0.14, 0], 
         'GiganticFist': ['fisico', 560, 0.16, 0],
         'RainyDeath':  ['fisico', 350, 0.20, 0],
         'Agilao': ['magico - fogo', 200, 0, 8],
         'Agidyne':  ['magico - fogo', 320, 0, 12],
         'Bufula': ['magico - gelo', 200, 0, 8],
         'Bufudyne': ['magico - gelo', 320, 0, 12], 
         'Megidola': ['magico', 360, 0, 32],
         'Megidolaon': ['magico', 420, 0, 60],
         'BlackViper': ['magico', 440, 0, 64],
         'Tarukaja': ['suporte', 0, 0, 12],
         'Rakukaja': ['suporte', 270, 0, 0],
         'Tarunda': ['suporte', 270, 0, 0],
         'Rakunda': ['suporte', 270, 0, 0]}

jogador01 = {"nome": input()}
jogador01['NV'], jogador01['HP'], jogador01['MP'], jogador01['ATK'], jogador01['MG'], jogador01['DEF'] = list(map(float, input().split()))

jogador02 = {"nome": input()}
jogador02['NV'], jogador02['HP'], jogador02['MP'], jogador02['ATK'], jogador02['MG'], jogador02['DEF'] = list(map(float, input().split()))

jogador01['SU'] = ''
jogador02['SU'] = ''

vez = 1
while jogador01['HP'] > 0 and jogador02['HP'] > 0:
    ataque = input()
    if dados[ataque][0] == 'fisico':
        if vez == 1:
            if jogador01['SU'] == "Tarukaja":
                up = jogador01['ATK'] * 0.25
                jogador01['ATK'] += up
                dano = 5 * (((jogador01['ATK']/jogador02['DEF']) * dados[ataque][1]) ** 0.5) * ((1 + (jogador01['NV'] - jogador02['NV'])) * 0.1)
                jogador02['HP'] -= dano 
                jogador01['HP'] -= jogador01['HP'] * dados[ataque][2]
                jogador01['ATK'] -= up
                jogador01['SU'] = ''
            elif jogador01['SU'] == "Rakukaja":
                up = jogador01['DEF'] * 0.25
                jogador01['DEF'] += up
                dano = 5 * (((jogador01['ATK']/jogador02['DEF']) * dados[ataque][1]) ** 0.5) * ((1 + (jogador01['NV'] - jogador02['NV'])) * 0.1)
                jogador02['HP'] -= dano 
                jogador01['HP'] -= jogador01['HP'] * dados[ataque][2]
                jogador01['DEF'] -= up
                jogador01['SU'] = ''
        else:
            dano = 5 * (((jogador02['ATK']/jogador01['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador02['NV'] - jogador01['NV']) * 0.1) + 1)
            jogador01['HP'] -= dano 
            jogador02['HP'] -= jogador01['HP'] * dados[ataque][2]
    if 'magico' in dados[ataque][0]:
        if vez == 1:
            dano = 5 * (((jogador01['ATK']/jogador02['DEF']) * dados[ataque][1]) ** 0.5) * ((1 + (jogador01['NV'] - jogador02['NV'])) * 0.1)
            jogador02['HP'] -= dano
            jogador01['MP'] -= dados[ataque][3] 
        else:
            dano = 5 * (((jogador02['ATK']/jogador01['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador02['NV'] - jogador01['NV']) * 0.1) + 1)
            jogador01['HP'] -= dano 
            jogador02['MP'] -= dados[ataque][3]
    if dados[ataque][0] == 'suporte':
        if vez == 1:
            jogador01['SU'] -= ataque
            jogador01['MP'] -= dados[ataque][3] 
        else:
            jogador02['SU'] = ataque
            jogador02['MP'] -= dados[ataque][3]
    
    if vez == 1:
        vez = 2
    else:
        vez = 1
        
        
if jogador01['HP'] <= 0:
    win = jogador02
    loser = jogador01
else:
    win = jogador01
    loser = jogador02 
print("%s is dead."%(loser['nome']))
print("%s HP: %.2f, MP: %.2f, ATK: %.1f, MAG: %.1f, DEF: %.1f"%(win['nome'], win['HP'], win['MP'], win['ATK'], win['MG'], win['DEF']))
