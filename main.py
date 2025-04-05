class Rule124():
    def __init__(self, tape=None):
        if tape is None:
            tape = []

        assert all()

        self.tape = tape

    def __str__(self):
        for cell in tape:
            print(cell)

    def tick(self):
        # Construct the next iteration on a new tape and move its reference after
        newTape = [None for _ in range(len(tape) + 1)]

        for cellIndex in range(len(tape) + 1):
            try:
                '''
                Pad current tape with two 0s on both ends to support changes at the
                indices before first and after last element of self.tape. 
                Ex. the following:
                    Index:     234567 (suppose these indices)
                    Tape:      101110
                    Next Itr.: ?1101?
                becomes:
                    Index:     0123456789
                    Tape:      0010111000
                    Next Itr.: ?01110110?
                so that index 1 and 8 can be checked and updated appropriately. Then
                the leading and trailing 0s may be stripped before the next tick (at
                least for Rule 110 and Rule 124 where life always spreads in a single direction).
                '''
                cellsAbove = ([0, 0] + tape + [0, 0])[cellIndex+1 : cellIndex+3]
            except IndexError as e:
                # cellIndex-1, cellIndex+1, or both were out of bound of self.tape
                if 0 <= len(tape) <= 2:
                    if len(tape) == 0:
                        cellsAbove = [0, 0, 0]
                    elif len(tape) == 1:
                        cellsAbove = [0, 1, 0]
                    elif len(tape) == 2:
                        if cellIndex == 0:
                            cellsAbove = [0, tape[cellIndex], tape[cellIndex+1]]
                        else:
                            cellsAbove = [tape[cellIndex-1], tape[cellIndex], 0]
                else:
                    # Test which index was out of bounds
                    try:
                        tape[cellIndex-1]
                    except IndexError as e:
                        # Tape has no more symbols to the left
            finally:
                if cellsAbove == [1, 1, 1]:
                        newTape[cellIndex] = 0
                    elif cellsAbove == [1, 1, 0]:
                        newTape[cellIndex] = 1
                    elif cellsAbove == [1, 0, 1]:
                        newTape[cellIndex] = 1
                    elif cellsAbove == [1, 0, 0]:
                        newTape[cellIndex] = 1
                    elif cellsAbove == [0, 1, 1]:
                        newTape[cellIndex] = 1
                    elif cellsAbove == [0, 1, 0]:
                        newTape[cellIndex] = 1
                    elif cellsAbove == [0, 0, 1]:
                        newTape[cellIndex] = 0
                    elif cellsAbove == [0, 0, 0]:
                        newTape[cellIndex] = 0        

        self.tape = newTape

def welcome():
    pass

def main():
    game = Rule124([1])

    for _ in range(10):
        game.tick()
        print(game)

if __name__ == '__main__':
    main()
