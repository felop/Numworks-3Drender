# Numworks 3Drender
<img src="numworks.jpg" width=44% align="right">

![](https://img.shields.io/tokei/lines/github/felop/numworks-3Drender?color=orange&logo=CodeForces&logoColor=orange)

Very inefficient way to render a 3D Scene on a numworks calculator, using Ray Marching.

I just rewrote [my GLSL scirpt](https://github.com/felop/NeuralRayMarching) in python to run it on my calculator. Fun to use dispite the extremely slow render speed per frame :
 - ~10 minutes
 - ~5 minutes (without the shadows)


### Examples of GLSL functions coded in python

```python
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
```
