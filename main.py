from startmenu import *

root = Tk()
StartMenu(root).pack(fill="both", expand=True)
pygame.mixer.init()
playIntroSong() 
root.mainloop()
