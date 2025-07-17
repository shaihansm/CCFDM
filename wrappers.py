import numpy as np

def _spec_to_box(s, dtype):
    dim = int(np.prod(s.shape))
    # existing code... s