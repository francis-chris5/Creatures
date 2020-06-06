bl_info = {
    "name": "Add Reptile Menu",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Menu to add new <Reptile> Mesh",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy


class ReptileMenu(bpy.types.Menu):
    bl_label = "Reptiles"
    bl_idname = "OBJECT_MT_reptile_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.add_iguana")

        
        

def draw_item(self, context):
    layout = self.layout
    layout.menu(ReptileMenu.bl_idname)



def register():
    bpy.utils.register_class(ReptileMenu)
    #bpy.types.VIEW3D_MT_mesh_add.append(draw_item)


def unregister():
    bpy.utils.unregister_class(ReptileMenu)
    #bpy.types.VIEW3D_MT_mesh_add.remove(draw_item)
    

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=ReptileMenu.bl_idname)
