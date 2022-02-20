from tkinter import *
from tkinter import messagebox
from sys import exit as exitt
from os import system
try:
    from pyperclip import copy
except ModuleNotFoundError:
    window = Tk()
    window.withdraw()
    messagebox.showwarning('pyperclip package missing', 'Missing package "pyperclip" for the working of this program. Click OK to attempt to install pyperclip for python.')
    status = system("python -m pip install pyperclip")
    if status != 0:
        messagebox.showerror('Error', "Couldn't install pyperclip automatically. Please try again manually in command prompt using command:\n\npip install pyperclip")
        window.destroy()
        exitt()
    else:
        window.destroy()
        pass
try:
    from main import Matrix
except ModuleNotFoundError:
    window = Tk()
    window.withdraw()
    messagebox.showerror('Matrix file not found', "Please save your python file containing the Matrix class in the same folder as this file and name it 'main.py'")
    window.destroy()
    exitt()


class MatrixGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Matrix Calculator GUI")

        self.root.minsize(500, 530)

        self.user_scr_width = self.root.winfo_screenwidth()
        self.user_scr_height = self.root.winfo_screenheight()
        root_x, root_y = (int(self.user_scr_width / 2 - 250), int(self.user_scr_height / 2 - 265))

        self.root.geometry(f"500x530+{root_x}+{root_y}")

        # colors
        self.darkest_gray = "#262626"
        self.dark_gray = "#363636"
        self.gray = "#404040"
        self.light_gray = "#464646"
        self.orange = "#edbc37"
        self.red = "#782a26"

        self.root.config(bg=self.darkest_gray)

        for i in range(2):
            Grid.columnconfigure(self.root, i, weight=1)
        Grid.rowconfigure(self.root, 1, weight=1)

        # MAIN FRAMES

        # main frame 1
        self.mainframe1 = Frame(self.root, bg=self.darkest_gray)

        self.ops_mainframe = Frame(self.mainframe1, bg=self.darkest_gray, height=65, highlightthickness=1, highlightbackground=self.gray)
        self.rcs_mainframe = Frame(self.mainframe1, bg=self.darkest_gray, height=65, highlightthickness=1, highlightbackground=self.gray)
        self.matrix_mainframe = Frame(self.mainframe1, bg=self.darkest_gray, highlightthickness=1, highlightbackground=self.gray)
        self.eval_frame = Frame(self.mainframe1, bg=self.darkest_gray, height=50)

        self.mainframe1.rowconfigure(1, weight=1)
        self.mainframe1.columnconfigure(0, weight=1)
        self.mainframe1.columnconfigure(1, weight=1)

        self.ops_mainframe.grid(row=0, column=0, sticky=NSEW)
        self.rcs_mainframe.grid(row=0, column=1, sticky=NSEW)
        self.matrix_mainframe.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        self.eval_frame.grid(row=2, column=0, columnspan=2, sticky=NSEW)

        self.draw_mainframe1()

        # operation selection
        self.ops_mainframe.rowconfigure(0, weight=1)
        for i in range(2):
            self.ops_mainframe.columnconfigure(i, weight=1)

        self.op_dict = {'Randomize': Matrix.randomize,
                        'Count': Matrix.count,
                        'Adjoint': Matrix.adjoint,
                        'Determinant': Matrix.determinant,
                        'Inverse': Matrix.inverse,
                        'Transpose': Matrix.transpose,
                        'Raw Input': Matrix}

        self.op_select_label = Label(self.ops_mainframe, bg=self.darkest_gray,
                                     text="Select:", fg="white", width=10) \
            .grid(row=0, column=0, sticky=E)

        self.op_value_inside = StringVar()
        self.op_value_inside.set("Randomize")
        self.op_active_function = self.op_dict.get(self.op_value_inside.get())

        self.op_select_menu = OptionMenu(self.ops_mainframe, self.op_value_inside, *self.op_dict.keys(), command=lambda e: self.set_function_labels())
        self.op_select_menu.config(bg=self.dark_gray, fg="white", width=10)
        self.op_select_menu["menu"].config(bg=self.dark_gray, fg="white")
        self.op_select_menu.grid(row=0, column=1, sticky=W)

        # row column selection
        self.rcs_mainframe.rowconfigure(0, weight=1)
        for i in range(5):
            self.rcs_mainframe.columnconfigure(i, weight=1)

        self.rs_label = Label(self.rcs_mainframe, bg=self.darkest_gray, fg="white", text="R:",
                              width=4).grid(row=0, column=0, sticky=E)
        self.rs_rawvalue = StringVar()
        self.rs_rawvalue.set("3")
        self.rs_value = self.rs_rawvalue.get()
        self.rs_entry = Entry(self.rcs_mainframe, bg=self.dark_gray, fg="white",
                              textvariable=self.rs_rawvalue, width=3)
        self.rs_entry.grid(row=0, column=1, sticky=W)

        self.cs_label = Label(self.rcs_mainframe, bg=self.darkest_gray, fg="white", text="C:",
                              width=4)
        self.cs_label.grid(row=0, column=2, sticky=E)
        self.cs_rawvalue = StringVar()
        self.cs_rawvalue.set("3")
        self.cs_value = self.cs_rawvalue.get()
        self.cs_entry = Entry(self.rcs_mainframe, bg=self.dark_gray, fg="white",
                              textvariable=self.cs_rawvalue, width=3)
        self.cs_entry.grid(row=0, column=3, sticky=W)

        self.cs_entry.bind("<KeyRelease>", lambda event="<KeyRelease>": self.draw_matrix_grid(event))
        self.rs_entry.bind("<KeyRelease>", lambda event="<KeyRelease>": self.draw_matrix_grid(event))

        # matrix field
        self.matrix_rows_entries = []
        self.matrix_rows_rawvalues = []
        self.given_matrix = []
        self.draw_matrix_grid(event="none")

        # bottom frame
        self.eval_frame.rowconfigure(0, weight=1)
        for i in range(2, 6):
            self.eval_frame.columnconfigure(i, weight=1)
        self.eval_button = Button(self.eval_frame, bg=self.gray, fg=self.orange,
                                  text="Evaluate", command=self.print_result, width=8,
                                  activebackground=self.dark_gray, activeforeground=self.orange)
        self.eval_button.grid(row=0, column=0, sticky=NS + W, padx=3)
        self.copy_button = Button(self.eval_frame, bg=self.gray, fg=self.orange,
                                  text="Copy Raw", command=self.copy_given_matrix, width=8,
                                  activebackground=self.dark_gray, activeforeground=self.orange)
        self.copy_button.grid(row=0, column=1, sticky=W, padx=3)

        # values for active function
        self.func_temp_label1 = Label(self.eval_frame, bg=self.darkest_gray, fg="white",
                                      width=6, text="lowest:")
        self.func_temp_rawval1 = StringVar()
        self.func_temp_entry1 = Entry(self.eval_frame, bg=self.dark_gray, fg="white",
                                      width=5, textvariable=self.func_temp_rawval1)

        self.func_temp_label2 = Label(self.eval_frame, bg=self.darkest_gray, fg="white",
                                      width=6, text="highest:")
        self.func_temp_rawval2 = StringVar()
        self.func_temp_entry2 = Entry(self.eval_frame, bg=self.dark_gray, fg="white",
                                      width=5, textvariable=self.func_temp_rawval2)
        self.set_function_labels()

        # result page
        self.mainframe2 = Frame(self.root, bg=self.darkest_gray)
        self.mainframe2.rowconfigure(0, weight=1)
        self.mainframe2.columnconfigure(0, weight=1)

        self.result_frame = Frame(self.mainframe2, bg=self.darkest_gray, highlightthickness=1, highlightbackground=self.gray)
        self.copy_frame = Frame(self.mainframe2, height=60, bg=self.dark_gray, highlightthickness=1, highlightbackground=self.gray)

        self.result_frame.grid(row=0, column=0, sticky=NSEW)
        self.copy_frame.grid(row=1, column=0, sticky=EW)

        self.copy_frame.columnconfigure(0, weight=1)

        self.given_matrix_result = "None"

        self.copy_result_button = Button(self.copy_frame, text="Copy Result", bg=self.orange, fg="black",
                                         activebackground=self.red, command=self.copy_result,
                                         width=15)
        self.copy_result_button.grid(row=0, column=0, columnspan=2, sticky=NS, pady=3)

        # categories menu
        self.category_menuframe = Frame(self.root,
                                        bg=self.gray,
                                        height=35
                                        )
        self.category_selection = 0

        Grid.rowconfigure(self.category_menuframe, 0, weight=1)

        self.oper_button = Button(
            self.category_menuframe,
            fg="white",
            bg=self.gray,
            activebackground=self.gray,
            activeforeground="white",
            width=10,
            border=1,
            text="Operation",
            disabledforeground="white",
            command=lambda sel=0: self.category_select(sel),
            relief=FLAT)
        self.result_button = Button(
            self.category_menuframe,
            fg="white",
            bg=self.gray,
            activebackground=self.gray,
            activeforeground="white",
            width=10,
            border=1,
            text="Result",
            disabledforeground="white",
            command=lambda sel=1: self.category_select(sel),
            relief=FLAT)

        self.oper_button.grid(row=0, column=0, sticky=NS)
        self.result_button.grid(row=0, column=1, sticky=NS)

        self.category_select(0)
        self.category_menuframe.grid(row=0, column=0, sticky=NSEW, columnspan=2)

    def copy_given_matrix(self):
        self.get_matrix()
        copy(str(self.given_matrix))

    def copy_result(self):
        copy(str(self.given_matrix_result))

    def draw_mainframe1(self):
        self.mainframe1.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    def draw_mainframe2(self):
        self.mainframe2.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    def remove_mainframe1(self):
        self.mainframe1.grid_remove()

    def remove_mainframe2(self):
        self.mainframe2.grid_remove()

    def set_function_labels(self):
        self.op_active_function = self.op_dict.get(self.op_value_inside.get())
        self.func_temp_entry1.config(width=5)
        self.func_temp_label1.grid_remove()
        self.func_temp_entry1.grid_remove()
        self.func_temp_label2.grid_remove()
        self.func_temp_entry2.grid_remove()
        self.func_temp_rawval1.set("0")
        self.func_temp_rawval2.set("0")

        if self.op_value_inside.get().lower() == "randomize":
            self.func_temp_label1.config(text="lowest:")
            self.func_temp_label2.config(text="highest:")
            self.func_temp_rawval1.set("0")
            self.func_temp_rawval2.set("100")

            self.func_temp_label1.grid(row=0, column=2, sticky=E)
            self.func_temp_entry1.grid(row=0, column=3, sticky=W, padx=3)
            self.func_temp_label2.grid(row=0, column=4, sticky=E)
            self.func_temp_entry2.grid(row=0, column=5, sticky=W, padx=3)

        elif self.op_value_inside.get().lower() == "count":
            self.func_temp_label1.config(text="element:")

            self.func_temp_label1.grid(row=0, column=2, sticky=E)
            self.func_temp_entry1.grid(row=0, column=3, sticky=W, padx=3)

        elif self.op_value_inside.get().lower() == "raw input":
            self.func_temp_label1.config(text="input:")
            self.func_temp_entry1.config(width=12)
            self.func_temp_rawval1.set("")

            self.func_temp_label1.grid(row=0, column=2, sticky=E)
            self.func_temp_entry1.grid(row=0, column=3, columnspan=5, sticky=W, padx=3)

    def get_result(self):
        self.cs_entry.config(bg=self.dark_gray)
        self.rs_entry.config(bg=self.dark_gray)
        self.get_matrix()
        if self.func_temp_rawval1.get() == "":
            self.func_temp_rawval1.set("0")
        if self.func_temp_rawval2.get() == "":
            self.func_temp_rawval1.set("0")

        if self.op_value_inside.get() == "Randomize":
            if (self.func_temp_rawval1.get()[0] == "-" and self.func_temp_rawval1.get()[1:].isdecimal()) or (self.func_temp_rawval1.get().isdecimal()):
                if (self.func_temp_rawval1.get()[0] == "-" and self.func_temp_rawval1.get()[1:].isdecimal()) or (self.func_temp_rawval1.get().isdecimal()):
                    if int(self.func_temp_rawval2.get()) >= int(self.func_temp_rawval1.get()):
                        self.func_temp_entry1.config(bg=self.dark_gray)
                        self.func_temp_entry2.config(bg=self.dark_gray)
                        self.given_matrix_result = self.op_active_function(Matrix(self.given_matrix), int(self.func_temp_rawval1.get()), int(self.func_temp_rawval2.get()))
                    else:
                        self.func_temp_entry1.config(bg=self.red)
                        self.func_temp_entry2.config(bg=self.red)
                else:
                    self.func_temp_entry1.config(bg=self.red)
                    self.func_temp_entry2.config(bg=self.red)
            else:
                self.func_temp_entry1.config(bg=self.red)
                self.func_temp_entry2.config(bg=self.red)
        elif self.op_value_inside.get() == "Count":
            if (self.func_temp_rawval1.get()[0] == "-" and self.func_temp_rawval1.get()[1:].isdecimal()) or (self.func_temp_rawval1.get().isdecimal()):
                self.func_temp_entry1.config(bg=self.dark_gray)
                self.func_temp_entry2.config(bg=self.dark_gray)
                self.given_matrix_result = self.op_active_function(Matrix(self.given_matrix))
            else:
                self.func_temp_entry1.config(bg=self.red)
        elif self.op_value_inside.get() == "Transpose":
            self.func_temp_entry1.config(bg=self.dark_gray)
            self.func_temp_entry2.config(bg=self.dark_gray)
            self.given_matrix_result = self.op_active_function(Matrix(self.given_matrix))
        elif self.op_value_inside.get() == "Determinant" or self.op_value_inside.get() == "Adjoint" or self.op_value_inside.get() == "Inverse":
            if int(self.cs_value) == int(self.rs_value):
                if int(self.cs_value) <= 8:
                    self.func_temp_entry1.config(bg=self.dark_gray)
                    self.func_temp_entry2.config(bg=self.dark_gray)
                    self.given_matrix_result = self.op_active_function(Matrix(self.given_matrix))
                else:
                    self.cs_entry.config(bg=self.red)
                    self.rs_entry.config(bg=self.red)
                    self.given_matrix_result = "Your matrix is too large for this operation!\n(max allowed: 8x8)"
            else:
                self.cs_entry.config(bg=self.red)
                self.rs_entry.config(bg=self.red)
                self.given_matrix_result = "Your matrix must be a Square Matrix for this operation!"
        elif self.op_value_inside.get() == "Raw Input":
            templist = eval(self.func_temp_rawval1.get())
            self.cs_rawvalue.set(len(templist[0]))
            self.rs_rawvalue.set(len(templist))
            self.draw_matrix_grid(event="none")
            try:
                if type(Matrix(templist)) is Matrix:
                    for x in range(len(templist)):
                        for y in range(len(templist[x])):
                            self.matrix_rows_rawvalues[x][y].set(str(templist[x][y]))
                    self.given_matrix_result = "Table updated with given matrix"
                else:
                    self.func_temp_entry1.config(bg=self.red)
                    self.given_matrix_result = "invalid"
            except TypeError:
                self.func_temp_entry1.config(bg=self.red)
                self.given_matrix_result = "invalid"
        else:
            self.func_temp_entry1.config(bg=self.dark_gray)
            self.func_temp_entry2.config(bg=self.dark_gray)
            self.given_matrix_result = "invalid"

    def print_result(self):
        self.get_result()
        self.category_select(1)
        self.recreate_result_frame()

        for x in range(20):
            self.result_frame.rowconfigure(x, weight=1)
        for y in range(20):
            self.result_frame.columnconfigure(y, weight=1)

        if type(self.given_matrix_result) is str or type(self.given_matrix_result) is int:
            Label(self.result_frame, text=str(self.given_matrix_result), bg=self.darkest_gray,
                  fg=self.orange).grid(row=0, column=0, columnspan=4, sticky=EW, padx=20, pady=10)

        elif type(self.given_matrix_result) is dict:
            for i, j in self.given_matrix_result.items():
                ind = list(self.given_matrix_result.keys()).index(i)
                if str(i) == str(self.func_temp_rawval1.get()):
                    Label(self.result_frame, text=str(str(i) + " : " + str(j)), width=3, bg=self.orange,
                          fg="black").grid(row=ind // 7, column=(ind % 7) * 3, columnspan=3, sticky=NSEW, padx=2, pady=2)
                else:
                    Label(self.result_frame, text=str(str(i) + " : " + str(j)), width=3, bg=self.darkest_gray,
                          fg="white").grid(row=ind // 7, column=(ind % 7) * 3, columnspan=3, sticky=NSEW, padx=2, pady=2)

        elif type(self.given_matrix_result) is Matrix:
            temp_result_list = list(self.given_matrix_result)
            for x in range(len(temp_result_list)):
                for y in range(len(temp_result_list[x])):
                    Label(self.result_frame, bg=self.darkest_gray, fg="white",
                          text=str(temp_result_list[x][y])[:4], width=4) \
                        .grid(row=x, column=y, padx=3, pady=3)

    def draw_matrix_grid(self, event):
        self.recreate_matrix_frame()
        for x in range(20):
            self.matrix_mainframe.rowconfigure(x, weight=1)
            for y in range(20):
                self.matrix_mainframe.columnconfigure(y, weight=1)
        self.rs_value = self.rs_rawvalue.get()
        self.cs_value = self.cs_rawvalue.get()
        if self.cs_value.isdecimal() and self.rs_value.isdecimal():
            self.cs_entry.config(bg=self.dark_gray)
            self.rs_entry.config(bg=self.dark_gray)
            if int(self.cs_value) > 20:
                self.cs_rawvalue.set("20")
            elif int(self.rs_value) > 20:
                self.rs_rawvalue.set("20")
            self.rs_value = self.rs_rawvalue.get()
            self.cs_value = self.cs_rawvalue.get()
            if int(self.cs_value) > 10 or int(self.rs_value) > 15:
                self.root.minsize(943, 772)
            else:
                self.root.minsize(500, 530)
                self.root.geometry("500x530")

            if int(self.cs_value) > 0 and int(self.rs_value) > 0:
                self.matrix_rows_entries = []
                self.matrix_rows_rawvalues = []
                for x in range(int(self.rs_value)):
                    self.matrix_rows_entries.append([])
                    self.matrix_rows_rawvalues.append([])
                    for y in range(int(self.cs_value)):
                        matrix_rawvalue = StringVar()
                        matrix_rawvalue.set("0")
                        self.matrix_rows_rawvalues[x].append(matrix_rawvalue)
                        self.matrix_rows_entries[x].append(Entry(
                            self.matrix_mainframe, bg=self.dark_gray, fg="white",
                            textvariable=self.matrix_rows_rawvalues[x][y], width=4))
                        self.matrix_rows_entries[x][y].grid(row=x, column=y, padx=4, pady=4)
            else:
                self.cs_entry.config(bg=self.red)
                self.rs_entry.config(bg=self.red)
        else:
            self.cs_entry.config(bg=self.red)
            self.rs_entry.config(bg=self.red)

    def get_matrix(self):
        messed_up = False
        self.given_matrix = []
        for x in range(int(self.rs_value)):
            self.given_matrix.append([])
            for y in range(int(self.cs_value)):
                if self.matrix_rows_rawvalues[x][y].get() == "":
                    self.matrix_rows_rawvalues[x][y].set("0")
                elif self.matrix_rows_rawvalues[x][y].get()[0] == "-":
                    if self.matrix_rows_rawvalues[x][y].get()[1:].isdecimal():
                        self.given_matrix[x].append(int(self.matrix_rows_rawvalues[x][y].get()))
                    else:
                        self.matrix_rows_entries[x][y].config(bg=self.red)
                        messed_up = True
                elif (self.matrix_rows_rawvalues[x][y].get()).isdecimal() or self.matrix_rows_rawvalues[x][y].get() == "0":
                    self.given_matrix[x].append(int(self.matrix_rows_rawvalues[x][y].get()))
                    self.matrix_rows_entries[x][y].config(bg=self.dark_gray)
                else:
                    self.matrix_rows_entries[x][y].config(bg=self.red)
                    messed_up = True

        if messed_up:
            self.given_matrix = []

    def recreate_matrix_frame(self):
        for widgs in self.matrix_mainframe.winfo_children():
            widgs.destroy()

    def recreate_result_frame(self):
        for widgs in self.result_frame.winfo_children():
            widgs.destroy()

    def category_select(self, sel):
        self.category_selection = sel
        if sel == 0:
            self.oper_button.config(
                bg=self.darkest_gray,
                activebackground=self.darkest_gray,
                state=DISABLED
            )
            self.result_button.config(
                bg=self.gray,
                activebackground=self.gray,
                state=ACTIVE
            )
            self.draw_mainframe1()
            self.remove_mainframe2()

        else:
            self.result_button.config(
                bg=self.darkest_gray,
                activebackground=self.darkest_gray,
                state=DISABLED
            )
            self.oper_button.config(
                bg=self.gray,
                activebackground=self.gray,
                state=ACTIVE
            )
            self.draw_mainframe2()
            self.remove_mainframe1()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    MatrixGUI().start()
