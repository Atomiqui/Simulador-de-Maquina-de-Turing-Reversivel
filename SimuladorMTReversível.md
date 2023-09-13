#  Simulador de Máquina de Turing Reversível

### Objetivo:
* Entender o artigo Logical Reversibility of Computation de C. H. Bennett, disponível nesse [link](https://www.dna.caltech.edu/courses/cs191/paperscs191/bennett1973.pdf).

* Construir uma Máquina de Turing (MT) reversível a partir das transições de uma MT ordinária.

* Simular as transições da MT feita a partir da construção e a sua reversão.

### Desenvolvimento:

Escolhemos Python como linguagem de programação, visando suas vantagens em relação a versatilidade.

Para realizar esse trabalho será necessária uma sequência lógica de ações:
* Ler o arquivo que contém a MT ordinária:
    * Abrir o arquivo da maneira solicitada;
    * Identificar as informações contidas em cada linha;
    * Extrair os dados de cada linha e armazenar de maneira organizada.

* (opcional) Confirmação de que as informações foram lidas corretamente;
    * Pode ser um print do que foi lido.

* Com as informações armazenadas, transformar as quintuplas nas quadruplas da MT Reversível;
    * Extrair as informações de uma transição;
    * Armazenar de maniera organizada ou retornar;
    * Usar as informações sobre cada transição quintupla para construir as transições quadruplas;

* Simular as transições:
    * Começa com um estado, um marcador de cabeça na fita e uma entrada;
    * A função percorre as quadruplas executando as transições até atingir um estado final.

* Printar um resultado para mostrar que funciona a simulação;

* Faz o reverse:
    * Desfaz o movimento da cabeça da fita realizado durante a simulação.

* Printar novamente para mostrar que é Reversível.