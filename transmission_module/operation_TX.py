from transmission_module.signal_generator_TX import signal_generator
from transmission_module.frame_generator_TX import frame_generator_TX
from utils.my_radio import MyRadio

# PLUTO SDR Setup


def operation_TX(my_SDR: MyRadio, msg: str, plotGraphs: bool, info: bool):
    buffer_length_TX = int(2**18)
    #PULSE
    OVERSAMPLING_RATE = 16
    HALF_NO_OF_SYMBOLS = 6
    ROLLOFF_FACTOR = 0.75
    DATA_LENGTH = 80
    my_frames, single_frame_length, my_header, data_len_with_id = frame_generator_TX(
        data_length=DATA_LENGTH,
        text_message=msg,
        header_type='barker13',
        modulation_type='QAM3',
        info=False)

    my_signal = signal_generator(symbol_frames=my_frames,
                                 buffer_len_TX=buffer_length_TX,
                                 oversampling_rate=OVERSAMPLING_RATE,
                                 half_number_of_symbols=HALF_NO_OF_SYMBOLS,
                                 beta=ROLLOFF_FACTOR,
                                 signal_or_symbols=1,
                                 visualize=plotGraphs,
                                 print_data=False)

    # plt.tight_layout()
    my_signal = my_signal[:buffer_length_TX]
    if info:
        print(f'Appended Symbol Frames Length = {len(my_frames)}')
        print(f'Symbol Frames = {my_frames[:50]}')
        print(f'Message Character Length = {len(msg)}')
        print(my_signal[:-100])
        print(len(my_signal))
        # print(
        #     f'LO Freq = {mySDR.sdr.tx_lo}\nSample Rate = {}\nGain = {txGain}\nPlutoSDR Tx Buffer Sample Size = {txLen}\nNof SPS = {OVERSAMPLING_RATE}\nNof Sidelobes ={HALF_NO_OF_SYMBOLS} \nbeta = {ROLLOFF_FACTOR}\nData Length = {DATA_LENGTH}\nOne Frame Length ={oneFrameLength}\nDataLenWithId = {dataLenWithID}\nHeader ={myHeader}'
        # )

    my_SDR.transmit_samples(my_signal)
    # plt.show()
