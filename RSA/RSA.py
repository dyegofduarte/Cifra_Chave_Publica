### SIMPLIFICAÇÃO DO PROCESSO DE RSA
## Simula a escolha de chaves Pública e Privada do usuário exemplificdo por Bob, depois simula uma mensagem criptografada do usuário Alice usando a chave pública de Bob, e por fim o usuário Bob descriptogrfa a mensagem usando sua chave privada

import random, math
from sympy import mod_inverse       # Necessário instalar o módulo "sympy" com o "pip install sympy"

# função para calcular o MMC
def calcular_mmc(a, b):
    return abs(a * b) // math.gcd(a, b)

# função para calcular o MDC
def calcular_mdc(a, b):
    return math.gcd(a, b)


# As variaveis "Primo1" e "Primo2" de Bob
Primo1 = int(input("Digite um número Primo para Bob: "))
Primo2 = int(input("Digite outro número Primo para Bob: "))

# Computa o móduloN, parte da chave pública
modN = Primo1 * Primo2 

# Computa o φ(móduloN), mantido secreto
modN2 = (Primo1 - 1) * (Primo2 - 1)


# Obtem "ex" e testa por MMC
#ex = random.randint(1, (modN2-1))    # função seleciona valor entre 1 e (modN2-1), inclusive, o menos 1 garante que satisfaça  (1 < e < φ(n))
ex = int(input("Digite valor para a várialvel E selecionada de Bob: "))

# Testa se "ex" e "φ(n)" são co-primos, se sim obtem a primeira parte da chave pública e assume "modN" como segunda parte
MDC = calcular_mdc(ex, modN2)
if (MDC == 1):
    # Determina a chave Pública de Bob
    Bob_PU1 = ex
    Bob_PU2 = modN

# Determinar dx
#dx = pow(ex, -1) % modN2
#if (pow(ex, -1) < 0):
dx = mod_inverse(ex, modN2)

# Determina a chave Privada de Bob
Bob_PRIV1 = dx
Bob_PRIV2 = modN

"""
Não estou conseguindo determinar o d

Determinar d = e−1 (mod λ(n)) = 1 mod 96
⚫ d é o inverso multiplicativo modular de e
módulo λ(n)
⚫ Resolver para d a equação d⋅e ≡ 1 (mod λ(n))
⚫ d mantido secreto como parte do expoente
da chave secreta

https://moodle.ufrgs.br/pluginfile.php/7158349/mod_resource/content/0/jcnobre-seg-aula10b.pdf
Slide 5
não bate o inverso multiplicativo de 37 é aproximadamente 0.027
(0.027 mod 96) da um numero abaixo de 0.027 também, da onde que saiu aquele 13 

Meus caulculos deram o resultado abaixo:
e-1 mod (p–1).(q–1) = 6597
(3533-1) mod (100).(112) = 6597
(3533-1) mod  11200 = 6597
"""


print(f"A Chave Pública de Bob é ({Bob_PU1}, {Bob_PU2})")
print(f"A Chave Privada de Bob é: ({Bob_PRIV1}, {Bob_PRIV2})")

#print(f"A Chave Pública de Bob é: ({ex}, {modN})")
#print(f"A Chave Privada de Bob é: ({dx}, {modN})")

# Alice vai enviar uma mensagem para Bob
Alice = int(input("Digite um número para representar a mensagem de Alice para Bob: "))

# Alice computa a sua mensagem usando a chave pública de Bob 
MAlice = (Alice ** Bob_PU1) % modN

print(f"A mensagem que a Alice vai enviar para Bob e {MAlice}")

# Bob Computa mensagem recebida de Alice usando sua chave Privada
MAlice_Bob = (MAlice ** Bob_PRIV1) % modN

# A mensagem de Alice recebida por Bob é 
print(f"A mensagem de Alice recebida por Bob é {MAlice_Bob}")
