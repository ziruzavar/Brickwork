class BrickWork:
    def __init__(self, n, m, layer):
        self.n = n
        self.m = m
        self.layer = layer  # First layer in form of a str
        self.first_layer = []
        self.second_layer = None
        self.__counter = 1

    # VALIDATIONS ///////////////////////////
    # Validating the range of n and m
    def __validate_range(self):
        if self.n > 100 or self.m > 100:
            return True

    # Validating if the n and m are equal to the given input
    def __validate_columns_and_rows(self):
        if len(self.layer) != self.n:
            return True
        for r in self.layer:
            if len(r.split()) != self.m:
                return True

    # Validating the bricks length
    def __validate_bricks_length(self):
        line = ' '.join(self.layer)
        int_line = [int(i) for i in line.split()]

        area = self.n * self.m
        for i in range(area / 2):
            if int_line.count(i) != 2:
                return True

    # END OF VALIDATIONS /////////////////////////

    # Applying the validations written above
    def __validate_input(self):
        if self.__validate_range() or self.__validate_columns_and_rows() or self.__validate_range():
            return False
        return True

    # BUILDING THE LAYERS ///////////////////

    # Transforming the given layer into a list
    def __build_first_layer(self):
        for row in self.layer:
            self.first_layer.append([int(i) for i in row.split()])

    # Building the second layer in form of a list
    def build_second_layer(self):

        if not self.__validate_input():  # Checking if the input is valid
            return False
        self.__build_first_layer()

        # Building the second layer with a random char-b
        self.second_layer = [['b' for _ in range(self.m)] for _ in self.layer]
        for row in range(0, self.n, 2):
            for col in range(0, self.m, 2):
                """ if the ch in the first layer are 11 switching them to 1
                                                                           1"""
                if self.first_layer[row][col] == self.first_layer[row][col + 1]:
                    self.second_layer[row][col], self.second_layer[row + 1][col] = self.__counter, self.__counter
                    self.__counter += 1
                    self.second_layer[row][col + 1], self.second_layer[row + 1][
                        col + 1] = self.__counter, self.__counter
                else:
                    """ Else the ch in the first layer are 1 switching them to 11
                                                           1"""
                    self.second_layer[row][col], self.second_layer[row][col + 1] = self.__counter, self.__counter
                    self.__counter += 1
                    self.second_layer[row + 1][col], self.second_layer[row + 1][
                        col + 1] = self.__counter, self.__counter
                self.__counter += 1
        return True

    # END //////////////////////////////////////////////////////////

    # PRINTING /////////////////////////////

    #  Reformatting the second layer into a str
    def __reformat_second_layer_as_str(self, second_layer):
        answer = ''
        for layer in second_layer:
            answer += ''.join([str(i) for i in layer]).replace('-', ' ')
            answer += '\n'

        if answer.split('\n')[-3] == '*' * ((self.m * 2) + 1):  # check if there will be a redundant line
            return answer[:-self.m * 2 - 3]  # Remove the redundant line
        return answer

    def print_second_layer(self):
        # The hardest part -
        # Making the second layer into a list surrounded with *
        cont = self.build_second_layer()
        if not cont:  # If the input isn't valid print - -1
            return print(f'-1 invalid input')

        #  Surrounding the second layer with *
        second_str_layer = [['*' for _ in range((2 * m) + 1)]]
        self.__counter = 0
        for i in range(0, self.n):
            second_str_layer.append([])
            second_str_layer[-1].append('*')
            for b in range(0, self.m):
                second_str_layer[self.__counter + 1].append(self.second_layer[i][b])
                second_str_layer[self.__counter + 1].append('*')
            second_str_layer.append(['*' for _ in range((2 * m) + 1)])
            self.__counter += 2
        # End of the surrounding

        # Removing the redundant * from the second layer
        for row in range(1, self.n * 2, 2):
            for col in range(1, self.m * 2, 2):
                if col + 2 == self.m * 2 + 1 and row + 2 == self.n * 2 + 1:
                    break
                elif col + 2 == self.m * 2 + 1:
                    if second_str_layer[row][col] == second_str_layer[row + 2][col] and second_str_layer[row][col] != '*':
                        second_str_layer[row + 1][col] = second_str_layer[row][col]
                        second_str_layer[row + 2][col] = '*'
                elif row + 2 == self.n * 2 + 1:
                    if second_str_layer[row][col] == second_str_layer[row][col + 2] and second_str_layer[row][col] != '*':
                        second_str_layer[row][col + 1] = '-'
                else:
                    if second_str_layer[row][col] == second_str_layer[row][col + 2] and second_str_layer[row][col] != '*':
                        second_str_layer[row][col + 1] = '-'
                        second_str_layer[row + 1][col + 1] = '*'
                    elif second_str_layer[row][col] == second_str_layer[row + 2][col] and second_str_layer[row][col] != '*':
                        second_str_layer[row + 1][col] = second_str_layer[row][col]
                        second_str_layer[row + 2][col] = '*'
        return print(self.__reformat_second_layer_as_str(second_str_layer))


n, m = input().split()  # Getting the n and m inputs
n, m = int(n), int(m)  # Making them into ints

# Getting the first layer input
layer = []
print('If you want to stop inputting-press Enter twice')
row = input()
while row:
    layer.append(row)
    row = input()
brick = BrickWork(n, m, layer)  # Instantiating a brick
# with the given n, and first_layer

# Printing the answer
brick.print_second_layer()

# The second layer in form of a list
print(brick.second_layer)
