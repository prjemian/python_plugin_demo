from .interfacer import PluginBase


class Plugin1(PluginBase):
    def register(self):
        print(f"register: {__file__}::{self.__class__.__name__}")

    def action(self):
        print(f"action: {__file__}::{self.__class__.__name__}")


class PluginA(PluginBase):
    def register(self):
        print(f"register: {__file__}::{self.__class__.__name__}")

    def action(self):
        print(f"action: {__file__}::{self.__class__.__name__}")
