# python_plugin_demo
Demonstration of a simple Python plugin system.

Derived from: https://gist.github.com/will-hart/5899567

## External plugin

from `/tmp/external_tmp.py`:

```py
"""
Example of user-supplied plugin (from outside the source tree).
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
(bluesky_2022_1) prjemian@zap:~/Documents/plugin_demo$ python ./demo.py 
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.interfacer.PluginBase'>
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_a.PluginA'>
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_a.PluginA'> - enrolling ...
PluginMounter.register <class 'plugins.example_a.PluginA'>.
register: /home/prjemian/Documents/plugin_demo/plugins/example_a.py::PluginA
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_1.Plugin1'>
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_1.Plugin1'> - enrolling ...
PluginMounter.register <class 'plugins.example_1.Plugin1'>.
register: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::Plugin1
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_1.PluginA'>
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'plugins.example_1.PluginA'> - enrolling ...
PluginMounter.register <class 'plugins.example_1.PluginA'>.
register: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::PluginA
main
list(PluginBase.plugins) = [<plugins.example_a.PluginA object at 0x7f392075e370>, <plugins.example_1.Plugin1 object at 0x7f3920634970>, <plugins.example_1.PluginA object at 0x7f3920634940>]
module_name='example_tmp' fp=<_io.TextIOWrapper name='/tmp/example_tmp.py' mode='r' encoding='utf-8'> path='/tmp/example_tmp.py', desc=('.py', 'r', 1)
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'example_tmp.PluginTmp'>
/home/prjemian/Documents/plugin_demo/plugins/interfacer.py::<class 'example_tmp.PluginTmp'> - enrolling ...
PluginMounter.register <class 'example_tmp.PluginTmp'>.
register: /tmp/example_tmp.py::PluginTmp
list(PluginBase.plugins) = [<plugins.example_a.PluginA object at 0x7f392075e370>, <plugins.example_1.Plugin1 object at 0x7f3920634970>, <plugins.example_1.PluginA object at 0x7f3920634940>, <example_tmp.PluginTmp object at 0x7f3920687310>]
plugin = <plugins.example_a.PluginA object at 0x7f392075e370>
action: /home/prjemian/Documents/plugin_demo/plugins/example_a.py::PluginA
plugin = <plugins.example_1.Plugin1 object at 0x7f3920634970>
action: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::Plugin1
plugin = <plugins.example_1.PluginA object at 0x7f3920634940>
action: /home/prjemian/Documents/plugin_demo/plugins/example_1.py::PluginA
plugin = <example_tmp.PluginTmp object at 0x7f3920687310>
action: /tmp/example_tmp.py::PluginTmp
```
