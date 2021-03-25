from scipy.stats import norm
from math import sqrt

from data import observation_count, sample_mean

alpha = 0.05
quantile = norm.ppf(1 - alpha / 2)

interval_half_length = quantile / sqrt(observation_count) * sqrt(sample_mean * (1 - sample_mean))

lower_bound = sample_mean - interval_half_length
upper_bound = sample_mean + interval_half_length

print(f'Estimate: {sample_mean:.2f}')
print(f'Confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]')
