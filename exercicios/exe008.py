num = int(input('Digite um valor em metros '))
print('A medida de {}m correspode a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f} mm'
.format(num,num/1000,num/100,num/10, num*10,num*100,num*1000))