#  - Imports:
import random

#  - Code:

UpperCase = chr(random.randint(65, 90)) # Gerando letras maiusculas;

LowerCase = chr(random.randint(97, 122)) # Gerando letras minusculas;

Special = chr(64) # Gerando um caractere especial;
list_numbers = []

for i in range(5):
  numbers = random.randrange(9)
  list_numbers.append(numbers)

random.shuffle(list_numbers) # Embaralhando os numeros(toque final);


list_numbers = str(list_numbers) [1:-1] # Tirando os colchetes;

list_numbers = list_numbers.replace(',', '') # Tirando as virgulas;

print(Special, UpperCase, LowerCase, list_numbers)