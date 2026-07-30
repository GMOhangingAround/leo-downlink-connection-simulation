# leo-downlink-connection-simulation

Simulates the downlink of a low Earth orbit satellite over a single pass, comparing a fixed QPSK link against adaptive modulation and coding across link budget, throughput and power.

## Requirements

**MATLAB:** R2020a or later. No extra toolboxes needed.

**Python:** 3.8+ with `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
```

## How to run

### MATLAB

Open the desired script in MATLAB and hit Run, or from the command window:

```matlab
cd matlab
plot1_elevation_fspl
```

### Python

From the project root:

```bash
cd python
python plot1_elevation_fspl.py
```

Each script generates one plot and saves it as a PNG in the working directory.

## Scripts

| # | File | Output |
|---|------|--------|
| 1 | `plot1_elevation_fspl` | Elevation angle and FSPL over the pass |
| 2 | `plot2_ebno_amc`       | Eb/N0 with AMC switching thresholds |
| 3 | `plot3_throughput`     | Throughput: fixed QPSK vs AMC |
| 4 | `plot4_power`          | Power consumption: fixed QPSK vs AMC |

## Parameters

Iridium-like downlink, taken from ETSI ETR 093:

- Altitude: 780 km
- Carrier frequency: 1.62 GHz
- Channel bandwidth: 31.5 kHz
- Bit rate: 50 kbps
- Pass duration: 420 s
- AMC thresholds (target BER = 10⁻⁵): BPSK < 9.6 dB ≤ QPSK < 13.5 dB ≤ 16-QAM

Edit parameters at the top of each script to experiment.
