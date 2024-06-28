# The Dealmaker: ANL 2024 Agent
This repository contains the implementation of our negotiation agent, The Dealmaker, developed for the Automated Negotiation League (ANL) 2024.

## Introduction
The Dealmaker is designed to negotiate bilaterally with other agents, aiming to maximize its individual utility without knowledge of its opponent's reservation value. It leverages concepts from game theory and negotiation strategy to achieve competitive results.

## Design Overview
The Dealmaker is built as a bilateral negotiation agent equipped with a utility function and access to its opponent’s utility function, excluding the opponent’s reservation value. The negotiation follows the Alternating Offers Protocol (AOP), where offers are exchanged until an agreement is reached or the negotiation fails.

# Agent Components
## Bidding Strategy
The bidding strategy balances exploration and exploitation. It generates offers based on a rational selection process, considering both immediate utility gain and long-term negotiation dynamics. The Dealmaker adapts its bidding strategy to varying opponent behaviors and negotiation contexts.

## Acceptance Strategy
The acceptance strategy strikes a balance between risk-taking and risk-aversion. It evaluates received offers against an adjusted aspiration level derived from relative time and the agent’s reserved value, enabling the agent to navigate negotiation dynamics effectively.

## Reservation Value Modeling
The Dealmaker estimates the opponent’s reservation value using advanced estimation techniques grounded in game theory. It iteratively refines its estimation based on data collected over multiple negotiation sessions, allowing it to anticipate opponent moves and optimize its strategies.

## Development Progression
Initial Implementation: Basic negotiation techniques were implemented.
Dynamic Bidding: Enhanced performance by incorporating dynamic programming and utility-maximizing algorithms.
Improved Bidding Function: Leveraged insights from the opponent’s utility function for sophisticated decision-making.
Competition Submission: Gained valuable insights from initial competition results.
Further Upgrades: Incorporated advanced strategies and refined opponent utility function utilization.
Impressive Competition Results: Achieved remarkable success through meticulous fine-tuning and strategic optimization.
Implementation Details
The Dealmaker is implemented in Python using the NegMAS framework. It integrates theoretical insights into practical negotiation strategies and reflects a deep understanding of game theory and negotiation dynamics.

## Evaluation Strategy
The Dealmaker will be evaluated based on its individual utility performance during the ANL 2024 tournament. Its adaptive strategies enable it to maximize average utility across multiple negotiation sessions.

## Conclusion
The Dealmaker showcases the potential of strategic decision-making and adaptive learning in negotiation settings. Its development underscores the iterative nature of agent development and the power of combining theoretical insights with practical implementation.

## Reflections and Project Experience
Developing The Dealmaker has been an enriching journey, filled with challenges and triumphs. We extend our gratitude to our mentor, Tamara, for her invaluable guidance and support. This project has been an incredible learning experience, and we are excited to see how The Dealmaker performs in the ANL 2024 tournament.
