"""
@author: Andre Rittner Pires Correa
"""


import matplotlib.pyplot as plt
import json


class Plot():
    
    def __init__(self,  RVE_origin, fibres):
        fig, ax = plt.subplots()
        rect = plt.Rectangle(RVE_origin, RVE_origin[0]*-2, RVE_origin[1]*-2, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        
        for fibre in fibres:
            x=fibre[0]
            y=fibre[1]
            circ = plt.Circle((x,y), fibre[2], linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(circ)
        
        size = max(-2*RVE_origin[0], -2*RVE_origin[1])
        ax.set_xlim(-size/2., size/2.)
        ax.set_ylim(-size/2., size/2.)
        plt.show()



        

    
