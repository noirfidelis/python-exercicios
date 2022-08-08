#Aumentos múltiplos
#salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    aumento = sal + (sal * 15 / 100)
    print(f'Quem ganhava R$ {sal:.2f} passa a receber R$ {aumento:.2f} agora.')
else:
    aumento2 = sal + (sal * 10 / 100)
    print(f'Quem ganhava R$ {sal:.2f} passa a receber R$ {aumento2:.2f} agora.')