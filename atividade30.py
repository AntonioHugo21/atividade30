# crie uma funcao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def calculo_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

def verificaçao_media(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

nota1 = float(input('Digite a sua 1 nota: '))
nota2 = float(input('Digite a sua 2 nota: '))
nota3 = float(input('Digite a sua 3 nota: '))

resultado_media = calculo_media(nota1, nota2, nota3)
print(resultado_media)

resultado_final = verificaçao_media(resultado_media)
print(resultado_final)