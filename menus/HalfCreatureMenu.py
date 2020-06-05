bl_info = {
    "name": "Add Half Creatures Menu",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Menu to add new <Half Creature> Mesh",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy


class HalfCreatureMenu(bpy.types.Menu):
    bl_label = "Half Creature Menu"
    bl_idname = "OBJECT_MT_half_creature_menu"

    def draw(self, context):
        layout = self.layout
        
        
        layout.operator("mesh.add_half_human")
        layout.operator("mesh.add_half_tiger")
        layout.operator("mesh.add_half_wolf")
        layout.operator("mesh.add_half_box_turtle")
        layout.operator("mesh.add_half_iguana")
        layout.operator("mesh.add_half_elephant")
        layout.operator("mesh.add_half_rabbit")
        
        

def draw_item(self, context):
    layout = self.layout
    layout.menu(HalfCreatureMenu.bl_idname)


def register():
    bpy.utils.register_class(HalfCreatureMenu)
    #bpy.types.VIEW3D_MT_mesh_add.append(draw_item)


def unregister():
    bpy.utils.unregister_class(HalfCreatureMenu)
    #bpy.types.VIEW3D_MT_mesh_add.remove(draw_item)
    

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=HalfCreatureMenu.bl_idname)
