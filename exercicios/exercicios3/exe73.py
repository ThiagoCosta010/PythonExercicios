times = ('Celtics', 'Bucks', '76ers', 'Cavs', 'Nets',
         'Knicks', 'Heat', 'Hawks', 'Raptors', 'Wizards',
         'Bulls', 'Pacers', 'Magic', 'Hornets', 'Pistons')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados {times[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados {times[-4]}')
print('-=' * 15)
print(f'Os times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na posiçao {times.index("Heat")+1}ª')
print('-=' * 15)
