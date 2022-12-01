brasileiro = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo',
              'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético MG',
              'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Os cinco primeiros colocados são: {brasileiro[0:5]}')
print(f'Os 4 últimos são: {brasileiro[16:]}')
print(f'Times em ordem alfabética: {sorted(brasileiro)}')
print(f'A Chapecoense está em {brasileiro.index("Chapecoense")+1}ª')
