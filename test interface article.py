import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
class Article:

    def __init__(self):
        self.root = ttk.Window(title="Facture Facile",themename="superhero",size=(1080,480))
        self.root.resizable(False,False)
        self.menu_frame = ttk.Frame()
        self.data_frame = ttk.Frame()
        self.bottom_frame =ttk.Frame()

        self.menu_frame.pack(fill=cttk.BOTH)
        self.data_frame.pack(fill=cttk.BOTH)
        self.bottom_frame.pack(fill=cttk.BOTH)

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
        bt_add.pack(side=cttk.LEFT,pady=40,padx=38)
        bt_change.pack(side=cttk.LEFT)
        bt_remove.pack(side=cttk.LEFT,pady=40,padx=38)
        bt_search.pack(side=cttk.LEFT)
        ########################################################
        #data_frame
        """
        split of the data frame
        """
        top_frame = ttk.LabelFrame(self.data_frame, text="Données Important",height=50)
        bottom_frame = ttk.LabelFrame(self.data_frame, text="Données Facultative")
        top_frame.pack(side=cttk.TOP,fill=cttk.X,padx=20)
        bottom_frame.pack(side=cttk.BOTTOM,fill=cttk.X,padx=20)

        #style
        style_data_label=ttk.Style()
        style_data_label.configure('TLabel',font=("Helvitica",16))

        #top_frame
        lb_name = ttk.Label(top_frame,text="Nom :",style="TLabel")
        entry_name = ttk.Entry(top_frame,width=30)
        lb_prix_htva = ttk.Label(top_frame,text="Prix HTVA :")
        entry_prix_htva = ttk.Entry(top_frame,width=20)
        lb_taux_tva = ttk.Label(top_frame,text="Taux TVA :")
        entry_taux_tva = ttk.Entry(top_frame,width=20)

            # pack
        lb_name.pack(side=cttk.LEFT,padx=10,pady=20)
        entry_name.pack(side=cttk.LEFT)
        lb_prix_htva.pack(side=cttk.LEFT,padx=10)
        entry_prix_htva.pack(side=cttk.LEFT)
        lb_taux_tva.pack(side=cttk.LEFT,padx=10)
        entry_taux_tva.pack(side=cttk.LEFT)

        #bottom_frame
        lb_description = ttk.Label(bottom_frame,text="Description:")
        entry_description = ttk.Entry(bottom_frame,width=105)
            #pack
        lb_description.pack(side=cttk.LEFT,padx=10,pady=20)
        entry_description.pack(side=cttk.LEFT)

        #############################################################
        #bottom_frame

        bt_confirm = ttk.Button(self.bottom_frame,text="CONFIRMER",style="success""Outline.TButton",width=25)
        bt_back = ttk.Button(self.bottom_frame,text="RETOUR",style="danger""Outline.TButton",width=25)

        bt_confirm.pack(side=cttk.RIGHT,pady=40,padx=38)
        bt_back.pack(side=cttk.LEFT,pady=40,padx=38)


    def start_article(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = Article()
    app.start_article()
