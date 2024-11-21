'''
THIS ADDON IS NOT COMPLETE. THERE IS NO FUNCTIONALITY TO THE CODE BELOW
'''


bl_info = {
    "name": "Accelertaion Animator",
    "author": "Bruno Albertoni",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Tool to convert acceleration and rotation data into position keyframes",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy
from bpy.types import Panel, Operator, AddonPreferences, \
    PropertyGroup  # panel will giev us the panel in the side menu and Operator allows us to add buttons to that panel
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, \
    IntVectorProperty, PointerProperty


class MainProperties(PropertyGroup):
    # Example property
    example_float: bpy.props.FloatProperty(
        name="Example Float",
        description="An example property",
        default=1.0,
    )


class MainPanel(bpy.types.Panel):
    bl_label = "Lights Setup"
    bl_idname = "OBJECT_PT_thatslit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Accel Anim"

    def draw(self, context):
        obj = context.object
        layout = self.layout
        scene = context.scene
        mytool = scene.AccelAnimProperties

        # Create a Simple Row

        row = layout.row()
        row.label(text="Test:", icon='OUTLINER_OB_LIGHT')

        row = layout.row()
        row.operator(ImportFile.bl_idname, text="Import File",
                     icon="FILE_NEW")  # button that should activate the ImportFile class

        row = layout.row()  # i put two in order to seperate it a little more
        row.label(text="Another Section:", icon="MATERIAL")
        row = layout.row()


class ImportFile(bpy.types.Operator):
    """Import the accelaration data into the addon"""  # description for me I think
    bl_idname = "object.import_file"  # make sure to have the "." in the name here
    bl_label = "Import the accelaration data into the addon"  # description for when the mouse is hovering for a while

    def execute(self, context):
        Properties = context.scene.AccelAnimProperties
        obj = bpy.context.object

        # Stuff here to exceute like a regular python file
        # using the Blender API of course
        # Placeholder for now
        self.report({'INFO'},
                    "Button works!")  # this give the little blue info bubble at the bottom of the screen in blender
        # you can use "INFO", "WARNING", "ERROR", and maybe some others that I havent explored

        return {'FINISHED'}  # this just lets blender know the program finished succsesfully


classes = [  # just put all the classes we will be registering here
    MainPanel,  # in the register and unregister parts of the code
    MainProperties,
    ImportFile
]

class_register, class_unregister = bpy.utils.register_classes_factory(classes)


def register():
    class_register()
    bpy.types.Scene.AccelAnimProperties = PointerProperty(type=MainProperties)


def unregister():
    class_unregister()


if __name__ == "__main__":
    register()