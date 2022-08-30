import random


# 队列
class Queue():
    def __init__(self):
        self.__array = []

    def push(self, content):
        self.__array.append(content)

    def size(self):
        return len(self.__array)

    def pop(self):
        for i in range(self.size() - 1):
            self.__array[i] = self.__array[i + 1]

    def front(self):
        return self.__array[0]

    def back(self):
        return self.__array[self.size() - 1]

    def empty(self):
        if self.size() <= 0:
            return True
        return False

    def out(self):
        for i in range(self.size()):
            print(self.__array[i], end=" ")
        print("\n")


def randomplace(mazesize, mode):
    global map
    x, y = 1, 0
    if mode == 0:  # "left-top"
        x = random.randint(0, int(mazesize / 5))
        y = random.randint(0, int(mazesize / 5))
    if mode == 1:  # "left-bottom"
        x = random.randint(0, int(mazesize / 5))
        y = random.randint(int(mazesize / 5), mazesize - 1)
    if mode == 2:  # "right-bottom"
        x = random.randint(int(mazesize / 5), mazesize - 1)
        y = random.randint(int(mazesize / 5), mazesize - 1)
    if mode == 3:  # "right-top"
        x = random.randint(0, int(mazesize / 5))
        y = random.randint(int(mazesize / 5), mazesize - 1)
    if map[x][y] == 0:
        return [x, y]
    mq = Queue()
    mq.push([x, y])
    wayx = [-1, 1, 0, 0]
    wayy = [0, 0, -1, 1]
    while mq.empty() == 0:
        top = mq.front()
        mq.pop()
        count += 1
        for i in range(4):
            nx, ny = top[0] + wayx[i], top[1] + wayy[i]
            if nx >= 0 and ny >= 0 and nx < mazesize and ny < mazesize:
                mq.push([nx, ny])
                if map[nx][ny] == 0:
                    return [nx, ny]
                count += 1
