from persistry.plugins.generic import GenericProfile2
class PluginClass(object):
    def __init__(self, hive_object):
        self.hive = hive_object
        self.result = []

    def process_plugin(self):
        current = self.hive.current_control_set
        paths = ["CurrentControlSet\\Control\\Session Manager\\BootExecute",
                 "CurrentControlSet\\Control\\Session Manager\\SetupExecute",
                 "CurrentControlSet\\Control\\Session Manager\\Execute",
                 "CurrentControlSet\\Control\\Session Manager\\S0InitialCommand"]
       
        gen = GenericProfile2(self.hive)
        for path in paths:
            gen.process_plugin(path)
            self.result += gen.result
        self.keys = gen.keys