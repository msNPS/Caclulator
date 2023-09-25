import customtkinter as tk
import math

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Add Two Numbers")

        self.label1 = tk.CTkLabel(master, text="Enter first number:")
        self.label1.pack(padx=50, pady=5)

        self.entry1 = tk.CTkEntry(master)
        self.entry1.pack(padx=50, pady=5)

        self.label2 = tk.CTkLabel(master, text="Enter second number:")
        self.label2.pack(padx=50, pady=5)

        self.entry2 = tk.CTkEntry(master)
        self.entry2.pack(padx=50, pady=5)

        self.button = tk.CTkButton(master, text="Add", command=self.add_numbers)
        self.button.pack(padx=50, pady=10)

        self.floor_button = tk.CTkButton(master, text="Floor Answer", command=self.floor_answer)
        self.floor_button.pack(padx=50, pady=10)

        self.ceil_button = tk.CTkButton(master, text="Ceil Answer", command=self.ceil_answer)
        self.ceil_button.pack(padx=50, pady=10)

        self.sqrt_button = tk.CTkButton(master, text="Square Root", command=self.sqrt_answer)
        self.sqrt_button.pack(padx=50, pady=10)

        self.result_label = tk.CTkLabel(master, text="")
        self.result_label.pack(padx=50, pady=10)

    def add_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            self.result_label.configure(text=f"The sum is: {result}")
        except ValueError:
            self.result_label.configure(text="Only enter real or integer numbers")

    def floor_answer(self):
        try:
            result = float(self.result_label.cget("text").split(": ")[1])
            floor_result = math.floor(result)
            self.result_label.configure(text=f"The sum is: {floor_result}")
        except IndexError:
            self.result_label.configure(text="Please add two numbers first")
        except ValueError:
            self.result_label.configure(text="The result is not a number")

    def ceil_answer(self):
        try:
            result = float(self.result_label.cget("text").split(": ")[1])
            ceil_result = math.ceil(result)
            self.result_label.configure(text=f"The sum is: {ceil_result}")
        except IndexError:
            self.result_label.configure(text="Please add two numbers first")
        except ValueError:
            self.result_label.configure(text="The result is not a number")

    def sqrt_answer(self):
        try:
            result = float(self.result_label.cget("text").split(": ")[1])
            sqrt_result = math.sqrt(result)
            self.result_label.configure(text=f"The sum is: {sqrt_result}")
        except IndexError:
            self.result_label.configure(text="Please add two numbers first")
        except ValueError:
            self.result_label.configure(text="The result is not a number")

tk.set_appearance_mode("light")
root = tk.CTk()
app = CalculatorGUI(root)
root.mainloop()