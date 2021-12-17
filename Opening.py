# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
        if 'orientation' not in self.parameters:
               self.parameters['orientation'] = 0     
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                # Définir ici les sommets
                    [0, 0, 0 ], #Sommet0
                    [0, 0, self.parameters['height']],#1
                    [self.parameters['width'], 0, self.parameters['height']], #2
                    [self.parameters['width'], 0, 0], #3
                    [0,self.parameters['thickness'] ,0], #4
                    [0,self.parameters['thickness'] ,self.parameters['height']], #5
                    [self.parameters['width'],self.parameters['thickness'], 0 ], #6
                    [self.parameters['width'],self.parameters['thickness'],self.parameters['height']]#7
                ]
        self.faces = [
                # définir ici les faces
                 #[0,3,2,1],
                 #[6,4,5,7],
                 [4,0,1,5],
                 [3,6,7,2],
                 [0,3,6,4],
                 [1,2,7,5]                
                ]   
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        
       
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen                
        #3eme face
        gl.glVertex3fv([0,self.parameters['thickness'] ,0])
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv( [0,self.parameters['thickness'] ,self.parameters['height']])
        #4eme face
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv([self.parameters['width'],self.parameters['thickness'], 0 ])
        gl.glVertex3fv([self.parameters['width'],self.parameters['thickness'],self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        #5eme face
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv([self.parameters['width'],self.parameters['thickness'], 0 ])
        gl.glVertex3fv([0,self.parameters['thickness'] ,0])
        #6eme face
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'],self.parameters['thickness'],self.parameters['height']])
        gl.glVertex3fv([0,self.parameters['thickness'] ,self.parameters['height']])
        
        gl.glEnd()
        
        gl.glPopMatrix()