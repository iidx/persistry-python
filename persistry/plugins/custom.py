from persistry.plugins.generic import GenericProfile1
class PluginClass(object):
    def __init__(self, hive_object):
        self.hive = hive_object
        self.result = []

    def process_plugin(self):
        current = self.hive.current_control_set
        paths = ["Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce",
                "Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "Microsoft\\Windows\\CurrentVersion\\Run",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
                "Microsoft\\Windows\\CurrentVersion\\RunOnce",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                "Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                "Microsoft\\Windows\\CurrentVersion\\RunServices",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Userinit",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Shell",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Taskman",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\System",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify",
                "Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList",
                "Microsoft\\Active Setup\\Installed Components",
                "Wow6432Node\\Microsoft\\Active Setup\\Installed Components",
                "Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks",
                "Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects",
                "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects",
                "Microsoft\\Windows NT\\CurrentVersion\\Drivers32",
                "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32",
                "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options",
                "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options",
                "Classes\\Exefile\\Shell\\Open\\Command\\(Default)",
                "Microsoft\\Windows NT\\CurrentVersion\\Windows\\Appinit_Dlls",
                "Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Appinit_Dlls",
                "Microsoft\\SchedulingAgent",
                "Microsoft\\Windows\\CurrentVersion\\Shell Extensions\\Approved",
                "Microsoft\\Windows NT\\CurrentVersion\\SvcHost",
                "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Run",
                "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce",
                "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunServices",
                "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce",
                "Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
                "Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Shell",
                "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Load",
                "Software\\Microsoft\\Command Processor\\Autorun",
                "ControlSet00#\\Services",
                "CurrentControlSet001\\Control\\Session Manager\\AppCertDlls",
                "CurrentControlSet001\\Control\\SecurityProviders\\SecurityProviders",
                "CurrentControlSet001\\Control\\Lsa\\Authentication Packages",
                "CurrentControlSet001\\Control\\Lsa\\Notification Packages",
                "CurrentControlSet001\\Control\\Lsa\\Security Packages",
                "ControlSet001\\Control\\Session Manager\\CWDIllegalInDllSearch",
                "ControlSet001\\Control\\SafeBoot",
                "Classes\\Exefile\\Shell\\Open\\Command\\(Default)"]
       
        gen = GenericProfile1(self.hive)
        for path in paths:
            print("\t[-] Processing...", path)
            gen.process_plugin(path)
            if gen.result:
                for x in gen.result:
                    print("\t", x)
            print('-'*50)
            self.result += gen.result
        self.keys = gen.keys
        #print(self.result)