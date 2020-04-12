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
         'Rakukaja': ['suporte', 0, 0, 12],
         'Tarunda': ['suporte', 0, 0, 12],
         'Rakunda': ['suporte', 0, 0, 12]}

jogador01 = {"nome": input()}
jogador01['NV'], jogador01['HP'], jogador01['MP'], jogador01['ATK'], jogador01['MG'], jogador01['DEF'] = list(map(float, input().split()))

jogador02 = {"nome": input()}
jogador02['NV'], jogador02['HP'], jogador02['MP'], jogador02['ATK'], jogador02['MG'], jogador02['DEF'] = list(map(float, input().split()))

jogador01['SU'] = ['', 0]
jogador02['SU'] = ['', 0]

vez = 1
while jogador01['HP'] > 0 and jogador02['HP'] > 0:
    ataque = input()
    if dados[ataque][0] == 'fisico':
        if vez == 1:
            if jogador01['SU'][0] == 'AT':
                up = jogador01['ATK'] * jogador01['SU'][1]
                jogador01['ATK'] += up 
            if jogador02['SU'][0] == 'DF':
                bu = jogador02['DEF'] * jogador02['SU'][1]
                jogador02['DEF'] += bu 
                
            dano = 5 * (((jogador01['ATK']/jogador02['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador01['NV'] - jogador02['NV']) * 0.1) + 1)
            jogador02['HP'] -= dano 
            jogador01['HP'] -= jogador01['HP'] * dados[ataque][2]
            
            if jogador01['SU'][0] == 'AT':
                jogador01['ATK'] -= up
                jogador01['SU'] = ['', 0] 
            if jogador02['SU'][0] == 'DF':
                jogador02['DEF'] -= bu
                jogador02['SU'] = ['', 0]
        else:
            if jogador02['SU'][0] == 'AT':
                up = jogador02['ATK'] * jogador02['SU'][1]
                jogador02['ATK'] += up 
            if jogador01['SU'][0] == 'DF':
                bu = jogador01['DEF'] * jogador01['SU'][1]
                jogador01['DEF'] += up 
                
            dano = 5 * (((jogador02['ATK']/jogador01['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador02['NV'] - jogador01['NV']) * 0.1) + 1)
            jogador01['HP'] -= dano 
            jogador02['HP'] -= jogador02['HP'] * dados[ataque][2]
            
            if jogador02['SU'][0] == 'AT':
                jogador02['ATK'] -= up 
                jogador02['SU'] = ['', 0]
            if jogador01['SU'][0] == 'DF':
                jogador01['DEF'] -= bu
                jogador01['SU'] = ['', 0]
    if 'magico' in dados[ataque][0]:
        if vez == 1:
            if jogador01['MP'] >= dados[ataque][3]:
                if jogador02['SU'][0] == 'DF':
                    up = jogador02['DEF'] * jogador02['SU'][1]
                    jogador02['DEF'] += up
                    
                dano = 5 * (((jogador01['MG']/jogador02['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador01['NV'] - jogador02['NV']) * 0.1) + 1)
                jogador02['HP'] -= dano
                jogador01['MP'] -= dados[ataque][3] 
                
                if jogador02['SU'][0] == 'DF':
                    jogador02['DEF'] -= up
                    jogador02['SU'] = ['', 0]
        else:
            if jogador02['MP'] >= dados[ataque][3]:
                if jogador01['SU'][0] == 'DF':
                    up = jogador01['DEF'] * jogador01['SU'][1]
                    jogador01['DEF'] += up
                    
                dano = 5 * (((jogador02['MG']/jogador01['DEF']) * dados[ataque][1]) ** 0.5) * (((jogador02['NV'] - jogador01['NV']) * 0.1) + 1)
                jogador01['HP'] -= dano 
                jogador02['MP'] -= dados[ataque][3]
                
                if jogador01['SU'][0] == 'DF':
                    jogador01['DEF'] -= up
                    jogador01['SU'] = ['', 0]
    if dados[ataque][0] == 'suporte':
        if vez == 1:
            if jogador01['MP'] >= dados[ataque][3]:
                if ataque == 'Tarukaja':
                    jogador01['SU'] = ['AT', 0.25]
                elif ataque == 'Rakukaja':
                    jogador01['SU'] = ['DF', 0.25]
                elif ataque == 'Tarunda':
                    jogador02['SU'] = ['AT', -0.25]
                else:
                    jogador02['SU'] = ['DF', -0.25]
                jogador01['MP'] -= dados[ataque][3] 
        else:
            if jogador02['MP'] >= dados[ataque][3]:
                if ataque == 'Tarukaja':
                    jogador02['SU'] = ['AT', 0.25]
                elif ataque == 'Rakukaja':
                    jogador02['SU'] = ['DF', 0.25]
                elif ataque == 'Tarunda':
                    jogador01['SU'] = ['AT', -0.25]
                else:
                    jogador01['SU'] = ['DF', -0.25]
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
