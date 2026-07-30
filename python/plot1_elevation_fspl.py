import matplotlib.pyplot as plt
import numpy as np

# Parameters 
T  = 420
theta_min = 8.2
theta_max = 90
Re = 6371e3 # in meters
h = 790e3
f = 1.62e9
c = 3e8
wavelength = c/f

#time array from 0 to T
t = np.arange(0, T+1, 1)

fig, ax1 = plt.subplots()

def elevation_function(t, theta_min, theta_max, T):
    return theta_min + (theta_max - theta_min) * np.sin(( np.pi * t )/ T)

def slant_range(elevation_deg, Re, h):
    elevation_rad = np.radians(elevation_deg)
    # central angle from elevation
    alpha = np.pi/2 - elevation_rad - np.arcsin(Re * np.cos(elevation_rad) / (Re + h))
    return np.sqrt(Re**2 + (Re + h)**2 - 2 * Re * (Re + h) * np.cos(alpha))

def fspl_function(R, wavelength):
    return 20 * np.log10(4 * np.pi * R / wavelength)

elevation = elevation_function(t, theta_min, theta_max, T)
slant = slant_range(elevation, Re, h)
fspl  =  fspl_function(slant, wavelength)

# Left axis - elevation
ax1.plot(t, elevation, 'b-', label='Elevation')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Elevation angle (°)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Right axis - FSPL
ax2 = ax1.twinx()
ax2.plot(t, fspl, 'r-', label='FSPL')
ax2.set_ylabel('FSPL (dB)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Elevation Angle and FSPL during Iridium Pass')
plt.show()
