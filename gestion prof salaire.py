from tkinter import *
from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkcalendar 
from tkcalendar import DateEntry
from tkinter import simpledialog
import os
import tempfile


window=Tk()
window.geometry("1120x580")
window.title("gestion")

#***********Variable**************
strcode=StringVar()
strEtab=StringVar()
strAnnèeAc=StringVar()
strNom=StringVar()
strDate=StringVar()
strPrenom=StringVar()
strExperience=StringVar()
strSexe=StringVar()
strIdendifiant=StringVar()
strGmail=StringVar()
strContact=StringVar()
strNationnalitè=StringVar()
strStatut=StringVar()
strAdresse=StringVar()

strmois=StringVar()
strmode=StringVar()
strnbrheure=StringVar()
strtarif=StringVar()
strmetier=StringVar()
stranne=StringVar()
strsalaire=StringVar()


#**********************************************************************************
def clear():
        Entry.delete(0,END)


def click(number):
        current=str(Entry.get())
        Entry.delete(0,END)
        Entry.insert(0, current+str(number))

def equal():
        s_num=float(Entry.get())
        Entry.delete(0, END)

        if to_do=='add':
             Entry.insert(0, f_num + s_num)

        if to_do=='sub':
            Entry.insert(0, f_num - s_num)

        if to_do=='multi':
            Entry.insert(0, f_num * s_num)

        if to_do=='div':
            Entry.insert(0, f_num / s_num)


def addition():
        global f_num
        global to_do
        to_do='add'
        f_num= float(Entry.get())
        Entry.delete(0, END)

def subtraction():
        global f_num
        global to_do
        to_do='sub'
        f_num= float(Entry.get())
        Entry.delete(0, END)

def multiplication():
        global f_num
        global to_do
        to_do='multi'
        f_num= float(Entry.get())
        Entry.delete(0, END)

def division():
        global f_num
        global to_do
        to_do='div'
        f_num= float(Entry.get())
        Entry.delete(0,END)
        

   

def calculate_net_salary():
        try:
                nombre_heure = float(strnbrheure.get())
                tarif_horaire = float(strtarif.get())

                salaire_net = nombre_heure * tarif_horaire

                en6.config(state=NORMAL)
                en6.delete(0, END)
                en6.insert(0, f"{salaire_net:.2f}")
                en6.config(state=DISABLED)
                txt_recu.delete(1.0,END)
                txt_recu.insert(END,f"\t Code :\t{strcode.get()}" )
                txt_recu.insert(END,f"\n\t Nom  :\t{ strNom.get()}" )
                txt_recu.insert(END,f"\n\t Prenom:\t{strPrenom.get()}" )
                txt_recu.insert(END,f"\n\t Sexe:\t{strSexe.get()}" )
                txt_recu.insert(END,f"\n\t Date de naissance:\t{ strDate.get() }" )
                txt_recu.insert(END,f"\n\t Etablissement :\t{strEtab.get()}" )
                txt_recu.insert(END,f"\n\t Anne Académique  :\t{strAnnèeAc.get()}" )
                txt_recu.insert(END,f"\n\t Experience:\t{strExperience.get()}" )
                txt_recu.insert(END,f"\n\t Identifiant:\t{strIdendifiant.get()}" )
                txt_recu.insert(END,f"\n\t Gmail:\t{strGmail.get()}" )
                txt_recu.insert(END,f"\n\t Contact :\t{strContact.get()}" )
                txt_recu.insert(END,f"\n\t Nationnalite  :\t{strNationnalitè.get()}" )
                txt_recu.insert(END,f"\n\t Statut:\t{strStatut.get()}" )
                txt_recu.insert(END,f"\n\t Adresse:\t{strAdresse.get()}" )
                txt_recu.insert(END,"\n*****************************************")  

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Nombre d'Heure and Tarif Horaire")
    

