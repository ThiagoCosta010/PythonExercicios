s1 = float(input('Primeiro segmento '))
s2 = float(input('Segundo segmento '))
s3 = float(input('Terceiro segmento '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos formam um triângulo')
    if s1 == s2 == s3:
        print('Lados iguais formam o Equilátero')
    elif  s1 != s2 != s3 != s1:
        print('Lados diferentes formam o Escaleno')
    else:
        print('Dois lados iguais formam o Isósceles')
else:
    print('Os segmentos não formam um triângulo')