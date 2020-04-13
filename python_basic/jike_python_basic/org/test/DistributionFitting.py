import pandas as pd
import numpy as np
import scipy.stats as st


class DistributionFitting:
    @staticmethod
    def best_fit(investment_size):
        codes = ['norm', 'cauchy', 'expon']

        df = pd.DataFrame(columns=['name', 'num_params', 'log_lik'])

        for code in codes:
            dist = getattr(st, code)
            fit = dist.fit(investment_size)
            df.loc[len(df)] = [
                code,
                len(fit),
                np.sum(dist.logpdf(
                    investment_size,
                    loc=fit[0],
                    scale=fit[1]
                ))
            ]

        df['aic'] = 2 * (df.num_params - df.log_lik)
        df['aic'] = df['aic'].astype(float)

        return (df.loc[df['aic'].idxmin()]['name'])