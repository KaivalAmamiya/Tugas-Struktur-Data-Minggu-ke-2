import time
import os

ROWS = 7
COLS = 7

# Grid awal (pola berbeda)
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

def tampilkan_grid(grid):
    for baris in grid:
        for sel in baris:
            print("⬛" if sel == 1 else "·", end=" ")
        print()
    print()

def hitung_tetangga(grid, r, c):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr = r + i
            nc = c + j
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                total += grid[nr][nc]
    return total

for generasi in range(6):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generasi ke-", generasi)
    tampilkan_grid(grid)

    grid_baru = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):
            tetangga = hitung_tetangga(grid, r, c)

            if grid[r][c] == 1 and tetangga in (2, 3):
                grid_baru[r][c] = 1
            elif grid[r][c] == 0 and tetangga == 3:
                grid_baru[r][c] = 1

    grid = grid_baru
    time.sleep(1)
