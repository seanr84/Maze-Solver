from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk() # Create the root widget (main window)
        self.__root.title("Maze Solver") # Set the window title
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width) # Set the window size and color
        self.__canvas.pack(fill=BOTH, expand=1) # Pack the canvas to fill the entire window
        self.__running = False # Data member to track whether the window is running
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # Binding the close button to the self.close function
        
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    

class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
