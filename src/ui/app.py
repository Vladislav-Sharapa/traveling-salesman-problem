import tkinter as tk
from services import *
from graph import GraphGeneration
from script import TravellingSalesmanProblem
from .validators import validator
from matplotlib import pyplot as plt

class App(tk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.__register_validators()
        self.configure_gui()
        
        for c in range(8): parent.columnconfigure(index=c, weight=1)
        for r in range(8): parent.rowconfigure(index=r, weight=1)

        btn_generator = tk.Button(text="Сгенерировать", width=15, command=self.__graph_generation_button)
        btn_generator.grid(row=0, column=0, columnspan=4,  ipadx=70, ipady=6, padx=5)

        label1 = tk.Label(text="Vertex: ")
        label1.grid(row=1, column=0, sticky=tk.E)
        self.entry_vertex = tk.Entry(self.parent)
        self.entry_vertex.grid(row=1, column=0, columnspan=4)
        self.entry_vertex.config(validate ="key",validatecommand =(self.is_digit_validator, '%P')) 

        label2 = tk.Label(text="a: ")
        label2.grid(row=2, column=0, sticky=tk.E)
        self.entry_a = tk.Entry()
        self.entry_a.grid(row=2, column=0, columnspan=4)
        self.entry_a.config(validate ="key",validatecommand =(self.is_digit_validator, '%P')) 

        label3 = tk.Label(text="b: ")
        label3.grid(row=3, column=0, sticky=tk.E)
        self.entry_b = tk.Entry()
        self.entry_b.grid(row=3, column=0, columnspan=4)
        self.entry_b.config(validate ="key",validatecommand =(self.is_digit_validator, '%P')) 

        self.errmsg : tk.StringVar = tk.StringVar()
        self.error_label = tk.Label(foreground="red", textvariable=self.errmsg, wraplength=250)
        self.error_label.grid(row=5,column=4, columnspan=2)

        btn_solution = tk.Button(text="Solution", width=15, command=self.__solution_button)
        btn_solution.grid(row=5, column=0, columnspan=4,  ipadx=70, ipady=6, padx=5)

        btn_graphic = tk.Button(text="Graphic", width=15, command=self.__plot_button)
        btn_graphic.grid(row=6, column=0, columnspan=4,  ipadx=70, ipady=6, padx=5, pady=5)

        self.listbox = tk.Listbox()
        self.listbox.grid(row=0, column=4, columnspan=4, rowspan=4,  ipadx=70, ipady=25, padx=5)

    def configure_gui(self):
        self.parent.title("Course project")
        self.parent.geometry("750x350")

    def __register_validators(self):
        self.is_digit_validator = self.parent.register(validator)
        self.vertex_validator = self.parent.register(validator)


    def __solution_button(self):
        self.clear_listbox()
        matrix = read_file()
        obj = TravellingSalesmanProblem(matrix)
        obj.solve(1, 0)
        self.output_matrix()
        self.output_result(obj.min_cost, obj.shortest_path)
        obj.draw_solution()
        write_result_in_file(len(matrix), obj.algorithm_execution_time)

    def __graph_generation_button(self):
        self.clear_listbox()

        vertex = self.entry_vertex.get()
        a = self.entry_a.get()
        b = self.entry_b.get()

        if vertex == "" or a == "" or b == "":
            self.errmsg.set("Fields must not be empty")
            return
        if int(vertex) < 4:
            self.errmsg.set('Number of vertex must be 4 or higher')
            return
        self.errmsg.set('')
        try:
            obj = GraphGeneration(int(vertex), int(a), int(b))
            write_matrix_in_file(obj.generate_matrix())
            self.output_matrix()
        except ValueError as error:
            self.errmsg.set(error)
        
    def __plot_button(self):
        data = read_pair_from_file()
        print(data)
        x_values = [x for x, _ in data] 
        y_values = [y for _, y in data] 

        plt.scatter(x_values, y_values)
        plt.xlabel('Number of cities') 
        plt.ylabel('Algorithm execution time')  
        plt.title('Data graph')  

        plt.show()


    def output_matrix(self):
        matrix = read_file()
        for i in range(len(matrix)):
            row = '|'
            for j in range(len(matrix[i])):
                row += str(matrix[i][j]) + " "
            row += "|"
            self.listbox.insert('end', row)

    def output_result(self, min_cost, distant):
        self.listbox.insert('end', f"Minimum Distance Travelled -> {min_cost}")
        row = ''
        for i in distant:
            row += str(i) + "->"
        self.listbox.insert('end', f"Shortest path: {row}")

    def clear_listbox(self):
        self.listbox.delete(0, 'end')
