import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_0():
    messagebox.showinfo("Names",f"Name_0: {name0.get()}\nName_1: {name1.get()}\nName_2: {name2.get()}\n")

def submit_1():
    messagebox.showinfo("Values",f"Value_0: {value0.get()}\nValue_1: {value1.get()}\nValue_2: {value2.get()}\n")



class Form(tk.Tk):


    def __init__(self):
       super().__init__()
       self.title("Tkinter example without formatting")
       self.index = 0
       self.left_column, self.right_column = 1, 2
       self.value_radio = tk.IntVar()
       self.value_radio.set(2)
       

    " LABEL "

    def main_label(self, text):
        label = ttk.Label (self, text=text )
        label.grid(
            pady=(0,10),
            padx=(5,0),
            row = self.index
        )
        self.index += 1

    def param_label(self, text):
        label = ttk.Label (self, text=text )
        label.grid(
            row = self.index,
            column = self.left_column
        )
        self.index += 1


    " ENTRY "

    def input_field(self):
        value_entry = tk.StringVar()
        entry = ttk.Entry(self, textvariable = value_entry)
        entry.grid(
            padx = (20,20),
            row = self.index - 1,
            column = self.right_column
        )
        self.index += 1
        return value_entry


    " SPINBOX "

    def spin_box(self, set_spinbox):
        value_spinbox = tk.IntVar()
        value_spinbox.set(set_spinbox)
        spin = ttk.Spinbox (self,values=(1,2,3,4,5),textvariable=value_spinbox,state='readonly')
        spin.grid(
            row=self.index - 1,
            column=self.right_column
        )
        self.index += 1
        return value_spinbox


    " COMBOBOX "

    def combo_box(self, inputValues):
        value_combo = tk.StringVar()
        values = ttk.Combobox(self, textvariable=value_combo)
        values["values"] = (inputValues)
        values["state"] = "readonly"
        values.grid(
            row=self.index-1,
            column=self.right_column
        )
        self.index += 1
        return value_combo


    " RADIO BUTTON "

    def radio_button(self, text,value):
        radioButton = ttk.Radiobutton (self, text=text, variable=self.value_radio, value=value)
        radioButton.grid(
            row=self.index-1,
            column=self.right_column,
        )
        self.index += 1


    " NOTEBOOK -> TAB "

    def notebook(self, text):
        t = ttk.Notebook(self)
        tab1 = ttk.Frame(t)
        t.add(tab1, text=text)
        t.grid(
            pady = (0,10),
            row = 0,
            column = self.index
        )
        self.index += 1
        

    " BUTTON "

    def submit_button(self, submit):
        button = tk.Button(self, text="submit", command=submit)
        button.grid(pady=(20,20),row=self.index, column = 2)
        self.index += 1



if __name__ == "__main__":
    
    combo_values = ["Juni","July","August"]

    tc = Form()
    
    tc.notebook("Tab_1")
    tc.notebook("Tab_2")
    tc.main_label("FORM_0")
    tc.param_label("Name_0:")
    name0 = tc.input_field()
    tc.param_label("Name_1:")
    name1 = tc.input_field()
    tc.param_label("Name_2:")
    name2 = tc.input_field()
    tc.submit_button(submit_0)
    tc.main_label("FORM_1")
    tc.param_label("Value_0:")
    value0 = tc.spin_box(5)
    tc.param_label("Value_1:")
    value1 = tc.combo_box(combo_values)
    tc.param_label("Value_2:")
    tc.radio_button("A <- 1",1)
    tc.radio_button("B <- 2",2)
    value2 = tc.value_radio
    tc.submit_button(submit_1)
    
    tc.mainloop()
