# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import *
from base64 import *
from PIL import Image, ImageTk
import qrcode

class ExitGenerator_GUI(Toplevel):
    ''' Interface graphique pour générateur d'autorisation de sortie numérique
    '''
    def __init__(self, debug = False):
        Toplevel.__init__(self)
        self.debug = debug
        self.liste_motifs_short = StringVar()
        self.liste_motifs_short.set('travail courses sante famille sports judiciaire missions')
        
    def interface(self):
        ''' Interface de la fenêtre
        '''
        
        couleur_fond = 'grey'
        couleur_texte = 'black'
        couleur_fond_saisie = 'blue'
        couleur_texte_saisie = 'white'
        couleur_activebackground = couleur_texte_saisie
        couleur_activeforeground = couleur_fond_saisie
        self.mon_qr_tk = ''
        
        self.title('Générateur Autorisation de Sortie')
        self.geometry('400x600')
        
        self.panel_001 = Label(self, bg = couleur_fond)
        
        self.label_prénom = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Prénom :')
        
        self.entry_prénom = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_nom = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Nom :')
        
        self.entry_nom = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_date_naissance = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Date de naissance :')
        
        self.entry_date_naissance = DateEntry(self.panel_001,
                                              foreground = couleur_texte_saisie,
                                              background = couleur_fond_saisie,
                                              borderwidth = 2,
                                              year = 1980)
        
        self.label_lieu_naissance = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Lieu de naissance :')
        
        self.entry_lieu_naissance = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_adresse = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Adresse :')
        
        self.entry_adresse = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_ville = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Ville :')
        
        self.entry_ville = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_cp = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Code Postal :')
        
        self.entry_cp = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.label_motif = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Motif :')
        
        self.entry_motif = Listbox(self.panel_001,
                                   fg = couleur_texte_saisie,
                                   bg = couleur_fond_saisie,
                                   selectbackground = couleur_texte_saisie,
                                   selectforeground = couleur_fond_saisie,
                                   relief = 'flat',
                                   listvariable = self.liste_motifs_short)
        
        self.label_date_sortie = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Date de sortie :')
        
        maintenant = datetime.now()
        
        self.entry_date_sortie = DateEntry(self.panel_001,
                                              foreground = couleur_texte_saisie,
                                              background = couleur_fond_saisie,
                                              borderwidth = 2,
                                              year = maintenant.year)
        
        self.label_heure_sortie = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Heure de sortie :')
        
        self.entry_heure_sortie = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.btn_generer = Button(self.panel_001,
                                  bg = couleur_fond_saisie,
                                  fg = couleur_texte_saisie,
                                  text = 'Générer',
                                  command = lambda: self.do_attestation(nom = self.entry_nom.get(),
                                                                        prénom = self.entry_prénom.get(),
                                                                        date_naissance = self.entry_date_naissance.get_date(),
                                                                        lieu_naissance = self.entry_lieu_naissance.get(),
                                                                        adresse = self.entry_adresse.get(),
                                                                        code_postal = self.entry_cp.get(),
                                                                        ville = self.entry_ville.get(),
                                                                        date_sortie = self.entry_date_sortie.get_date(),
                                                                        heure_sortie = self.entry_heure_sortie.get(),
                                                                        motif = self.entry_motif.get(self.entry_motif.curselection())),
                                  activebackground = couleur_activebackground,
                                  activeforeground = couleur_activeforeground)
                                  
        """ Implantation des composants
        """
        
        self.panel_001.pack(fill = BOTH,
                            expand = True)
        
        Grid.rowconfigure(self.panel_001, 0, weight=1)
        Grid.rowconfigure(self.panel_001, 1, weight=1)
        Grid.rowconfigure(self.panel_001, 2, weight=1)
        Grid.rowconfigure(self.panel_001, 3, weight=1)
        Grid.rowconfigure(self.panel_001, 4, weight=1)
        Grid.rowconfigure(self.panel_001, 5, weight=1)
        Grid.rowconfigure(self.panel_001, 6, weight=1)
        Grid.rowconfigure(self.panel_001, 7, weight=1)
        Grid.rowconfigure(self.panel_001, 8, weight=1)
        Grid.rowconfigure(self.panel_001, 9, weight=1)
        Grid.rowconfigure(self.panel_001, 10, weight=1)
        Grid.columnconfigure(self.panel_001, 0, weight=1)
        Grid.columnconfigure(self.panel_001, 1, weight=1)
        
        self.label_prénom.grid(column = 0,
                                row = 0,
                                sticky = W+E)
        
        self.entry_prénom.grid(column = 1,
                               row = 0,
                               sticky = W+E)
        
        self.label_nom.grid(column = 0,
                                row = 1,
                                sticky = W+E)
        
        self.entry_nom.grid(column = 1,
                               row = 1,
                               sticky = W+E)
        
        self.label_date_naissance.grid(column = 0,
                                row = 2,
                                sticky = W+E)
        
        self.entry_date_naissance.grid(column = 1,
                               row = 2,
                               sticky = W+E)
        
        self.label_lieu_naissance.grid(column = 0,
                                row = 3,
                                sticky = W+E)
        
        self.entry_lieu_naissance.grid(column = 1,
                               row = 3,
                               sticky = W+E)
        
        self.label_adresse.grid(column = 0,
                                row = 4,
                                sticky = W+E)
        
        self.entry_adresse.grid(column = 1,
                               row = 4,
                               sticky = W+E)
        
        self.label_ville.grid(column = 0,
                                row = 5,
                                sticky = W+E)
        
        self.entry_ville.grid(column = 1,
                               row = 5,
                               sticky = W+E)
        
        self.label_cp.grid(column = 0,
                                row = 6,
                                sticky = W+E)
        
        self.entry_cp.grid(column = 1,
                               row = 6,
                               sticky = W+E)
        
        self.label_motif.grid(column = 0,
                                row = 7,
                                sticky = W+E)
        
        self.entry_motif.grid(column = 1,
                               row = 7,
                               sticky = W+E)
        
        self.label_date_sortie.grid(column = 0,
                                row = 8,
                                sticky = W+E)
        
        self.entry_date_sortie.grid(column = 1,
                               row = 8,
                               sticky = W+E)
        
        self.label_heure_sortie.grid(column = 0,
                                row = 9,
                                sticky = W+E)
        
        self.entry_heure_sortie.grid(column = 1,
                               row = 9,
                               sticky = W+E)
        
        self.btn_generer.grid(column = 0,
                              row = 10,
                              sticky=W+E,
                              columnspan = 2)
    
    def run(self):
        self.interface()
        
    def do_attestation(self, nom, prénom, date_naissance, lieu_naissance, adresse, code_postal, ville, date_sortie, heure_sortie, motif):
        '''
        Génération de l'attestation.
        
        Modèle:
        
        Cree le: 06/04/2020 a 08h31; Nom: Dupont; Prenom: Jean; Naissance: 01/01/1997 a Lyon; Adresse: 999 avenue de France 75001 Paris; Sortie: 06/04/2020 a 08h30; Motifs: sport
        '''
        maintenant = datetime.now()
        date_creation = '{:%d/%m/%Y}'.format(maintenant)
        heure_creation = '{:%Hh%M}'.format(maintenant)
        date_naissance = '{:%d/%m/%Y}'.format(date_naissance)
        date_sortie = '{:%d/%m/%Y}'.format(date_sortie)
        self.autorisation = qrcode.QRCode(version = 2,
                              error_correction = qrcode.constants.ERROR_CORRECT_L,
                              box_size=5,
                              border=4)
        self.autorisation.add_data('Cree le: {} a {}; Nom: {}; Prenom: {}; Naissance: {} a {}; Adresse: {} {} {}; Sortie: {} a {}; Motifs: {}'.format(date_creation,
                                                                                                                                                                       nom,
                                                                                                                                                                       heure_creation,
                                                                                                                                                                       prénom,
                                                                                                                                                                       date_naissance,
                                                                                                                                                                       lieu_naissance,
                                                                                                                                                                       adresse,
                                                                                                                                                                       code_postal,
                                                                                                                                                                       ville,
                                                                                                                                                                       date_sortie,
                                                                                                                                                                       heure_sortie,
                                                                                                                                                                       motif))
        self.autorisation.make(fit = True)
        self.mon_qr = self.autorisation.make_image(fill_color="black", back_color="white")
        self.mon_qr_tk = ImageTk.PhotoImage(self.mon_qr)
        
        
        
        self.fenetre_qr = Toplevel()
        self.fenetre_qr.title('Votre autorisation')
        
        self.fenetre_qr.afficher_qr = Button(self.fenetre_qr,
                                   image = self.mon_qr_tk,
                                   command = self.do_record)
        
        self.fenetre_qr.afficher_qr.pack(fill = BOTH, expand = 1)
        
    def do_record(self):
        ''' Enregistement de l'image
        '''
        self.mon_qr.save('autorisation.png')
        self.fenetre_qr.destroy()

if __name__ == '__main__':
    w = Tk()
    
    def do_GUI_attestation():
        ''' Lancer la GUI pour la création de l'attestation
        '''
        App = ExitGenerator_GUI(debug = True)
        App.run()
        
    w.title('pyExitGenerator - Cliquez pour générer une attestation')
    w.fichier_image = Image.open('images/get-me-out.jpg')
    w.geometry('300x200')
    
    w.fichier_image_converti = ImageTk.PhotoImage(w.fichier_image)
    
    w.bouton = Button(w,
                      image = w.fichier_image_converti,
                      command = do_GUI_attestation)
    
    w.bouton.pack(expand = 1,
                  fill=BOTH)
   
    w.resizable(width = False,
                height = False)
   
    w.mainloop()
