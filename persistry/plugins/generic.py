class GenericProfile1(object):
    """
        @description: Key - Value 단순 조합 프로필
        @profiles: knowndlls
    """
    def __init__(self, hive_object):
        self.hive = hive_object

    def process_plugin(self, subkey_path):
        self.result = []
        if 'CurrentControlSet' in subkey_path:
            subkey_path = self.hive.set_current_control_set(subkey_path)
        for hive in self.hive.get_hive_objects():
            try:
                key = hive.get_key_by_path(subkey_path)
                last_write = str(key.last_written_time)
                for v in hive.get_key_by_path(subkey_path).values:
                    print(v.data)
                    self.result.append([last_write, v.name, self.hive.get_string(v)])
            except Exception as e:
                pass
    @property
    def keys(self):
        return ('Last Written Time', 'Entry Name', 'Image Path')

class GenericProfile2(object):
    """
        @description: value or subkey를 입력하면 알아서 뚝딱해줍니다. 일단 실험용
        @profiles: appinit, bootexecute
    """
    def __init__(self, hive_object):
        self.hive = hive_object

    def process_plugin(self, subkey_path):
        self.result = []
        if 'CurrentControlSet' in subkey_path:
            subkey_path = self.hive.set_current_control_set(subkey_path)

        for hive in self.hive.get_hive_objects():
            try:
                val = None
                key = hive.get_key_by_path(subkey_path)
                if not key:
                    key = hive.get_key_by_path(subkey_path[:subkey_path.rfind('\\')])
                    val = subkey_path.split('\\')[-1]
                last_write = str(key.last_written_time)
                value_str = self.hive.get_string(key.get_value_by_name(val))

                for v in key.values:
                    self.result.append([last_write, v.name, self.hive.get_string(v)])
            except Exception as e:
                pass
    
    @property
    def keys(self):
        return ('Last Written Time', 'Entry Name', 'Image Path')


