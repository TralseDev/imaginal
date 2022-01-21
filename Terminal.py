class Terminal:
    """
    Terminal class, made for terminal stuff
    """

    def __init__(self, width) -> None:
        self.width = width

    def print_char(self, x, y, char):
        print("\033["+str(y)+";"+str(x)+"H"+char)

    def print(self, colors={}, end='\n') -> None:
        """
        Iterate through string, get color value from dict and print it using function `print_c`
        """
        my_output = ""
        for col in colors:
            for x, i in enumerate(dict(col)):
                if i[1] % self.width == 0 and x != 0:
                    my_output += '\n'
                my_output += self.print_c(col[i])
            if end == "\r":
                self.print_char(1, 2, my_output)
            else:
                print(my_output)
            break

    def print_c(self, rgb: tuple, char: chr = ' ') -> str:
        r, g, b = rgb
        return f"\x1b[48;2;{r};{g};{b}m{char}\x1b[0m"
