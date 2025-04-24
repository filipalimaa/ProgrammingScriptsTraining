# ESTRUTURA DE CONTROLO - DECISÕES

# if + variavel + condição + :
     

"""
IF = SE
ELSE IF = ELIF = ENTÃO
ELSE

OPERADORES =  == (igual), != (diferente), <>, <=, >=

# verificar idade de uma pessoa

idade = int(input("Quantos anos tu tens?"))

if idade >= 18:
    print("Tu és maior de idade!)
    
elif idade >= 10:
    print("És uma jovem criança")    
       
else:
    print("Tu es menor de idade")    

"""

idade = int(input("Quantos anos tu tens?"))

if idade >= 18:
    if idade >= 65:
        print("fora do espectro")
    else:
        print("es um adulto")
            
    if idade >= 18 and idade <= 65:
        print("És um adulto")
    else:
         print("fora do espectro")     
         
    if idade <= 65:
        print("És um adulto")
    else:
         print("fora do espectro") 
    
    if idade <= 18 or idade >= 65:
        print("fora do espectro")   
    else:
         print("És um adulto")             
    
    
elif idade >= 10:
    print("És uma jovem criança")    
       
else:
    print("Tu es menor de idade")    



# funções 
#def nomeFuncao():
    