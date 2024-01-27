from tkinter import *
from tkinter import messagebox , ttk
import tempfile
import random
from PIL import ImageTk , Image
import os
from time import strftime
c=Tk()
c.geometry("1500x800")


#***************************************************************

def heure ():
    heur=strftime("%H:%M:%S")
    lblh.config(text=heur)
    lblh.after(1000,heure)


def fonctioncaté(event):
    selected_cat = str(en4.get())
    if selected_cat == "vetement":
        en5.config(values=list_souscaté)
        en5.current(0)
    elif selected_cat == "style de vie":
        en5.config(values=list_souscaté2)
        en5.current(0)
    elif selected_cat == "tel":
        en5.config(values=list_souscaté3)
        en5.current(0)

def fonction_souscaté(event):
    selected_souscat = str(en5.get())
    if selected_souscat == "pantelon":
        en6.config(values=pantelon)
        en6.current(0)
    elif selected_souscat == "tshirt":
        en6.config(values=tshirt)
        en6.current(0)
    elif selected_souscat == "shirt":
        en6.config(values=shirt)
        en6.current(0)
    elif selected_souscat == "soap":
        en6.config(values=soap)
        en6.current(0)
    elif selected_souscat == "creme":
        en6.config(values=creme)
        en6.current(0)
    elif selected_souscat == "huile":
        en6.config(values=huile)
        en6.current(0)
    elif selected_souscat == "samsung":
        en6.config(values=samsung)
        en6.current(0)
    elif selected_souscat == "oppo":
        en6.config(values=oppo)
        en6.current(0)
    elif selected_souscat == "iphone":
        en6.config(values=iphone)
        en6.current(0)

def fonction_nomproduit(event):
    selected_nom_produit = str(en6.get())

    if selected_nom_produit == "levis":
        en8.config(values=prix_levis)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit == "adidas":
        en8.config(values=prix_adidas)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit == "nike":
        en8.config(values=prix_nike)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="polo":
        en8.config(values=prix_polo)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="h&m":
        en8.config(values=prix_hm)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="vectoria":
        en8.config(values=prix_vectoria)
        en8.current(0)
        intqte.set(1)
    
    elif selected_nom_produit=="louis":
        en8.config(values=prix_louis)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="peter":
        en8.config(values=prix_peter)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="bal":
        en8.config(values=prix_bal)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="lux":
        en8.config(values=prix_lux)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="nivea":
        en8.config(values=prix_nivea)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="avon":
        en8.config(values=prix_avon)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="ponds":
        en8.config(values=prix_ponds)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="olay":
        en8.config(values=prix_olay)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="garnier":
        en8.config(values=prix_garnier)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="rose":
        en8.config(values=prix_rose)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="argan":
        en8.config(values=prix_argan)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="azir":
        en8.config(values=prix_azir)
        en8.current(0)
        intqte.set(1)


    elif selected_nom_produit=="sam1":
        en8.config(values=prix_sam1)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="sam2":
        en8.config(values=prix_sam2)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="sam3":
        en8.config(values=prix_sam3)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="op1":
        en8.config(values=prix_op1)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="op2":
        en8.config(values=prix_op2)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="op3":
        en8.config(values=prix_op3)
        en8.current(0)
        intqte.set(1)

    elif selected_nom_produit=="ip1":
        en8.config(values=prix_ip1)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="ip2":
        en8.config(values=prix_ip2)
        en8.current(0)
        intqte.set(1)
    elif selected_nom_produit=="ip3":
        en8.config(values=prix_ip3)
        en8.current(0)
        intqte.set(1)


l=[]
def ajouter():
    prix=intprix.get()
    qte=intqte.get() * prix
    l.append(qte)
    if en5.get()==0 :
        messagebox.showerror("Erreur","selectionnez un produit") 
    else:
        txt_recu.insert(END,f'\n{en5.get()}\t\t{intqte.get()}\t\t{qte}')
        strtotalb.set(str("Rs.%.2f"%(sum(l))))
        strtax.set(str("Rs.%.2f"%(sum(l)-(intprix.get())*1/100)))
        strtotalnet.set(str("Rs.%.2f"%sum(l)+((((sum(l)-(intprix.get()))*1/100)))))


def generer_facture():
    if strproduit.get() == "":
        messagebox.showerror("Erreur", "Ajouter un produit")
    else:
        text = txt_recu.get(10.0, (10.0 + float(len(l))))
        bienvenu()
        text = txt_recu.insert(END, text)
        txt_recu.insert(END, "\n*********************************")
        txt_recu.insert(END, f'\n Total Brut :\t\t \t {strtotalb.get()}')
        txt_recu.insert(END, f'\n Tax:\t\t \t {strtax.get()}')
        txt_recu.insert(END, f'\n Total net :\t\t \t {strtotalnet.get()}')

