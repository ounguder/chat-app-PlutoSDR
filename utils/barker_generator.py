from numpy import add, array
"""
    Generates a Barker code header based on the specified Barker type and modulation type.

    Parameters:
    - barker_type (str): Type of Barker code to generate ('barker13', 'barker11', or 'barker7').
    - modulation_type (str): Type of modulation ('QAM3' or other).

    Returns:
    - header (array of complex numbers): Barker code header modulated based on the specified Barker type and modulation type.
    """

def barker_generator(barker_type, modulation_type):
    headerType = barker_type
    header = array([])
    if headerType == 'barker13':
        barker_real = [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1]
        barker_imag = [1j, 1j, 1j, 1j, 1j, -1j, -1j, 1j, 1j, -1j, 1j, -1j, 1j]
        header = add(barker_real, barker_imag)
    elif headerType == 'barker11':
        barker_real = [1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1]
        barker_imag = [1j, 1j, 1j, -1j, -1j, -1j, 1j, -1j, -1j, 1j, -1j]
        header = add(barker_real, barker_imag)
    elif headerType == 'barker7':
        barker_real = [1, 1, 1, -1, -1, 1, -1]
        barker_imag = [1j, 1j, 1j, -1j, -1j, 1j, -1j]
        header = add(barker_real, barker_imag)
    else:
        print('Input header')

    if modulation_type == 'QAM3':
        header = header * 3
    else:
        header = header * 1.1
    return header