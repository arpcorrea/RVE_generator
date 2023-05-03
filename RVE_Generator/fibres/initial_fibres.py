"""
@author: Andre Rittner Pires Correa
"""


import numpy as np
import random

class Place_Fibre():
    
    def __init__(self,  RVE, fibres):
        # import pdb; pdb.set_trace()
        rve_origin = RVE.origin
        Vf_target = RVE.Vf
        r=fibres.radius
        tol = r/4.8
        max_penetration=r/4.
        self.place_initial_fibres(rve_origin, r)
        
        while self.Vf_actual < Vf_target:    
            # import pdb; pdb.set_trace()
            self.do_loop(rve_origin, r, tol, max_penetration, self.fibres)
        
        
        
    def place_initial_fibres(self, rve_origin, r):
        l=rve_origin[0]
        t = rve_origin[1]
        point = [(-l, -t, r),(l, t, r),(l, - t, r),(-l, t, r), (0,0,r)]
        self.fibres = point
        self.Vf_actual = 2*np.pi*r**2/(2*rve_origin[0]*2*rve_origin[1])
        return self.fibres, self.Vf_actual
    
    
    def create_fibre(self, l, w, r, tol, max_penetration):
        # import pdb; pdb.set_trace()
        flag=0
        flagx_accept=0
        flagy_accept=0
        flagx=0
        flagy=0
        point=[]
        while flag == 0:
            while flagx_accept == 0:
                x = random.uniform(-l/2, l/2.)
                if x>-l/2.+r+tol and x<l/2.-r-tol:
                    flagx=0
                    flagx_accept=1
                elif x>l/2.-max_penetration:
                    flagx = 1
                    flagx_accept=1
                elif x<-l/2+max_penetration:
                    flagx=-1
                    flagx_accept=1
    
            while flagy_accept == 0:
                y = random.uniform(-w/2., w/2.)
                if y>-w/2.+r+tol and y<w/2.-r-tol:
                    flagy=0
                    flagy_accept=1
                elif y>w/2.-max_penetration:
                    flagy = 1
                    flagy_accept=1
                elif y<-w/2+max_penetration:
                    flagy=-1
                    flagy_accept=1
                    
            if flagx==0 and flagy==0:
                point.append((x,y,r))
            elif flagx==0 and flagy==1:
                point.append((x,y,r))
                point.append((x,y-w,r))
            elif flagx==0 and flagy==-1:
                point.append((x,y,r))
                point.append((x,y+w,r))
            elif flagx==1 and flagy==0:
                point.append((x,y,r))
                point.append((x-l,y,r))
            elif flagx==-1 and flagy==0:
                point.append((x,y,r))
                point.append((x+l,y,r))
            
            flag = 1
           
        return point    
    
    
    
    def distance_check(self, circles, fibres) :
        # import pdb; pdb.set_trace()
        distances=[]
        for circle in circles:
            xc=circle[0]
            yc=circle[1]
            for fibre in fibres:
                # import pdb; pdb.set_trace()
                xf = fibre[0]
                yf = fibre[1]
                distances.append(np.sqrt(((xc-xf)**2)+((yc-yf)**2)))        
        return distances
    
    def check_colision(self, distances, r, tol):
        for distance in distances:
            if distance < 2*r+tol:
                return False
        return True
            
    
    def do_loop(self, rve_origin, r, tol, max_penetration, fibres ):
        # import pdb; pdb.set_trace()
        test_fibres = self.create_fibre(-2*rve_origin[0], -2*rve_origin[1], r, tol, max_penetration)
        distance = self.distance_check(test_fibres, fibres)
        a = self.check_colision(distance, r, tol)
        if a == True:
            # import pdb; pdb.set_trace()
            for circle in test_fibres:
                fibres.append(circle)
                self.Vf_actual = self.Vf_actual+np.pi*(r**2)/(2*rve_origin[0]*2*rve_origin[1])
        self.fibres = fibres

                

        
    
    

        

    
