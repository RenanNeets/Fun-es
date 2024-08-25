"""

#Cria uma função
def Print():
    #Define o que a função vai fazer
    print(1)
#Chama ela
Print()

"""
"""

#Função só vai funcionar com os parâmetros inseridos
#-----------(argumento)---"parâmetro"
def imprimir(a,b,c):
    print(a,b,c)
imprimir(1,2,3)
def saudacao(nome='Sem nome'):
    print(f"Olá, {nome}")
saudacao("1")
saudacao()
"""

"""
def soma(x=None,y=None, z=None):
    #print(f'{x=}+ y={y}','|', 'x+y =',x+y)
    if z is not None:
        print('Com Z')
        print(x+y+z)
    else:
        print('Sem Z')
        print(x+y)
soma(1,2)
soma(5,6,9)
"""
"""
x=2
y= 4
def escopo():
    #global x
    x=1
    def outra_funcao():
        y=2
        print(x+y)
    outra_funcao()
    print(x)
escopo()
print(x, y)
escopo()
"""
"""
def soma(x,y):
    return x+y
soma1=soma(2,2)
soma2=soma(3,3)
#print(soma1+soma2)
#Empacotador de argumentos
def somador(*args):
    total=0
    for numero in args:
        total+= numero
    return total
somador_1 = somador(1,2,3,4,5,6)
print(somador_1)
#Usando um pack de numeros
#      *args -> Empacota um conjunto de numeros
def sub(args):
    total=0
    for numero in args:
        total-= numero
    return total
numeros = 1,2,3,4,5,6
print(sub(numeros))
"""
# Higher Order Functions
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)
def soma(x,y):
    return x+y
v = executa(saudacao, 'Bom Dia', 'Nome')
b = executa(soma, 1, 2)
print(v)
print(b)
#Closure

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar
"""
s1 = criar_saudacao('Bom dia' )
s2 = criar_saudacao('Boa noite' )
#Vai entregar a rota onde guardou os arg da função1
print(s1) 
print(s2)
#Vai entregar o resultado da função 2
#Aqui ocorre o Closure
print(s1('Luiz')) 
print(s2('Bruno'))
"""
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')
for nome in ['Maria', 'Joana']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))