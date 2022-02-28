"""
Demonstration of a simple plugin system.
"""


from plugins import PluginBase
from plugins import install_user_plugin

def main():
    print("main")
    print(f"{len(PluginBase.plugins) = }")
    install_user_plugin("/tmp/example_tmp.py")
    print(f"{len(PluginBase.plugins) = }")

    for plugin in PluginBase.plugins:
        print(f"main(): {plugin = }")
        plugin.action()


if __name__ == "__main__":
    main()
