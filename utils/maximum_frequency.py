from numpy import fft, argmax, arange, abs


def maximum_frequency(rx_nth_power, fs):
    """
    Calculate the frequency corresponding to the maximum amplitude in a signal's power spectral density.

    This function takes the Nth power received signal 'rxNthPower' and its sampling frequency 'fs', computes
    the power spectral density (PSD) of the signal, and determines the frequency corresponding to the
    maximum amplitude in the PSD.

    Args:
        rxNthPower (numpy.ndarray): Nth power received signal.
        fs (float): Sampling frequency of the signal.

    Returns:
        float: The frequency corresponding to the maximum amplitude in the power spectral density.

    Note:
        This function uses the Fast Fourier Transform (FFT) to calculate the power spectral density of
        the squared received signal. The frequency corresponding to the maximum amplitude is determined
        from the PSD.

    Example:
        receivedSignalSquared = np.array([...])  # Squared received signal
        samplingFrequency = 1000                 # Sampling frequency of the signal
        maxFrequency = maxFreq(receivedSignalSquared, samplingFrequency)
        # Returns the frequency corresponding to the maximum amplitude in the PSD.
    """
    psd = fft.fftshift(abs(fft.fft(rx_nth_power)))
    f = arange(-fs / 2.0, fs / 2.0, fs / len(psd))
    max_freq = f[argmax(psd)]
    return max_freq
