# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:53:19 2018

@author: davidcamara
"""

class Recomendation(object):
    '''Gene Adaptation'''
    
    def __init__(self,probUse):
        '''Probability of use of this class for each chromosome'''
        self.probUse = probUse
        
    def execute(self):
        
        abstract