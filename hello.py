import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.hi_there = None
        self.master = master
        self.pack()
        self.create_widgets()
        self.lit = []

    def start_dimu_naki(self):
        entry1 = tk.Entry(root)

        canvas1.create_window(200, 140, window=entry1)

        label2 = tk.Label(self.master, text=f'Enter number of intigers you want to sum')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)

        def jogkorum(x):
            y = 0
            for i in x:
                y += int(i)
            return y

        def get_square_root():
            data = entry1.get()
            if data != '':
                self.lit.append(data)
            label3 = tk.Label(root, text='The sum of ' + str(len(self.lit)) + "th number" + ' is ',
                              font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)
            label4 = tk.Label(root, text=jogkorum(self.lit), font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)

        button = tk.Button(text='Get the Total sum', command=get_square_root, bg='brown', fg='white',
                           font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 180, window=button)
        print(sum(self.lit))

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.button = tk.Button(self, text="Start The process", fg="red",
                                command=self.start_dimu_naki)
        self.button.pack(side="bottom")


root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate total Sum')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

app = Application(master=root)
app.mainloop()
