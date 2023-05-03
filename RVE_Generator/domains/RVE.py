"""
@author: Andre Rittner Pires Correa
"""

# from .domains import RectangularDomain

import numpy as np


class RVE_definition:    
    def __init__(self, RVE):
        self.origin = (-float(RVE['Length'])/2., -float(RVE['Thickness'])/2.)
        self.Vf=float(RVE['Fibre Volumetric Fraction'])
        
class Fibre_definition:    
    def __init__(self, fibres):
        self.radius = float(fibres['Radius'])
        

