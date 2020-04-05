from constants import flags_list
class DNA:
    def __init__(self):
        self.data = '10010010010010010010010010010010010010010010010010010010'

    def string_to_flag(self):
        flags = list()
        for x in self.data:
            if self.data[56] == '0':
                flags.append('-f' + flags_list[56])
            if self.data[56] == '1':
                flags.append('-fno' + flags_list[56])
            elif x == '1':
                flags.append('-f' + flags_list[x])
            else:
                flags.append('-fno' + flags_list[x])
        ' '.join(flags)
        return flags
