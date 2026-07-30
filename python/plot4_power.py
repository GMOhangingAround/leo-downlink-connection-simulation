import numpy as np
import matplotlib.pyplot as plt

# Parameters
T, theta_min, theta_max = 420, 8.2, 90
Re, h = 6371e3, 790e3
wavelength = 3e8 / 1.62e9

# Pass geometry
t = np.arange(0, T + 1)
elev = np.deg2rad(theta_min + (theta_max - theta_min) * np.sin(np.pi * t / T))
alpha = np.pi/2 - elev - np.arcsin(Re * np.cos(elev) / (Re + h))
slant = np.sqrt(Re**2 + (Re + h)**2 - 2 * Re * (Re + h) * np.cos(alpha))

# FSPL and Eb/N0 (peak 16 dB at min FSPL)
fspl = 20 * np.log10(4 * np.pi * slant / wavelength)
EbN0 = 16 - (fspl - fspl.min())

# AMC thresholds
th_BQ, th_Q16 = 9.6, 13.5

# Power consumption
fixed_QPSK_power = np.ones_like(t, dtype=float)
required = np.where(EbN0 < th_Q16, th_BQ, th_Q16)  # required Eb/N0 per region
AMC_power = np.minimum(10 ** ((required - EbN0) / 10), 1)

# Plot
plt.figure(figsize=(6, 3.5))
plt.plot(t, fixed_QPSK_power, 'r--', lw=2, label='Fixed QPSK')
plt.plot(t, AMC_power, 'b-', lw=2, label='AMC')
plt.xlabel('Time (s)'); plt.ylabel('Normalised Power Consumption')
plt.title('Power Consumption Comparison: Fixed QPSK vs AMC')
plt.ylim(0, 1.2); plt.grid(True); plt.legend()
plt.tight_layout()
plt.savefig('power_comparison.png', dpi=150)
plt.show()
