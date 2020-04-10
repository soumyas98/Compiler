class MemberMD:
    def __init__(self, e_time, c_time, e_file):
        self.exec_time = e_time
        self.compile_time = c_time
        self.exec_file = e_file

    def get_dict(self):
        d = dict()
        d['exec-time'] = self.exec_time
        d['comp-time'] = self.compile_time
        d['exec-file'] = self.exec_file
        return d

    def __repr__(self):
        return 'e_time: {}s, c_time: {}s, file: {}'.format(
            self.exec_time, self.compile_time, self.exec_file
        )
