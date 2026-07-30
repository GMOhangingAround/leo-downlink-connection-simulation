% Plot 2: Eb/N0 variation with AMC switching points
clear; clc; close all;
% Parameters
T = 420;
theta_min = 8.2;
theta_max = 90;
Re = 6371e3; % Earth radius in metres
h = 790e3; % Satellite altitude in metres
f = 1.62e9; % Carrier frequency in Hz
c = 3e8; % Speed of light in m/s
wavelength = c / f;
% Time array
t = 0:1:T;
% Elevation angle model
elevation = theta_min + (theta_max - theta_min) .* sin((pi .* t) ./ T);
% Slant range calculation
elevation_rad = deg2rad(elevation);
alpha = pi/2 - elevation_rad - asin((Re .* cos(elevation_rad)) ./ (Re + h));
slant = sqrt(Re.^2 + (Re + h).^2 - ...
2 .* Re .* (Re + h) .* cos(alpha));
% FSPL calculation
fspl = 20 .* log10((4 .* pi .* slant) ./ wavelength);
% Eb/N0 model
% Assumption: peak Eb/N0 is 16 dB at minimum FSPL
EbN0_peak = 16;
fspl_min = min(fspl);
EbN0 = EbN0_peak - (fspl - fspl_min);
% AMC thresholds
threshold_BPSK_QPSK = 9.6;
threshold_QPSK_16QAM = 13.5;
% Plot
figure;
plot(t, EbN0, 'b-', 'LineWidth', 2);
hold on;
yline(threshold_BPSK_QPSK, 'r--', 'LineWidth', 1.5);
yline(threshold_QPSK_16QAM, 'm--', 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('E_b/N_0 (dB)');
title('E_b/N_0 Variation with AMC Switching Points');
grid on;
legend('E_b/N_0', ...
'BPSK to QPSK threshold = 9.6 dB', ...
'QPSK to 16-QAM threshold = 13.5 dB', ...
'Location', 'best');
hold off;
