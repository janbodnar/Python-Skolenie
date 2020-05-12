#!/usr/bin/env python3

import numpy as np

# prints array without truncation; sets the linewidth
with np.printoptions(threshold=np.inf, linewidth=180):

    vals = np.arange(1, 10_000)
    print(vals)


# The use of a context manager (the with-block) ensures that after the context 
# manager is finished, the print options will revert to whatever
# they were before the block started. It ensures the setting is temporary,
# and only applied to code within the block.
