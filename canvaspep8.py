class Canvas:

    def __init__(self, i, j):
        self.matrix = [[0 for x in range(i)] for y in range(j)]
        self.aux = 0

    def clearcanvas(self):
        self.matrix = [[0 for x in range(len(self.matrix[0]))]
                       for y in range(len(self.matrix))]

    def colorpixel(self, x, y, c):
        self.matrix[y - 1][x - 1] = c

    def verticalsegment(self, x, y1, y2, c):
        for i in range(min(y1, y2) - 1, max(y1, y2)):
            self.matrix[i][x - 1] = c

    def horizontalsegment(self, x1, x2, y, c):
        for i in range((min(x1, x2) - 1), max(x1, x2)):
            self.matrix[y - 1][i] = c

    def rectangle(self, x1, y1, x2, y2, c):
        if x1 <= x2 and y1 <= y2:
            for i in range(y1 - 1, y2):
                for j in range(x1 - 1, x2):
                    self.matrix[i][j] = c

    def floodfill(self, x, y, c):
        if self.matrix[y][x] == self.aux:
            self.matrix[y][x] = c
            if y > 0:
                self.floodfill(x, y - 1, c)
            if y < len(self.matrix) - 1:
                self.floodfill(x, y + 1, c)
            if x > 0:
                self.floodfill(x - 1, y, c)
            if x < len(self.matrix[0]) - 1:
                self.floodfill(x + 1, y, c)

    '''
    def printmatrix(self):
        output = ['' for x in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                output[i]+=str((self.matrix[i][j]))
        for i in range(len(self.matrix)):
            print(output[i])
    '''

    def savefile(self, file_name):
        output = ['' for x in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                output[i] += str((self.matrix[i][j]))

        f = open(file_name, 'w')

        for i in range(len(self.matrix)):
            print >> f, output[i]

        f.close()


def min(a, b):
    if a >= b:
        return b
    elif a < b:
        return a


def max(a, b):
    if a <= b:
        return b
    elif a > b:
        return a


def main():
    object_exists = False
    loop_break = False
    while not loop_break:
        buffer_string = raw_input()
        user_string = buffer_string.split()
        if user_string[0] == 'I' and len(user_string) >= 3:
            my_object = Canvas(int(user_string[1]), int(user_string[2]))
            object_exists = True
        if object_exists:
            if user_string[0] == 'C':
                my_object.clearcanvas()
            elif user_string[0] == 'L' and len(user_string) >= 4:
                my_object.colorpixel(int(user_string[1]), int(
                    user_string[2]), user_string[3])
            elif user_string[0] == 'V' and len(user_string) >= 5:
                my_object.verticalsegment(int(user_string[1]), int(
                    user_string[2]), int(user_string[3]), user_string[4])
            elif user_string[0] == 'H' and len(user_string) >= 5:
                my_object.horizontalsegment(int(user_string[1]), int(
                    user_string[2]), int(user_string[3]), user_string[4])
            elif user_string[0] == 'K' and len(user_string) >= 6:
                my_object.rectangle(int(user_string[1]), int(
                    user_string[2]), int(user_string[3]), int(
                        user_string[4]), user_string[5])
            elif user_string[0] == 'F' and len(user_string) >= 4:
                my_object.floodfill(
                    int(user_string[1])-1, int(user_string[2])-1,
                    user_string[3])
            elif user_string[0] == 'S' and len(user_string) >= 2:
                my_object.savefile(user_string[1])
            elif user_string[0] == 'X':
                break

if __name__ == "__main__":
    main()
