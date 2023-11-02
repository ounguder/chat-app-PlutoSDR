from numpy import arange, sqrt, cos, sin, pi


def srrc(syms, beta, P, t_off=0):
    """
    Generate a Square-Root Raised Cosine (SRRC) pulse shape.

    This function generates a Square-Root Raised Cosine (SRRC) pulse shape for pulse shaping in
    digital communication systems. The generated pulse shape is scaled based on provided parameters.

    Args:
        syms (int): Half of the total number of symbols.
        beta (float): Roll-off factor for the SRRC pulse shape.
        P (int): Oversampling factor.
        t_off (float, optional): Time offset. Default is 0.

    Returns:
        numpy.ndarray: An array representing the generated SRRC pulse shape.

    Note:
        The SRRC pulse shape is generated based on the provided parameters. It is used for pulse
        shaping in digital communication systems.

    Example:
        halfSymbols = 4        # Half of the total number of symbols
        rollOffFactor = 0.5    # Roll-off factor for the SRRC pulse shape
        oversamplingFactor = 8 # Oversampling factor
        pulseShape = srrc(halfSymbols, rollOffFactor, oversamplingFactor)
        # Returns the generated SRRC pulse shape.

    """
    # s = (4*beta/np.sqrt(P)) kismi srrcyi scale ediyor.
    # syms  = Half of Total Number of Symbols
    P = P
    beta = beta
    length_SRRC = P * syms * 2
    start = float((-length_SRRC / 2) + 1e-8 + t_off)
    stop = float((length_SRRC / 2) + 1e-8 + t_off)
    step = float(1)
    k = arange(start=start, stop=stop + 1, step=step, dtype=float)
    if beta == 0:
        beta = 1e-8
    denom = (pi * (1 - 16 * ((float(beta) * k / float(P))**2)))
    # s = (np.cos((1 + beta) * np.pi * k / P) + (np.sin(
    #     (1 - beta) * np.pi * k / P) / (4 * beta * k / P))) / denom
    s = (4 * beta / sqrt(P)) * (cos((1 + beta) * pi * k / P) + (sin(
        (1 - beta) * pi * k / P) / (4 * beta * k / P))) / denom
    return s