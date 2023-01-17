lar = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
area = lar*alt
print('Sua parade tem a dimensão de {}X{} e a sua área é de {}m²'.format(lar, alt, area))
print('Para pintar essa parede, você precisara de {:.2f}l de tinta'.format(area/2))