def sauvegarder():
    op = messagebox.askyesno("Sauvegarder", "Voulez-vous sauvegarder la facture ?")
    if op:
        donnefacture = txt_recu.get(1.0, END)
        f1 = open(f"C:/Users/Administrateur/Desktop/dos/{strfacture.get()}.txt", "w")
        f1.write(donnefacture)
        messagebox.showinfo('INFO', f"La facture numéro : {strfacture.get()} a été enregistrée")
        f1.close()

def imprimer():
    fichier = tempfile.mktemp(".txt")
    open(fichier, "w").write(txt_recu.get("1.0", END))
    os.startfile(fichier, "print")

def rechercher():
    trouver = "non"
    for i in os.listdir('C:/Users/Administrateur/Desktop/dos/'):
        if i.split(".")[0] == strrech.get():
            f1 = open(f"C:/Users/Administrateur/Desktop/dos//{i}")
            txt_recu.delete(1.0, END)
            for d in f1:
                txt_recu.insert(END, d)
            f1.close()
            trouver = "oui"
    if trouver == "non":
        messagebox.showerror("Erreur", "La facture n'existe pas")

def rein():
    txt_recu.delete(1.0, END)
    strnom.set("")
    strcontact.set("")
    x = random.randint(1000, 9999)
    strfacture.set(str(x))
    stremail.set("")
    strproduit.set("")
    intprix.set("")
    intqte.set("")
    strtotalb.set("")
    strtax.set("")
    strtotalnet.set("")
    strrech.set("")
    bienvenu()
#***************************************************************
z=random.randint(1000,9999)

strnom=StringVar()
strcontact=StringVar()
strfacture=StringVar()
stremail=StringVar()
strproduit=StringVar()

intprix=IntVar()
intqte=IntVar()

strtotalb=StringVar()
strtax = StringVar()
strtotalnet=StringVar()
strrech=StringVar()

strfacture.set(z)
#***************************************************************

list_caté=["selection","vetement","style de vie","tel"]

list_souscaté=["pantelon","tshirt","shirt"]

pantelon=["levis","adidas","nike"]
prix_levis=500
prix_adidas=100
prix_nike=500

tshirt=["polo","h&m","vectoria"]
prix_polo=500
prix_hm=300
prix_vectoria=500

shirt=["louis","peter","bal"]
prix_louis=500
prix_peter=200
prix_bal=50


list_souscaté2=["soap","creme","huile"]

soap=["lux","nivea","avon"]
prix_lux=50
prix_nivea=30
prix_avon=20


creme=["ponds","olay","garnier"]
prix_ponds=300
prix_olay=600
prix_garnier=200

huile=["rose","argan","azir"]
prix_rose=20
prix_argan=100
prix_azir=10

list_souscaté3=["samsung","oppo","iphone"]


samsung=["sam1","sam2","sam3"]
prix_sam1=2000
prix_sam2=2700
prix_sam3=5000

oppo=["op1","op2","op3"]
prix_op1=1000
prix_op2=5000
prix_op3=6000

iphone=["ip1","ip2","ip3"]
prix_ip1=1000
prix_ip2=5000
prix_ip3=6000






#***************************************************************
lbl1=Label(c,text="SUPER MARCHE OUSMANE NDOME",font=("algerian",25,"bold"),bg="lightblue",width=72).place(x=0,y=0)

lblh=Label(c,text="HH:MM:SS",bg="lightblue",font=("Times",10,"bold"))
lblh.place(x=5,y=15)
heure()
#***************************************************************
frame1=Frame(c ,height=700,relief=GROOVE, width=1465, highlightbackground="lightgrey", highlightthickness=1)
frame1.place(x=15,y=70)
#***************************************************************
labelframe=LabelFrame(frame1,text="Client", font=("Arial", 12, "bold"),height=130, width=300).place(x=10,y=10)
label1 = Label(labelframe, text="Contact", font=("Arial", 11, "bold")).place(x=30, y=110)

en1=Entry(labelframe,width=25,textvariable=strcontact)
en1.place(x=130,y=110)
lbl2=Label(labelframe,text="Nom Client", font=("Arial", 11, "bold")).place(x=30,y=140)
en2=Entry(labelframe,width=25,textvariable=strnom)
en2.place(x=130,y=140)
lbl3=Label(labelframe,text="Email", font=("Arial", 11, "bold")).place(x=30,y=170)
en3=Entry(labelframe,width=25,textvariable=stremail)
en3.place(x=130,y=170)
#***************************************************************
labelframe1=LabelFrame(frame1,text="Produit", font=("Arial", 12, "bold"),height=130, width=600).place(x=330,y=10)
label4 = Label(labelframe1, text="Sel Catégorie", font=("Arial", 11, "bold")).place(x=350, y=110)
en4=ttk.Combobox(labelframe1,values=list_caté,width=25)
en4.place(x=500,y=110)

