from microbit import *

Rs = pin6
E = pin7
DB = [pin16,pin15,pin14,pin13,pin12,pin8,pin3,pin4]

#ecriture sur le bus
def ecrireSurLeBus(donnee):
 for i in range (0,8):
    DB[i].write_digital(((donnee & (1<<i))>>i))
 #envoyer commande  
def envoyerCommande(cmde):
    pin6.write_digital(0)
    pin7.write_digital(1)
    ecrireSurLeBus(cmde)
    sleep(1)
    pin7.write_digital(0)
    


#afficher caractere    
def afficherCaractere(car):
    pin6.write_digital(1)
    pin7.write_digital(1)
    ecrireSurLeBus(ord(car))
    sleep(1)
    pin7.write_digital(0)
    

#afficher message
def afficherMessage(txt):

    for i in range(0,len(txt)):
        afficherCaractere(txt[i])  
    
display.off()

#positionnement de curseur
def positionnerCurseur(lig,col):
    if lig == 1:
        envoyerCommande(0x80+ (col-1))
    if lig == 2:
        envoyerCommande(0xC0+ (col-1))
x= 250
#initialisation de l'ecran
envoyerCommande(0x0D)
envoyerCommande(0x01)
envoyerCommande(0x3F)
#positionner sur deuxieme colonne
positionnerCurseur(2,2)
afficherMessage('x/3='+str(x/3))
