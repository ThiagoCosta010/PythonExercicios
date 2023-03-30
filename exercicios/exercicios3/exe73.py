times = ('Celtics', 'Bucks', '76ers', 'Cavs', 'Nets',
         'Knicks', 'Heat', 'Hawks', 'Raptors', 'Wizards',
         'Bulls', 'Pacers', 'Magic', 'Hornets', 'Pistons')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados {times[0:5]}')
print('-=' * 15)
print(f'Últimos 4 colocados {times[-4:]}')
print('-=' * 15)
print(f'Em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'Em que posição está o Nets ? {times.index("Nets")+1}')
print('-=' * 15)
