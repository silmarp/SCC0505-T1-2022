<h1 align="center">SCC505</h1>
<h1 align="center">Introdução à teoria da computação</h1>


<h3 align="center">Helena Ribeiro Neves | 11200272</h3>
<h3 align="center">Mauricio Hitoshi Murakami | 10295346</h3>
<h3 align="center">Roberto Severo Utagawa | 12690712</h3>
<h3 align="center">Érika Hortência Cardoso | 10696830</h3>
<h3 align="center">Silmar Pereira da Silva Junior | 12623950</h3>

<br>
<br>

## 1 Quanto a solução :
### 1.1 Linguagem, tecnicas ultilizadas e outros aspectos:
Para esse projeto foi escolhido a linguagem de programação python, juntamente ao paradgima de programação orientada a objetos (POO) e foram usadas tecnicas como recursividade e list comprehension durante a criação do projeto.
Essa solução funciona para automatos finitos deterministicos (AFDs) e não deterministicos (AFNs) sendo o melhor caso posivel com deterministicos (abordaremos o motivo na seção 3.1)
Ademais, referente a aquitetura do projeto toda a parte de construção dos automatos e suas capacidades foi separada do arquivo principal, tal escolha trará algumas vantagens como veremos na seção 2.2.
### 1.2 Vantagens e desvantagens:
A escolha de uma linguagem de alto nivel como python para o projeto foi devido a facilidade que a linguagem proporciona para escrever o codigo, sendo dinamicamente tipada e com diversas abstrações para facilitar esse processo, além de aumentar a velocidade com que se escreve, pelo mesmo motivo.
Já o paradigma de POO fornece uma melhor organização e portanto facilidade para entender o projeto a partir do momento em que se tem certa familiaridade com tal paradigma. Outra vantagem estará na capacidade de escalar o projeto pois a organização e estrutura reforçadas pelo POO facilitam nesse processo.
## 2 Quanto ao codigo fonte:
### 2.1 Estrutura:
Todo o codigo fonte do programa esta presente na pasta "src/", na pasta em questão o programa é dividido em um arquivo principal "main.py", um arquivo de testes unitarios "tests.py" e uma pasta com 3 aquivos "*.py" que juntos representam o automato, suas propriedades e funções.
Essa estrutura foi usada pois o intuito do grupo era usar o automato como um modulo isolado, ao invez de definir e usar no mesmo arquivo, portanto não há nenhuma definição do automato na main, apenas usos, tal abordagem permite a portabilidade da estrutura automato para outros projetos.
Quanto a execução do codigo em si, tudo começa na main, recebendo um input do usuario com o nome do aquivo contendo as instruções para criação do automato, processando-as e passando como parametros para o construtor da classe Automato

![[Pasted image 20220506181833.png]]

Após receber os parametros para a criação do objeto automato o construtor ira definir os atributos do proprio objeto chamando no processo mais dois construtores com os dados que recebeu.
Esses construtores são das classes Estado e Transição que armazenarão informações sobre esses dois componentes do automato, como no caso do estado se ele é terminal e quais são suas transições e no caso das transições o simbolo terminal dela e seu destino.
![[Pasted image 20220506182945.png]]
![[Pasted image 20220506182959.png]]

### 2.2 Funcionalidade:
Após todo o processo do item anterior teremos por fim o objeto automato, e para o automato realizar sua função e processar cadeias de simbolos ele terá dois métodos, um que recebera a cadeia, chamara uma função recursiva e retornara o resultado. O segundo metodo é a propria função recursiva.

![[Pasted image 20220506183336.png]]

A maneira com que ela funciona é recebendo o estado atual do automato, e a cadeia a ser processada. 
Em caso de o estado possuir uma transição com o primeiro simbolo da cadeia ele irá realizar a transição e consumir o simbolo, passando a nova cadeia e o novo estado para a função recursiva.
Esse processo ira ocorrer até que haja um simbolo a ser processado sem uma transição correspondente (retornando false ou rejeitada) ou estar com a cadeia vazia, nesse momento checa-se se o estado atual é terminal, se não for sera false (rejeitada) se for sera true (ou aceita)

Obs: o algoritimo ira funcionar com AFNs pois testa todos as possiveis transições ao invés de a primeira possivel
### 2.3 Testes e escalabilidade
Como foi mencionado (seção 2.1) junto ao arquivo main, há um arquivo de testes unitários, o motivo do grupo ao criar tal arquivo, além de seguir uma boa praticas de desenvolvimento, é permitir uma melhor esclabilidade do código, caso precisémos adicionar funcionalidades ou corrigir bugs, os testes ajudarão a descobrir se a alteração ou adição de codigo fará outras partes do algoritimo pararem de funcionar.
O teste é realizado seguindo os passos de criar 2 automatos, um AFD e um AFN ultilizando o construtor (seção 2.1) e então passa-los para suas funções e teste respectivas.

Casa função de teste ira usar de uma tupla contendo varias listas de 2 dados, uma cadeia a ser processada (string) e um booleano correspondente, passara a cadeia para a função de processamento de cadeias do automato (seção 2.2) e ira comparar os resultados com o booleano dado.
![[Pasted image 20220506184727.png]]

Somado aos testes, outro fator que favorece a escalabilidade do codigo é a separação da estrutura automato do programa principal (seção 2.1), essa modularidade permitira que o automato seja usado junto a outras bibliotecas e em outros projetos, sem o codigo feito na main para servir proposito apenas a essa situação especifica

## 3 Quanto a complexidade e eficiência:
Para pensarmos sobre o uso/complexidade de memoria do automato devemos revisar o processo de criação do mesmo, como mencionado na seção 2 o automato é criado pelo seu construtor que cria suas variaveis internas e aciona mais 2 construtores o de estados e o de transições, portanto a complexidade de memoria do programa será dependende desses fatores, sendo assim podemos dizer que o algoritimo quanto a memoria será O(a+e+t), sendo a o numero de automatos construidos, e, o numero de estados e t o numero de transições.

Já falando da complexidade de tempo temos as situações extremas do melhor caso e o pior.
No melhor caso seria um AFD em que durante o processamento o algoritimo ira passar procurar nas possiveis transições a correta e ir o proximo estado, sendo assim a complexidade sera dependente do tamanho da cadeia de caracteres e do numero de transições. Desta forma o melhor caso seria O(c+t), sendo c o tamanho da cadeia e t a quantidade de transições.

No pior caso estariamos ultilizando um AFN e portanto durante o processamento ao invez de se ter apenas um caminho possivel teremos varios e portanto será necessario checar todas as possibilidades até encontrar a correta, podendo realizar  mesma transição até t vezes sendo assim a complexidade ficará como O(c+t²).
Uma possivel solução para esse pior caso seria a implementação de multithreading, usando um novo thread toda vez que houver mais de uma possibilidade de transição, assim reduzindo o tempo para algo mais proximo a complexidade do melhor caso, entretanto essa implementação traria seus proprios problemas, como a dificuldade de se lidar com multiplos threads e o limite de threads na maquína, então decidimos deixar para uma futura implementação.