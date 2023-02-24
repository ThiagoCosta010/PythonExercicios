times = ('Celtics', 'Bucks', '76ers', 'Cavs', 'Nets',
         'Knicks', 'Heat', 'Hawks', 'Raptors', 'Wizards',
         'Bulls', 'Pacers', 'Magic', 'Hornets', 'Pistons')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Bulls")+1}ª posição')
