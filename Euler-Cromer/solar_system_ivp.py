import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sp_to_xyz(sp):
    # Takes a spherical-coordinate and return an xyz-coordinate
    sp = np.array(sp)
    return np.array([sp[0]*np.sin(np.radians(sp[2]))*np.cos(np.radians(sp[1])), sp[0]*np.sin(np.radians(sp[2]))*np.sin(np.radians(sp[1])), sp[0]*np.cos(np.radians(sp[2]))])
def xyz_to_sp(xyz):
    # Takes an xyz-coordinate and return spherical-coordinate
    return np.array([np.linalg.norm(xyz),np.arctan2(xyz[1],xyz[0]),np.arcos(xzy[2],np.linalg.norm(xyz))])
def derivs(t, currsp):
    # Derivs function for sp coordinates
    r,phi,theta = currsp
    vcirc = np.sqrt(GM*(2/r-1/a))    # m/s
    drdt = 0
    dphidt = +vcirc
    dthetadt = 0
    return [drdt, dphidt, dthetadt]
# Assigning constants for derivatives
T = 1e3
dt = 1
time = [1,T]
tarray = np.arange(1,T,1)
# Assigning planets variabels in spherical coordinates
merc_sp = np.array([0.3871*1.496e+11, 0, 90])
a = 0.3871*1.496e+11
GM = 2.2032e13
sol_merc = np.transpose(solve_ivp(derivs, time, merc_sp,t_eval=tarray)).tolist()
ven_sp = np.array([0.7233*1.496e+11, 0, 90])
a = 0.7233*1.496e+11
GM = 3.24859e14
sol_ven = np.transpose(solve_ivp(derivs, time, ven_sp,t_eval=tarray)).tolist()
earth_sp = np.array([1.000*1.496e+11, 0, 90]).tolist()
a = 1.000*1.496e+11
GM = 3.986004418e14
sol_earth = np.transpose(solve_ivp(derivs, time, earth_sp, t_eval=tarray)).tolist()
mars_sp = np.array([1.5273*1.496e+11, 0, 90])
a = 1.5273*1.496e+11
GM = 4.282837e13
sol_mars = np.transpose(solve_ivp(derivs, time, mars_sp, t_eval=tarray)).tolist()
jup_sp = np.array([5.2028*1.496e+11, 0, 90])
a = 5.2028*1.496e+11
GM = 1.26686534e17
sol_jup = np.transpose(solve_ivp(derivs, time, jup_sp, t_eval=tarray)).tolist()
sat_sp = np.array([9.5388*1.496e+11, 0, 90])
a = 9.5388*1.496e+11
GM = 3.7931187e16
sol_sat = np.transpose(solve_ivp(derivs, time, sat_sp, t_eval=tarray)).tolist()
ura_sp = np.array([19.1914*1.496e+11, 0, 90])
a = 19.1914*1.496e+11
GM = 5.793939e15
sol_ura = np.transpose(solve_ivp(derivs, time, ura_sp, t_eval=tarray)).tolist()
nep_sp = np.array([30.0611*1.496e+11, 0, 90])
a = 30.0611*1.496e+11
GM = 6.836529e15
sol_nep = np.transpose(solve_ivp(derivs, time, nep_sp, t_eval=tarray)).tolist()
# Scale to make in a billionth times smaller
scale = 10**-9
# Change spherical to xyz
sol_merc = sp_to_xyz(sol_merc.y)*scale
sol_ven = sp_to_xyz(sol_ven.y)*scale
sol_earth = sp_to_xyz(sol_earth.y)*scale
sol_mars = sp_to_xyz(sol_mars.y)*scale
sol_jup = sp_to_xyz(sol_jup.y)*scale
sol_sat = sp_to_xyz(sol_sat.y)*scale
sol_ura = sp_to_xyz(sol_ura.y)*scale
sol_nep = sp_to_xyz(sol_nep.y)*scale
f = open("solar_system_new.xyz", "+w")
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