def sauvegarder():
        code_professeur = entcode.get()
        etablissement = enteta.get()
        annee_academique = combo_var_academique.get()
        nom = entnom.get()
        date_naissance = combo_var_date_naissance.get()
        prenom = entpre.get()
        experience = entexp.get()
        sexe = combo_var_sexe.get()
        identifiant = entiden.get()
        gmail = entgmail.get()
        contact = entcon.get()
        nationalite = entnat.get()
        statut = combo_var_statut.get()
        adresse = entad.get()


        mois = en1.get()
        annee = en2.get()
        mode_paiement = combo_var_mode_paiement.get()
        matiere = en3.get()
        nombre_heure = en4.get()
        tarif_horaire = en5.get()
        salaire_net = en6.get()

        try:
            with open(f"Professeur{code_professeur}_data.txt", "w") as file:
                file.write(f"Code Professeur: {code_professeur}\n")
                file.write(f"Etablissement: {etablissement}\n")
                file.write(f"Année Académique: {annee_academique}\n")
                file.write(f"Nom: {nom}\n")
                file.write(f"Date de Naissance: {date_naissance}\n")
                file.write(f"Prenom: {prenom}\n")
                file.write(f"Experience: {experience}\n")
                file.write(f"Sexe: {sexe}\n")
                file.write(f"Identifiant: {identifiant}\n")
                file.write(f"Gmail: {gmail}\n")
                file.write(f"Contact: {contact}\n")
                file.write(f"Nationalité: {nationalite}\n")
                file.write(f"Statut: {statut}\n")
                file.write(f"Adresse: {adresse}\n\n")

                file.write(f"Mois: {mois}\n")
                file.write(f"Année: {annee}\n")
                file.write(f"Mode de Paiement: {mode_paiement}\n")
                file.write(f"Matière: {matiere}\n")
                file.write(f"Nombre d'Heures: {nombre_heure}\n")
                file.write(f"Tarif Horaire: {tarif_horaire}\n")
                file.write(f"Salaire Net: {salaire_net}\n")
                
            messagebox.showinfo("Saved", "Data has been saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data. Error: {str(e)}")
def imprimer():
    fichier = tempfile.mktemp(".txt")
    open(fichier, "w").write(txt_recu.get("1.0", END))
    os.startfile(fichier, "print")


def reinitialiser():
        entcode.delete(0, END)
        enteta.delete(0, END)
        combo_var_academique.set("")
        entad.delete(0, END)
        entcon.delete(0, END)
        entexp.delete(0, END)
        entgmail.delete(0, END)
        entiden.delete(0, END)
        entpre.delete(0, END)
        combo_var_mode_paiement.set("")
        combo_var_sexe.set("")
        combo_var_statut.set("")
        entnat.delete(0,END)
        entnom.delete(0, END)


        en1.delete(0, END)
        en2.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en5.delete(0, END)
        combo_var_mode_paiement.set("") 

        en6.config(state=NORMAL)
        en6.delete(0, END)
        en6.config(state=DISABLED)
        bienvenu()
        messagebox.showinfo("Reinitialized", "Values have been reset.")
        

def supprimer():
        ask=messagebox.askyesno("YES OR NO","Are you sure ??")
        if ask:
                code_professeur =simpledialog.askstring("Input","Enter the professor's code: ")
        try:
            os.remove(f"Professeur{code_professeur}_data.txt")
            messagebox.showinfo("Deleted", f"Data for Code Professeur {code_professeur} has been deleted successfully!")

        except FileNotFoundError:
            messagebox.showwarning("Not Found", f"No data file found for Code Professeur {code_professeur}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete data. Error: {str(e)}")

def rechercher():
    directory_path = "any file in your pc"
    code_to_search = strcode.get()
    filename=(f"Professeur{strcode}_data.txt")
    
    trouver = "non"
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt') and filename.split('.')[0] == code_to_search:
            messagebox.showinfo('info', 'La facture existe')
            txt_recu.delete("1.0", END)
            with open(os.path.join(directory_path, filename), 'r') as file:
                txt_recu.insert(END, file.read())
            trouver = "oui"
            break

    if trouver == "non":
        messagebox.showerror("Erreur", "La facture n'existe pas")



