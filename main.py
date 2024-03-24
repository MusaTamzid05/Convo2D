import random
import time

def calculate_convo_width(width, kernel_size, stride, padding):
    return ((width - kernel_size + (2 * padding)) /stride) + 1

class Conv2D:
    '''
    This is for educational perpose.The code is not optimize for speed
    but for understanding of mortals(mee!!)
    '''
    def __init__(self, mat, kernel_size=3, stride=1, padding=0):
        self.mat = mat
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.kernel = []

        for _ in range(kernel_size):
            row = []
            for _ in range(kernel_size):
                row.append(random.uniform(0, 1))
            self.kernel.append(row)





    def forward(self):

        if self.padding > 0:
            new_mat = []

            for _ in range(self.padding):
                new_mat.append([0 for _ in range((self.padding * 2) + len(self.mat[0]))])

            for row in self.mat:
                new_row = [0 for _ in range(self.padding)] + row +  [0 for _ in range(self.padding)] 
                new_mat.append(new_row)

            for _ in range(self.padding):
                new_mat.append([0 for _ in range((self.padding * 2) + len(self.mat[0]))])

            self.mat = new_mat



        result = []
        result_row = []




        for row in range(0, len(self.mat), self.stride):
            for col in range(0, len(self.mat[0]), self.stride):

                if (row  + (self.kernel_size - 1)) >= len(self.mat):
                    continue

                if (col + (self.kernel_size - 1)) >= len(self.mat[0]):
                    if len(result_row):
                        result.append(result_row)
                        result_row = []

                    continue

                sum_ = 0

                for i in range(self.kernel_size):
                    for j in range(self.kernel_size):
                        sum_ += self.kernel[i][j] * self.mat[row + i][col + j]

                result_row.append(sum_)

        if len(result_row):
            result.append(result_row)


        return result







def main():

    mat = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            ]

    convo = Conv2D(mat=mat, stride=2, padding=0)
    result = convo.forward()

    print(len(result), len(result[0]))


if __name__ == "__main__":
    main()
