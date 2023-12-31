## Projeto e Analise de Algoritmos 2023.1

Alunos: João Pedro Silva Cunha, Julio Cezar Nolasco, Luiz Fernando Kozak, Willian Dos Santos Alves

Nesse repositorio você encontra o código fonte e um breve relatório (PAA-DivConq.pdf) do estudo feito.

Link para apresentação: https://www.canva.com/design/DAFmY_EjLxc/ox0tWyoiVt3IBg61E40dZw/edit?utm_content=DAFmY_EjLxc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# Dividir e Conquistar

O método de "Divisão e Conquista" é uma abordagem algorítmica eficiente para resolver problemas complexos, decompondo-os em subproblemas menores e mais simples. Essa estratégia é amplamente utilizada em ciência da computação e algoritmos, e pode ser aplicada em uma variedade de contextos.

O processo básico do método "Divisão e Conquista" envolve três etapas principais:

1.Divisão: O problema original é dividido em subproblemas menores e mais fáceis de resolver. Essa divisão pode ser realizada recursivamente até que os subproblemas sejam suficientemente simples.

2.Conquista: Os subproblemas são resolvidos individualmente, seja diretamente ou novamente aplicando a estratégia de "Divisão e Conquista" a eles. Essa etapa envolve a solução dos subproblemas de maneira independente.

3.Combinação: As soluções dos subproblemas são combinadas para obter a solução final do problema original. Essa combinação geralmente envolve a fusão das soluções parciais de forma adequada.

A eficiência do método "Divisão e Conquista" reside na redução da complexidade do problema original por meio de sua divisão em subproblemas menores.

![Conceito](public/imagem.webp)

# Problema

Para ilustrar de forma didática e lúdica vamos considerar o seguinte problema.

### ENCONTRE O MENOR E O MAIOR ELEMENTO EM UMA MATRIZ

Neste problema, recebemos uma matriz de elementos e temos que ncontrar o
elemento mínimo e máximo da matriz fornecida. Resolveremos o problema dado pelo algoritmo de dividir e conquistar. Aqui, dividimos os elementos como a primeira etapa do algoritmo de divisão e conquista, encontramos os elementos mínimos e máximos da matriz como conquista da solução e finalizamos a resposta no final combinando os resultados.

# Como Executar

Na pasta fonte vc vai se deparar com o um arquivo de módulos que vai constar as funções de dividir para conquistar de máximo e mínimo, e um arquivo principal que deverá ser executado em que vai constar a declaração do nosso vetor como estrutura de dados.

```
/bin/python3 main.py
```

# O programa

Ao executar o programa ele vai estar aplicando a divisão e conquista de modo em que ambas situações de máximo e minímo ele vai percorrer o vetor buscando o final dele e tornando a comparação entre pares apenas e não como de um valor por todos os outros no pior caso de uma situação convencional.

Com isso ao terminar o processo, a saída esperada é semelhante a isso...

```
O maior valor é:  x
O menor valor é:  y
```

E assim ao fechar a imagem retornar a execução do programa e ser redirecionado novamente para o início do programa.
