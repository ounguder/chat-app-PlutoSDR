from scipy.signal import convolve
from numpy import fix
from .pulse_shape import srrc


def interpolation_with_sinc(sampledData,
                            t: float,
                            oneSidedLength,
                            osFactor,
                            beta=0):
    """
    Interpolate sampled data using a sinc-based interpolation filter.

    This function performs interpolation on the given 'sampledData' using a sinc-based interpolation
    filter, particularly suited for Pulse Amplitude Modulation (PAM) signals. The interpolation is
    performed at the specified time 't' using the provided parameters.

    Args:
        sampledData (numpy.ndarray): Array containing sampled data to be interpolated.
        t (float): Time at which interpolation is performed.
        oneSidedLength (int): Half of the number of symbols in the SRRC pulse.
        osFactor (int): Oversampling factor.
        beta (float, optional): Roll-off factor for the SRRC pulse. Default is 0.

    Returns:
        float: Interpolated value at the specified time 't'.

    Note:
        This function utilizes the 'srrc' function to generate a raised cosine pulse and convolves
        it with the given 'sampledData' to perform interpolation.

    Example:
        data = np.array([...])      # Sampled data array
        time = 2.5                  # Time at which interpolation is performed
        halfSymbols = 4             # Half of the number of symbols in SRRC pulse
        oversamplingFactor = 8      # Oversampling factor
        interpolatedValue = interpolationWithSinc(data, time, halfSymbols, oversamplingFactor)
        # Returns the interpolated value at the specified time 't'.

    """
    # index is the starting point
    nOfLobes = oneSidedLength
    P = osFactor
    l = P * nOfLobes
    tnow = int(fix(t))
    tau = t - fix(t)
    # print(f'tau from int = {tau}')
    s_tau = srrc(l, beta, 1, tau)
    x_tau = convolve(sampledData[tnow - l:tnow + l + 1], s_tau, 'full')
    y = x_tau[(2 * l) + 2]
    return y