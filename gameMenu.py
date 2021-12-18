# MODULE TKINTERIFY MODIFIÉ (https://github.com/rbricheno/tkinterify)


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
import tkinter as tk
import base64, click, sys
from io import StringIO




def GameWindow(cli_group, app_name="Crystal Quest"):
    root = tk.Tk()
    w = 800 # width for the Tk root
    h = 600 # height for the Tk root
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(False, False)
    root.wm_title(app_name)

    img = base64.b64decode(iconimgdata)
    photo = tk.PhotoImage(data=img)
    root.iconphoto(False, photo)

    minimap_img = tk.PhotoImage(file="map.gif", width=180, height=180)
    minimap_label = tk.Label(root, image=minimap_img)
    minimap_label.place(x=0, y=620, relwidth=1, relheight=1)

    initial_output = "Vous vous réveiller par un bruit de pas ;\nle bruit de pas de gardes royaux au pied de votre porte.\nVous vous levez, ouvrez la porte et un message vous est tendu : \n*** Sir, le royaume court un grave danger, ***\n*** les 3 cristaux de Dahal ont été volé à Icegate. ***\n*** Le royaume est tombé dans une nuit éternelle ***\n*** où les monstres peuvent y refaire leur apparition. ***\n*** Par ordre du roi, vous devez les retrouver  ***\n*** et arrêter celui qui les a dérobés… ***\nVous n'avez pas besoin d'en lire plus, vous saviez que cela allait arriver,\net vous en savez le danger, mais vous vous rappelez également\nvos mauvaises relations récentes avec le Roi. Vous devez prendre une décision.\nCommandes disponibles : accepter / refuser\n"

    run_string = tk.StringVar()
    entry_run = tk.Entry(root, textvariable=run_string, width=50)
    scrollbar_widget = tk.Scrollbar(root)
    text_widget = tk.Text(root)


    def clear_callback():
        # Because the text widget is usually disabled, we have to explicitly enable it before we can write to it.
        text_widget.config(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, initial_output)
        text_widget.config(state='disabled')

    def run_callback():
        command_args = []
        try:
            command_parts = run_string.get().split()
            command_name = command_parts[0]
        except IndexError:
            return
        if len(command_parts) > 1:
            command_args = command_parts[1:]

        if command_name:
            try:
                # Redirect stdout so we can read the output into a string for display within out GUI
                real_stdout = sys.stdout
                fake_stdout = StringIO()
                sys.stdout.flush()
                sys.stdout = fake_stdout

                # Obtain list of available commands
                available_commands = cli_group.commands
                command_name_list = list(cli_group.commands.keys())
                if command_name in command_name_list:
                    try:
                        # Make a fake context in which to run the command
                        context = available_commands[command_name].make_context("tk", command_args)
                        # Invoke the command within the fake context
                        available_commands[command_name].invoke(context)
                    except click.exceptions.UsageError as e:
                        print(e)
                        print(initial_output)
                else:
                    print("Command non trouvée.\n")

                # Put stdout back
                sys.stdout.flush()
                sys.stdout = real_stdout
                sys.stdout.flush()
                output_string = fake_stdout.getvalue()
                fake_stdout.close()

                # Update the text output widget
                text_widget.config(state='normal')
                text_widget.delete(1.0, tk.END)
                text_widget.insert(tk.END, output_string)
                text_widget.config(state='disabled')

            except IndexError:
                pass

    # More GUI widgets
    button_run = tk.Button(root, text="Run", command=run_callback)

    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, initial_output)

    entry_run.place(x=0, y=550, width=590, height=20)
    button_run.place(x=590, y=550, height=20)
    text_widget.place(x=0, y=0, width=620, height=550)



    root.mainloop()