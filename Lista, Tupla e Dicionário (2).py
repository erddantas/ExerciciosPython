#!/usr/bin/env python
# coding: utf-8

# # Listas em Python
# 
# --> É uma estrutura de dados mais básica em Python
# 
# --> Sequência de objetos, uma coleção ordenada
# 
# --> Os elementos são separados por , e os elementos de uma lista são envolvidos por **[ ]**
# 
# --> Pode ter uma lista dentro de outras
# 
# --> Podemos alterar as listas
# 
# **DICAS:**
# 
# --> A função `len` retorna o comprimento da uma lista ( a qtd de elementos em uma lista)
# 
# --> Se usarmos a função `sum` soma os elementos da lista.
# 
#         Ex: sum(lst_1) --> Soma é 6, pq 1+2+3
#         
# --> O operador in serve para verificar a assiciação á lista.
# 
#         Ex: 1 in lst_1 ou
#         
#             1 in [1,2,3]
#             
# --> Contatenar listas:`extend` -> Juntas as listas e faz uma alteração na lista inicial
# 
#                               `+`-> Não quer modificar a lista, quer criar uma outra lista com os valores da 1 e outros valores
#                               
# --> Anexar itens pontuais a lista: `append`

# In[17]:


# Elementos de uma lista não precisam ser  do mesmo tipo 
lst_1 = [1, 2, 3]   
lst_2 = [1, 2, 3.0]
lst_3 = [1, 2, '3']
lst_chars = ['a', 'b', 'c']

# Criando uma lista elementos
lst_n = list(range(10))   # <-- IMPORTANTE: O range significa que vai criar uma lista com 10 elementos, mas em Python a lista começa com 0
lst_comp = [i for i in range(10)]

assert lst_n == lst_comp  # <-- ASSERT: É uma verificação em tempo de execução de uma condição, Se a condição escrita não for verdadeira, uma exceção acontece e o programa para.

print(lst_n)


# In[6]:


## Discutir acesso aos elementos
print(lst_1[0])          # <-- Está trazendo o PRIMEIRO elemento da lista 1 
print(lst_1[2])          # <-- Está trazendo o TERCEIRO elemento da lista 1

"""IMPORTANTE: Se no caso da lst_1, se colocarmos print(lst_1[3]), vai dar erro pq nessa lista existe apenas 3 elementos, não 4 como informado"""

try:                     # <-- IMPORTANTE: A função do try/ except é testar pontos criticos do código, lugares aonde há grande possibilidade de erro.
    lst_1[3]             # <-- O código está falando para tentar pegar o 4 elemento da lista 1
except Exception as e:   # <-- O cógigo está falando que caso não consiga trazer o elemento, a exceção é Exception e apelidou de e
    print(e)             # <-- Caso a excecção for verdade: imprimir e que nesse caso é "list index out of range"

print(lst_1[-1])         # <-- "Pythonic" para trazer ÚLTIMO elemento
print(lst_1[-3])         # <-- "Pythonic" para trazer PRIMEIRO elemento

try:                     # <-- Mesma coisa que o try / except anterior, porém de trás para frente agora
    lst_1[-4]
except Exception as e:
    print(e)          


# In[7]:


# Repartindo as listas
print(lst_n[3:9])        #<-- Pedindo para imprimir os elementos a partir do 4 até o 9 elemento
print(lst_n[3:])         #<-- Pedindo para imprimir os elementos a partir do 4 até o final da lista
print(lst_n[:9])         #<-- Pedindo para imprimir todos os elementos até o 9
print(lst_n[3:9:2])      #<-- 
print(lst_n[::2])        #<-- Trazer os elementos de dois em dois


# -------------------------
# Notem a sintaxe de acesso:
# 
# `lst_n` é o nome da variável
# 
# Ele é seguido de alguma "instrução entre colchetes"
# 
# `var_name [ código ]`

# In[12]:


# exemplo exotérico

"""O Pyhton nesses casos ele responde como bouleans, então ele responde 0 = Falso e 1 = Verdadeiro."""
print(lst_chars[5 > 3])  #<-- Nesse caso, estamos pendindo para imprimir com os valores da lista lst_chras, se 5 é maior que 3. A resposta é b pelo fato desse valor ser o elemento 1 da lista, que significa verdadeiro



# In[13]:


## discutir types

def print_lst_types(lst):
    """ Vai na lista que queremos, e vê o TIPO de elemento dessa lista e imprimi o TIPO DE CADA ELEMENTO (int, float...)"""
    for element in lst: 
        print(type(element))

def print_lst_elements(lst):
    """Vai na lista que queremos e IMPRIME O ELEMENTO (Os valores dentro da lista)"""
    for element in lst:
        print(element)


# In[14]:


print_lst_types(lst_2)  #<-- Imprimindo o tipo de cada elemento da lista2


# In[20]:


print_lst_types(lst_3) #<-- Imprimindo o tipo de cada elemento da lista3


# In[15]:


print(type(lst_3))    #<-- Imprimi se a classe, se é tupla, lista ....


# In[8]:


print_lst_elements(lst_3) #<-- Imprimindo o elemento da lista3


