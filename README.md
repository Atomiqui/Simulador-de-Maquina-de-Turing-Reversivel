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


### `make_transitions`:

1. **Definição da Função:**
   ```python
   def make_transitions(states, input_symbols, queue_symbols, quadruples, entry):
   ```

   - Esta função recebe cinco argumentos: `states` (uma lista de estados da máquina de Turing), `input_symbols` (uma lista de símbolos que podem aparecer na fita de entrada), `queue_symbols` (uma lista de símbolos que podem ser escritos na fita de entrada), `quadruples` (uma lista de quadruplas que descrevem as transições da máquina de Turing) e `entry` (uma string que representa a entrada inicial da máquina de Turing).

2. **Inicialização de Variáveis:**
   ```python
   state_marker = quadruples[0][0]
   head_marker = 0
   input_tape = list(entry + "B")
   history_tape = []
   output_tape = []
   final_state = quadruples[-1][2]
   ```

   - `state_marker` é inicializado com o primeiro estado das quadruplas.
   - `head_marker` é inicializado com 0, representando a posição inicial da cabeça de leitura/escrita na fita.
   - `input_tape` é uma lista que representa a fita de entrada. A entrada fornecida é concatenada com um símbolo 'B' (indicando o final da entrada) e convertida em uma lista.
   - `history_tape` é uma lista vazia que será usada para manter um registro das transições feitas pela máquina.
   - `output_tape` é uma lista vazia que representará a fita de saída.
   - `final_state` é inicializado com o último estado das quadruplas, que representa o estado final da máquina de Turing.

3. **Execução da Simulação:**
   ```python
   while state_marker != final_state:
   ```

   - O loop continua enquanto o estado atual não é o estado final.

4. **Iteração sobre as Quadruplas:**
   ```python
   nt = 0
   for quadruple in quadruples:
       if state_marker == quadruple[0]:
   ```

   - `nt` é uma variável usada para manter o número de quadrupla atual (índice).
   - A função itera sobre as quadruplas procurando aquelas em que o estado atual (`state_marker`) corresponde ao estado de origem da quadrupla.

5. **Verificação da Condição de Transição:**
   ```python
   if input_tape[head_marker] == quadruple[1]:
   ```

   - Verifica se o símbolo na fita de entrada na posição atual da cabeça de leitura (`head_marker`) é igual ao símbolo de entrada da quadrupla.

6. **Execução da Transição:**
   ```python
   state_marker = quadruple[2]
   if quadruple[3] == "L":
       head_marker -= 1
   elif quadruple[3] == "R":
       head_marker += 1
   else:
       input_tape[head_marker] = quadruple[3]
   history_tape.append(nt)
   ```

   - Atualiza o estado atual (`state_marker`) com o estado de destino da quadrupla.
   - Move a cabeça de leitura/escrita para a esquerda (`L`) ou direita (`R`) ou escreve um novo símbolo na fita, conforme especificado na quadrupla.
   - Registra o número da quadrupla no `history_tape` para manter um registro das transições.

7. **Atualização da Fita de Saída:**
   ```python
   output_tape = copy(input_tape)
   ```

   - Atualiza a fita de saída com uma cópia da fita de entrada atualizada.

8. **Retorno dos Resultados:**
   ```python
   return input_tape, history_tape, output_tape
   ```

   - Retorna três valores: a fita de entrada final, o histórico das transições e a fita de saída final.

No geral, esta função simula a execução de uma máquina de Turing com base nas quadruplas fornecidas e na entrada inicial, mantendo o controle das transições feitas e gerando uma fita de saída como resultado. A máquina de Turing é uma abstração teórica de um modelo de computação que pode realizar cálculos complexos e é uma base importante na teoria da computação.


### `reverse_movement`


1. **Definição da Função:**
   ```python
   def reverse_movement(history_tape, quadruples, input_tape, head_marker):
   ```

   - Esta função recebe quatro argumentos: `history_tape` (uma lista que contém o histórico de transições da máquina de Turing), `quadruples` (uma lista de quadruplas que descrevem as transições da máquina de Turing), `input_tape` (uma lista que representa a fita de entrada da máquina de Turing) e `head_marker` (a posição atual da cabeça de leitura/escrita na fita).

2. **Inicialização de Variáveis:**
   ```python
   i = len(history_tape) - 1
   ```

   - `i` é inicializado com o índice do último elemento na lista `history_tape`. Isso permite percorrer o histórico de transições da máquina de Turing em ordem reversa.

3. **Iteração sobre o Histórico de Transições:**
   ```python
   while i >= 0:
   ```

   - O loop executa enquanto `i` for maior ou igual a 0, ou seja, enquanto houver elementos no histórico para processar.

4. **Obtenção do Nome da Quadrupla a partir do Histórico:**
   ```python
   name = history_tape[i]
   ```

   - `name` é definido como o valor na posição `i` da lista `history_tape`, que representa o número da quadrupla no histórico.

5. **Verificação da Direção da Transição:**
   ```python
   if quadruples[name][3] == "R":
       head_marker -= 1
   elif quadruples[name][3] == "L":
       head_marker += 1
   else:
       input_tape[head_marker] = quadruples[name][1]
   ```

   - Verifica a direção da transição da quadrupla correspondente àquela etapa no histórico.
   - Se a direção for "R" (para a direita), decrementa a posição da cabeça de leitura/escrita (`head_marker`) em 1, movendo a cabeça para a direita.
   - Se a direção for "L" (para a esquerda), incrementa a posição da cabeça de leitura/escrita (`head_marker`) em 1, movendo a cabeça para a esquerda.
   - Se a direção for diferente de "R" ou "L", significa que a quadrupla escreve um novo símbolo na fita, e esse símbolo é armazenado na posição atual da fita de entrada (`input_tape`) indicada por `head_marker`.

6. **Atualização do Índice e Remoção do Histórico:**
   ```python
   i -= 1
   history_tape.pop()
   ```

   - Decrementa o índice `i` para processar a próxima etapa no histórico em ordem reversa.
   - Remove o último elemento da lista `history_tape`, pois ele já foi processado.

Em resumo, a função `reverse_movement` reverte as transições feitas pela máquina de Turing, seguindo o histórico de transições em ordem reversa. Isso permite "desfazer" as ações da máquina e retornar à sua configuração anterior, antes de uma determinada transição ter sido aplicada. Essa função pode ser útil em cenários onde você deseja reverter a máquina de Turing para uma etapa anterior em sua execução.
