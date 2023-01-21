def concatenacao(palavra1, palavra2):
    return palavra1 + ' ' + palavra2

def entrada_usuario():
    palavra1 = str(input('Digite a primeira palavra: '))
    palavra2 = str(input('Digite a segunda palavra: '))
    return concatenacao(palavra1, palavra2)

print(entrada_usuario())
