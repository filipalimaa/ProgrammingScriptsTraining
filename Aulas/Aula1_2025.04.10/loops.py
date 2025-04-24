# ESTRUTURA DE CONTROLE - LOOPS
# Servem para repetir o mesmo bloco de codigo um numero de vezes

# TIPOS D EESTRUTURA DE LOOPS:
    # while - repete enquanto uma condição for verdadeira
    # for - repete um bloco de codigo numa sequencia limitada (lista, intervalo)
    # do while - garante que pelo menos 1 vez o codigo é executado    
    
""" for numero in range(1, 6):  # range(1, 6) gera 1, 2, 3, 4, 5
    print(f"Número: {numero}")     """
    
# Contagem regressiva
contador = 5
while contador > 0:
    print(f"Contagem: {contador}")
    contador -= 1  # Diminui 1 a cada iteração
print("Fim!")    