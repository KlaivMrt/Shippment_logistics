import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class Win:
    def __init__(self, controller, root):
        self.controller = controller
        self.v_frame = tk.Frame(root)
        self.i_frame = tk.Frame(root)
        self.sh_frame = tk.Frame(root)

        self.v_frame.pack(pady=5)
        self.i_frame.pack(side=tk.LEFT)
        self.sh_frame.pack(side=tk.RIGHT)

        # Volume
        self.volume = tk.Label(self.v_frame, text='Volume :')
        self.v_entry = tk.Entry(self.v_frame)
        self.set_btn = tk.Button(self.v_frame, text='Set', padx=30, command=self.get_volume)
        self.reset_btn = tk.Button(self.v_frame, text='Reset', padx=30, command=self.reset)

        self.volume.grid(row=0, column=0, padx=(0, 15))
        self.v_entry.grid(row=0, column=1, padx=25)
        self.set_btn.grid(row=0, column=2, padx=(15, 0))
        self.reset_btn.grid(row=0, column=3, padx=(15, 0))

        # Items
        self.iw_frame = tk.Frame(self.i_frame)
        self.iw_frame.pack()

        self.items = tk.Label(self.iw_frame, text='Items Directory :')
        self.i_btn = tk.Button(self.iw_frame, text='Open', command=self.get_items_directory, state='disabled')

        self.items.grid(row=0, column=0, padx=(0, 15))
        self.i_btn.grid(row=0, column=2, padx=(0, 15))

        # Shipments

        self.shw_frame = tk.Frame(self.sh_frame)
        self.shw_frame.pack()

        self.shipments = tk.Label(self.shw_frame, text='Shipments :')
        self.sh_entry = tk.Entry(self.shw_frame, state='disabled')
        self.sh_btn = tk.Button(self.shw_frame, text='Proceed', state='disabled',
                                command=lambda: [self.prepare_shipments(), self.controller.read()])

        self.shipments.grid(row=0, column=0, padx=(0, 15))
        self.sh_entry.grid(row=0, column=1, padx=(0, 15))
        self.sh_btn.grid(row=0, column=2, padx=(0, 15))

    def get_items_directory(self):
        directory = filedialog.askopenfilename(initialdir="/", title="Select a File",)
        self.i_btn['state'] = 'disabled'
        self.controller.pass_items_directory(directory)

    def get_volume(self):

        try:
            volume = int(self.v_entry.get())
            self.set_btn['state'] = 'disabled'
            self.v_entry['state'] = 'disabled'
            self.i_btn['state'] = 'normal'
            self.sh_entry['state'] = 'normal'
            self.sh_btn['state'] = 'normal'
            self.controller.pass_volume(int(volume))
        except ValueError:
            self.v_entry.delete(0, 'end')

    def prepare_shipments(self):
        f_name = self.sh_entry.get()
        self.sh_entry.delete(0, 'end')
        self.sh_entry['state'] = 'disabled'
        self.sh_btn['state'] = 'disabled'
        self.controller.prepare_shipments(f_name)

    def reset(self):
        self.controller.reset()
        self.v_entry['state'] = 'normal'
        self.v_entry.delete(0, 'end')
        self.set_btn['state'] = 'normal'
        self.i_btn['state'] = 'disabled'
        self.sh_entry['state'] = 'disabled'
        self.sh_btn['state'] = 'disabled'


class Reader:
    def __init__(self, controller):
        self.root = tk.Toplevel()
        self.root.resizable(False, False)
        self.controller = controller

        # Create main frames
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)

        self.frame1.pack(side=tk.LEFT)
        self.frame2.pack(side=tk.RIGHT)

        # Create canvases
        self.canvas1 = tk.Canvas(self.frame1)
        self.canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.canvas2 = tk.Canvas(self.frame2)
        self.canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create scrollbars
        self.scroll1 = ttk.Scrollbar(self.frame1, orient=tk.VERTICAL, command=self.canvas1.yview)
        self.scroll1.pack(side=tk.RIGHT, fill=tk.Y)

        self.scroll2 = ttk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.canvas2.yview)
        self.scroll2.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvases
        self.canvas1.config(yscrollcommand=self.scroll1.set)
        self.canvas1.bind('<Configure>', lambda e: self.canvas1.configure(scrollregion=self.canvas1.bbox('all')))

        self.canvas2.config(yscrollcommand=self.scroll2.set)
        self.canvas2.bind('<Configure>', lambda e: self.canvas2.configure(scrollregion=self.canvas2.bbox('all')))

        # Create another frame inside the canvas
        self.f1 = tk.Frame(self.canvas1)
        self.f2 = tk.Frame(self.canvas2)

        # Add these new frames in a win in the canvases
        self.canvas1.create_window((0, 0), window=self.f1, anchor='nw')
        self.canvas2.create_window((0, 0), window=self.f2, anchor='nw')

        self.reader1 = tk.Label(self.f1)
        self.reader1.grid(row=0, column=0)

        self.reader2 = tk.Label(self.f2)
        self.reader2.grid(row=0, column=0)