#************************************************************************************************** 
lbl1 = CTkLabel(window, text="GESTION DE PAIE DE PROFESSEURS", font=("algerian", 30, "bold"), text_color="wheat2",height=20, fg_color="tan4", width=1150).place(x=0, y=0)
frame = Frame(window, height=490, width=580, highlightbackground="lightgrey", highlightthickness=3)
frame.place(x=6, y=69)
lbl2 = CTkLabel(window, text="INFORMATION PROFESSEUR", font=("algerian", 20, "bold"), text_color="wheat2", fg_color="burlywood4", width=580).place(x=6, y=40)
lbl3 = Label(frame, text="Code Professeur", font=("times", 15, "bold")).place(x=70, y=30)
entcode = ttk.Entry(frame, font=("times", 13, "bold"),width=13,textvariable=strcode)
entcode.place(x=225, y=33)
bt1 = Button(frame, text="Rechercher", bg="wheat4", fg="black",width=13, font=("times", 10, "bold"),command=rechercher).place(x=380, y=32)
lbl4 = Label(frame, text="Etablissement", font=("times", 13, "bold")).place(x=5, y=105)
enteta = ttk.Entry(frame, width=20,textvariable=strEtab)
enteta.place(x=138, y=110)
lbl5 = Label(frame, text="Annèe Acadèmique", font=("times", 13, "bold")).place(x=285, y=105)
combo_var_academique=ttk.Combobox(frame, width=17, values=["2020-2021", "2021-2022", "2022-2023"],textvariable=strAnnèeAc)
combo_var_academique.place(x=440, y=110)
lbl6 = Label(frame, text="Nom", font=("times", 13, "bold")).place(x=5, y=155)
entnom = ttk.Entry(frame, width=20,textvariable=strNom)
entnom.place(x=135, y=160)
lbl7 = Label(frame, text="Date Naissance ", font=("times", 13, "bold")).place(x=285, y=155)
combo_var_date_naissance=DateEntry(frame, width=17,textvariable=strDate)
combo_var_date_naissance.place(x=440, y=158)
lbl8 = Label(frame, text="Prenom", font=("times", 13, "bold")).place(x=5, y=200)
entpre = ttk.Entry(frame, width=20,textvariable=strPrenom)
entpre.place(x=135, y=205)
lbl9 = Label(frame, text="Experience", font=("times", 13, "bold")).place(x=285, y=200)
entexp = ttk.Entry(frame, width=20,textvariable=strExperience)
entexp.place(x=440, y=205)
lbl10 = Label(frame, text="Sexe", font=("times", 13, "bold")).place(x=5, y=245)
combo_var_sexe=ttk.Combobox(frame, values=["Femme", "Homme"],width=17,textvariable=strSexe)
combo_var_sexe.place(x=135, y=250)
lbl11 = Label(frame, text="Idendifiant", font=("times", 13, "bold")).place(x=285, y=245)
entiden = ttk.Entry(frame, width=20,textvariable=strIdendifiant)
entiden.place(x=440, y=250)
lbl12 = Label(frame, text="Email", font=("times", 13, "bold")).place(x=5, y=290)
entgmail = ttk.Entry(frame, width=20,textvariable=strGmail)
entgmail.place(x=135, y=295)
lbl13 = Label(frame, text="Contact", font=("times", 13, "bold")).place(x=285, y=290)
entcon = ttk.Entry(frame, width=20,textvariable=strContact)
entcon.place(x=440, y=295)
lbl14 = Label(frame, text="Nationnalitè", font=("times", 13, "bold")).place(x=5, y=335)
entnat = ttk.Entry(frame, width=20,textvariable=strNationnalitè)
entnat.place(x=135, y=340)
lbl15 = Label(frame, text="Statut", font=("times", 13, "bold")).place(x=285, y=335)
combo_var_statut=ttk.Combobox(frame, values=["Mariè", "Celibataire", "Devorcé"], width=17,textvariable=strStatut)
combo_var_statut.place(x=440, y=340)
lbl16 = Label(frame, text="Adresse", font=("times", 13, "bold")).place(x=5, y=380)
entad = CTkEntry(frame, width=300, height=79, fg_color="white", border_color="lightgrey", bg_color="black",textvariable=strAdresse)
entad.place(x=135, y=390)


lb17 = CTkLabel(window, text="SALAIRE PROFESSEUR", font=("algerian", 20, "bold"), text_color="wheat2", fg_color="burlywood4", width=510).place(x=600, y=40)
frame1 = Frame(window, height=235, width=510, highlightbackground="lightgrey", highlightthickness=3)
frame1.place(x=600, y=69)
lab1 = Label(frame1, text="Mois", font=("times", 13, "bold")).place(x=10, y=25)
en1 = ttk.Entry(frame1, width=15,textvariable=strmois)
en1.place(x=160, y=30)
lab2 = Label(frame1, text="Annèe", font=("times", 13, "bold")).place(x=290, y=25)
en2 = ttk.Entry(frame1, width=15,textvariable=stranne)
en2.place(x=400, y=30)
lab3 = Label(frame1, text="Mode de Paiement", font=("times", 13, "bold")).place(x=10, y=65)
combo_var_mode_paiement=ttk.Combobox(frame1, values=["Espèce", "Carte Bancaire", "Chèque"],width=12,textvariable=strmode)
combo_var_mode_paiement.place(x=160, y=70)
lab4 = Label(frame1, text="Metier", font=("times", 13, "bold")).place(x=290, y=65)
en3 = ttk.Entry(frame1, width=15,textvariable=strmetier)
en3.place(x=400, y=72)
lab5 = Label(frame1, text="Nombre d'heures", font=("times", 13, "bold")).place(x=10, y=100)
en4 = ttk.Entry(frame1, width=15,textvariable=strnbrheure)
en4.place(x=160, y=105)
lab6 = Label(frame1, text="Tarif Horaire", font=("times", 13, "bold")).place(x=290, y=105)
en5 = ttk.Entry(frame1, width=15,textvariable=strtarif)
en5.place(x=400, y=105)
lab7 = Label(frame1, text="Salaire Net", font=("times", 13, "bold")).place(x=150, y=143)
en6 = ttk.Entry(frame1, width=15,textvariable=strsalaire)
en6.place(x=250, y=145)

