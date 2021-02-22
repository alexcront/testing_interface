import tkinter.filedialog
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        test = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAALwAAAC8BDoOZKgAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAGHSURBVDiNjdLPiw1QFAfwzxkzjKQpIVkMO6KQH6VsFLGibORvsECK2FhYiFlYEllZ2KBEQlGiWSgLShZWkkwJUxRjqK/Fu08vDc+p2+mee77f7zn3nMI+bMIP/2ez8TDJTRjEdlzrvia5+y90VQ3gAn4TfMAWDLWErX0q+IKPvYHTSWAediTR73QxSQw21UtYjQdVNYINPQJv8A0rMJnkTK/6YPMjuIHvPW+3sAuj7X45ycs/++kSHMZmvEsyjqstPt7nP34THMJ6PK2qpX9p4UlPBXf+JBjVGcugzj5M4R52YhrXcbCq9rb8OVU1keQVnMaa1sZanXEOY1bz83EOC3umMIwxrOxWsLu1sAy3sarF32IpxpJ8gKpa0EQP4ORAS1yHx3ivs6qz8bz5JUle94DHcCzJFH52KziPbTjb7i8wibk6+6GqTmExjib51PJSuIL7+Gpm+47PmMBEkslGuAj7C9V6HpoJneRZVZ3AoyQPG3g5juB4tV/ta1W1Bxub4DtcTDL9C8yWo9qNPNBXAAAAAElFTkSuQmCC"""
        p1 = tk.PhotoImage(data=test) 
        self.master.iconphoto(False, p1) 
        self.create_widgets()

    def create_widgets(self):
        test = """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"""
        self.img1 = tk.PhotoImage(data=test)
        self.rtc = tk.Button(self, text="Force RTC", image = self.img1, command = self.force_rtc)
        self.rtc.grid(row=0, column=0)

        test = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAS8SURBVFiFtZd7TFNnGId/rbQ9BXp6ilwc4DYkMcoIETsuTh1x4AAdWEBAEgZRHJJsU7OJcSTDGbOEkUxxUUGYTjQyYXEXzNAqC4wBAg7MVHZRwoSJcUCgV3qj/fYH6bD0Dvgm55/vfN/7POf9LuccYPGC8qJFdVweX+UpYAYAiBcxt9Pg8b3pto0pu9TVbVPk4Mlm4iVg5ABinA1kLQZ9+54j8XqD4bvUglIBizWTcrC/GxUfvKVQK2VvAuh+XgKUwMe/7vC5nvUi/yD/uTddkWAvAM7lezPXItZtSWT8Aq3gALDilRh8eEJKe9M+UgCxtvrMtwJcvjcjXRsnid5ZUu1pLru9GPqzD8f2J8tViokkAF0LFXAL7kzCXQGH8KG/7uD2jVo8HbwDDw6FqORCiDdlOJRYshhwxeQoLnyai5b6MmSvM2DPNj9sCGOjqrIWXHo5AkPCAACM7wsIezWe6m39NlOv07QCeOxqBShPAXMzOiFLnHvgJP9Z+PDD33C6eAvezQ7FgfwwcDxm13Xzrcf45JIOReVSi2SD97tRUSzRqOXjG13ZBXbhI4P9qCxOwtlSMT4qCLeAAwDF88C0XmuVcEV4DLIO1fH5AlGDMwG7cI1agdMHt+LEwUgkbgi2OfiXvlGERMRZtU9OAcGr12Nar13mSMAuHAAaq0uQGR+A9ISXbQ7WG0z4qnEIkZtyLNplU4BSQ9BUtV/nwaG+97AD5/oGBLWuikqIsAVXysbQJa3D+UaJXfvy8/0IXROPwJDVFnCFhqCpaq+uv/2bXq1KttuWAEUzzE0e3zs6/9AZlq19fq/zGtI3h2IpQ9nBs9Az5A/Je8es4D9Wvq+731bfq1XJ4gFo504BRdP0jYzMrLWRa8JZF8sKQUwmq/TjIw8QudLLJvp6+wiONwciq+QKvGgfh3DA8l3AFTLMtdT0DHFFZZXnxYZ6LPU04NzRPJhMRguIYGkQfn+ktmiTKfXY99lt7Dv+ENNB262evKlqrxmeYIbP1GoWLk2RpEWf+vLs/4eM0WjErty38a/chJ0f14LNnjm3plQylBdGITmWwYv+HPwxpIW0cwQxiXlI2X0UHC5lBb/382UzXPOsOMse3Bz2JHQaFXpu1kM+NgTf4FWIfH0bePzZaXEFDgAskUh0KTVje9oXVWesVrs5DAYD8nfkQDHthbxDNWCxHR8fjubcSoDP56v+mZB5cblch0ldlXAHDgBsHo962t3Z6RAOABwOB7WXvwbtocaFsnds7g534QDAlskms3PSJPLbXV2O+jmVmA/82RALhcKJnzpuEYWROL0m9dMkLSuHvJaYTWrateTzZgM5fFVPorYWaSlvpgOAvRPKsQTDiGTuSqx9I4uU/qAhUVuLdAuBmyOWpoUuSwxMqEhcsoT4LV9JfPwCf50PfO5S7lIo5ElpyUlO14RMY8CUEQhY5qvTKkc7JsaebIAbc+4sHFZiWKUn98bV5EjFKbWAYdqxwLK7JTGs0pO7YypSc+WqsuXB32uwsH8LFySEMxJyIyGPlDpyd0xFdhQUaoWMqOV5gi0kfHx9p843Xid9TyZJZn6BVkAvXtld/SoWCxlRg1KpeMlkNC4BoAQwvQj8gf8A4zALCaZc4HoAAAAASUVORK5CYII="""
        self.img2 = tk.PhotoImage(data=test)
        self.clear = tk.Button(self, text="Clear", image = self.img2, command=self.clear_textarea)
        self.clear.grid(row=0, column=2)

        test = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAJASURBVFiF7Ze/bxJhGMe/7738KgeYMliNFrxouzAYoBo7GBMnoqNL42CcHTqYGCdaoDjYJiad/Bcah06auDi4kGjqQQcWoxX7A1MHG9DDQvve44BFftSDUugtfKZLnvfu+8nz5N67FzAZBgBKUvVbGX9RFiJMBN6PIImx0j7o1uZM6G2LwPiT1XeTysjEpHJa4hKrFedep7E+G2I4Br64StFIEF9//MKS+lnbFfrtegkJAMpChJvDu0GZSxd9cZV8cZWURLpQX/N7XZgKXZQdXHp1PqHeaBAgAj9uOAAIndzRSBDRSBCCyNNc93tduBuuSvhjH27WBE6S0eFqJ5gkvTRFAKh2QicaMk2gHkuvH5ha2zZPgEAP33zMj/y97sjEUMDtsGpKMrMohJ4/gscOADAwm5LMLMpWrgGQuxK4d3VMzuZ3piu6foT8f9i5hMDZYcM1hgJepx3XL53pKrxTTH8LTBdoGUFht4LlTO7nVlFzkt6bLyOTIM555NKdyxfcniGbsUA1vPTUJewL2Vig0guBQCxr+1b8/Xh5Nffo/rVxd32tZQRbBc3pEraehQNANhao8FPy/GZBczbXWgSIwHsZfsCn6bHyYT87bXfC0UT6ASNyt1t3GAQUN2ZDz43WdLAVkwOA8W7y/3vbdrKtwMZM6Fl34Z0xGMFgBIMRSADAGITQqZ85DQidwBj2awJ2C19J5b6fiITQCakv28LO+QrQeDhdKgtxpV+H0wMYg3BY+Pu9yt7UWmxivZ9ZHfEH09HnzEDjyiQAAAAASUVORK5CYII="""
        self.img3 = tk.PhotoImage(data=test)
        self.save = tk.Button(self, text="Save", image = self.img3, command=self.save_text)
        self.save.grid(row=0, column=3)


        self.scroll_y = tk.Scrollbar(self)
        self.scroll_y.grid(row=0, column=1)

        self.text = tk.Text(self)
        self.text.grid(row=0, column=1)

        self.text.configure(yscrollcommand=self.scroll_y.set)
        
        self.scroll_y.config(command=self.text.yview)

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.filemenu.add_command(label="New", command=self.donothing)
        # self.filemenu.add_command(label="Open", command=self.donothing)
        # self.filemenu.add_command(label="Save", command=self.donothing)
        # self.filemenu.add_command(label="Save as...", command=self.donothing)

        # self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # self.editmenu = tk.Menu(self.menubar, tearoff=0)
        # self.editmenu.add_command(label="Undo", command=self.donothing)

        # self.editmenu.add_separator()

        # self.editmenu.add_command(label="Cut", command=self.donothing)
        # self.editmenu.add_command(label="Copy", command=self.donothing)
        # self.editmenu.add_command(label="Paste", command=self.donothing)
        # self.editmenu.add_command(label="Delete", command=self.donothing)
        # self.editmenu.add_command(label="Select All", command=self.donothing)

        # self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        # self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        # self.helpmenu.add_command(label="Help Index", command=self.donothing)
        # self.helpmenu.add_command(label="About...", command=self.donothing)
        # self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.master.config(menu=self.menubar)

    def donothing(self):
       filewin = tk.Toplevel(self)
       button = tk.Button(filewin, text="Do nothing button")
       button.grid()
    def force_rtc(self):
        self.text.tag_config('warning', background="yellow", foreground="red")
        self.text.tag_config('OK', background="white", foreground="green")
        try:
            import isystem.connect as ic
            cmgr = ic.ConnectionMgr()
            cmgr.connectMRU('')
            debugCtrl = ic.CDebugFacade(cmgr)
            dataCtrl = ic.CDataController(cmgr)

            self.text.insert(tk.END, "Setting wakeup from tranciever value to Validated" + "\n")
            dataCtrl.modify(ic.IConnectDebug.fRealTime, 'BswM_EcuMWakeupState[0]', '2')
             # Check written value
            self.text.insert(tk.END, 'BswM_EcuMWakeupState[0] = ' + str(dataCtrl.evaluate(ic.IConnectDebug.fRealTime, 'BswM_EcuMWakeupState[0]').getLong()) + "\n", 'OK')
            self.text.insert(tk.END, "-----" + "\n")

            self.text.insert(tk.END, "Setting RTC wakeup value to Validated" + "\n")
            dataCtrl.modify(ic.IConnectDebug.fRealTime, 'BswM_EcuMWakeupState[2]', '2')
            self.text.insert(tk.END, 'BswM_EcuMWakeupState[2] = ' + str(dataCtrl.evaluate(ic.IConnectDebug.fRealTime, 'BswM_EcuMWakeupState[2]').getLong()) + "\n", 'OK')
            self.text.insert(tk.END, "-----" + "\n")

            self.text.insert(tk.END, "Setting EcuM_ValidatedWakeups value to 2080(both TRCV and RTC)" + "\n")
            dataCtrl.modify(ic.IConnectDebug.fRealTime, 'EcuM_ValidatedWakeups', '2080')
            self.text.insert(tk.END, 'EcuM_ValidatedWakeups = ' + str(dataCtrl.evaluate(ic.IConnectDebug.fRealTime, 'EcuM_ValidatedWakeups').getLong()) + "\n", 'OK')
            self.text.insert(tk.END, "-----" + "\n")


            # Search for line Rte_Write_my_function(my_variable);'.
            lineDesc = ic.CLineDescription(ic.CLineDescription.E_RESOURCE_FUNCTION,
                                            'Rte_Write_my_function(my_variable);',
                                            0,     # start at the beginning of a function
                                            True,  # perform search
                                            0,     # no limit
                                            ic.CLineDescription.E_SEARCH_ANY,
                                            ic.CLineDescription.E_MATCH_PLAIN,
                                            "}",
                                            0,
                                            fileLocation)

            lineLocation = addrCtrl.getSourceLocation(lineDesc)
            print('file: ', lineLocation.getFileName())
            print('line: ', lineLocation.getLineNumber())
            self.text.insert(tk.END, 'file: ' + lineLocation.getFileName() + "\n", 'OK')
            self.text.insert(tk.END, 'line: ' + lineLocation.getLineNumber() + "\n", 'OK')
        except:
            self.text.insert(tk.END, "Winidea is not present on this computer!" + "\n", 'warning')

    def clear_textarea(self):
        self.text.delete('1.0', tk.END)

    def save_text(self):
        f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.text.get(1.0, tk.END)) # starts from `1.0`, not `0.0`
        f.write(text2save)
        f.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)

    app.master.title("My testing interface")
    app.master.minsize(800, 400)
    app.mainloop()
