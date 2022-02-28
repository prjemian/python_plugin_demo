# python_plugin_demo
Demonstration of a simple Python plugin system.

Derived from: https://gist.github.com/will-hart/5899567

## External plugin

from `/tmp/external_tmp.py`:

```py
"""
Example of user-supplied plugin.
"""

from plugins.interfacer import PluginBase


class PluginTmp(PluginBase):
    def register(self):
        print(f"register: {__file__}::{self.__class__.__name__}")

    def action(self):
        print(f"action: {__file__}::{self.__class__.__name__}")
```

## Output

Output from running `demo.py`:

```
register: /home/prjemian/Documents/plugin_demo/plugins/example_a.py::PluginA
register: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::Plugin1
register: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::PluginA
main
len(PluginBase.plugins) = 3
register: /tmp/example_tmp.py::PluginTmp
len(PluginBase.plugins) = 4
main(): plugin = <plugins.example_a.PluginA object at 0x7f22581ada90>
action: /home/prjemian/Documents/plugin_demo/plugins/example_a.py::PluginA
main(): plugin = <plugins.example_1.Plugin1 object at 0x7f22581c5040>
action: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::Plugin1
main(): plugin = <plugins.example_1.PluginA object at 0x7f2258149040>
action: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::PluginA
main(): plugin = <example_tmp.PluginTmp object at 0x7f2258149160>
action: /tmp/example_tmp.py::PluginTmp
```
