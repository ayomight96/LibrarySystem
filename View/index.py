import tkinter as tk
import sys

sys.path.insert(1, '/Users/mac/Documents/PYTHON FOLDER/LibrarySystem')
from Controller.LibrarySystem import LibrarySystem



root = tk.Tk()
LibrarySystem(root)
root.mainloop()
