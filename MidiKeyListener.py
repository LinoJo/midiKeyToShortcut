import threading
import pygame.midi
import WindowsKeyMapper


class MidiKeyListener:
    midi_device_id = False
    midi_device = -1
    is_running = False
    thread = -1

    def __init__(self, mapping_list):
        self.mapping_list = mapping_list

    def check_system(self):
        if not self.midi_device_id:
            print('NoMidiDevice', self.midi_device)
            exit(1)
        if self.mapping_list == - 1:
            print('NoMappingList', self.mapping_list)
            exit(2)
        if self.is_running:
            print('ListinerIsRunning')
            exit(3)

    def search_midi_device(self, name):
        # Loop through connected Midi-Devices
        # mdi => midi_device_id
        for midi_device_id in range(pygame.midi.get_count()):
            # is Input enable
            if pygame.midi.get_device_info(midi_device_id)[2] == 1:
                # uncomment folling row to print active Midi-Devices
                # print(pygame.midi.get_device_info(mdi))
                if name in pygame.midi.get_device_info(midi_device_id):
                    # save the wanted midi_device_id
                    self.midi_device_id = midi_device_id
                    break

        # If nothing is found exit program
        if not self.midi_device_id:
            print(str(name) + ' not found!')
            exit(404)
        print(str(pygame.midi.get_device_info(self.midi_device_id)[1]) + ' is selected!')
        self.midi_device = pygame.midi.Input(self.midi_device_id)

    def start(self):
        self.check_system()
        self.is_running = True
        self.thread = threading.Thread(target=self.run_listiener, args=())
        self.thread.start()

    def stop(self):
        self.is_running = False

    def run_listiener(self):
        t1 = {}
        t2 = {}
        while self.is_running:
            try:
                if self.midi_device.poll():
                    midi_events = self.midi_device.read(10)
                    status = midi_events[0][0][0]
                    key_id = midi_events[0][0][1]
                    value = midi_events[0][0][2]
                    data3 = midi_events[0][0][3]
                    timestamp = midi_events[0][1]

                    # "Program change"-Event (mostly Slider and toggle-buttons) see nanoKontrol2
                    # if status == 176:
                    # print(key_id, value, data3)

                    # "Node on"-Event
                    if status == 144:
                        # print(key_id)
                        for element in self.mapping_list:
                            if str(key_id) in element['midi_key']:
                                t2[key_id] = threading.Thread(target=WindowsKeyMapper.run_shortcut_event_with_sleep,
                                                              args=(element['wait'], element['keys']))
                                t2[key_id].start()
                                print(element)

                # "Node of"-Event
                # if status == 128:
                #       print(str(midi_events))

            except Exception as ex:
                WindowsKeyMapper.exit_script()
                print(repr(ex))


WindowsKeyMapper.exit_script()
print('Listener ist stop')
