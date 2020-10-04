import tkinter as tk

class Launch():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        self.__table = [[0 for i in range(9)] for j in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'gray'
                else:
                    color = 'white'

                self.__table[i][j] = tk.Entry(window, width = 2, font = ('Arial', 18), bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black', textvar = board[i][j])
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j)
                
        menu = tk.Menu(window)
        window.config(menu = menu)
        file = tk.Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = window.quit)
        file.add_command(label = 'Solve', command = self.solveSudoku)
        file.add_command(label = 'Clear', command = self.clearAll)

    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if board[i][j].get() == '':
                    continue
                if len(board[i][j].get()) > 1 or board[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    board[i][j].set('')

    def clearAll(self):
        for i in range(9):
            for j in range(9):
                board[i][j].set('')
        
    def isValid(self, row, col, num):
        for i in range(9):
            if board[row][i].get() == str(num):
                return False

        for j in range(9):
            if board[j][col].get() == str(num):
                return False

        for i in range((row-(row%3)), (row-(row%3))+3):
            for j in range((col-(col%3)),(col-(col%3))+3):
                if board[i][j].get() == str(num):
                    return False        
        return True
    
    def solveSudoku(self):
        row = -1
        col = -1
        flag = False
        for i in range(9):
            for j in range(9):
                if board[i][j].get() == '':
                    row = i
                    col = j
                    flag = True
                    break
            if flag is True:
                break
        if row==-1:
            return True
        for num in range(1,10):
            if self.isValid(row,col,num):
                board[i][j].set(str(num))
                if self.solveSudoku()==True:
                    return True
                board[i][j].set('')
        return False

root = tk.Tk()
board = [[0 for i in range(9)] for j in range(9)]
for i in range(0,9):
    for j in range(0,9):
        board[i][j] = tk.StringVar(root)

app = Launch(root)
root.mainloop()