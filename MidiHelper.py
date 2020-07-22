class MidiHelper():
    def __init__(self, id, name, ):
        self.id = id
        self.name = name
        self.node_on = 144
        self.node_of = 128
        self.mode_change = 176
        self.programm_change = 192
        self.channel_aftertouch = 208
        self.pitch_wheel_range = 224
        self.system_exclusive = 240