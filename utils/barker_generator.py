from numpy import add, array


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