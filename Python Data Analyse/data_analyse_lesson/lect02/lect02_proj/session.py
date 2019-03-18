""" Sessionization
session.py To iteratively discover sessions in the timestamps and hold active
session information to apply to new timestamps coming.

Author: Peng Wang <peng.wang@guavus.com>
"""
import numpy as np


class Sessionizer(object):
    def __init__(self, min_session_length=3, max_error=None,
                 max_pctg_error=None, max_session_period=1440,
                 active_sessions=None, max_session_id=None):
        """
        Parameters
        ----------
        min_session_length: int, default 3.
            Minimum length to be considered as session.
        max_error: float, max allowed error for session period, optional.
            If None, no error is allowed.
        max_pctg_error: float, max percentage erorr for session period, optional.
            If None, no error is allowed.
        max_session_period: float,  default 1440 minutes (1 day).
            Max allowed session period.
        active_sessions: list or 2d array, optional.
            Buffered session information to use for predicting sessions for
            new alarms, hold timestamps, session_ids, session_periods,
            session_length. If None, restart the sessionization process.
        max_session_id: int, optional.
            The newest session_id currently. If None, defaults to -1.
        """
        self.min_session_length = min_session_length

        if max_error is None:
            self.max_error = 0.0
        else:
            self.max_error = max_error
        if max_pctg_error is None:
            self.max_pctg_error = 0.0
        else:
            self.max_pctg_error = max_pctg_error
        if max_session_period is None:
            self.max_session_period = np.Inf
        else:
            self.max_session_period = max_session_period

        self.active_session_timestamps = []
        self.active_session_ids = []
        self.active_session_periods = []
        self.active_session_lengths = []

        if active_sessions is not None:
            last_ts = active_sessions[-1][0]
            ## active sessions only contain the session in last
            ## min_session_length * max_session_period
            first_ts = last_ts - self.min_session_length * self.max_session_period
            for ts, si, sp, sl in active_sessions:
                if ts < first_ts:
                    continue
                self.active_session_timestamps.append(ts)
                self.active_session_ids.append(si)
                self.active_session_periods.append(sp)
                self.active_session_lengths.append(sl)

        if max_session_id is None:
            self.max_session_id = -1
        else:
            self.max_session_id = max_session_id

    def sessionize(self, X):
        """Iteratively discover sessions.
        Parameters
        ----------
        X: list or array-like, timestamps (converted to float) to be sessionized.
        """
        X = list(X)
        all_timestamps = self.active_session_timestamps + X
        ## number of active alarms and new alarms
        self.n_actives_ = len(self.active_session_ids)
        self.n_samples_ = len(X)
        ## sesion_ids_ holds the discovered session_ids_
        ## sesion_id of -1 means it is a singleton or has not been assigned to a session.
        self.session_ids_ = [-1 for _ in range(self.n_samples_)]
        self.session_periods_ = [-1 for _ in range(self.n_samples_)]
        self.session_lengths_ = [-1 for _ in range(self.n_samples_)]

        ## try to match new alarms to exsiting sessions
        active_session_map = dict()
        for i in range(self.n_actives_):
            if self.is_sessionized(i):
                sid = self.active_session_ids[i]
                sp = self.active_session_periods[i]
                sl = self.active_session_lengths[i]
                if sid not in active_session_map:
                    active_session_map[sid] = {"si": [i], "sp": sp, "sl": sl}
                else:
                    active_session_map[sid]["si"].append(i)
        ## first try to map new alarms to the active sessions
        for sid in sorted(active_session_map.keys()):
            session = active_session_map.get(sid)
            indices, intervals = self._match_active_session(session,
                                                            all_timestamps)
            old_si = session["si"]
            old_sp = session["sp"]
            old_sl = session["sl"]

            ## update session_length, session_period, sessio_id
            new_sl = old_sl + len(indices)
            new_sp = (old_sp * (old_sl - 1) + np.sum(intervals)) / float(new_sl - 1)
            ## update active alarm
            for i in old_si:
                self.active_session_periods[i] = new_sp
                self.active_session_lengths[i] = new_sl
            ## update new alarm
            for i in indices:
                j = i - self.n_actives_
                self.session_ids_[j] = sid
                self.session_periods_[j] = new_sp
                self.session_lengths_[j] = new_sl

        ## iteratively searching for new sessions
        step = 1
        while step < self.get_n_unsessionized() - 1:
            indices, intervals = self._find_new_session(all_timestamps, step)

            ## valid sessions should meet the minimum length requirement
            session_length = len(indices)
            if session_length < self.min_session_length:
                step += 1
                continue

            ## valid sessions should have a period no greater than max_period
            period = np.mean(intervals)
            if period > self.max_session_period:
                step += 1
                continue

            ## a new session is found, increment max_session_id
            self.max_session_id += 1
            for i in indices:
                if i < self.n_actives_:
                    self.active_session_ids[i] = self.max_session_id
                    self.active_session_periods[i] = period
                    self.active_session_lengths[i] = session_length
                else:
                    j = i - self.n_actives_
                    self.session_ids_[j] = self.max_session_id
                    self.session_periods_[j] = period
                    self.session_lengths_[j] = session_length

        ## update active sessions
        self._update_active_sessions(X)

        return self

    def _match_active_session(self, session, X):
        """Method to map new alarms to active sessions.
        Parameters
        ----------
        session: dictionary, hold the information of a active session to be
        mapped.
        X: list or array, timestamps of new alarms.

        Returns
        -------
        indices: list, the list of indices of the new alarms mapped to an active
        session.
        intervals: list, the list of time intervals of the new alarms mapped to
        an active session.
        """
        indices = []
        intervals = []

        prev = session["si"][-1]  ## the index of last alarm in the active sesion
        min_interval = session["sp"]  ## set to the active session_period
        max_interval = session["sp"]  ## set to the active session_period
        prev_ts = self.active_session_timestamps[prev]  ## timestamp of last
        while prev is not None:
            _next = self._find_session_next(X, min_interval, max_interval, prev, forward=True)
            ## search forward in the new alarms
            if _next is not None:
                indices.append(_next)
                intervals.append(X[_next] - prev_ts)
                prev_ts = X[_next]
                ## update the min and max intervals
                min_interval = min(min_interval, intervals[-1])
                max_interval = max(max_interval, intervals[-1])
            prev = _next

        return indices, intervals

    def _find_new_session(self, X, step):
        """Method to find one session in X.
        Parameters
        ----------
        X: list or array-like, timestamps.
        step: int, number of steps to look for session seed in the iteration.

        Returns
        -------
        indices: list, the list of index of the discovered session.
        intervals: list, the sucessive intervals between the timestamps in the session.
        """
        left = -1
        ## max error allowed for session period
        max_error = max(self.max_error,
                        self.max_pctg_error * self.max_session_period)
        while left < self.n_actives_ + self.n_samples_:
            indices = []
            intervals = []
            ## find the left seed index of a new session
            left = self._find_next(left)
            if left is None:
                return indices, intervals
            indices.append(left)

            ## find the right seed index of a new session
            right = left
            for _ in range(step):
                if right is None:
                    break
                right = self._find_next(right)
            if right is None:
                return indices, intervals

            indices.append(right)
            intervals.append(X[right] - X[left])
            if np.mean(intervals) > self.max_session_period + max_error:
                left += 1
                continue

            ## once the seed indices (left/right) are found
            ## use the mean interval of the candidate session as period and search within
            ## time(left)-period <= t <= time(right) + period for next ring
            ## search forward
            prev = right
            while True:
                min_intervals = np.min(intervals)
                max_intervals = np.max(intervals)
                _next = self._find_session_next(X, min_intervals, max_intervals, prev, forward=True)
                if _next is None:
                    break
                indices.append(_next)
                intervals.append(X[_next] - X[prev])
                prev = _next

            ## search backward
            prev = left
            while True:
                min_intervals = np.min(intervals)
                max_intervals = np.max(intervals)
                _next = self._find_session_next(X, min_intervals, max_intervals, prev, forward=False)
                if _next is None:
                    break
                indices.append(_next)
                intervals.append(X[prev] - X[_next])
                prev = _next

            ## return the index and intervals if the candidate meet
            if (len(indices) >= self.min_session_length and
                    np.mean(intervals) <= self.max_session_period + max_error):
                return indices, intervals

            ## increment left seed index
            left += 1

        return indices, intervals

    def _find_session_next(self, X, min_interval, max_interval, i, forward=True):
        """Method to look for the next index belonging to the current session.
        Parameters
        ----------
        X: list or array-like, timestamps.
        min_interval: float, the minimum time interval in the current session.
        max_interval: float, the maximum time interval in the current session.
        i: int, the starting index to look
        forward: bool, default=True.
            Direction to search for the next index. If True, search forward; if
            False, search backward.
        """
        if forward:
            step = 1
            end = len(X)
        else:
            step = -1
            end = -1
        for j in range(i + step, end, step):
            if self.is_sessionized(j):
                continue
            interval = (X[j] - X[i]) * step
            max_error = max(self.max_error, max_interval * self.max_pctg_error)
            if interval < min_interval - max_error:
                continue
            elif interval > max_interval + max_error:
                break
            else:
                return j

        return None

    def _find_next(self, i):
        """Method to find the next un-sessionized index of the input array.
        Parameters
        ----------
        i: int, starting index to search the next index.
        """
        for j in range(i + 1, self.n_actives_ + self.n_samples_):
            if not self.is_sessionized(j):
                return j
        return None

    def _update_active_sessions(self, X):
        """Method to update active sessions.
        Parameters
        ----------
        X: list or array, the timestamps of new alarms.
        """
        ## hold the old active alarms
        tmp_timestamps = self.active_session_timestamps + X
        tmp_ids = self.active_session_ids + self.session_ids_
        tmp_periods = self.active_session_periods + self.session_periods_
        tmp_lengths = self.active_session_lengths + self.session_lengths_

        ## reset active alarms to empty
        self.active_session_timestamps = []
        self.active_session_ids = []
        self.active_session_periods = []
        self.active_session_lengths = []

        ## update the active alarms
        last_ts = tmp_timestamps[-1]
        first_ts = last_ts - self.min_session_length * self.max_session_period
        for ts, i, p, l in zip(tmp_timestamps, tmp_ids, tmp_periods, tmp_lengths):
            if ts < first_ts:
                continue
            else:
                self.active_session_timestamps.append(ts)
                self.active_session_ids.append(i)
                self.active_session_periods.append(p)
                self.active_session_lengths.append(l)

        return self

    def is_sessionized(self, i):
        """Method return whether ith element of the input has been sessionized.
        Parameters
        ----------
        i: int, index of the element.
        """
        if i < self.n_actives_:
            return self.active_session_ids[i] > -1

        j = i - self.n_actives_
        return self.session_ids_[j] > -1

    def get_n_unsessionized(self):
        """Return the number of unsessionized."""
        return np.sum([1 for sid in
                       self.active_session_ids + self.session_ids_ if sid == -1])

    def get_session_ids(self):
        """Return the session ids."""
        return self.session_ids_

    def get_session_periods(self):
        """Return the session periods."""
        return self.session_periods_

    def get_session_lengths(self):
        return self.session_lengths_


