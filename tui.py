import time

import pytermgui as ptg
from pytermgui.enums import SizePolicy as SP

from enigma import Enigma

decoder = Enigma()
encoder = Enigma()

default_encoder = "[2 @34;123;255]Cipher text is: [inverse]"
default_decoder = "[2 @34;123;255]Decoded text is: [inverse]"

encoder_text_input = ptg.InputField(prompt="Enter Plain Text: ")
encoder_result = ptg.Label()
decoder_result = ptg.Label()
decoder_text_input = ptg.InputField(prompt="Enter Encoded Text: ")
total_count = ptg.Label("-0-")


def handle_encode(e):
    val = encoder_text_input.value
    val = encoder.run(val)
    if len(val) == 0:
        encoder_result.value = ""
        return
    encoder_result.value = default_encoder + val


def handle_decode(e):
    val = decoder_text_input.value
    val = decoder.run(val)
    if len(val) == 0:
        decoder_result.value = ""
        return
    decoder_result.value = default_decoder + val


encoder_button = ptg.Button("Encode Value", onclick=handle_encode)
decoder_button = ptg.Button("Decode Value", onclick=handle_decode)


def _define_layout():
    layout = ptg.Layout()
    layout.add_slot("Header", height=1)
    layout.add_break()
    layout.add_slot("body_top")
    layout.add_break()
    layout.add_slot("body_bottom")
    layout.add_break()
    layout.add_slot("footer", height=1)

    return layout


with ptg.WindowManager() as manager:
    manager.layout = _define_layout()

    manager.add(ptg.Window("[bold]Enigma Python App", box="EMPTY"))

    encoder_win = ptg.Window(
                   encoder_text_input,
                   "\n\n",
                   encoder_button,
                   "\n\n",
                   encoder_result,
                   title="Encoder",
            )

    decoder_win = ptg.Window(
                    decoder_text_input,
                    "\n\n",
                    decoder_button,
                    "\n\n",
                    decoder_result,
                    title="Decoder"
            )

    manager.add(encoder_win, assign="body_top")
    manager.add(decoder_win, assign="body_bottom")

    footer = ptg.Window(total_count, box="EMPTY")

    manager.add(footer, assign="footer")

