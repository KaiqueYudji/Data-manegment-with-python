""" O que a função json.loads faz? \

 A função json.loads é responsável por converter uma string no formato json em um oobjeto python correspondente, como um dicionário, lista, inteiro, etc...
 Mas você pode pensar, como o json.loads converte um json em uma lista?? A resposta é: Arquivos json podem armazenas uma lista de objetos json, isso é muito comum. 
 Neste caso, a função json.loads iria converter esta lista de objetos json para uma lista de dicionários. 
 Se um campo do meu objeto json guarda um número json, o json.loads converte para um valor do tipo int, e assim por diante... Esta função sempre vai converter
 uma string json pra os tipos de dados equivalentes em python

 """


import json

def generating_qty_total_of_characters():

    qty_male_characters = 0
    qty_female_characters = 0
    qty_undefined_gender = 0

    json_to_dict = []

    with open("star_wars.json") as json_file:
       json_file = json_file.read()
       json_to_dict = json.loads(json_file); """ Este json loads converte uma array de objetos json em uma lista de dicionário python """

      
    for character in json_to_dict:
           print(f"This is the character's name:{character['name']}\nAnd this is the character's gender:{character['gender']}\n") 

           if(character['gender'] == 'male'):
               qty_male_characters+=1
           elif(character['gender'] == 'female'):
               qty_female_characters+=1
           else:
               qty_undefined_gender+=1 


    print(f"The total number of male characters is: {qty_male_characters}\nThe total number of female characters is: {qty_female_characters}\nThe total number of n/a characters is: {qty_undefined_gender}")
               

    


generating_qty_total_of_characters() 