btn = CTkButton(frame1, text="Calculer", width=100, font=("times", 13, "bold"), fg_color="saddle brown", text_color="wheat2", command=calculate_net_salary).place(x=30, y=190)
btn1 = CTkButton(frame1, text="Sauvegarder", width=100, font=("times", 13, "bold"), fg_color="wheat4", text_color="wheat2",command=sauvegarder).place(x=145, y=190)
btn2 = CTkButton(frame1, text="Reinitialiser", width=100, font=("times", 13, "bold"), fg_color="saddle brown", text_color="wheat2",command=reinitialiser).place(x=265, y=190)
btn3 = CTkButton(frame1, text="Supprimer", width=100, font=("times", 13, "bold"), fg_color="wheat4", text_color="wheat2",command=supprimer).place(x=380, y=190)


frame2 = Frame(window, height=205, width=179, highlightbackground="lightgrey", highlightthickness=3)
frame2.place(x=610, y=340)
Entry=Entry(frame2,font=("consolas",20),bg="lightgrey",width=11, background="white")
Entry.place(x=2,y=0)

Button1=Button(frame2,text="1",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(1))
Button1.place(x=0,y=38)
Button2=Button(frame2,text="2",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(2))
Button2.place(x=43,y=38)
Button3=Button(frame2,text="3",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(3))
Button3.place(x=86,y=38)
divide=Button(frame2,text="C",width=3,font=("consolas",15, "bold"),bg="wheat4",command=clear)
divide.place(x=129,y=38)
Button4=Button(frame2,text="4",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(4))
Button4.place(x=0,y=78)
Button5=Button(frame2,text="5",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(5))
Button5.place(x=43,y=78)
Button6=Button(frame2,text="6",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(6))
Button6.place(x=86,y=78)
multipe=Button(frame2,text="*",width=3,font=("consolas",15, "bold"),bg="wheat4",command=multiplication)
multipe.place(x=129,y=78)
Button7=Button(frame2,text="7",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(7))
Button7.place(x=0,y=118)
Button8=Button(frame2,text="8",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(8))
Button8.place(x=43,y=118)
Button9=Button(frame2,text="9",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(9))
Button9.place(x=86,y=118)
minus=Button(frame2,text="-",width=3,font=("consolas",15, "bold"),bg="wheat4",command=subtraction)
minus.place(x=129,y=118)
Button10=Button(frame2,text="0",width=3,font=("consolas",15, "bold"),bg="wheat3",command=lambda :click(0))
Button10.place(x=0,y=158)
Button11=Button(frame2,text="=",width=3,font=("consolas",15, "bold"),bg="wheat4",command=equal)
Button11.place(x=43,y=158)
Button12=Button(frame2,text="/",width=3,font=("consolas",15, "bold"),bg="wheat4",command=division)
Button12.place(x=86,y=158)
plus=Button(frame2,text="+",width=3,font=("consolas",15, "bold"),bg="wheat4",command=addition)
plus.place(x=129,y=158)


frame3 = Frame(window, height=220, width=287, highlightbackground="lightgrey", highlightthickness=3)
frame3.place(x=820, y=340)
title=CTkLabel(window,text="RECU DE SALAIRE",font=("algerian",20,"bold"),  text_color="wheat2", fg_color="burlywood4", width=287).place(x=820,y=310)

frame4=Frame(frame3, height=160, width=260, highlightbackground="lightgrey", highlightthickness=1).place(x=10,y=5)

#************************************************************************************
txt_recu=Text(frame4, font=("times new roman",7), bg="linen", width=51, height=13)
txt_recu.place(x=833,y=348)

def bienvenu():
        txt_recu.delete(1.0,END)
        txt_recu.insert(END,f"\t Code :" )
        txt_recu.insert(END,f"\n\t Nom  :" )
        txt_recu.insert(END,f"\n\t Prenom:" )
        txt_recu.insert(END,f"\n\t Sexe:" )
        txt_recu.insert(END,f"\n\t Date de naissance:" )
        txt_recu.insert(END,f"\n\t Etablissement :" )
        txt_recu.insert(END,f"\n\t Anne Académique  :" )
        txt_recu.insert(END,f"\n\t Experience:" )
        txt_recu.insert(END,f"\n\t Identifiant:" )
        txt_recu.insert(END,f"\n\t Email:" )
        txt_recu.insert(END,f"\n\t Contact :" )
        txt_recu.insert(END,f"\n\t Nationnalite  :" )
        txt_recu.insert(END,f"\n\t Statut:" )
        txt_recu.insert(END,f"\n\t Adresse:" )
        txt_recu.insert(END,"\n*****************************************")      
bienvenu()


btnimprimer=Button(frame3,text="Imprimer",bg="wheat4", fg="black",width=13, font=("times", 10, "bold"),command=imprimer)
btnimprimer.place(x=100,y=175)



 

window.mainloop()
