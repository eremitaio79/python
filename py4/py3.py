"""
Leia a idade do usuário e classifique-o em:
– Criança – 0 a 12 anos
– Adolescente – 13 a 17 anos
– Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
"""
idade = int(input('Entre a idade: '))

if 0 <= idade <= 12:
    print('Criança')
else:
    if 12 < idade <= 18:
        print('Adolescente')
    else:
        if idade > 17:
            print('Adulto')
        else:
            print('Idade inválida.')

"""
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; 
passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, 
reprovado ou pegou exame
– Se a média for maior ou igual 0.0 e menor ou igual 4.0, o aluno está reprovado
– Se a média for maior que 4.0 e menor do que 6.0, o aluno pegou exame
– Se a média for maior ou igual a 6.0, o aluno está aprovado
– Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
"""
