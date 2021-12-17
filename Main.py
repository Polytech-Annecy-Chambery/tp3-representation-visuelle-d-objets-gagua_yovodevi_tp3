# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017
=@author: lfoul
"""


from sys import exit
import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu
from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy


def Q1a():
    return Configuration()
    
def Q1b_f():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 0, 0]}). \
        setParameter('xAxisColor', [1, 0, 1]). \
        setParameter('yAxisColor', [1,0,0]) \
        
def Q2b():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
            ) 

def Q2c():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
            )

def Q3a():
    WALL1=Wall({'position': [1, 1, 0], 'width':7 , 'height':2.6 , 'orientation':90 ,'thickness':0.2 ,'color':[0.7,0.7,0.7]})
    return Configuration().add(WALL1)
  
   

def Q4a():
    # Ecriture en utilisant des variables : A compléter
    wall1 = Wall({'position': [0, 0, 0], 'width':7 , 'height':2.6 , 'orientation':0 ,'thickness':0.2 ,'color':[0.7,0.7,0.7]})
    wall2 = Wall({'position': [7,0,0], 'width':7 , 'height':2.6 , 'orientation':90 ,'thickness':0.2 ,'color':[0.7,0.7,0.7]})
    wall3 = Wall({'position': [0,7,0], 'width':7 , 'height':2.6 , 'orientation':0 ,'thickness':0.2 ,'color':[0.7,0.7,0.7]})
    wall4 = Wall({'position': [0,0,0 ], 'width':7 , 'height':2.6 , 'orientation':90,'thickness':0.2 ,'color':[0.7,0.7,0.7]})  
    house = House({'position': [-3, 1, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)   
    
def Q5a():  
    # Ecriture avec mélange de variable et de chaînage    
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
    return Configuration().add(opening1).add(opening2)
    
def Q5b():  
    # Ecriture avec mélange de variable et de chaînage   
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    print(section.canCreateOpening(opening1))
    print(section.canCreateOpening(opening2))    
    print(section.canCreateOpening(opening3))
    return Configuration()    
    
def Q5c1():      
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    sections = section.createNewSections(opening1)
    configuration = Configuration()
    for x in sections:
        configuration.add(x)    
    return configuration     
    
def Q5c2():      
    section = Section({'width':7, 'height':2.6})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    sections = section.createNewSections(opening2)
    configuration = Configuration()
    for section in sections:
        configuration.add(section)    
    return configuration    

def Q5d():      
    pass
    
def Q6():  
    pass  
 
def main():
    # Enlever un des commentaires pour la question traitée
    
    #configuration = Q1a()
    #configuration = Q1b_f()
    #configuration = Q2b()
    #configuration = Q2c()
    #configuration = Q3a()
    #configuration = Q4a()
    #configuration = Q5a()
    configuration = Q5b()
    # configuration = Q5c1()
    # configuration = Q5c2() 
    # configuration = Q5d()
    # configuration = Q6()
    configuration.display()     
         
# Calls the main function
if __name__ == "__main__":
    main()

    # pygame.init()
    # display=(600,600)
    # pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    # # Sets the screen color (white)
    # gl.glClearColor(1, 1, 1, 1)
    # # Clears the buffers and sets DEPTH_TEST to remove hidden surfaces==
    # gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)                  
    # gl.glEnable(gl.GL_DEPTH_TEST)    
    
    # # Placer ici l'utilisation de gluPerspective.
    # glu.gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # gl.glTranslatef(0.0, 2, -5)
    # gl.glRotatef(-90, 1, 0, 0)
    
    
    # gl.glBegin(gl.GL_LINES) # Indique que l'on va commencer un trace en mode lignes (segments)    
    
    # gl.glColor3fv([1, 0, 0]) # Indique la couleur du prochian segment x en RGB
    # gl.glVertex3fv((0, 0, -2)) # Premier vertice : dÃ©part de la ligne
    # gl.glVertex3fv((1, 0, -2)) # DeuxiÃ¨me vertice : fin de la ligne
    
    # gl.glColor3fv([0, 1, 0]) # Indique la couleur du prochian segment y en RGB
    # gl.glVertex3fv((0, 0, -2)) # Premier vertice : dÃ©part de la ligne
    # gl.glVertex3fv((0, 1, -2)) # DeuxiÃ¨me vertice : fin de la ligne
    
    # gl.glColor3fv([0, 0, 1]) # Indique la couleur du prochian segment Z en RGB
    # gl.glVertex3fv((0, 0, -2)) # Premier vertice : dÃ©part de la ligne
    # gl.glVertex3fv((0, 0, -1)) # DeuxiÃ¨me vertice : fin de la ligne
    
    
    # gl.glEnd() # Fin du tracÃ©
    # pygame.display.flip() # Met Ã  jour l'affichage de la fenÃªtre graphique
    
    # continuer=True
    
    # while continuer:
    #     for event in pygame.event.get():
    #         	if event.type == pygame.QUIT:
    #                 continuer=False
    #                 pygame.quit()
    #                 exit()    
