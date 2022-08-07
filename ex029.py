#Radar eletrônico
v = float(input('\033[1;34mQual é a velocidade atual do carro?\033[m'))
# R$7,00 por cada Km acima do limite.
multa = 7 * (v - 80)
if v <= 80:
    print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')
else:
    print('\033[1;31mQUER MORRER? Multado! Você excedeu o limite permitido que é de \033[1;33m80 Km/h!\033[m')
    print(f'\033[1;31mVocê deve pagar uma multa de \033[1;32mR$ {multa:.2f}!')