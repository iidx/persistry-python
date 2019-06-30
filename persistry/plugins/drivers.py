from persistry.plugins.generic import GenericProfile1
class PluginClass(object):
    def __init__(self, hive_object):
        self.hive = hive_object

    def process_plugin(self):
        current = self.hive.current_control_set
        path = 'Microsoft\\Windows NT\\CurrentVersion\\Font Drivers'
        gen = GenericProfile1(self.hive)
        gen.process_plugin(path)
        
        self.keys = gen.keys
        self.result = gen.result