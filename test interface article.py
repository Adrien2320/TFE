import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
class Article:

    def __init__(self):
        self.root = ttk.Window(title="Facture Facile",themename="superhero")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        app_width = 1100
        app_height = 500
        pos_screen_width = (screen_width//2)- (app_width//2)
        pos_screen_height = (screen_height//2) - (app_height//2)
        self.root.geometry(f"{app_width}x{app_height}+{pos_screen_width}+{pos_screen_height}")
        self.root.resizable(False,False)
        self.menu_frame = ttk.Frame()
        self.data_frame = ttk.Frame()
        self.bottom_frame =ttk.Frame()

        self.menu_frame.pack(fill=cttk.BOTH,expand=True)
        self.data_frame.pack(fill=cttk.BOTH,expand=True)
        self.bottom_frame.pack(fill=cttk.BOTH,expand=True)

        ########################################################
            #style
        style_menu=ttk.Style()
        style_menu.configure('Outline.TButton',font=("Helvitica",21))

        #menu_frame
        bt_add = ttk.Button(self.menu_frame, text="AJOUTER", style="Outline.TButton")
        bt_change =ttk.Button(self.menu_frame, text="MODIFIER", style="Outline.TButton")
        bt_remove =ttk.Button(self.menu_frame, text="SUPPRIMER", style="Outline.TButton")
        bt_search = ttk.Button(self.menu_frame, text="RECHERCHER", style="Outline.TButton")
        #pack
        bt_add.pack(side=cttk.LEFT,pady=40,expand=True,fill=cttk.X,padx=10)
        bt_change.pack(side=cttk.LEFT,expand=True,fill=cttk.X,padx=10)
        bt_remove.pack(side=cttk.LEFT,pady=40,expand=True,fill=cttk.X,padx=10)
        bt_search.pack(side=cttk.LEFT,expand=True,fill=cttk.X,padx=10)
        ########################################################
        #data_frame
        """
        split of the data frame
        """
        top_frame = ttk.LabelFrame(self.data_frame, text="Données Important")
        bottom_frame = ttk.LabelFrame(self.data_frame, text="Données Facultative")
        top_frame.pack(side=cttk.TOP,fill=cttk.X,padx=20)
        bottom_frame.pack(side=cttk.BOTTOM,fill=cttk.X,padx=20)

        #style
        style_data_label=ttk.Style()
        style_data_label.configure('TLabel',font=("Helvitica",25))

        #top_frame
        lb_name = ttk.Label(top_frame,text="Nom :",style="TLabel")
        entry_name = ttk.Entry(top_frame)
        lb_prix_htva = ttk.Label(top_frame,text="Prix HTVA :")
        entry_prix_htva = ttk.Entry(top_frame,width=20)
        lb_taux_tva = ttk.Label(top_frame,text="Taux TVA :")
        entry_taux_tva = ttk.Entry(top_frame,width=20)

            # pack
        lb_name.pack(side=cttk.LEFT,padx=10,pady=30)
        entry_name.pack(side=cttk.LEFT,expand=True,fill=cttk.X)
        lb_prix_htva.pack(side=cttk.LEFT,padx=10)
        entry_prix_htva.pack(side=cttk.LEFT)
        lb_taux_tva.pack(side=cttk.LEFT,padx=10)
        entry_taux_tva.pack(side=cttk.LEFT,padx=10)

        #bottom_frame
        lb_description = ttk.Label(bottom_frame,text="Description:")
        entry_description = ttk.Entry(bottom_frame)
            #pack
        lb_description.pack(side=cttk.LEFT,padx=10,pady=30)
        entry_description.pack(side=cttk.LEFT,expand=True,fill=cttk.X,padx=10)

        #############################################################
        #bottom_frame

        bt_confirm = ttk.Button(self.bottom_frame,text="CONFIRMER",style="success""Outline.TButton",width=25)
        bt_back = ttk.Button(self.bottom_frame,text="RETOUR",style="danger""Outline.TButton",width=25)

        bt_confirm.pack(side=cttk.RIGHT,pady=40,padx=40,expand=True)
        bt_back.pack(side=cttk.LEFT,pady=40,padx=40,expand=True)


    def start_article(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = Article()
    app.start_article()