# # Tuplas
# 
# --> São primas ***imutáveis*** das listas
# 
# --> Quase tudo que se faz em uma lista, que NÃO envolva modificar, você pode fazer em uma tupla
# 
# --> Usamos ***( )*** em tuplas

# In[26]:


tup_1 = (1,2,3)  
tup_2 = (1,2,'3') # <-- Os elementos não precisam ser do mesmo tipo


# In[10]:


print(tup_1[0])


# In[24]:


lst_1[0] = 25 #--> Você pode alterar o valor de uma lista
print(lst_1)


# In[23]:


tup_1[0] = 25 #--> Você não consegue alterar o valor de uma tupla, da erro


# In[27]:


s = "parangaricotirimirruaru"

print(s[11]) # <-- Imprimir o valor 11 da tupla


# In[28]:


s[11] = 'x' # <-- Não consegue alterar o valor da tupla


# # Dicionários em Python
# 
# --> Associa valores com chaves e permite que você recupere o valor correspondente de uma dada chave
# 
#             Ex: Lista telefonica 
# 
# --> ***Chave:***Qualquer valor imutavel
# 
#             Ex: Nome do contato
#            
# --> ***Valor:*** Qualquer objeto de dados
# 
#             Ex: Número do telefone
#             
#             
# --> Usamos ***{ }*** em dicionários
# 

# In[30]:


dict_str_int = {'um': 1, 'dois': 2, 'três': 1} #<-- O 1 é a chave, depois é o valor
dict_int_str = {1: 'um', 2: 'dois', 3: 'um'}

dict_compr = {str(i): i for i in range(10)}


# In[31]:


dict_doidao = {
    True: False,
    (1,2,3): 4,
    (0,False, None): [],
    "string": "string",
    3.3: 6.6
}


# In[32]:


print(dict_int_str[5-3]) #<-- A chave é um número, e o resultado da conta é a chave e atrelado a essa chave tem um valor que é o dois
print(dict_int_str[10//5])


# In[33]:


dict_doidao[5 == 5] #<-- A chave é o true, mas o valor associado a essa chave é false, por isso o resultado


# In[19]:


dict_doidao['lista'] = lst_1

dict_doidao['lista'][0] # o mesmo que (dict_doidao['lista'])[0] E que lst_1[0]


# In[20]:


dir(list) # <-- Mostra o que dá pra fazer com lista...


# In[35]:


def dir_condensed(x):  #<-- Função pra tirar as infos com __ e traz as ações que podemos fazer com a tupla
    for string in dir(x):
        if not string.startswith("__"):
            print(string)

dir_condensed(tup_1)


# In[36]:


help(lst_1.append) #<-- Traz o que a função append faz, documentação


# # Exercício

# In[73]:


def funcao(lst, num):
    """Função recebe uma lista e um número e devolve uma dupla de listas..."""
    
    assert type(lst) == type([]), "first param must be a list"
    
    out = {True: [], False: []}
    for element in lst:
        out[ element <= num ].append(element)
        
    return out[True], out[False]


# In[74]:


def funcao(lst, num):
    """Função recebe uma lista e um número e devolve uma dupla de listas..."""
    
    assert type(lst) == type([]), "first param must be a list"
    
    out = {True: [], False: []}
    for element in lst:
        out[ element <= num ].append(element)
        
    return out[True], out[False]


#  - **0**. Dada a função `funcao` acima, escreva uma docstring descritiva. Aproveite pra renomear e dar um nome descritivo.
#  - **Aleph**. Utilize a função, ou apenas se inspire nela, e escreva uma função `quick_sort`, que ordena uma lista numérica.
#  - **A**. Critique a função `funcao`. O que ela tem de bom? O que ela tem de ruim?

# # Resolução Exercício

# In[85]:


lst = [2,1,4,5]
num = 4
print(type(lst))


# In[87]:


def mod_lst(lst, num): #<-- Mod: Modify e lst: List
    """Função recebe uma lista e um número e devolve uma dupla de listas..."""
                                     # Tipo um if com exception
    assert type(lst) == type([]),"s" #<-- assert, serve para validar a função.Se a condição escrita não for verdadeira, uma exceção acontece e o programa para
                                 
    out = {True: [], False: []}  # <-- Um dicionário que dependendo da resposta anterior, vai mostrar uma lista
    for element in lst:                        
        out[ element <= num ].append(element) # <-- Se o elemento da lista foi menor que o numero informado a função vai atualizar a lista
                                              # <-- Dependedo da chave que for a saída, true ou false, o valor, lista dessa chave, va entrar na frente da lista lst e as duas listas serão contatenadas, por causa do append a lst original será alterada
        
    return out[True], out[False] #<-- Será criado uma nova lista, onde dentro dela existe sub- listas, a lista do dicionário junto com a lst e depois a lista do false
mod_lst(lst,num)  #<-- Mostrar o resultado da função


# In[88]:


x = mod_lst


# In[89]:


x(lst,num)


# In[90]:


dict_doidao = {"o meu deus":mod_lst} # <--O valor de um dicionario pode ser um valor


# In[92]:


dict_doidao ["o meu deus"] (lst,num) #<-- Estamos chamando o dicionário, a chave o meu deus e os dados de entrada que deve ser utilizado no código,


# In[ ]:




