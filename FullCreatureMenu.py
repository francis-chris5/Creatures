bl_info = {
    "name": "Add Full Creatures Menu",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Menu to add new <Full Creature> Mesh",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy


class FullCreatureMenu(bpy.types.Menu):
    bl_label = "Full Creature Menu"
    bl_idname = "OBJECT_MT_full_creature_menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("mesh.add_human")
        layout.operator("mesh.add_tiger")
        layout.operator("mesh.add_wolf")
        layout.operator("mesh.add_box_turtle")
        layout.operator("mesh.add_iguana")
        
        

def draw_item(self, context):
    layout = self.layout
    layout.menu(FullCreatureMenu.bl_idname)



def register():
    bpy.utils.register_class(FullCreatureMenu)
    #bpy.types.VIEW3D_MT_mesh_add.append(draw_item)


def unregister():
    bpy.utils.unregister_class(FullCreatureMenu)
    #bpy.types.VIEW3D_MT_mesh_add.remove(draw_item)
    

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=FullCreatureMenu.bl_idname)
