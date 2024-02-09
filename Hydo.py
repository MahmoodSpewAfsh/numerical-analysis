
"""this code is created due to the assignment by mahmood hasani"""


import matplotlib.pyplot as plt
import numpy as np
# we start by the parameters of the equation of our problem whe l = 0 and we used the euler method
psi = 0
dpsi = 1
E = 0
x = 0 
dE = 0.01
hb = 1
m = 1
a = 1
dx = 0.01
n =1
Et =n**2*np.pi**2*hb**2/(2*m*a**2)
psifinal = 1
while psifinal > 0:
    x = 0
    psi = 0
    dpsi =1
    Lpsi = []
    Lx = []
    Lpsi.append(psi)
    Lx.append(x)
    while x<a:
        ddpsi = -2*m*E*psi
        dpsi = dpsi + ddpsi*dx
        psi = psi + dpsi * dx
        x = x + dx
        E = E + dE
        Lpsi.append(psi)
        Lx.append(x)
    print(E)   
    for i in range(len(Lx)):
        Lx[i] = Lx[i] * 50
 
    plt.plot(Lx, Lpsi, label = "when E = {}".format(E))
    plt.legend()
    psifinal = psi
    
    
print(E)

plt.show()
print("exact value is for n =1:{}".format(Et))

# we continue the proccess by the last E we have get 2 times more

psi = 0
dpsi = 1
x = 0 
dE = 0.02
hb = 1
m = 1
a = 1
dx = 0.01
n =2
Et =n**2*np.pi**2*hb**2/(2*m*a**2)
psifinal = -1
while psifinal < 0:
    x = 0
    psi = 0
    dpsi =1
    Lpsi = []
    Lx = []
    Lpsi.append(psi)
    Lx.append(x)
    while x<a:
        ddpsi = -2*m*E*psi
        dpsi = dpsi + ddpsi*dx
        psi = psi + dpsi * dx
        x = x + dx
        E = E + dE
        Lpsi.append(psi)
        Lx.append(x)
    print(E)    
    for i in range(len(Lx)):
        Lx[i] = Lx[i] * 50
    plt.plot(Lx, Lpsi, label = "when E = {}".format(E))
    plt.legend()
    psifinal = psi
    
plt.show()
print("exact value is for n=2:{}".format(Et))

psi = 0
dpsi = 1
x = 0 
dE = 0.02
hb = 1
m = 1
a = 1
dx = 0.01
n =3
Et =n**2*np.pi**2*hb**2/(2*m*a**2)
psifinal = 1
while psifinal > 0:
    x = 0
    psi = 0
    dpsi =1
    Lpsi = []
    Lx = []
    Lpsi.append(psi)
    Lx.append(x)
    while x<a:
        ddpsi = -2*m*E*psi
        dpsi = dpsi + ddpsi*dx
        psi = psi + dpsi * dx
        x = x + dx
        E = E + dE
        Lpsi.append(psi)
        Lx.append(x)
    print(E)  
    for i in range(len(Lx)):
        Lx[i] = Lx[i] * 50
  
    plt.plot(Lx, Lpsi, label = "when E = {}".format(E))
    plt.legend()
    psifinal = psi
    
plt.show()
print("exact value is for n = 3:{}".format(Et))