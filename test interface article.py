import tkinter as tk
import tkinter.constants as ctk
from tkinter import ttk


class GuiArticle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("720x480")
        self.top_frame = tk.Frame(self.root, background="gray")
        self.data_frame = tk.Frame(self.root, background="green")
        self.down_frame = tk.Frame(self.root, background="brown")

        # pack of Frame
        self.top_frame.pack(fill=ctk.BOTH)
        self.data_frame.pack(fill=ctk.BOTH, expand=True)
        self.down_frame.pack(fill=ctk.BOTH, expand=True)

    ##############################################################

        # the widgets of top frame
        self.bt_add = tk.Button(
            self.top_frame,
            text="AJOUTER",
            width=20,
            height=5,
            border=5,
            background="#99FF99",
        )
        self.bt_change = tk.Button(
            self.top_frame,
            text="MODIFIER",
            width=20,
            height=5,
            border=5,
            background="#FFCC99",
        )
        self.bt_remove = tk.Button(
            self.top_frame,
            text="SUPPRIMER",
            width=20,
            height=5,
            border=5,
            background="#FFFF99",
        )
        self.bt_search = tk.Button(
            self.top_frame,
            text="RECHERCHER",
            width=20,
            height=5,
            border=5,
            background="#E5CCFF",
        )

        # pack of widgets of the top frame
        self.bt_add.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH, expand=True)
        self.bt_change.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH, expand=True)
        self.bt_remove.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH, expand=True)
        self.bt_search.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH, expand=True)

    ###################################################################################
        #  the widgets of the text frame
        self.lb_nom = tk.Label(self.data_frame, text="NOM:",width=10,height=2,background="#CCCCCC")
        self.entry_nom = ttk.Entry(self.data_frame,width=30)

        self.lb_prix_htva = tk.Label(self.data_frame, text="PRIX HTVA:", width=10, height=2, background="#CCCCCC")
        self.entry_prix_htva = ttk.Entry(self.data_frame, width=10)

        self.lb_taux_tva = tk.Label(self.data_frame,text="TAUX TVA",width=10,height=2,background="#CCCCCC")
        self.entry_taux_tva = ttk.Entry(self.data_frame, width=10)

        self.lb_nom.grid(column=0,row=0,padx=5,pady=2)
        self.entry_nom.grid(column=1,row=0)
        self.lb_prix_htva.grid(column=2,row=0,padx=5,pady=2)
        self.entry_prix_htva.grid(column=3,row=0)
        self.lb_taux_tva.grid(column=4,row=0,padx=5,pady=2)
        self.entry_taux_tva.grid(column=5,row=0)

    #################################################################################

    def start_gui_article(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = GuiArticle()
    window.start_gui_article()
