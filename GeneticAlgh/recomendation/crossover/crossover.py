# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:52:42 2018

@author: davidcamara
"""

from GeneticAlgh.recomendation.recomendation import Recomendation

import numpy as np

class Crossover(Recomendation):
    
    def execute(self,popClass):
        newPopClass = self.__cross(popClass)
        return newPopClass

    def __cross(self,popClass):
        '''Choose two chromosomes parents and create two childs and substitute'''
        crossoverPopulation = np.zeros((popClass.numChromosomes,popClass.numGenes))
        for ch in range(0,popClass.numChromosomes-1,2):
            if self.probUse > np.random.rand():
                parent0 = popClass.population[ch]
                parent1 = popClass.population[ch+1]

                childs = [0,0]
                for child in range(len(childs)):
                    randomGens = np.random.randint(0,2,popClass.numGenes)
                    
                    gensFromParent0 = np.where(randomGens==0)[0]
                    gensFromParent1 = np.where(randomGens==1)[0]
                    
                    createdChild = np.zeros((1,popClass.numGenes)).ravel()
                    createdChild[gensFromParent0] = parent0[gensFromParent0]
                    createdChild[gensFromParent1] = parent1[gensFromParent1]
                    childs[child] = createdChild

                crossoverPopulation[ch] = childs[0]
                crossoverPopulation[ch+1] = childs[1]

        if popClass.numChromosomes % 2 != 0:
            crossoverPopulation[-1] = popClass.population[-1]
        popClass.setPopulation(crossoverPopulation.astype(int))
        return popClass
