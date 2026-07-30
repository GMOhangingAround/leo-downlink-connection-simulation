"""
Plot 2: Eb/N0 variation with AMC switching points
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 420                  # Pass duration (s)
theta_min = 8.2          # Min elevation angle (deg)
theta_max = 90           # Max elevation angle (deg)
Re = 6371e3              # Earth radius (m)
h = 790e3                # Satellite altitude (m)
f = 1.62e9               # Carrier frequency (Hz)
c = 3e8                  # Speed of light (m/s)
wavelength = c / f

# Time array
t = np.arange(0, T + 1, 1)

# Elevation angle model (sinusoidal pass)
elevation = theta_min + (theta_max - theta_min) * np.sin((np.pi * t) / T)
elevation_rad = np.deg2rad(elevation)

# Slant range (law of cosines, central angle alpha)
alpha = np.pi / 2 - elevation_rad - np.arcsin((Re * np.cos(elevation_rad)) / (Re + h))
slant = np.sqrt(Re**2 + (Re + h)**2 - 2 * Re * (Re + h) * np.cos(alpha))

# Free-space path loss (dB)
fspl = 20 * np.log10((4 * np.pi * slant) / wavelength)

# Eb/N0 model — assume peak Eb/N0 of 16 dB at minimum FSPL
EbN0_peak = 16
fspl_min = np.min(fspl)
EbN0 = EbN0_peak - (fspl - fspl_min)

# AMC thresholds (dB)
threshold_BPSK_QPSK = 9.6
threshold_QPSK_16QAM = 13.5

# Plot
plt.figure(figsize=(6, 3.5))
plt.plot(t, EbN0, 'b-', lw=2, label=r'$E_b/N_0$')
plt.axhline(9.6, color='r', ls='--', label='BPSK→QPSK = 9.6 dB')
plt.axhline(13.5, color='m', ls='--', label='QPSK→16-QAM = 13.5 dB')
plt.xlabel('Time (s)'); plt.ylabel(r'$E_b/N_0$ (dB)')
plt.title(r'$E_b/N_0$ Variation with AMC Switching Points')
plt.grid(True); plt.legend()
plt.tight_layout()
plt.savefig('ebno_amc.png', dpi=150)
plt.show()
