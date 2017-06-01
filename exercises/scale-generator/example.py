class Scale(object):

    ASCENDING_INTERVALS = ['m', 'M', 'A']
    CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A',
                       'A#', 'B']
    FLAT_CHROMATIC_SCALE = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
                            'A', 'Bb', 'B']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb',
                 'eb']

    def __init__(self, tonic, scale_name, pattern=None):
        self.tonic = tonic.capitalize()
        self.name = self.tonic + ' ' + scale_name
        if pattern is None:
            self.pattern = []
        else:
            self.pattern = pattern
        self.chromatic_scale = self.CHROMATIC_SCALE
        if tonic in self.FLAT_KEYS:
            self.chromatic_scale = self.FLAT_CHROMATIC_SCALE
        self.pitches = self.assign_pitches()

    def assign_pitches(self):
        if not self.pattern:
            return self.reorder_chromatic_scale()
        last_index = 0
        pitches = []
        scale = self.reorder_chromatic_scale()
        for i, interval in enumerate(self.pattern):
            pitches.append(scale[last_index])
            last_index += self.ASCENDING_INTERVALS.index(interval) + 1
        return pitches

    def reorder_chromatic_scale(self):
        index = self.chromatic_scale.index(self.tonic)
        return self.chromatic_scale[index:] + self.chromatic_scale[:index]
