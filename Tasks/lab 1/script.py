class Matrix:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.calculatable = True
        self.array = data

    def __add__(self, other):
        result = self
        try:
            for i in range(self.rows):
                for j in range(self.columns):
                    result.array[i][j] += other.array[i][j]
        except:
            result.calculatable = False

        return result

    def __sub__(self, other):
        result = self
        try:
            for i in range(self.rows):
                for j in range(self.columns):
                    result.array[i][j] -= other.array[i][j]
        except:
            result.calculatable = False

        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            result = self

            try:
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.array[i][j] *= other
            except:
                result.calculatable = False

            return result

        else:
            result = Matrix(self.rows, other.columns, [[0.0] * other.columns for i in range(self.rows)])
            result.calculatable &= self.calculatable & other.calculatable

            try:
                for i in range(self.rows):
                    for j in range(self.columns):
                        for k in range(other.rows):
                            result.array[i][j] += self.array[i][k] * other.array[k][j]
            except:
                result.calculatable = False

            return result

    def transpose(self):
        result = Matrix(self.columns, self.rows, [[0.0] * self.rows for i in range(self.columns)])
        result.calculatable = self.calculatable

        try:
            for i in range(self.rows):
                for j in range(self.columns):
                    result.array[j][i] = self.array[i][j]
        except:
            result.calculatable = False

        return result


def claculate(alpha, beta, A, B, C, D, F):
    X = C * (A * alpha + B.transpose() * beta).transpose() * D - F
    if X.calculatable:
        out = '1\n' + str(X.rows) + ' ' + str(X.columns) + '\n'

        for i in range(X.rows):
            for j in range(X.columns):
                out += str(X.array[i][j])
                if j < X.columns - 1:
                    out += ' '
            if i < X.rows - 1:
                out += '\n'
    else:
        out = '0'

    return out


if __name__ == '__main__':
    fin = open("input.txt", 'r')
    fout = open("output.txt", 'w')

    alpha, beta = map(float, fin.readline().split())

    n, m = map(int, fin.readline().split())
    l = list(map(float, fin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(l[0:m])
        l = l[m:]

    A = Matrix(n, m, arr)

    n, m = map(int, fin.readline().split())
    l = list(map(float, fin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(l[0:m])
        l = l[m:]

    B = Matrix(n, m, arr)

    n, m = map(int, fin.readline().split())
    l = list(map(float, fin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(l[0:m])
        l = l[m:]

    C = Matrix(n, m, arr)

    n, m = map(int, fin.readline().split())
    l = list(map(float, fin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(l[0:m])
        l = l[m:]

    D = Matrix(n, m, arr)

    n, m = map(int, fin.readline().split())
    l = list(map(float, fin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(l[0:m])
        l = l[m:]

    F = Matrix(n, m, arr)

    fout.write(claculate(alpha, beta, A, B, C, D, F))
