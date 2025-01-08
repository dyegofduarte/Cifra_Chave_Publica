### SIMPLIFICAÇÃO DO PROCESSO DE DIFFIE-HELMAN
import random

# As variaveis "Primo" e "Base" são públicas e acordadas entre Alice e Bob
Primo = int(input("Digite um número Primo Público para Alice e Bob: "))
Base = int(input("Digite um número Base Público para Alice e Bob: "))

print("\n")
### Alice escolhe seu segredo e envia para Bob a computação com seu segredo
# Alice escolhe sua variável segredo "segredoA"
#segredoA = random.randint(0, 100)   # escolhe um número aleatório entre 0 e 100
segredoA = int(input("Digite um número Secreto para Alice: "))

# Alice envia a Bob "ASB"
ASB = (Base ** segredoA) % Primo


### Bob escolhe seu segredo e envia para Alice a computação com seu segredo
# Bob escolhe sua variável segredo "segredoB"
#segredoB = random.randint(0, 100)   # escolhe um número aleatório entre 0 e 100
segredoB = int(input("Digite um número Secreto para Bob: "))

# Bob envia a Bob "BSA"
BSA = (Base ** segredoB) % Primo


# Alice Calcula sua chave compartilhada
sharedA = (BSA ** segredoA) % Primo


# Alice Calcula sua chave compartilhada
sharedB = (ASB ** segredoB) % Primo

print("\n")

# Valida se as chaves compartilhadas de Alice e Bob são iguais
if (sharedA == sharedB):
    print("A chave compartilhada de Alice e Bob é", sharedA)
    
