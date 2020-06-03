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

moduleName = ["add_human", "add_tiger", "add_wolf", "add_box_turtle", "add_iguana", "add_elephant", "add_half_human", "add_half_tiger", "add_half_wolf", "add_half_box_turtle", "add_half_iguana", "add_half_elephant","CreatureMenu", "FullCreatureMenu", "HalfCreatureMenu"]

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