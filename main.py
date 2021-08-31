from tkinter import *
from tkinter import messagebox


class Window:
    def __init__(self, width, height, x, y, title, resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)
        self.root['bg'] = '#323232'

    def draw_widget(self):
        def add_digit(digit):
            value = calc.get()
            if value[0] == '0' and len(value) == 1:
                value = value[1:]
            calc.delete(0, END)
            calc.insert(0, value+digit)

        def add_operation(operation):
            value = calc.get()
            if value[-1] in '-+/*':
                value = value[:-1]
            elif '+' in value or '-' in value or '/' in value or '*' in value:
                calculate()
                value = calc.get()
            calc.delete(0, END)
            calc.insert(0, value+operation)

        def calculate():
            value = calc.get()
            if value[-1] in '+-/*':
                value = value+value[:-1]
            calc.delete(0, END)
            try:
                calc.insert(0, eval(value))
            except (NameError, SyntaxError):
                messagebox.showinfo('Внимание', 'Нужно вводить только цифры!')
                calc.insert(0, 0)
            except ZeroDivisionError:
                messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
                calc.insert(0, 0)

        def clear():
            calc.delete(0, END)
            calc.insert(0, 0)

        def make_operation_button(operation):
            return Button(self.root, text=operation, font='Arial 13', bd=0, bg='#323232',  fg='#FFA310',
                          command=lambda: add_operation(operation))

        def make_calc_button(operation):
            return Button(self.root, text=operation, font='Arial 13', bd=0, bg='#323232',  fg='#FFA310',
                          command=calculate)

        def make_clear_button(operation):
            return Button(self.root, text=operation, font='Arial 13', bd=0, bg='#323232',  fg='#FFA310',
                          command=clear)

        def make_button(digit):
            return Button(self.root, text=digit, font='Arial 13', bd=0, bg='#323232', fg='white',
                          command=lambda: add_digit(digit))

        def press_key(event):
            if event.char.isdigit():
                add_digit(event.char)
            elif event.char in '+-/*':
                add_operation(event.char)
            elif event.char == '\r':
                calculate()

        self.root.bind('<Key>', press_key)

        calc = Entry(self.root, justify=RIGHT, font='Arial 15', width=15, bd=0)
        calc.insert(0, 0)
        calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

        make_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
        make_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
        make_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
        make_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
        make_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
        make_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
        make_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
        make_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
        make_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
        make_button('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)

        make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

        make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
        make_clear_button('C').grid(row=4, column=0, stick='wens', padx=5, pady=5)

        self.root.grid_columnconfigure(0, minsize=60)
        self.root.grid_columnconfigure(1, minsize=60)
        self.root.grid_columnconfigure(2, minsize=60)
        self.root.grid_columnconfigure(3, minsize=60)

        self.root.grid_rowconfigure(1, minsize=60)
        self.root.grid_rowconfigure(2, minsize=60)
        self.root.grid_rowconfigure(3, minsize=60)
        self.root.grid_rowconfigure(4, minsize=60)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(240, 270, 100, 200, 'Calc')
    window.draw_widget()
    window.run()
