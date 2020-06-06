bl_info = {
    "name": "Add Mammal Menu",
    "author": "Christopher S. Francis",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Menu to add new <Mammal> Mesh",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy


class MammalMenu(bpy.types.Menu):
    bl_label = "Mammal Menu"
    bl_idname = "OBJECT_MT_mammal_menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("mesh.add_human")
        layout.operator("mesh.add_tiger")
        layout.operator("mesh.add_wolf")
        layout.operator("mesh.add_elephant")
        layout.operator("mesh.add_rabbit")
        
        

def draw_item(self, context):
    layout = self.layout
    layout.menu(MammalMenu.bl_idname)



def register():
    bpy.utils.register_class(MammalMenu)
    #bpy.types.VIEW3D_MT_mesh_add.append(draw_item)


def unregister():
    bpy.utils.unregister_class(MammalMenu)
    #bpy.types.VIEW3D_MT_mesh_add.remove(draw_item)
    

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=MammalMenu.bl_idname)
