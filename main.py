# inspire by https://github.com/kushalbhabra/pyMidi

import pygame.midi
import ConfigFileHelper
import MidiKeyListener

# (Default-)Variables
device_id = -1
# wanted_midi_device = b'nanoKONTROL2'
wanted_midi_device = b'nanoPAD2'

# Read Keys from File
filename = "config.txt"
mapping_list = ConfigFileHelper.get_file_content(filename)

# init
pygame.init()
pygame.midi.init()

midiListener = MidiKeyListener.MidiKeyListener(mapping_list)
midiListener.search_midi_device(wanted_midi_device)
midiListener.start()

while True:
    pass

print("skip exit")
WindowsKeyMapper.exit_script()
pygame.midi.quit()
pygame.quit()
exit()
