import customtkinter as ctk
from page.home import Home
from page.login import Login
from page.signup import Signup
from page.settings import Settings


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title("Productivity Tracker and Timer")
        self.geometry("400x600+50+50")
        # self.minsize(800, 600)
        # self.maxsize(800, 600)

        self.page_class = {
            "Login": Login, 
            "Signup": Signup,
            "Home": Home, 
            "Settings": Settings
        }

        self.page = dict.fromkeys(self.page_class.keys())
        
        # self.showPage("Login")
        self.showPage("Home") # debug
            
    def showPage(self, page_name):
        if self.page[page_name] is None:
            self.initPage(page_name)
            
        self.page[page_name].tkraise() # pyright: ignore

    def initPage(self, page_name):
        f = self.page_class[page_name](self)
        f.grid(row=0, column=0, sticky="nesw")
        self.page[page_name] = f

    def deletePage(self, page_name):
        if self.page[page_name] is None:
            return

        self.page[page_name].destroy() # pyright: ignore
        self.page[page_name] = None

    def deletePageAll(self):
        for i in self.page_class.keys():
            self.deletePage(i)

    def reinitPage(self, page_name):
        self.deletePage(page_name)
        self.initPage(page_name)

    def reinitPageAll(self):
        for i in self.page_class.keys():
            self.reinitPage(i)


