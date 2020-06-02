bl_info = {
    "name": "Add Creatures Menu",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Menu to add new <Creature> Mesh",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy


class CreatureMenu(bpy.types.Menu):
    bl_label = "Creature Menu"
    bl_idname = "object.Creatures"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("mesh.add_human")
        layout.operator("mesh.add_tiger")
        layout.operator("mesh.add_wolf")
        layout.operator("mesh.add_box_turtle")
        layout.operator("mesh.add_iguana")
        
        

def draw_item(self, context):
    layout = self.layout
    layout.menu(CreatureMenu.bl_idname)


addon_keymaps = []
def register():
    bpy.utils.register_class(CreatureMenu)



def unregister():
    bpy.utils.unregister_class(CreatureMenu)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=CreatureMenu.bl_idname)
