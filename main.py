import customtkinter as tk

class CustomTkinterApp:
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

root = tk.CTk()
app = CustomTkinterApp(root)
root.mainloop()
