Um dia extra é adicionado ao calendário quase a cada quatro anos como 29 de fevereiro, e esse dia é chamado de ano bissexto. Ele corrige o calendário porque o nosso planeta leva aproximadamente 365,25 dias para orbitar o Sol. Um ano bissexto contém esse dia extra.

No calendário Gregoriano, três condições são usadas para identificar anos bissextos:

• O ano pode ser dividido por 4? Então é bissexto, a menos que:
 • O ano também possa ser dividido por 100. Nesse caso, não é bissexto, a menos que:
  • O ano também seja divisível por 400. Se for, aí sim ele é bissexto.

Isso significa que, no calendário Gregoriano, os anos 2000 e 2400 são bissextos, enquanto 1800, 1900, 2100, 2200, 2300 e 2500 não são bissextos.

Tarefa

Dado um ano, determine se ele é bissexto.
Se for bissexto, retorne o Booleano True, caso contrário retorne False.

O código fornecido lê um valor da entrada padrão (STDIN) e envia esse valor para a função is_leap. Você só precisa completar essa função.

Formato de Entrada

Leia year, o ano a ser testado.

Restrições

1900 ≤ year ≤ 10⁵

Formato de Saída

A função deve retornar um valor Booleano (True/False).
A saída será tratada pelo código base fornecido.

Exemplo de Entrada

1990

Exemplo de Saída

False

Explicação

1990 não é múltiplo de 4, portanto não é um ano bissexto.