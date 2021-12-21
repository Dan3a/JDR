# Copyright 2021, Dan3A, rremi0     Contact : 21985756+Dan3a@users.noreply.github.com

# This file is part of Crystal Quest.

#     Crystal Quest is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     Crystal Quest is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with Crystal Quest.  If not, see https://www.gnu.org/licenses/. 

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