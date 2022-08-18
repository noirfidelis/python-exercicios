#Conversor de moedas
d = float(input('Tem quanto de grana ai? R$'))
dollar = d / 5.17
euro = d / 5.25
libra = d / 6.24
iene = d / 0.038
bitcoin = d / 121.489 #misericórdia
print(f'Com R$ {d:.2f} da pra você comprar:')
print(f'US$ {dollar:.2f}')
print(f'€ {euro:.2f}')
print(f'£ {libra:.2f}')
print(f'¥ {iene:.2f}')
print(f'₿ {bitcoin}')