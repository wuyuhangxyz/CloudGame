from maze import Maze
import pygame


def newmaze(size):
    maze = Maze(size, size)
    maze.generate_matrix_dfs()
    maps = []
    for i in maze.print_matrix():
        maps.append(list(i))
    # print(maps)
    return maps


def newmazeofnpeople(size):
    mid = int(size / 2)
    print(mid)
    maze = Maze(size, size)
    maze.generate_matrix_dfs()
    maps = []
    for i in maze.print_matrix():
        maps.append(list(i))
    for i in range(mid - 3, mid + 3):
        for j in range(mid - 3, mid + 3):
            maps[i][j] = 0
    return maps


wayx = [-1, 1, 0, 0, -1, 1, -1, 1]
wayy = [0, 0, -1, 1, 1, -1, -1, 1]


# 绘制x-x+w,y-y+w部分地图，每个格子大小为size
# 其中绘制部分以nnx，nny为左上角坐标，mode=0时显示现在的位置,1时不显示
def apr(x, y, w, size, screen, nnx=0, nny=0, mode=0):
    global nx, ny, vstmap
    nnnx = nnx
    nnny = nny
    for i in range(x, x + w):
        nnnx = nnx
        for j in range(y, y + w):
            if i >= 0 and i < mazesize and j >= 0 and j < mazesize:
                if i == nx and j == ny and mode == 1:
                    pygame.draw.rect(screen, (100, 120, 150), pygame.Rect(nnnx, nnny, size, size), 0)

                elif mode == 1 and vstmap[i][j] == -3 and map[i][j] == 0:
                    for m in range(len(wayx)):
                        sx, sy = i + wayx[m], j + wayy[m]
                        if sx >= 0 and sx < mazesize and sy >= 0 and sy < mazesize and map[sx][sy] == -1:
                            vstmap[sx][sy] = -3
                    pygame.draw.rect(screen, (253, 249, 238), pygame.Rect(nnnx, nnny, size, size), 0)
                elif mode == 1 and vstmap[i][j] == -3 and map[i][j] == -1:
                    pygame.draw.rect(screen, (107, 84, 85), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == -1 and mode == 0:
                    pygame.draw.rect(screen, (107, 84, 85), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == 0 and mode == 0:
                    pygame.draw.rect(screen, (253, 249, 238), pygame.Rect(nnnx, nnny, size, size), 0)

                nnnx += size
        nnny += size


def aprlian1(x, y, w, size, screen, nnx=0, nny=0, mode=0):
    global nx, ny, vstmap, map, listoflian1
    nnnx = nnx
    nnny = nny
    for i in range(x, x + w):
        nnnx = nnx
        for j in range(y, y + w):
            if i >= 0 and i < mazesize and j >= 0 and j < mazesize:
                if i == nx and j == ny:
                    pygame.draw.rect(screen, listoflian1[0][2], pygame.Rect(nnnx, nnny, size, size), 0)
                if i == int(mazesize / 2) and j == (mazesize / 2):
                    pygame.draw.rect(screen, (200, 50, 50), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == -1:
                    pygame.draw.rect(screen, (107, 84, 85), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == 0:
                    pygame.draw.rect(screen, (253, 249, 238), pygame.Rect(nnnx, nnny, size, size), 0)
                for k in listoflian1:
                    tempcup = [i, j]
                    if tempcup == k[1]:
                        pygame.draw.rect(screen, k[2], pygame.Rect(nnnx, nnny, size, size), 0)
                nnnx += size
        nnny += size


def guaapr(x, y, w, size, screen, nnx=0, nny=0):
    global nx, ny, vstmap
    nnnx = nnx
    nnny = nny
    for i in range(x, x + w):
        nnnx = nnx
        for j in range(y, y + w):
            if i >= 0 and i < mazesize and j >= 0 and j < mazesize:
                if i == nx and j == ny:
                    pygame.draw.rect(screen, (100, 120, 150), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == -1:
                    pygame.draw.rect(screen, (107, 84, 85), pygame.Rect(nnnx, nnny, size, size), 0)
                elif map[i][j] == 0:
                    pygame.draw.rect(screen, (253, 249, 238), pygame.Rect(nnnx, nnny, size, size), 0)

                nnnx += size
        nnny += size


def drawdui(x, y, ll):
    global mazesize, listoflian1, screen
    nx = x
    ny = y
    for i in listoflian1:
        pygame.draw.rect(screen, i[2], pygame.Rect(nx, ny, 100, 30), 0)
        screen.blit(pygame.font.Font("HYTiaoTiaoTiJ.ttf", 20).render(i[0], True, i[2]), (nx + 110, ny))
        if i[3] == 1:
            screen.blit(pygame.font.Font("HYTiaoTiaoTiJ.ttf", 20).render("Arrived!", True, (200, 50, 50)),
                        (nx + 110 + 12 * len(i[0]), ny))
        ny += 35
