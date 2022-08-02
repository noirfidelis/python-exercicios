#Conversor de Moedas
d = float(input('Tem quanto de grana ai? R$'))
dollar = d / 5.28
euro = d / 5.37
libra = d / 6.43
iene = d / 0.040
bitcoin = d / 121.466 #misericórdia
print(f'Com R$ {d:.2f} da pra você comprar:')
print(f'US$ {dollar:.2f}')
print(f'€ {euro:.2f}')
print(f'£ {libra:.2f}')
print(f'¥ {iene:.2f}')
print(f'₿ {bitcoin}')