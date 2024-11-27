import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Parámetros del modelo
grid_size = 50
prob_quema = 0.3  # Probabilidad de que un árbol sano se queme por un vecino en llamas
steps = 50 

# Estados
Sano = 0   
Ardiendo = 1  
Quemado = 2     

grid = np.zeros((grid_size, grid_size), dtype=int)

# Se inicia el incendio desde un árbol al azar
x, y = np.random.randint(0, grid_size, size=2)
grid[x, y] = Ardiendo

# Función para actualizar el estado de la cuadrícula
def update(grid):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == Sano: 
                # Verifica si algún vecino está en llamas. En caso afirmativo, el árbol se prende fuego y luego pasa al estado Quemado.
                neighbors = grid[max(0, i-1):min(grid_size, i+2), max(0, j-1):min(grid_size, j+2)]
                if Ardiendo in neighbors:
                    if np.random.rand() < prob_quema:
                        new_grid[i, j] = Ardiendo  
            elif grid[i, j] == Ardiendo:  
                new_grid[i, j] = Quemado  
    return new_grid

# Animación
fig, ax = plt.subplots(figsize=(6, 6))
colores = ["green", "orange", "black"]
cmap_personal=LinearSegmentedColormap.from_list("cmap_personal", colores,3)
im = ax.imshow(grid, cmap=cmap_personal, vmin=0, vmax=2)

def animate(frame):
    global grid
    grid = update(grid)
    im.set_array(grid)
    ax.set_title('Modelo de incendio forestal')
    return [im]

ani = animation.FuncAnimation(fig, animate, frames=steps, interval=200, blit=True)
plt.colorbar(im, ticks=[0, 1, 2], label="Estado (0=Sano, 1=Ardiendo, 2=Quemado)")
plt.show()

