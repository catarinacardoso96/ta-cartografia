# TA - Módulo Cartografia
## Grupo
- Catarina Cardoso - a75037
- Luciano Silva - a75155

## Implementação

Esta implementação segue o seguinte método:
- melhoria do contraste/brilho da imagem; desta forma conseguiu-se realçar a forma das estradas que ficaram mais salientes
- cálculo da distância da cor de cada pixel à cor média das estradas que foi assumida como (180, 180, 180 - BGR); esta cor foi selecionada depois de alguns testes manuais e não automatizados.
- binarização da imagem por truncação e por threshold; ambos os métodos foram encontrados na documentação do OpenCV.
- seleção na imagem original dos pixeis a brancos na binarizada.

## Desafios

Durante o desenvolvimento encontraram-se alguns desafios que poderão ser considerados como trabalho futuro. Eram estes:
- a resolução da imagem utilizada era um pouco baixa, pelo que ao fazer zoom perdiam-se muitos detalhes importantes para a segmentação. A utilização de um algoritmo como o Canny tornou-se impossibilitada pois o algoritmo detetava demasiadas linhas e não foi possível extrair a informação importante.
- o tamanho das imagens causava erros de memória no processo de segmentação; poderia-se desenvolver um programa que permitisse ao utilizador recortar apenas a parte que lhe interessa ou navegar pela imagem grande enquanto a segmentação era feita em "real-time"

## Discussão

A proposta inicial não foi passível de ser resolvida. As imagens abaixo representam os resultados conseguidos com o algoritmo descrito na implementação.

![Imagem utilizada para teste](https://github.com/catarinacardoso96/ta-cartografia/blob/master/test.png)

![Resultados após a aplicação do algoritmo](https://github.com/catarinacardoso96/ta-cartografia/blob/master/result.png)
