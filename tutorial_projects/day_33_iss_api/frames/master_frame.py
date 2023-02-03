import tkinter as tk
import abc
from global_data import GlobalData


class MasterFrame(tk.Frame, metaclass=abc.ABCMeta):
    def __init__(self, master, global_data: GlobalData):
        super().__init__(master=master)
        self.global_data: GlobalData = global_data

    @abc.abstractmethod
    def update_loop(self):
        pass



