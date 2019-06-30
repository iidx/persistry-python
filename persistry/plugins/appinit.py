from persistry.plugins.generic import GenericProfile2
class PluginClass(object):
    def __init__(self, hive_object):
        self.hive = hive_object
        self.result = []

    def process_plugin(self):
        appinit_dlls = ["Microsoft\\Windows NT\\CurrentVersion\\Windows\\AppInit_DLLs",
                        "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\AppInit_DLLs",
                        "Microsoft\\Windows NT\\CurrentVersion\\Windows\\LoadAppInit_DLLs",
                        "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\LoadAppInit_DLLs",
                        "CurrentControlSet\\Control\\Session Manager\\AppCertDlls"]

        gen = GenericProfile2(self.hive)
        for path in appinit_dlls:
            gen.process_plugin(path)
            self.result += gen.result
        self.keys = gen.keys