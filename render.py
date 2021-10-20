from math import sqrt, atan, pi
import kandinsky

MAX_STEP = 50
MAX_DIST = 20
SURFACE_DIST = 0.01

###################
# maths functions #
###################

def length(o,p):
    return sqrt((o[0]-p[0])**2+(o[1]-p[1])**2+(o[2]-p[2])**2)

def product(list0,list2):
    facteurs = []
    for num0, num2 in zip(list0, list2):
        facteurs.append(num0 * num2)
    return facteurs

def addition(list0,list2):
    termes = []
    for num0, num2 in zip(list0, list2):
        termes.append(num0 + num2)
    return termes

def normalize(v):
    root = sqrt(v[0]**2+v[1]**2+v[2]**2)
    v = [i/root for i in v]
    return v

###################
# maths functions #
###################

def GetDist(point):
    sphere      = [0.5,0.5,2.5,0.5]
    sphereDist  = length(point,sphere)-sphere[3]
    planeDist   = point[1]
    distance    = min(sphereDist,planeDist)
    return distance

def GetNormal(p):
    d = GetDist(p)
    e = [0.01,0]
    n = [d-GetDist([p[0]-e[0],p[1]-e[1],p[2]-e[1]]),
         d-GetDist([p[0]-e[1],p[1]-e[0],p[2]-e[1]]),
         d-GetDist([p[0]-e[1],p[1]-e[1],p[2]-e[0]])]
    return normalize(n)

def GetLight(p):
    lightPos = [1,2,-1]
    l = normalize([lightPos[0]-p[0],lightPos[1]-p[1],lightPos[2]-p[2]])
    n = GetNormal(p)
    dif = min(max(l[0]*n[0]+l[1]*n[1]+l[2]*n[2],0),1)
    d = RayMarch([p[0]+n[0]*SURFACE_DIST*2,p[1]+n[1]*SURFACE_DIST*2,p[2]+n[2]*SURFACE_DIST*2],l)
    if d<length(lightPos,p):
        dif *= .1
    return float(dif)

def RayMarch(ro, rd):
    global distanceMapNN
    dO = 0
    for i in range(MAX_STEP):
        p   = addition(ro, [rd[0]*dO,rd[1]*dO,rd[2]*dO] )
        dS  = GetDist(p)
        dO += dS
        if dO>=MAX_DIST:
          dO = MAX_DIST
          break
        if dS<=SURFACE_DIST:
          break
    return dO

def ImageGen(x,y,resolution):
    uv = [(x-.5*resolution[0])/resolution[1],(y-.5*resolution[1])/resolution[1]]
    ro = [0.,.5,0]
    col = [0,0,0]
    rd = normalize((uv[0],uv[1],1))
    d = RayMarch(ro,rd)

    p = [ro[0]+rd[0]*d,ro[1]+rd[1]*d,ro[2]+rd[2]*d]
    dif = GetLight(p);
    col = [dif*255,dif*255,dif*255]

    return col

resolution = (320,222,3)

for y in range(resolution[1]):
    for x in range(resolution[0]):
        kandinsky.set_pixel(x,y, kandinsky.color(ImageGen(x,resolution[1]-y,resolution)))
