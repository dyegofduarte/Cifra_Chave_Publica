from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Gerar parâmetros DH
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Gerar chaves privadas
private_key_A = parameters.generate_private_key()
private_key_B = parameters.generate_private_key()

# Gerar chaves públicas
public_key_A = private_key_A.public_key()
public_key_B = private_key_B.public_key()

# Compartilhar chaves públicas e gerar chave compartilhada
shared_key_A = private_key_A.exchange(public_key_B)
shared_key_B = private_key_B.exchange(public_key_A)

# Verificar se as chaves compartilhadas são iguais
assert shared_key_A == shared_key_B


print("Chave compartilhada salva no arquivo Chave_Compartilhada.pem")
with open("Chave_Compartilhada.pem", 'w') as arquivo_saida:
        arquivo_saida.write(shared_key_A)


print("Chave privada A salva no arquivo Chave_Privada-A.pem")
with open("Chave_Privada-A.pem", 'w') as arquivo_saida:
        arquivo_saida.write(private_key_A)


print("Chave privada B salva no arquivo Chave_Privada-B.pem")
with open("Chave_Privada-A.pem", 'w') as arquivo_saida:
        arquivo_saida.write(private_key_B)

print("Chave publica A salva no arquivo Chave_Publica-A.pub")
with open("Chave_Publica-A.pub", 'w') as arquivo_saida:
        arquivo_saida.write(public_key_A)

print("Chave publica B salva no arquivo Chave_Publica-B.pub")
with open("Chave_Publica-B.pub", 'w') as arquivo_saida:
        arquivo_saida.write(public_key_B)