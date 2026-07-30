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

# Throughput
fixed_QPSK = np.full_like(t, 2, dtype=float)
AMC = np.where(EbN0 < 9.6, 1, np.where(EbN0 < 13.5, 2, 4))

# Plot
plt.figure(figsize=(6, 3.5))
plt.plot(t, fixed_QPSK, 'r--', lw=2, label='Fixed QPSK')
plt.plot(t, AMC, 'b-', lw=2, label='AMC')
plt.xlabel('Time (s)'); plt.ylabel('Throughput (bits/symbol)')
plt.title('Throughput Comparison: Fixed QPSK vs AMC')
plt.ylim(0, 5); plt.grid(True); plt.legend()
plt.tight_layout()
plt.savefig('throughput_comparison.png', dpi=150)
plt.show()
