import customtkinter
import pyautogui
from PIL import Image

ico_uptade = customtkinter.CTkImage(light_image=Image.open('перезагрузка.png'), dark_image=Image.open('перезагрузка.png'), size=(30, 30))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        # add widgets to app
        #self.button = customtkinter.CTkButton(self, command=self.button_click)
        #self.button.grid(row=0, column=0, padx=20, pady=10)

        self.segemented_button = customtkinter.CTkSegmentedButton(self, values=["Value 1", "Value 2", "Value 3"],command=self.segmented_button_callback)
        self.segemented_button.grid(row=0, column=0, padx=20, pady=10)
        self.segemented_button.set("Value 1")

        self.updatebtn = customtkinter.CTkButton(self, width=30, height=30, command=self.button_click, image=ico_uptade)
        self.updatebtn.grid(padx=20, pady=30)


    # add methods to app
    def button_click(self):
        print("button click")

    def segmented_button_callback(value):
        print("segmented button clicked:", value)

app = App()
app.mainloop()