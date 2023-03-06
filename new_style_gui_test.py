import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk


class App(ttk.Window):
    def __init__(self, title: str, size: tuple, theme="default"):
        """

        :param title: title of the application
        :param size: (X;Y)
        """
        # main setup
        super().__init__(themename=theme)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pos_screen_width = (screen_width // 2) - (size[0] // 2)
        pos_screen_height = (screen_height // 2) - (size[1] // 2)
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{pos_screen_width}+{pos_screen_height}")
        self.resizable(False, False)

        self.menu = Menu(self)
        self.data_article = DataArticle(self)
        self.end = MenuOption(self)

    def start_app(self):
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=cttk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        menu_bt_font = ("Helvitica", 20)
        # style of bt_add
        style_menu_add = ttk.Style()
        style_menu_add.configure(
            "bt_add.Outline.TButton",
            font=menu_bt_font,
            background="#99FF99",
            foreground="#646464",
            bordercolor="#99FF99",
        )
        # style of bt_change
        style_menu_change = ttk.Style()
        style_menu_change.configure(
            "bt_change.Outline.TButton",
            font=menu_bt_font,
            background="#FFCC99",
            foreground="#646464",
            bordercolor="#FFCC99",
        )
        # style of bt_remove
        style_menu_remove = ttk.Style()
        style_menu_remove.configure(
            "bt_remove.Outline.TButton",
            font=menu_bt_font,
            background="#FFFF99",
            foreground="#646464",
            bordercolor="#FFFF99",
        )
        # style of bt_search
        style_menu_remove = ttk.Style()
        style_menu_remove.configure(
            "bt_search.Outline.TButton",
            font=menu_bt_font,
            background="#E5CCFF",
            foreground="#646464",
            bordercolor="#E5CCFF",
        )

        # menu_frame
        bt_add = ttk.Button(self, text="AJOUTER", style="bt_add.Outline.TButton")
        bt_change = ttk.Button(self, text="MODIFIER", style="bt_change.Outline.TButton")
        bt_remove = ttk.Button(
            self, text="SUPPRIMER", style="bt_remove.Outline.TButton"
        )
        bt_search = ttk.Button(
            self, text="RECHERCHER", style="bt_search.Outline.TButton"
        )
        # pack
        bt_add.pack(side=cttk.LEFT, expand=True, fill=cttk.BOTH, padx=10, pady=30)
        bt_change.pack(side=cttk.LEFT, expand=True, fill=cttk.BOTH, padx=10, pady=30)
        bt_remove.pack(side=cttk.LEFT, expand=True, fill=cttk.BOTH, padx=10, pady=30)
        bt_search.pack(side=cttk.LEFT, expand=True, fill=cttk.BOTH, padx=10, pady=30)


class DataArticle(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=cttk.BOTH, expand=True)

        self.top_frame = self.TopFrame(self, "Données Important")
        self.bottom_frame = self.BottomFrame(self, "Données Facultative")

    class TopFrame(ttk.LabelFrame):
        def __init__(self, parent, title: str):
            super().__init__(parent, text=title)
            self.pack(side=cttk.TOP, fill=cttk.X, padx=20, pady=10)
            self.create_widgets()

        def create_widgets(self):
            # style
            font_universal = ("Helvitica", 20)
            #style of all the Labels
            style_data_label = ttk.Style()
            style_data_label.configure("TLabel", font=font_universal)
            # résoudre problème pour entry la taille écriture
            """
            # style of all the entrys
            style_data_entry = ttk.Style()
            style_data_entry.configure("TEntry", font=font_universal)
            """

            # top_frame
            lb_name = ttk.Label(self, text="Nom :", style="TLabel")
            entry_name = ttk.Entry(self)
            lb_prix_htva = ttk.Label(self, text="Prix HTVA :", style="TLabel")
            entry_prix_htva = ttk.Entry(self, width=20)
            lb_taux_tva = ttk.Label(self, text="Taux TVA :", style="TLabel")
            entry_taux_tva = ttk.Entry(self, width=20)

            # pack
            lb_name.pack(side=cttk.LEFT, padx=10, pady=30)
            entry_name.pack(side=cttk.LEFT, expand=True, fill=cttk.X)
            lb_prix_htva.pack(side=cttk.LEFT, padx=10)
            entry_prix_htva.pack(side=cttk.LEFT)
            lb_taux_tva.pack(side=cttk.LEFT, padx=10)
            entry_taux_tva.pack(side=cttk.LEFT, padx=10)

    class BottomFrame(ttk.LabelFrame):
        def __init__(self, parent, title: str):
            super().__init__(parent, text=title)
            self.pack(side=cttk.TOP, fill=cttk.X, padx=20, pady=10)
            self.create_widgets()

        def create_widgets(self):
            # bottom_frame
            lb_description = ttk.Label(self, text="Description:")
            entry_description = ttk.Entry(self)
            # pack
            lb_description.pack(side=cttk.LEFT, padx=10, pady=30)
            entry_description.pack(side=cttk.LEFT, expand=True, fill=cttk.X, padx=10)


class MenuOption(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=cttk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        bt_confirm = ttk.Button(
            self, text="CONFIRMER", style="success" "Outline.TButton", width=25
        )
        bt_back = ttk.Button(
            self, text="RETOUR", style="danger" "Outline.TButton", width=25
        )

        bt_confirm.pack(side=cttk.RIGHT, fill=cttk.BOTH, pady=20, padx=40, expand=True)
        bt_back.pack(side=cttk.LEFT, fill=cttk.BOTH, pady=20, padx=40, expand=True)


if __name__ == "__main__":
    easy_invoice = App("Facture Facile", (1100, 550), "superhero")
    easy_invoice.start_app()
