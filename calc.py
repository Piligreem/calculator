from tkinter import *


class Calculator:

    def logic(self, btn: str) -> None:
        '''Управяет логикой кнопок'''
        simple_btn = (
            '.', '+', '-', '%', '/', '*',
            '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '(', ')',
            )
        try:
            if btn in simple_btn:
                self.input.insert(END, btn)
            elif btn == 'C':
                self.input.delete(0, END)
            elif btn == '=':
                answer = eval(self.input.get())
                self.input.delete(0, END)
                self.input.insert(END, f'{answer}')
            elif btn == '^2':
                self.input.insert(END, '**2')
            elif btn == 'sqrt':
                self.input.insert(END, 'sqrt(')
            elif btn == 'Del':
                end = len(self.input.get())
                self.input.delete(end-1, end)
            elif btn == '1/x':
                self.input.insert(END, '(1/')
        
        except (SyntaxError, NameError, TypeError):
            self.input.delete(0, END)

    def __init__(self):
        self.window = Tk()
        self.window.title('Calculator')
        self.window.iconbitmap('./icon.ico')
        self.window.geometry('492x438')
        self.window.configure(background='#cce2e7')
        self.window.resizable(width=False, height=False)

        self.btns = (
            (),  # Для того, чтобы поместить поле ввода на строку 0
            ('7', '8', '9', '-', '*', '(',),
            ('4', '5', '6', '+', '/', ')',),
            ('1', '2', '3', '=', '%', 'sqrt',),
            ('0', '.', 'x^2', '1/x', 'C', 'Del',),
        )

        self.input = Entry(
            textvariable=StringVar(),
            width=25,
            cursor=None,
            justify='right',
            font='Courier 20',
            bg='#BAD1CE',
            fg='black'
        )
        self.input.grid(
            row=0,
            column=0,
            columnspan=6,
            ipady=30,
        )
        # Добавление кнопок на окно
        for row in range(1, len(self.btns)):
            for column in range(len(self.btns[row])):
                name_btn = self.btns[row][column]
                btn = Button(
                    text=name_btn,
                    activebackground='#8B9BAC',
                    activeforeground='black',
                    background='#006497',
                    foreground='white',
                    width=8,
                    height=4,
                    font='16',
                    command=lambda x=name_btn: self.logic(x), # связывание функции кнопки с методом обработки логики кнопок
                )
                btn.grid(
                    row=row,
                    column=column
                )

        self.window.mainloop()

Calculator()
