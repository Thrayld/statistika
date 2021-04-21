import pandas as pd
import scipy.stats as stats

slow = (27.4, 26.2, 26.2, 29.4, 30.1, 28.2, 27.0, 28.4)
shock = (25.9, 26.4, 27.0, 27.8, 26.3, 27.6, 27.0, 25.6)

df = pd.DataFrame({'slow': slow, 'shock': shock})
print(df.describe())

_, p_value = stats.ttest_ind(df['slow'], df['shock'],
                             equal_var=False,
                             alternative='greater')
print(f'p-value: {p_value:.3f}')
