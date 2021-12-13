from startMenu import *
from gameMenu import *

startWindow = tk.Tk()
StartMenu(startWindow).pack(fill="both", expand=True)
startWindow.mainloop()


if playButtonState==True:
    startWindow.quit()
