"""
**Submitted to ANAC 2024 Automated Negotiation League**
*Team* type your team name here
*Authors* type your team member names with their emails here

This code is free to use or update given that proper attribution is given to
the authors and the ANAC 2024 ANL competition.
"""
import random

from negmas.sao import ResponseType, SAONegotiator, SAOResponse, SAOState


class MyNegotiator(SAONegotiator):
    """
    Your agent code. This is the ONLY class you need to implement
    """

    rational_outcomes = tuple()

    def on_preferences_changed(self, changes) -> None:
        """
        Called when the ufun is set and on any change to the ufun.

        Remarks:
            - Can optionally be used for initializing your agent.
            - We use it to save a list of all rational outcomes.

        """
        if self.ufun is None:
            return
        self.rational_outcomes = [
            _
            for _ in self.nmi.outcome_space.enumerate_or_sample()
            if self.ufun(_) > self.ufun.reserved_value
        ]

    def __call__(self, state: SAOState) -> SAOResponse:
        """
        Called to (counter-)offer.

        Args:
            state: the `SAOState` containing the offer from your partner (None if you are just starting the negotiation)
                   and other information about the negotiation (e.g. current step, relative time, etc).
        Returns:
            A response of type `SAOResponse` which indicates whether you accept, or reject the offer or leave the negotiation.
            If you reject an offer, you are required to pass a counter offer.

        Remarks:
            - This is the ONLY function you need to implement.
            - You can access your ufun using `self.ufun`.
            - You can access the mechanism for helpful functions like sampling from the outcome space using `self.nmi` (returns an `SAONMI` instance).
            - You can access the current offer (from your partner) as `state.current_offer`.
              - If this is `None`, you are starting the negotiation now (no offers yet).
        """
        offer = state.current_offer
        if self.ufun is None:
            return SAOResponse(ResponseType.END_NEGOTIATION, None)
        if self.ufun(offer) > (2 * self.ufun.reserved_value):
            return SAOResponse(ResponseType.ACCEPT_OFFER, offer)
        return SAOResponse(
            ResponseType.REJECT_OFFER, random.choice(self.rational_outcomes)
        )


if __name__ == "__main__":
    from .helpers.runner import run_a_tournament

    # if you want to do a very small test, use the parameter small=True here. Otherwise, you can use the default parameters.
    run_a_tournament(MyNegotiator, small=True)
