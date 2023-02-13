tabu = int(input('Quer ver a tabuada de qual valor ? '))
c = 1
while tabu > 0:
    print(f'{tabu} X {c} = {tabu*c}')
    c += 1
    if c == 11:
        c = 1
        tabu = int(input('Quer ver a tabuada de qual valor ? '))
print('fim')
