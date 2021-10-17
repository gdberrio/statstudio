import pymc3 as pm
import pandas as pd
import numpy as np
import json
from typing import Dict

def CountModel(data: Dict, data_column: str, samples: int = 10000) -> pm.backends.base.MultiTrace:
    """
    Generates trace for Count Model, to check changepoint in count data
    :param data: original count data dataframe
    :param data_column: column in count data dataframe to evaluate
    :param samples: number of samples to MCMC
    :return: trace with samples
    """
    count_data = np.array(list(data.values())).astype(np.float)
    n_count_data = len(count_data)

    with pm.Model() as model:
        alpha = 1.0 / count_data.mean()

        lambda_1 = pm.Exponential('lambda_1', alpha)
        lambda_2 = pm.Exponential('lambda_2', alpha)

        tau = pm.DiscreteUniform('tau', lower = 0, upper = n_count_data - 1)

        idx = np.arange(n_count_data)
        lambda_ = pm.math.switch(tau > idx, lambda_1, lambda_2)

        observation = pm.Poisson('obs', lambda_, observed = count_data)

        step = pm.Metropolis()

        trace = pm.sample(samples, tune = 5000, step = step, cores=1)

    return np.mean(trace['tau'])

if __name__ == '__main__':
    print('import complete!')