

def calculate_convo_width(width, kernel_size, stride, padding):
    return ((width - kernel_size + (2 * padding)) /stride) + 1

class Conv2D:
    '''
    This is for educational perpose.The code is not optimize for speed
    but for understanding of mortals(mee!!)
    '''
    def __init__(self, width):
        pass

def main():
    print(calculate_convo_width(width=5, kernel_size=3, stride=2, padding=0))

if __name__ == "__main__":
    main()
