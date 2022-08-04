#Reajuste Salarial
sal = float(input('Qual é o salário do funcionário? R$'))
aumento = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R$ {sal}, com 15% de aumento, passa a receeber R$ {aumento:.2f}')