# Regular Expressions -- RegEx
import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# passando o padrao
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

# procurando padrao em uma frase
# Se encontrar retorna o objeto Match
# Se nao encontrar retornar NONE
busca = padrao.search(endereco) # Objeto Match

if busca:
    cep = busca.group()
    print(cep)