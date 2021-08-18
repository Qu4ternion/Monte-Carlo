# Monte-Carlo: simulation to build a Probability Density Distribution (PDF) of losses in a credit portfolio.

## Problem statement:
Commercial banks need to manage and hedge their risks. Before they can do so, they must first study their risks. Among all the credits granted by the bank, there is always a portion that will surely fail, thus causing a portfolio loss. In order for a financing organization to remain solvent and not fall into financial complications, it must properly estimate and anticipate these losses in order to cover them with a certain economic capital: a sort of monetary safety cushion.

## Method:
In order to estimate these important quantities, we use a Correlation Matrix of defaults within 3 economic sectors which we decompose into a Lower Triangular Matrix using a Cholesky Decomposition. We then use an Inverse Normal Law to simulate a Random Vector of 3 distinct Failure Thresholds for each sector. We then generate a new random vector with the desired Correlation Structure. This vector is fed into the simulation loop to build the final statistical distribution (PDF), which can now be used to calculate important quantities such as Expected Loss, Unexpected Loss, Extreme Loss, Maximum Loss, Confidence Intervals, etc.
