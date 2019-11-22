from tkinter import *


class Topics:
    def __init__(self):
        self.v = []
        self.root = Tk()
        self.root.title('Topics')
        self.root.geometry('750x750')
        #self.bP=Button(self.root, text="Publish", width=10, height=1, command=self.adaugare_topic).pack()
        self.menubar=Menu(self.root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Add", command=self.adaugare_topic)
        filemenu.add_command(label="Erase", command=self.stergere_topic)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(self.menubar, tearoff=0)

        editmenu.add_separator()

        self.root.config(menu=self.menubar)
        self.root.mainloop()


    def adaugare_topic(self):
        self.labelTopic = Label(self.root, text="Nume topic ")
        self.labelTopic.grid(row=0, column=0)
        self.entryTopic = Entry(self.root)

        self.entryTopic.grid(row=1, column=0)
        self.buttonOk = Button(self.root, text='OK', command=self.add)
        self.buttonOk.grid(row=3, column=0)

    def add(self):
        self.v.append(self.entryTopic.get())
        self.textbox=Text(self.root, height=10, width=30)
        self.textbox.grid(row=4,column=0)

        for i in self.v:
            self.textbox.insert(INSERT+'\n',i+'\n')


    def stergere_topic(self):
        add = Toplevel(self.root)
        button = Button(add, text="Stergere topic")
        button.pack()



