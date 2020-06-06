bl_info = {
    "name": "Creatures",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a series of accurately scaled and proportioned starter meshes for modeling animals",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

moduleName = ["mammals.add_human", "mammals.add_tiger", "mammals.add_wolf", "amphibians.add_box_turtle", "reptiles.add_iguana", "mammals.add_elephant",  "mammals.add_rabbit", "menus.CreatureMenu", "menus.MammalMenu", "menus.AmphibianMenu", "menus.ReptileMenu"]

import sys
import importlib

modulesFullNames = {}
for currentModuleName in moduleName:
	modulesFullNames[currentModuleName] = ("{}.{}".format(__name__, currentModuleName))
	
for currentModuleFullName in modulesFullNames.values():
	if currentModuleFullName in sys.modules:
		importlib.reload(sys.modules[currentModuleFullName])
	else:
		globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
		setattr(globals()[currentModuleFullName], "modulesNames", modulesFullNames)
		
def register():
	for currentModuleName in modulesFullNames.values():
		if currentModuleName in sys.modules:
			if hasattr(sys.modules[currentModuleName], "register"):
				sys.modules[currentModuleName].register()
				
def unregister():
	for currentModuleName in modulesFullNames.values():
		if currentModuleName in sys.modules:
			if hasattr(sys.modules[currentModuleName], "unregister"):
				sys.modules[currentModuleName].unregister()
				
if __name__ == "__main__":
	register();