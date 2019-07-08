from persistry.plugins.generic import GenericProfile2
class PluginClass(object):
    def __init__(self, hive_object):
        self.hive = hive_object
        self.result = []

    def process_plugin(self):
        current = self.hive.current_control_set
        paths = ["Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Shell",
                 "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Userinit",
                 "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Taskman"]

        gen = GenericProfile2(self.hive)
        for path in paths:
            gen.process_plugin(path)
            self.result += gen.result
        self.keys = gen.keys