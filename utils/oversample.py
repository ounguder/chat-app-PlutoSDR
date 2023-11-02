from numpy import zeros


def oversample(my_array, M):
    """
    Oversample an input array by inserting M - 1 zeros between each element.

    This function takes an input array and increases its sampling rate by inserting
    M - 1 zeros between each element. This is commonly used in digital signal processing
    to increase the number of samples for interpolation or other operations.

    Args:
        myArray (numpy.ndarray): Input array to be oversampled.
        M (int): Oversampling factor, indicating the number of samples between each element.

    Returns:
        numpy.ndarray: The oversampled array with M - 1 zeros inserted between each element.

    Example:
        originalArray = np.array([1, 2, 3])  # Input array
        oversamplingFactor = 4               # Oversampling factor
        oversampledArray = oversample(originalArray, oversamplingFactor)
        # oversampledArray contains [1, 0, 0, 0, 2, 0, 0, 0, 3]

    """
    N = len(my_array)
    oversampled_array = zeros(N * M)
    oversampled_array[::M] = my_array
    return oversampled_array