lbl5=Label(labelframe1,text="Sous Catégorie", font=("Arial", 11, "bold")).place(x=350,y=140)
en5=ttk.Combobox(labelframe1,values=[""],width=25)
en5.place(x=500,y=140)

lbl6=Label(labelframe1,text="Nom Produit", font=("Arial", 11, "bold")).place(x=350,y=170)
en6=ttk.Combobox(labelframe1,width=25, textvariable=strproduit)
en6.place(x=500,y=170)


en4.bind("<<ComboboxSelected>>", fonctioncaté)
en5.bind("<<ComboboxSelected>>", fonction_souscaté)
en6.bind("<<ComboboxSelected>>", fonction_nomproduit)




lbl7=Label(labelframe1,text="Qté", font=("Arial", 11, "bold")).place(x=690,y=110)
en7=ttk.Combobox(labelframe1,width=25, textvariable=intqte)
en7.place(x=750,y=110)
lbl8=Label(labelframe1,text="Prix", font=("Arial", 11, "bold")).place(x=690,y=140)
en8=ttk.Combobox(labelframe1,width=25, textvariable=intprix)
en8.place(x=750,y=140)


#***************************************************************
Labeln=Label(frame1,text="N° Facture ", font=("Arial", 15, "bold")).place(x=980,y=65)
entry1=Entry(frame1, font=("Arial", 15))
entry1.place(x=1100,y=65)
btn1=Button(frame1,bg="indian red",text="Rechercher", font=("Arial", 10, "bold"),pady=10,borderwidth=3,command=rechercher)
btn1.place(x=1330,y=55)

#***************************************************************
imge=ImageTk.PhotoImage(Image.open("C:/Users/Administrateur/Downloads/notsuper.jpg"))
lblimage=Label(image=imge, width=710,height=365)
lblimage.place(x=150,y=230)

#***************************************************************
lblframe2=LabelFrame(frame1,text="Facture", font=("Arial", 12, "bold"),height=380, width=430).place(x=980,y=150)


txt_recu=Text(lblframe2,font=("times new roman",15),width=40,height=15)
txt_recu.place(x=1010,y=250)

#*****************************************************************
def bienvenu():
    txt_recu.delete(1.0,END)
    txt_recu.insert(END," Bienvenu chez super marché ousmane")
    txt_recu.insert(END,f"\n\n Numéro Facture :{strfacture.get()}" )
    txt_recu.insert(END,f"\n\n Nom Client :{strnom.get()}" )
    txt_recu.insert(END,f"\n\n Tel:{strcontact.get()}" )
    txt_recu.insert(END,f"\n\n Email:{stremail.get()}" )
    txt_recu.insert(END,"\n*****************************************")
    txt_recu.insert(END,f"\n\n Produit : \t\t Qte :\t\tPrix :")
    txt_recu.insert(END,"\n*****************************************")
bienvenu()


#***************************************************************
labelframe3=LabelFrame(frame1,text="Boutton", font=("Arial", 12, "bold"),height=140, width=1440).place(x=10,y=550)
lbl9 = Label(labelframe3, text="Total Brut", font=("Arial", 11, "bold")).place(x=30, y=660)
en9=Entry(labelframe3,width=25,textvariable=strtotalb)
en9.place(x=130,y=660)

lbl10 = Label(labelframe3, text="Taxe", font=("Arial", 11, "bold")).place(x=30, y=690)
en10=Entry(labelframe3,width=25,textvariable=strtax)
en10.place(x=130,y=690)

lbl11 = Label(labelframe3, text="Total Net", font=("Arial", 11, "bold")).place(x=30, y=720)
en11=Entry(labelframe3,width=25,textvariable=strtotalnet)
en11.place(x=130,y=720)

#***************************************************************
btn2 = Button(labelframe3, text="Ajouter Card", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15,command=ajouter)
btn2.place(x=315, y=670)
btn3 = Button(labelframe3, text="Générer Facture", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15,command=generer_facture)
btn3.place(x=515, y=670)
btn4 = Button(labelframe3, text="Sauv Facture", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15,command=sauvegarder)
btn4.place(x=715, y=670)
btn5 = Button(labelframe3, text="Imprimer", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15,command=imprimer)
btn5.place(x=915, y=670)
btn6 = Button(labelframe3, text="Réinitialiser", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15,command=rein)
btn6.place(x=1115, y=670)
btn7 = Button(labelframe3, text="Quitter", font=("Arial", 10, "bold"),pady=8,borderwidth=5, bg="pale violet red", width=15, command=c.quit)
btn7.place(x=1315, y=670)


c.mainloop()
