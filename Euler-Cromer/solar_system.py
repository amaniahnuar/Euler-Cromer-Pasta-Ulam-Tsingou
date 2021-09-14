import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def sp_to_xyz(sp):
    # Takes a spherical-coordinate and return an xyz-coordinate
    return np.array([sp[0]*np.sin(np.radians(sp[2]))*np.cos(np.radians(sp[1])), sp[0]*np.sin(np.radians(sp[2]))*np.sin(np.radians(sp[1])), sp[0]*np.cos(np.radians(sp[2]))])
def xyz_to_sp(xyz):
    # Takes an xyz-coordinate and return spherical-coordinate
    return np.array([np.linalg.norm(xyz),np.arctan2(xyz[1],xyz[0]),np.arcos(xzy[2],np.linalg.norm(xyz))])
def derivs(currsp, t,GM):
    # Derivs function for sp coordinates
    r,phi,theta = currsp
    vcirc = np.sqrt(GM/r)    # m/s
    drdt = 0
    dphidt = +vcirc
    dthetadt = 0
    return [drdt, dphidt, dthetadt]
# Assigning constants for derivatives
T = 1000
dt = 1
time = np.arange(0,T,dt)
# Assigning planets variabels in spherical coordinates
merc_sp = np.array([57.91e9, 0, 90])
ven_sp = np.array([108.2e9, 0, 90])
earth_sp = np.array([227.9e9, 0, 90])
mars_sp = np.array([778.5e9, 0, 90])
jup_sp = np.array([1434e9, 0, 90])
sat_sp = np.array([4495e9, 0, 90])
ura_sp = np.array([2871e9, 0, 90])
nep_sp = np.array([4495e9, 0, 90])
# Finding (spherical) position for each and have them in 3 lists of 3 components
sol_merc = np.transpose(odeint(derivs, merc_sp, time, args=(3.24859e14,)))
sol_ven = np.transpose(odeint(derivs, ven_sp, time, args=(3.24859e14,)))
sol_earth = np.transpose(odeint(derivs, earth_sp, time, args=(3.24859e14,)))
sol_mars = np.transpose(odeint(derivs, mars_sp, time, args=(3.24859e14,)))
sol_jup = np.transpose(odeint(derivs, jup_sp, time, args=(3.24859e14,)))
sol_sat = np.transpose(odeint(derivs, sat_sp, time, args=(3.24859e14,)))
sol_ura = np.transpose(odeint(derivs, ura_sp, time, args=(3.24859e14,)))
sol_nep = np.transpose(odeint(derivs, nep_sp, time, args=(3.24859e14,)))
# Scale to make in a billionth times smaller
scale = 10**-9
# Change spherical to xyz
sol_merc = sp_to_xyz(sol_merc)*scale
sol_ven = sp_to_xyz(sol_ven)*scale
sol_earth = sp_to_xyz(sol_earth)*scale
sol_mars = sp_to_xyz(sol_mars)*scale
sol_jup = sp_to_xyz(sol_jup)*scale
sol_sat = sp_to_xyz(sol_sat)*scale
sol_ura = sp_to_xyz(sol_ura)*scale
sol_nep = sp_to_xyz(sol_nep)*scale
f = open("solar_system.xyz", "+w")
for i in range(len(sol_earth[0])):
    f.write("8\nplanets for solar system\n")
    f.write(str(1)+" "+str(sol_merc[0][i])+" "+str(sol_merc[1][i])+" "+str(sol_merc[2][i])+"\n")
    f.write(str(2)+" "+str(sol_ven[0][i])+" "+str(sol_ven[1][i])+" "+str(sol_ven[2][i])+"\n")
    f.write(str(3)+" "+str(sol_earth[0][i])+" "+str(sol_earth[1][i])+" "+str(sol_earth[2][i])+"\n")
    f.write(str(4)+" "+str(sol_mars[0][i])+" "+str(sol_mars[1][i])+" "+str(sol_mars[2][i])+"\n")
    f.write(str(5)+" "+str(sol_jup[0][i])+" "+str(sol_jup[1][i])+" "+str(sol_jup[2][i])+"\n")
    f.write(str(6)+" "+str(sol_sat[0][i])+" "+str(sol_sat[1][i])+" "+str(sol_sat[2][i])+"\n")
    f.write(str(7)+" "+str(sol_ura[0][i])+" "+str(sol_ura[1][i])+" "+str(sol_ura[2][i])+"\n")
    f.write(str(8)+" "+str(sol_nep[0][i])+" "+str(sol_nep[1][i])+" "+str(sol_nep[2][i])+"\n")
f.close()
