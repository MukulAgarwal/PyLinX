'''
Created on 13.11.2014

@author: wplaum
'''
class ToolSelected():
    none            = 0
    newVarElement   = 1
    newPlus         = 2
    max             = newPlus

# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. This function was taken from 
# http://www.ariel.com.au/a/python-point-int-poly.html
# and does not fall under the terms of licence of PyLinXSS

def point_inside_polygon(x,y,polygons):
    
    idxPolygons = []
    
    #print "polygons: ", polygons
    for l in range(len(polygons)):
        inside = False
        poly = polygons[l]
        if poly != None:
            n = len(poly)
            p1x,p1y = poly[0]
            for i in range(n+1):
                p2x,p2y = poly[i % n]
                if y > min(p1y,p2y):
                    if y <= max(p1y,p2y):
                        if x <= max(p1x,p2x):
                            if p1y != p2y:
                                xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
                p1x,p1y = p2x,p2y
            if inside == True:
                idxPolygons.append(l)
            
    return idxPolygons


