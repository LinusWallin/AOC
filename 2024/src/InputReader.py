class InputReader:
    """A class to read AOC problem input
    """
    def __init__(self, day, DEBUG):
        """Initializes arguments

        Args:
            day (int): AOC day number
            DEBUG (bool): Option for debugging
        """
        self.day = day
        self.DEBUG = DEBUG

    def ReadInput(self, splitSymbol):
        """Reads AOC input file and splits it at a defined symbol. The split list is then
        returned

        Args:
            splitSymbol(str): Symbol to split the data of the text file by

        Returns:
            list (list[str]): input list for the specific problem
        """
        with open(f"../data/Day{self.day}{'DEBUG' if self.DEBUG else ''}.txt", "r") as inputFile:
            input:list[str] = inputFile.read().split(splitSymbol)
        return input
