% Plot 3: Throughput comparison between Fixed QPSK and AMC
clear; clc; close all;
% Parameters
T = 420;
theta_min = 8.2;
theta_max = 90;
Re = 6371e3;
h = 790e3;
f = 1.62e9;
c = 3e8;
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
EbN0_peak = 16;
fspl_min = min(fspl);
EbN0 = EbN0_peak - (fspl - fspl_min);
% AMC thresholds
threshold_BPSK_QPSK = 9.6;
threshold_QPSK_16QAM = 13.5;
% Fixed QPSK throughput
fixed_QPSK_throughput = 2 .* ones(size(t)); % bits/symbol
% AMC throughput
AMC_throughput = zeros(size(t));
for i = 1:length(t)
if EbN0(i) < threshold_BPSK_QPSK
AMC_throughput(i) = 1; % BPSK
elseif EbN0(i) < threshold_QPSK_16QAM
AMC_throughput(i) = 2; % QPSK
else
AMC_throughput(i) = 4; % 16-QAM
end
end
% Plot
figure;
plot(t, fixed_QPSK_throughput, 'r--', 'LineWidth', 2);
hold on;
plot(t, AMC_throughput, 'b-', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Throughput (bits/symbol)');
title('Throughput Comparison: Fixed QPSK vs AMC');
grid on;
legend('Fixed QPSK', 'AMC', 'Location', 'best');
ylim([0 5]);
hold off;
