def load_plugin():
    mod = __import__("strings_parte2_module")
    return mod

def call_plugin(*args, **kwargs):
    plugin = load_plugin()
    plugin.plugin_main(*args, **kwargs)
    
# call_plugin(texto, limite_de_comprimento)
call_plugin('In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.', 40)