def test_params(X, X_test, **kwargs):
    """Test sessionization parameters with X and X_test)."""
    print(25 * "-" + " Test " + 25 * "-")
    print("\n".join(["%s=%s" % (k, v) for k, v in kwargs.items()]))
    print("\n")
    sessionizer = Sessionizer(**kwargs)
    sessionizer.sessionize(X)

    print("training timestamps:\n", X)
    print("training session_ids:\n", sessionizer.get_session_ids())
    print("training session_periods:\n", sessionizer.get_session_periods())
    print("training session_lengths:\n", sessionizer.get_session_lengths())
    print("\n")
    print(sessionizer.sessionize(X_test))
    print("test timestamps:\n", X_test)
    print("test session_ids:\n", sessionizer.get_session_ids())
    print("test session_periods:\n", sessionizer.get_session_periods())
    print("test session_lengths:\n", sessionizer.get_session_lengths())
    print(56 * "-")
    print("\n")


def test():
    """
    Test cases and expected output.
    """
    X = [1, 11, 20, 30, 40, 47, 50, 61, 75, 89, 92]  ## train
    X_test = [103, 105, 118, 121]  ## test

    ## Parmaeter set 1
    ## X session_ids should be [-1, -1, 0, 0, 0, 1, 0, 1, 1, 1, -1]
    ## X session_periods should be [-1, -1, 10, 10, 10, 14, 10, 14, 14, 14, -1]
    ## X session_lengths should be [-1, -1, 4, 4, 4, 4, 4, 4, 4, 4, -1]
    ## X_test session_ids should be [1, 2, 2, -1]
    ## X_test sesion_periods should be [14, 13, 13, -1]
    ## X_test sessin_lengths should be [5, 3, 3, -1]
    params = {"min_session_length": 3,
              "max_error": 0,
              "max_pctg_error": 0,
              "max_session_period": 1440}
    test_params(X, X_test, **params)

    ## Parameter set 2
    ## X session_ids should be [0, 0, 0, 0, 0, -1, 0, 0, -1, -1, -1]
    ## X session_periods should be [10, 10, 10, 10, 10, -1, 10, 10, -1, -1, -1]
    ## X session_lengths should be [7, 7, 7, 7, 7, -1, 7, 7, -1, -1, -1]
    ## X_test session_ids should be [1, 2, 2, -1]
    ## X_test session_periods should be [28, 13, 13, -1]
    ## X_test session_lengths should be [3, 3, 3, -1]
    params = {"min_session_length": 3,
              "max_error": 1,
              "max_pctg_error": 0,
              "max_session_period": 1440}
    test_params(X, X_test, **params)

    ## Parameter set 3
    ## X session_ids should be [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ## X session_periods should be [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ## X session_lengths should be [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ## X_test session_ids should be [0, -1, -1, -1]
    ## X_test session_periods should be [14, -1, -1, -1]
    ## X_test session_lengths should be [5, -1, -1, -1]
    params = {"min_session_length": 5,
              "max_error": 0,
              "max_pctg_error": 0,
              "max_session_period": 1440}
    test_params(X, X_test, **params)

    ## Parameter set 4
    ## X session_ids should be [-1, -1, 0, 0, 0, -1, 0, -1, -1, -1, -1]
    ## X session_periods should be [-1, -1, 10, 10, 10, -1, 10, -1, -1, -1, -1]
    ## X session_lengths should be [-1, -1, 4, 4, 4, -1, 4, -1, -1, -1, -1]
    ## X_test session_ids should be [-1, -1, -1, -1]
    ## X_test session_periods should be [-1, -1, -1, -1]
    ## X_test session_lengths should be [-1, -1, -1, -1]

    params = {"min_session_length": 3,
              "max_error": 0,
              "max_pctg_error": 0,
              "max_session_period": 13}
    test_params(X, X_test, **params)


if __name__ == "__main__":
    test()
