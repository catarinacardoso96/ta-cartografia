# Proposta

O projecto Europeu Copernicus é um projeto de observação da Terra e está a disponibilizar imagens de satélite de forma gratuita.

O objetivo deste pequeno projeto é identificar estradas em imagens de satélite. As imagens a considerar são as recolhidas pelos satélites Sentinel-2, operados pela ESA.

O projeto passa por identificar estradas nas imagens e depois comparar os resultados obtidos com um dataset com as estradas que efetivamente existem (recorrendo ao OpenStreetMap), de forma a avaliar a extração efetuada.

Os dados do OpenStreetMap estão no formato vetorial, enquanto que os dados extraídos das imagens estão no formato raster (de imagem). Como trabalho adicional, poderão passar as estradas identificadas para vectores.

Para a comparação entre as estradas extraídas de forma automática e as estradas existentes, podem-se considerar dois cenários:

uma análise visual, por exemplo, no QGIS, sem qualquer forma automatizada e sem qualquer cálculo de métricas (dados quantitativos)
uma análise quantitativa
Os trabalhos podem ser feitos individualmente ou em grupo de dois.


# Imagens

As imagens do Sentinel podem ser descarregadas a partir de: https://scihub.copernicus.eu/dhus/#/hom

Nos filtros, devem-se indicar os critérios de pesquisas. Deve-se preferir imagens com uma baixa taxa de nuvens. 

Imagem para teste (Noroeste de Portugal)

A imagem de teste pode ser descarregada a partir do seguinte link:
https://scihub.copernicus.eu/dhus/odata/v1/Products('3df8693a-bb39-4114-a262-166a0884eb87')/$value

Na verdade, não se trata de uma imagem apenas. Na terminologia do Copernicus trata-se de um ''produto''. Um produto inclui várias imagens, captadas com diferentes sensores. As imagens que vamos usar estão na pasta:


GRANULE/L2A_T29TNF_A005497_20180326T112919/IMG_DATA/R10m

O produto inclui várias imagens. Cabe aos alunos escolherem a banda ou conjunto de bandas, onde é mais fácil identificar as estradas.

Dados do OpenStreetMap

Os dados das estradas para Portugal podem ser descarregados a partir de: http://openstreetmap.pt/wp-content/uploads/

Descarreguem vias.zip e abram-na no QGIS.

Software: QGIS e OpenCV

Usem o QGIS para a visualização das imagens e das camadas vetoriais. Criem no QGIS polígonos para recortarem as imagens para trabalharem com áreas mais pequenas enquanto estão a afinar os algoritmos.

Para o tratamento das imagens podem usar o OpenCV. Para o OpenCV já há alguns exemplos que podem tirar partido numa análise inicial.

Apontadores iniciais

Canny edge detector
Changing the contrast and brightness of an image
Histogram Equalization
Exemplo muito básico de utilização do Canny
Grass com Canny
River Detection in Remotely Sensed Imagery Using Gabor Filtering and Path Opening

# Entrega

Link para um repositório Github público com o código
Imagens de teste e resultados no Github
Não é preciso relatório. Em vez do relatório, será avaliado o Readme.md que estiver no repositório do Github.