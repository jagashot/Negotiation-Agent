import numpy as np
from negmas.sao import SAOResponse, SAONegotiator
from negmas import Outcome, ResponseType, SAOState
from scipy.optimize import curve_fit
from typing import List

class Ilan(SAONegotiator):
    def __init__(self, *args, e: float = 5.0, aggressiveness: float = 0.8, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.e = e
        self.aggressiveness = aggressiveness
        self.total_rounds = 0  
        self.opponent_times = []
        self.opponents_utilities = []
        self._past_opponent_rv = 0.0
        self._rational = []

    def on_session_starting(self):
        super().on_session_starting()
        self.total_rounds = self.session.n_steps  

    def __call__(self, state: SAOState) -> SAOResponse:
        self.update_reserved_value(state.current_offer, state.relative_time)
        if self.is_acceptable(state.current_offer, state.relative_time):
            return SAOResponse(ResponseType.ACCEPT_OFFER, state.current_offer)
        return SAOResponse(ResponseType.REJECT_OFFER, self.generate_offer(state.relative_time))

    def generate_offer(self, relative_time) -> Outcome:
        if not self._rational or abs(self.opponent_ufun.reserved_value - self._past_opponent_rv) > 1e-3:
            self._rational = sorted(
                [
                    (my_util, opp_util, _)
                    for _ in self.nmi.outcome_space.enumerate_or_sample(levels=10, max_cardinality=100_00)
                    if (my_util := float(self.ufun(_))) > self.ufun.reserved_value
                       and (opp_util := float(self.opponent_ufun(_))) > self.opponent_ufun.reserved_value
                ]
            )
        if not self._rational:
            return self.ufun.best()
        asp = (1.0 - np.power(relative_time, self.e)) + 1.0
        max_rational = len(self._rational) - 1
        idx = max(0, min(max_rational, int(asp * max_rational * self.aggressiveness)))  
        return self._rational[idx][-1]

    def is_acceptable(self, offer, relative_time) -> bool:
        if offer is None:
            return False
        asp = (1.0 - np.power(relative_time, self.e)) + self.ufun.reserved_value
        return float(self.ufun(offer)) >= asp * 1.2  

    def update_reserved_value(self, offer, relative_time):
        if offer is None:
            return
        self.opponents_utilities.append(float(self.opponent_ufun(offer)))
        self.opponent_times.append(relative_time)
        bounds = ((0.2, 0.0), (5.0, min(self.opponents_utilities)))
        try:
            optimal_vals, _ = curve_fit(
                lambda x, e, rv: (self.opponents_utilities[0] - rv) * (1.0 - np.power(x, e)) + rv,
                self.opponent_times,
                self.opponents_utilities,
                bounds=bounds,
            )
            self._past_opponent_rv = self.opponent_ufun.reserved_value
            self.opponent_ufun.reserved_value = optimal_vals[1] * 0.9  
        except Exception as e:
            pass

def update_strategy_results(agent: Ilan, opponent_results: List[float]):
    agent.opponents_utilities.extend(opponent_results)
    agent.update_reserved_value(None, 0.0) 

# if __name__ == "__main__":
#     from .helpers.runner import run_a_tournament

#     run_a_tournament([Ilan])