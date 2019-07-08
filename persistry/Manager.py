#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import imp
from enum import Enum
import pyregf
from collections import namedtuple
import persistry

class PluginManager:
    def __init__(self, plugin_directory=None):
        if not plugin_directory:
            persistry_path = os.path.abspath(os.path.dirname(persistry.__file__))
            plugin_directory = os.path.join(persistry_path, "plugins/")
        self.plugin_directory = plugin_directory
        self.plugins = []
        self._set_plugins()

    def _set_plugins(self):
        for plugin in os.listdir(self.plugin_directory):
            if plugin.endswith(".py") and plugin[:-3] != "__init__":
                if plugin == 'generic.py':
                    continue
                plugin_name = plugin[:-3]
                self.plugins.append(plugin_name)

    def load_plugin(self, plugin):
        try:
            found_plugin = imp.find_module(plugin, [self.plugin_directory])
        except ImportError as error:
            print('Plugin Not Found:', error)
            return None
        try:
            module = imp.load_module(plugin, found_plugin[0], found_plugin[1], found_plugin[2])
        except TypeError as error:
            print(error)
            return None
        return module

class HiveManager:
    def __init__(self, path):
        """
            path에서 registry hive를 읽어와 pyregf 객체를 지정해둠
        """
        self.path = path
        self.hives = {
            'DEFAULT': None,
            'NTUSER.DAT': [],
            'SAM': None,
            'SOFTWARE': None,
            'SECURITY': None,
            'SYSTEM': None,
            'UsrClass.dat': None,
        }
        self._loader()

    def _loader(self):
        for hive_name in self.hives:
            path = os.path.join(self.path, hive_name)
            if not os.path.isfile(path):
                continue
            try:
                reg = pyregf.file()
                reg.open(path)
            except Exception as e:
                print('reg open error', e)
                sys.exit(-1)
            if hive_name == 'NTUSER.DAT':
                self.hives[hive_name].append(reg)
            else:
                self.hives[hive_name] = reg
        self._set_current_control_set_string()

    def get_string(self, hive_object):
        """
            @description: data_as_string 메소드가 유니코드를 차별해요. 짜증나ㅋㅋ
            @input: pyregf type object
        """
        try:
            string = hive_object.data_as_string
            return string
        except:
            pass
        try:
            """
                만약 \x00\x00으로 문자열 혹은 데이터를 구분한다면 strip되서 붙어버림
                따로 처리가 필요한경우 \x00\x00을 선행적으로 다른 문자열로 치환 필요.
            """
            string = hive_object.data.replace(b'\x00', b'')
            return string.decode('utf-8')
        except:
            return None

    def _set_current_control_set_string(self):
        """
            @getter: self.current_control_set
            @type: integer
        """
        ccs_value = self.system.get_key_by_path('Select')
        ccs_value = ccs_value.get_value_by_name('Current').data_as_integer
        self.current_control_set = "ControlSet00%d" % ccs_value

    def set_current_control_set(self, string):
        return string.replace('CurrentControlSet', self.current_control_set)

    def add_user_profile(self, path):
        """
            ntuser.dat 추가
            --add-user-profile=uc:\\user1\\ntuser.dat
        """
        pass
    
    def get_hive_objects(self):
        return (self.default, self.ntuser, self.sam, self.software, self.security, self.system, self.usrclass)

    @property
    def default(self):
        return self.hives['DEFAULT']
    
    @property
    def ntuser(self):
        #temporal setting
        return self.hives['NTUSER.DAT'][0]
    
    @property
    def sam(self):
        return self.hives['SAM']
    
    @property
    def software(self):
        return self.hives['SOFTWARE']

    @property
    def security(self):
        return self.hives['SECURITY']
    
    @property
    def system(self):
        return self.hives['SYSTEM']
    
    @property
    def usrclass(self):
        return self.hives['UsrClass.dat']

class Persistry:
    def __init__(self, hive_path):
        self.hive = HiveManager(hive_path)
        self.plugin = PluginManager()

    def analysis(self):
        """
            플러그인 돌려돌려돌림판
        """
        for module_name in self.plugin.plugins:
            print('[+]', module_name, 'start')
            mod = self.plugin.load_plugin(module_name)
            mod = mod.PluginClass(self.hive)
            mod.process_plugin()