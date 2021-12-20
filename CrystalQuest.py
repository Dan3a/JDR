from MainWindow import *
import threading as thread
from chevalier import *
class App:

    def run(self):
        self.mainWindow = MainWindow()
        self.logicThreadInstance = thread.Thread(target=self.logicThread)
        self.logicThreadInstance.start()
        self.mainWindow.mainloop()
    
    def logicThread(self):
        jeu(self.mainWindow)
        
if __name__ == "__main__":
    app=App()
    app.run()