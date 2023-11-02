from numpy import zeros, mod, base_repr, floor, sqrt
from numpy.random import rand


def pam_to_letters(symbols_PAM):
    """
    Convert a sequence of PAM-encoded symbols to a string of corresponding letters.

    This function converts a sequence of PAM-encoded symbols into a string of letters,
    where each letter corresponds to a group of four PAM symbols. The PAM symbols are mapped
    to letters based on a specified mapping scheme.

    Args:
        my4Pam (numpy.ndarray): Input array containing PAM-encoded symbols.

    Returns:
        str: The generated string of letters corresponding to the PAM-encoded symbols.

    Note:
        This function assumes a specific PAM-to-letter mapping:
        - PAM 3 maps to binary '01'
        - PAM 1 maps to binary '11'
        - PAM -1 maps to binary '10'
        - PAM -3 maps to binary '00'
        # Default Cast => -3 = -1-1j, -1=-1+j, 1 = +1-1j, 3=1+1j

    Example:
        pamSymbols = np.array([3, 1, -1, 3, 0, -1, 1])  # Input PAM-encoded symbols
        letterString = pam2letters(pamSymbols)
        # letterString contains "31-3"

    """
    N = len(symbols_PAM)
    off = mod(N, 4)
    if off != 0:
        symbols_PAM = symbols_PAM[:N - off]
        # print("Dropping last 2 PAM")
    my_4base = ""
    converted_string = ""

    for symbol in symbols_PAM:
        my_4base += chr(int((symbol + 99) / 2))
        my4bin = (symbol + 99) / 2
        if len(my_4base) == 4:
            my_char = chr(int(my_4base, 4))
            my_4base = ""
            converted_string += my_char
    return converted_string


def letters_to_pam(text):
    """
    Convert a string of letters to a sequence of PAM-encoded symbols.

    This function converts a string of letters into a sequence of PAM-encoded symbols,
    where each letter is mapped to a group of four PAM symbols. The PAM symbols are
    generated based on a specific encoding scheme.

    Args:
        text (str): Input string containing letters to be converted.

    Returns:
        numpy.ndarray: An array of PAM-encoded symbols generated from the input letters.

    Note:
        This function processes input letters to generate PAM-encoded symbols using a specific
        encoding method. Each letter is first converted to a base-4 representation using
        `np.base_repr(ord(c), 4)`, and then the resulting string is padded with zeros to ensure
        a length of four. The PAM symbols are then generated using the formula:
        symbol = 2 * ord(letter) - 99

    Example:
        inputText = "HELLO"         # Input text containing letters
        pamSymbols = letters2pam(inputText)
        # pamSymbols contains [1, -3, -1, -3, -1, 3, -3, -1, 1, 1, 1, -1]

    """
    msg = ""

    for c in text:
        letter = base_repr(ord(c), 4)
        if len(letter) == 4:
            letter = letter
        else:
            letter = '0' + letter
        msg += letter
    symbols_PAM = zeros(len(msg), dtype=int)
    for i in range(len(msg)):
        symbols_PAM[i] = 2 * ord(msg[i]) - 99
    return symbols_PAM


def qam_to_pam(symbols_QAM):
    """
    Convert a sequence of QAM-encoded symbols to a sequence of corresponding PAM-encoded symbols.

    This function converts a sequence of QAM (Quadrature Amplitude Modulation)-encoded symbols into
    a sequence of corresponding PAM (Pulse Amplitude Modulation)-encoded symbols, based on a
    predefined mapping.

    Args:
        QAMSymbols (numpy.ndarray): Input array containing QAM-encoded symbols.

    Returns:
        numpy.ndarray: An array of PAM-encoded symbols generated from the QAM-encoded symbols.

    Note:
        This function performs a conversion of QAM-encoded symbols to PAM-encoded symbols using a
        predefined mapping:
        - QAM (-1 - 1j) maps to PAM -3
        - QAM (-1 + 1j) maps to PAM -1
        - QAM (1 - 1j) maps to PAM 1
        - QAM (1 + 1j) maps to PAM 3

    Example:
        qamSymbols = np.array([1 + 1j, -1 - 1j, -1 + 1j, 1 - 1j])  # Input QAM-encoded symbols
        pamSymbols = qam2pam(qamSymbols)
        # pamSymbols contains [3, -3, -1, 1]

    """
    N = len(symbols_QAM)
    symbols_PAM = zeros(N, dtype=int)
    for i in range(N):
        if symbols_QAM[i] == (-1 - 1j):
            symbols_PAM[i] = -3
        elif symbols_QAM[i] == (-1 + 1j):
            symbols_PAM[i] = -1
        elif symbols_QAM[i] == (1 - 1j):
            symbols_PAM[i] = 1
        else:
            symbols_PAM[i] = 3
    return symbols_PAM


