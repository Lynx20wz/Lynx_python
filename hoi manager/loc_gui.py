import os
from time import sleep
from tkinter import filedialog

import customtkinter


# from loc import work


class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.resizable(False, False)
        self.title("Помощник локализации")
        self.attributes('-topmost', True)  # закрепить наверху
        self.grid_columnconfigure((0, 1), weight=1)
        self.mode = customtkinter.IntVar(value=1)

        self.setting_frame = customtkinter.CTkFrame(self, width=600)
        self.setting_frame.grid(column=0, row=1, padx=15, pady=10, sticky="ew")

        self.window_with_file = customtkinter.CTkEntry(
                master=self, width=400, placeholder_text='Введите путь к файлу', corner_radius=0
        )
        self.window_with_file.grid(row=0, column=0, padx=(5, 0), pady=(20, 0), sticky='e')

        self.clipboard = customtkinter.CTkButton(
                master=self, text='Вставить', command=self.btn_clip, width=60, corner_radius=0
        )
        self.clipboard.grid(row=0, column=0, padx=0, pady=(20, 0), sticky='e')

        self.btn_open = customtkinter.CTkButton(
                master=self, text='Открыть файл', command=self.open_file, corner_radius=0
        )
        self.btn_open.grid(row=0, column=1, padx=(10, 5), pady=(20, 0), sticky='w')

        self.chance_mode1 = customtkinter.CTkRadioButton(
                self.setting_frame, variable=self.mode, value=1, text='Авто-локализация'
        )
        self.chance_mode1.grid(row=1, column=0, padx=23, pady=(10, 5), sticky='w')
        self.chance_mode2 = customtkinter.CTkRadioButton(
                self.setting_frame, variable=self.mode, value=2, text='Сделать заготовку'
        )
        self.chance_mode2.grid(row=2, column=0, padx=23, pady=(5, 10), sticky='w')

        self.need_zero = customtkinter.StringVar(value='нет')
        self.check_zero = customtkinter.CTkCheckBox(
                self.setting_frame, text='Вставлять ли "0"?', variable=self.need_zero, onvalue='да', offvalue='нет'
        )
        self.check_zero.grid(row=1, column=1, pady=(10, 5), sticky='w')

        self.need_space = customtkinter.StringVar(value='нет')
        self.check_space = customtkinter.CTkCheckBox(
                self.setting_frame, text='Вставлять ли пробелы?', variable=self.need_space, onvalue='да', offvalue='нет'
        )
        self.check_space.grid(row=2, column=1, pady=(5, 10), sticky='w')

    def open_file(self):
        possible_file = self.window_with_file.get().replace('"', '').strip()
        if possible_file == '':
            file = filedialog.askopenfilename(
                    title='Выберете файл для локализации', filetypes=[('Файл hoi4', '*.txt')]
            )
            if file == '':
                self.window_with_file.configure(
                        placeholder_text='Файл не выбран!', placeholder_text_color='red3'
                )
                self.update()
                sleep(2)
                self.window_with_file.configure(
                        placeholder_text='Введите путь к файлу', placeholder_text_color=('gray52', 'gray62')
                )
        elif os.path.isfile(possible_file):
            file = possible_file

    def btn_clip(self):
        clip_text = self.clipboard_get()
        self.window_with_file.insert(0, clip_text)


if __name__ == '__main__':
    app = Gui()
    app.mainloop()
