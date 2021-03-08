import tkinter as tk
from view import Win, Reader
from model import Model


class Controller:
    def __init__(self, root):
        self.win = Win(self, root)
        self.model = Model()

    def pass_items_directory(self, direct):
        self.model.items_directory(direct)

    def pass_volume(self, volume):
        self.model.set_volume(volume)

    def prepare_shipments(self, f_name):
        self.model.prepare_shipments_csv(f_name)

    def reset(self):
        self.model.reset()

    def read(self):
        items, shipments = self.model.read()
        rdr = Reader(self)
        rdr.reader1['text'] = items
        rdr.reader2['text'] = shipments


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Outbound_logistics')
    root.resizable(False, False)
    Controller(root)
    root.mainloop()
