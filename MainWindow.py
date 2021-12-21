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

import tkinter as tk
import base64, pyglet, AnimatedGif


class MainWindow(tk.Tk):
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
    windowTitle = "Crystal Quest"
    lastEntry = ""
    pyglet.font.add_file('LuxuriousRoman-Regular.ttf')

    def __init__(self, width=800, height=600):
        super().__init__()

        self.width = width
        self.height = height

        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.resizable(False, False)
        self.wm_title(self.windowTitle)
        self.configure(bg='black')

        img = base64.b64decode(self.iconimgdata)
        photo = tk.PhotoImage(data=img)
        self.iconphoto(False, photo)

        # self.minimapImg = tk.PhotoImage(file="mapanimquick.gif")
        # self.minimapLabel = tk.Label(self, image=self.minimapImg)
        # self.minimapLabel.configure(bd=0)
        # self.minimapLabel.place(x=620, y=0)

        self.minimapGif = AnimatedGif.AnimatedGif(self, 'mapanim.gif', 30)
        self.minimapGif.place(x=620, y=0)
        self.minimapGif.configure(bd=0)
        self.minimapGif.start()

        run_string = tk.StringVar()

        self.entry_run = tk.Entry(self, textvariable=run_string, width=50)
        self.text_widget = tk.Text(self)

        self.button_run = tk.Button(self, text="Run", command = self.runCallback)

        self.text_widget.configure(bg='#111111', fg='white', font=('Luxurious Roman',12))
        self.entry_run.configure(bg='#3a3a3a', fg='white', font=('Luxurious Roman',12))
        self.button_run.configure(bg='#3a3a3a', fg='white', font=('Luxurious Roman',12))

        self.entry_run.place(x=0, y=550, width=570, height=50)
        self.button_run.place(x=570, y=550, height=50, width=50)
        self.text_widget.place(x=0, y=0, width=620, height=550)    


    def printInTextArea(self, *args, end="\n"):
        for i in range(len(args)):
            self.text_widget.insert(tk.END, args[i])
        self.text_widget.insert(tk.END, end)
        self.text_widget.see(tk.END)

    def getEntryText(self):
        text = self.entry_run.get()
        self.entry_run.delete(0, tk.END)
        return text

    def runCallback(self):
        self.lastEntry = self.getEntryText()

    def waitForEntryText(self):
        self.waitForEntryText("")

    def waitForEntryText(self, textToPrint):
        self.printInTextArea(textToPrint)
        while self.lastEntry == "":
            pass
        text = self.lastEntry
        self.lastEntry = ""
        self.text_widget.delete(1.0, tk.END)
        return text
