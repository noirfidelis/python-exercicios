#Conversor de Temperatura
temp = float(input('Informe a temperatura em ºC:'))
c = temp * 1.8 + 32#fórmula para converter de celsius para fahrenheit
print(f'A temperatura de {temp}ºC corresponde a {c:.1f}ºF')
temp2 = float(input('Informe a temperatura em ºF:'))
f = (temp2 - 32) / 1.8#fórmula para converter de fahrenheit para celsius
print(f'A temperatura de {temp2}ºF corresponde a {f:.1f}ºC')