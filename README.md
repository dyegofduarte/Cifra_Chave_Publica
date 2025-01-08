# Cifra_Chave_Publica
UFRGS | Computer Systems Security | Criptografia de Chave Pública


- Criei um script para Diffie-Helman chamado **DH.py** e um para RSA chamado **RSA.py**

- Nos exemplos simulei a comunicação entre os pseudônimos **Alice** e **Bob**

- Diffie-Helman: <br>
    •	Ao executar o script DH.py, é solicitado um número primo acordado e público para Alice e Bob <br>
    •	Depois é solicitado um número base também público <br>
    •	Depois é solicitado um número secreto para Alice e outro para Bob <br>
    •	Com base nos valores tanto públicos quanto secretos, é aplicado as fórmulas descritas nos slides, e como saída retorna a chave compartilhada por Alice e Bob usada para a comunicação <br>

- RSA: <br>
    •	Ao executar o script RSA.py, são solicitados dois números primos para Bob <br>
    •	Depois é solicitado um valor para a variável E de Bob <br>
    •	Com base nos 2 números primos de Bob mais a variável E, o script retorna os valores de chave pública e privada de Bob <br>
    •	Por último, o script solicita um valor para representar uma mensagem que Alice cifra e com a chave pública de Bob <br>
    •	A mensagem é decifrada com a chave privada de Bob e retorna o valor da mensagem que Alice enviou <br>
