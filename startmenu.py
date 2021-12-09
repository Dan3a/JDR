from tkinter import *

class Window(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        root.geometry("800x600")
        root.resizable(False, False)
        root.wm_title("Crystal Quest Launcher")
        canvas = Canvas(root, width = 800, height = 600)      
        canvas.pack()      
        self.img = PhotoImage(file="logolarge.gif")  # Use self.image
        logo = canvas.create_image(400,0, anchor=N, image=self.img) 
    

    def playButton(self):

if __name__ == "__main__":
    root = Tk()
    Window(root).pack(fill="both", expand=True)
    root.mainloop()

