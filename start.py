# Copyright 2021, Dan3A, rremi0     Contact : 21985756+Dan3a@users.noreply.github.com

# This file is part of Crystal Quest.

#     Crystal Quest is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     Crystal Quest is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABI LITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with Crystal Quest.  If not, see https://www.gnu.org/licenses/. 

# Image en base64
iconimgdata = b'iVBORw0KGgoAAAANSUhEUgAAABcAAAAbCAYAAACX6BTbAAAGFElEQVRIiWVWS' \
              b'4gc1xU9971XVV3V1b/pVqtHI9mjsUbIRDKGxFmZBBKTRRZJcIwXgWyyTggEvM' \
              b'w6i6xs8MLbEAwhCs4i5IMhiBCMkBkTy8lYsjUfW5rpmemZ/lV3dVXX55n7qmc' \
              b'kOw8eXVVdde+pc889t+h3G0dIcw1e7bKFy0slVEsSkziDZ0v4jsD2SazvPAzw' \
              b'7bUq3tsN8OLlKiqOhC2JMg3sj+c4ChIIAqQgSAIsSVCDMEWlJE3w3jRB2QSUa' \
              b'PsW/rU91q+9cQcizynpjvRbqy2KP+/r1wWRFNBrP7yh33z5Ck6mCZ9DEkEsfo' \
              b'mPNw9DHAZzEIq1O4jg2UL/8e6x/sVrf6PkUZ8D4+L3r6N5YxmrP7gODqRI0N5' \
              b'fNuknv3oX80xrm5HyFqcbUJ/0ZgiiDNNWjmeaJZSU0L/88xbeu3nXIHBqHmxL' \
              b'mNe0zRbwWxWkg5ATIA9iuv1ZoF95rqkncV68gSBDkVo/52L7eIZRlOLW1kgPu' \
              b'hMEG9sQRMQInJKEWy9zUpOAd7XlQyx5yCdzzAch7r6zieXq8/jmJV9rgNSCHn' \
              b'G94+HFtZpBdLFqY743gCRBkoRBRlFWoFYERwk4/BaKINMcySCETQJ6ltD7f30' \
              b'AIsCRQksJBHEG1ZskYPTPtl39VMPBz3eGmEtCPp7B9mzYtoIlBD8E2ypoiQRB' \
              b'E1Au29AcRBDCvTHe+ccOfvS9y3g0jLUlBamP9qe4dxjq716t4zdvbyLc3IdSE' \
              b'm6zjNa1DuKDERxJBjGj5+CcSFZLULUSRlt9MA1KCpp2p3ocZaawjiIofoC1ut' \
              b'2PkJ8ERgVSa2QnU6SDKUqWMjcz50VwpkjAEmTo0Q0PQms0Oj78io2yI0/lqJU' \
              b'SQtcciXpJwa24gKOQjyJYSsIGoBSZQI5FBTWLBJYEGu0yznfKiE5mcCxlrjHN' \
              b'Os0w2ptAffpxD+VOBQfB3CC0yiVIz0G17cFWEukwgiWFQf5kcN6ep2ALAgVJ8' \
              b'awgjPYCI4DoeAaV9gLE0Rza5htF8aBjoVwtwbEkZsH8cXBV/O8sZHmaLF1IlA' \
              b't/WhfeKj0cY3ZEcC434TgW/KaLatvHhfOe8Y+PDyYGUcl6jJx/+Vql6kBBA54' \
              b'FpLkBEZ9E3LHIwgRKCW4WoWudKvyGg6urdVOUcZTi6YaDrQW/BfKimIyKr609' \
              b'VTXaDpsepkdThMcRkkmC/c2+6W4uqJFSchTga9/oQAjS3X5EaX+GScOB6yrIL' \
              b'IdrPaaE0bslheWqbTq72XYhOh6GvRDhYI6jewO2ABIWd6IgyoYRPtse4pONLu' \
              b'aHE9TPefj6io/Wsm/QMnJO4JrCEtorFZzzLUMPe4kthb64UsHxzrAwLo5rDti' \
              b'AZwkO7jzCtZfW8MxqDb4lTZFqSy7So/DLyKXAUstFrjV8Rxn/hgDYWILDCEqw' \
              b'fRCE8Q0y1SfiVtYaaca3aez2Y3RanqGBkZuiLiTZbrkYRVlhv5I0T42/v/URo' \
              b'vHc8G2us/zOPJiIuu939dOrdYO6U7HNVOov+ybwqb5bF3xcqjvIcm2UwfZ66/' \
              b'f3kYSZiVFYLiMXhfgtIiOldBzj89t7uNb2dN2VpmidCxWjlFOtL1+qoMZWbAk' \
              b'seUpzoKAXQxGoGHPFqFMXb7QRdkMkY8MVTxDq3e/j4TDWz6/4PGHohasNxGmO' \
              b'fpiaZN4517wpEemdrSFuvf0pBzM8NzseXnp1HY2mA/XTV59FnGncO5hif+MAO' \
              b'k7hVxzTmUxJmOR6yVNIMo2yLcx8HUeZ5gF+87cfnPJL68818Z2XrxTFXSz6cH' \
              b'+KlZptupHX3mhupjlb9oWqjX//8yEe3O7CDA9xOt1pMVCK85/9+gVD21eXejS' \
              b'MjRqqJR4KwPmKxed6qxvi5h/+a9r6Wz9ep0vr9TP/4Ddi/jnZE0s/eZLOc1Ls' \
              b'5Q8HMTeHZgXwJ8x//neCO396YHhllCe7Y33l2pIJzp8hLMWvBP7SevDhMYbHE' \
              b'ejW1sj8wVP/g3d3H/sCf5sYPo1E2RbO9MuDgFAcCxAa7RKEFOgfhGdJpCVJ3d' \
              b'84RNCd6OOd0UItHPT/+DWFOtMvQGa688cPgGEvepISQ36WZPgCVhY7eBY73j4' \
              b'AAAAASUVORK5CYII='