def pam_to_qam(symbols_PAM):
    """
    Convert a sequence of PAM-encoded symbols to a sequence of corresponding QAM-encoded symbols.

    This function converts a sequence of PAM (Pulse Amplitude Modulation)-encoded symbols into
    a sequence of corresponding QAM (Quadrature Amplitude Modulation)-encoded symbols, based on a
    predefined mapping.

    Args:
        PAMsymbols (numpy.ndarray): Input array containing PAM-encoded symbols.

    Returns:
        numpy.ndarray: An array of QAM-encoded symbols generated from the PAM-encoded symbols.

    Note:
        This function performs a conversion of PAM-encoded symbols to QAM-encoded symbols using a
        predefined mapping:
        - PAM -3 maps to QAM (-1 - 1j)
        - PAM -1 maps to QAM (-1 + 1j)
        - PAM 1 maps to QAM (1 - 1j)
        - PAM 3 maps to QAM (1 + 1j)

    Example:
        pamSymbols = np.array([3, -3, -1, 1])  # Input PAM-encoded symbols
        qamSymbols = pam2qam(pamSymbols)
        # qamSymbols contains [(1 + 1j), (-1 - 1j), (-1 + 1j), (1 - 1j)]

    """
    N = len(symbols_PAM)
    symbols_QAM = zeros(N, dtype=complex)
    for i in range(N):
        if symbols_PAM[i] == -3:
            symbols_QAM[i] = (-1 - 1j)
        elif symbols_PAM[i] == -1:
            symbols_QAM[i] = (-1 + 1j)
        elif symbols_PAM[i] == 1:
            symbols_QAM[i] = (1 - 1j)
        else:
            symbols_QAM[i] = (1 + 1j)
    return symbols_QAM


def qam3_to_pam(symbols_QAM3):
    """
    Convert a sequence of 32-QAM-encoded symbols to a sequence of corresponding PAM-encoded symbols.

    This function converts a sequence of 32-QAM-encoded symbols into a sequence of corresponding
    PAM (Pulse Amplitude Modulation)-encoded symbols, based on a predefined mapping.

    Args:
        QAMSymbols (numpy.ndarray): Input array containing 32-QAM-encoded symbols.

    Returns:
        numpy.ndarray: An array of PAM-encoded symbols generated from the 32-QAM-encoded symbols.

    Note:
        This function performs a conversion of 32-QAM-encoded symbols to PAM-encoded symbols using a
        predefined mapping:
        - QAM (-3 - 3j) maps to PAM -3
        - QAM (-1 - 1j) maps to PAM -1
        - QAM (1 + 1j) maps to PAM 1
        - QAM (3 + 3j) maps to PAM 3

    Example:
        qamSymbols = np.array([1 + 1j, -3 - 3j, -1 - 1j, 3 + 3j])  # Input 32-QAM-encoded symbols
        pamSymbols = qam32pam(qamSymbols)
        # pamSymbols contains [3, -3, -1, 1]

    """
    N = len(symbols_QAM3)
    symbols_PAM = zeros(N, dtype=int)
    for i in range(N):
        if symbols_QAM3[i] == (-3 - 3j):
            symbols_PAM[i] = -3
        elif symbols_QAM3[i] == (-1 - 1j):
            symbols_PAM[i] = -1
        elif symbols_QAM3[i] == (1 + 1j):
            symbols_PAM[i] = 1
        else:
            symbols_PAM[i] = 3
    return symbols_PAM


def pam_to_qam3(symbols_PAM):
    """
    Convert a sequence of PAM-encoded symbols to a sequence of corresponding 32-QAM-encoded symbols.

    This function converts a sequence of PAM (Pulse Amplitude Modulation)-encoded symbols into
    a sequence of corresponding 32-QAM (Quadrature Amplitude Modulation)-encoded symbols,
    based on a predefined mapping.

    Args:
        PAMsymbols (numpy.ndarray): Input array containing PAM-encoded symbols.

    Returns:
        numpy.ndarray: An array of 32-QAM-encoded symbols generated from the PAM-encoded symbols.

    Note:
        This function performs a conversion of PAM-encoded symbols to 32-QAM-encoded symbols using a
        predefined mapping:
        - PAM -3 maps to QAM (-3 - 3j)
        - PAM -1 maps to QAM (-1 - 1j)
        - PAM 1 maps to QAM (1 + 1j)
        - PAM 3 maps to QAM (3 + 3j)

    Example:
        pamSymbols = np.array([3, -3, -1, 1])  # Input PAM-encoded symbols
        qamSymbols = pam2qam3(pamSymbols)
        # qamSymbols contains [(-3 - 3j), (-1 - 1j), (1 + 1j), (3 + 3j)]

    """
    N = len(symbols_PAM)
    symbols_QAM3 = zeros(N, dtype=complex)
    for i in range(N):
        if symbols_PAM[i] == -3:
            symbols_QAM3[i] = (-3 - 3j)
        elif symbols_PAM[i] == -1:
            symbols_QAM3[i] = (-1 - 1j)
        elif symbols_PAM[i] == 1:
            symbols_QAM3[i] = (1 + 1j)
        else:
            symbols_QAM3[i] = (3 + 3j)
    return symbols_QAM3


def pam(len, M, var):
    """
    Generate a sequence of PAM-encoded symbols.

    This function generates a sequence of PAM (Pulse Amplitude Modulation)-encoded symbols.
    The PAM symbols are randomly generated and scaled based on the specified modulation
    order (M) and variance. Each symbol is calculated using a specific formula.

    Args:
        length (int): Length of the desired PAM sequence.
        M (int): Modulation order, representing the number of amplitude levels.
        variance (float): Variance of the generated PAM symbols.

    Returns:
        numpy.ndarray: An array of PAM-encoded symbols with the specified length.

    Note:
        The PAM-encoded symbols are generated using the formula:
        symbol = (2 * np.floor(M * np.random.rand()) - M + 1) * np.sqrt(3 * variance / (M**2 - 1))

    Example:
        sequenceLength = 10      # Desired sequence length
        modulationOrder = 4     # Modulation order (number of amplitude levels)
        symbolVariance = 0.5    # Variance of the PAM symbols
        pamSequence = pam(sequenceLength, modulationOrder, symbolVariance)

    """
    sequence = (2 * floor(M * rand(len)) - M + 1) * sqrt(3 * var / (M**2 - 1))
    return sequence