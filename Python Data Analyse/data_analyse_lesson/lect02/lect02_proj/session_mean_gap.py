"""
session class to be used for sessionization
input is array with 2 columns (first column timestamp, second column transaction duration)
session_ids, gaps, real_gaps will be computed for each record
"""

import numba
import numpy as np
from sklearn.utils.validation import check_is_fitted


@numba.jit
def is_sorted(array):
    """O(1) implementation on random arrays."""
    for i in xrange(array.size-1):
        if array[i+1] < array[i]:
            return False
    return True

@numba.jit
def if_and_or(b, x, y):
    """conditional OR function
    """
    if b:
        return x
    return y


class Sessionizer(object):
    def __init__(self, initial_gap=1.0, gap_factor=2.0):
        self.initial_gap = initial_gap
        self.gap_factor = gap_factor

    def fit(self, X):
        """ Fit the data and save sessions.

        Parameters
        ----------
        X: array, with 2 columns.
            First column the timestamps, second column transaction duration.
        """
        self.n_samples_ = X.shape[0]
        self.X_ = X
        ## assure X is sorted in first column
        assert is_sorted(X[:, 0])
        ## assure there is at least one observation
        assert self.n_samples_ > 0
        ## assure timestamps is sorted
        assert is_sorted(self.X_[:, 0])
        ## session_ids
        self.session_ids_ = np.zeros((self.n_samples_, ), dtype=np.int32)
        self.gaps_ = np.zeros((self.n_samples_, ), dtype=np.float64)
        self.real_gaps_ = np.zeros((self.n_samples_, ), dtype=np.float64)

        if sum((self._get_gap(i) > 0 for i in xrange(1, self.n_samples_))) > 0:
            self.mean_gap_initial_ = self.initial_gap
        else:
            self.mean_gap_initial_ = 0.0

        mean_gap = self.mean_gap_initial_
        sum_gap = 0.0
        cnt_gap = 0
        session_id = 0
        session_start_idx = 0
        for i in xrange(1, self.n_samples_):
            gap = self._get_gap(i)
            td = self._get_td(i)
            self.gaps_[i] = if_and_or(gap > 0, gap, td)
            #self.real_gaps_[i] = gap
            self.real_gaps_[i] = if_and_or(gap > 0, gap, 0)
            if gap > self.gap_factor * mean_gap:
                self.session_ids_[session_start_idx:i] = session_id
                session_id += 1
                session_start_idx = i
                mean_gap = self.mean_gap_initial_
                sum_gap = 0.0
                cnt_gap = 0
            else:
                if gap > 0:
                    sum_gap += gap
                    cnt_gap += 1
                    mean_gap = sum_gap / cnt_gap
        self.session_ids_[session_start_idx:] = session_id
        return self

    def _get_gap(self, i):
        """ Compute time delta between the start of (i)th tranction and
            the end of (i-1)th transaction
        """
        assert i > 0
        assert i < self.n_samples_
        return self.X_[i, 0] - self.X_[i-1, 0] - self.X_[i-1, 1]

    def _get_td(self, i):
        """ Compute time delta between the start of (i)th tranction and
            the start of (i-1)th transaction
        """
        assert i > 0
        assert i < self.n_samples_
        return self.X_[i, 0] - self.X_[i-1, 0]

    def get_session_id(self):
        """ return session_id
	    """
        check_is_fitted(self, ["session_ids_", "gaps_"])
        return self.session_ids_

    def get_gap(self):
        """ return gap
	    if two consecutive transaction have overlap (the next start is before the last end time)
		    the difference of the two start_time will be as the gap
	    else if no overlap
		the gap is the different between the previous end_time and current start_time
	    """
        check_is_fitted(self, ["session_ids_", "gaps_"])
        return self.gaps_

    def get_real_gap(self):
        """return real_gap
	    if two consecutive transaction have overlap
		    real gap will be 0
	    else if no overlap
		    real_gap is the different between the previous end_time and current start_time
	    """
        check_is_fitted(self, ["session_ids_", "gaps_"])
        return self.real_gaps_
