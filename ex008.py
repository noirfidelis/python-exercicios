#Conversor de Medidas
dist = float(input('Uma distância em metros:'))
#KmHmDAmMmDmCmMm -  ca ga da menino deve comer muitamerda
print(f'A medida de {dist} corresponde a')
km = dist / 1000
print(f'{km}km')
hm = dist / 100
print(f'{hm}hm')
dam = dist / 10
print(f'{dam}dam')
dm = dist * 10
print(f'{dm:.0f}dm')
cm = dist * 100
print(f'{cm:.0f}cm')
mm = dist * 1000
print(f'{mm:.0f}mm')