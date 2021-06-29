import re

url = 'www.bytebank.com.br/cambio'
padrao_url =  re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL nao é valida")

print("A URL é valida!")