# Installation automatique des dépendances
import os
# os.system("python -m pip install --upgrade pip --user")
os.system("python -m pip install pyglet --user")
os.system("python -m pip install pygame --user")

# os.system("python -m pip install base64 --user")

import tkinter as tk
import base64,pyglet
from pygame import mixer


# Classe du menu principal
class StartMenu(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        # Définition de la taille et de la position de la fenêtre
        w = 800
        h = 600

        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(False, False)
        root.wm_title("Crystal Quest Launcher")

        img = base64.b64decode(iconimgdata)
        photo = tk.PhotoImage(data=img)
        root.iconphoto(False, photo)

        self.img = tk.PhotoImage(file="logolarge.gif")  # Use self.image
        background_label = tk.Label(root, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        mixer.init()
        playIntroSong() 

        quitButton = tk.Button(
            root,
            font=('Middle Ages PERSONAL USE',25),
            text="Quit",
            fg='white',
            bg='black',
            command=lambda: root.quit(),
        )
        quitButton.place(x=340, y=470)

        playButton = tk.Button(
            root,
            font=('Middle Ages PERSONAL USE',30),
            text="Play",
            fg='white',
            bg='black',
            command=lambda: StartGameMenu(),
        )
        playButton.place(x=325, y=355)
        
        def StartGameMenu():
            mixer.music.stop()
            os.system("python CrystalQuest.py")

# Purement pour la musique
def playIntroSong(): 
    mixer.music.load("assets/songs/intro.mp3")
    mixer.music.play(loops=999)

pyglet.font.add_file('MiddleAges_PERSONAL_USE.ttf')

startWindow = tk.Tk()
StartMenu(startWindow).pack(fill="both", expand=True)
startWindow.mainloop() 