class PluginClass(object):
    service_types = {
        0x001: "Kernel driver",
        0x002: "File system driver",
        0x004: "Arguments for adapter",
        0x008: "File system driver",
        0x010: "Own_Process",
        0x020: "Share_Process",
        0x100: "Interactive",
        0x110: "Interactive",
        0x120: "Share_process Interactive",
        -1: "Unknown",
    }
    service_startup = {
        0x00: "Boot Start",
        0x01: "System Start",
        0x02: "Auto Start",
        0x03: "Manual",
        0x04: "Disabled",
        -1: "Unknown",
    }

    def __init__(self, hive_object):
        self.hive = hive_object

    def process_plugin(self):
        self.result = {}
        for hive_object in self.hive.get_hive_objects():
            self.process_services(hive_object)

    def _type_check(self, type_val):
        if type_val not in self.service_types.keys():
            return self.service_types[-1]
        return self.service_types[type_val]
    
    def _startup_check(self, startup_val):
        if startup_val not in self.service_startup.keys():
            return self.service_startup[-1]
        return self.service_startup[startup_val]

    def process_services(self, hive):
            service_path = '%s\\Services' % (self.hive.current_control_set)
            services = hive.get_key_by_path(service_path)
            if not services:
                return {}

            service_list = []
            objects_list = []
            for service in services.sub_keys:
                service_list.append(service.name)
            
            for service_name in service_list:
                tlist = []
                k = hive.get_key_by_path(service_path + "\\" + service_name)
                key_name = k.name
                last_write = str(k.last_written_time)

                try:
                    type_name = k.get_value_by_name("Type").data_as_integer
                    type_name = self._type_check(type_name)
                except:
                    type_name = "Unknown"
                try:
                    image_path = self.hive.get_string(k.get_value_by_name("ImagePath"))
                except:
                    image_path = "Unknown"
                try:
                    display_name = self.hive.get_string(k.get_value_by_name("DisplayName"))
                except:
                    display_name = "Unknown"
                try:
                    failure_cmd = self.hive.get_string(k.get_value_by_name("FailureCommand"))
                except:
                    failure_cmd = "Unknown"
                try:
                    description = self.hive.get_string(k.get_value_by_name("Description"))
                except:
                    description = "Unknown"
                try:
                    group_name = self.hive.get_string(k.get_value_by_name("Group"))
                except:
                    group_name = "Unknown"
                try:
                    start_type = k.get_value_by_name("Start").data_as_integer
                    start_type = self._startup_check(start_type)
                except:
                    start_type = "Unknown"
                try:
                    service_dll = k.get_subkey_by_name("Parameters")
                    service_dll = self.hive.get_string(service_dll.get_value_by_name("ServiceDll"))
                except:
                    service_dll = "Unknown"

                objects_list.append([last_write, key_name, image_path, type_name, \
                                     display_name, start_type, description, group_name, failure_cmd, service_dll])

            for entry in objects_list:
                keyname = entry.pop(1)
                self.result[keyname] = entry
            

    @property
    def keys(self):
        return ('Last Written Time', 'Entry Name', 'Image Path', 'Type', 'Display Name', 'Startup Type', \
                'Description', 'Group', 'Failure Command', 'Service DLL')