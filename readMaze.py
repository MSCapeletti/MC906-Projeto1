import numpy as np

# 0 representa os pontos em branco (precisamos discutir o que eles significam)
# 1 representa as paredes (nao podem ser atravessadas)
# 2 representa as areas cinzas (o objetivo eh percorrer o maximo antes de chegar ao objetivo)
# 3 representa os fantasmas
# 4 representa a posicao inicial
# 5 representa o objetivo

# A organizacao do arquivo do labirinto deve ser: numLinhas numColunas coordenada00 coordenada01 ...
def readMaze(filename="Maze"):
    array = np.fromfile(filename, 'int32', -1, ' ')
    maze = np.reshape(array[2:], (array[0], array[1]))
    return maze, array[0], array[1]