# Network-Socket
Soquete de rede desenvolvido para a matéria de Redes de Computadores 1.

## Descrição
O cliente envia ao servidor características visuais de cor, formato e tamanho para receber de resposta uma tela 400x400 printada com a figura gerada dentro das informações enviadas. As cores se resumem nas mais simples (azul, vermelho, rosa, verde...).

O formato em três possíveis: 
* quadrado 
* circulo
* triângulo

E o tamanho em: 
* pequeno 
* médio
* grande

## Funcionamento
**Ex:** Com o cliente já conectado ao servidor. Caso se digite “azul”, “quadrado” e “medio”, o cliente receberá como retorno visual uma tela em branco com um quadrado de tamanho médio na tonalidade de azul. Para gerar esse efeito, foi utilizada a biblioteca Pygame no código.

Não são aceitos caracteres em maiúsculo, com acentuação ou com algum outro nome de complemento. Nomes de cores escritos como “Azul”, “AZUL” ou “azul marinho” serão tratados como erro. Igualmente nos nomes disponíveis para formato e tamanho.


## Tipos de Mensagens/Operações

- **Enviado pelo cliente:** String
- **Enviado pelo servidor:** retorno visual


## CÓDIGOS DE ERRO RETORNADOS PELO CLIENTE/SERVIDOR
Caso a conexão não tenha êxito, o cliente retorna o erro de conexão recusada.

_error: [Errno 111] Connection refused_

Para haver retorno do servidor ao cliente, é necessário que as Strings esteja de acordo com o que foi explicado acima em relação a caracteres não aceitos (dígitos em maiúsculo, com palavras a mais ou até mesmo string vazia) é retornado o erro de operação indisponível.

_erro: [Errno 402] Operation unavailable_

