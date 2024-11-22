bl_info = {
    "name": "Accelertaion Animator",
    "author": "Bruno Albertoni",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Tool to convert linear acceleration and gyroscope data from Phyphox into position keyframes",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from bpy.types import Panel, Operator, AddonPreferences, PropertyGroup #panel will giev us the panel in the side menu and Operator allows us to add buttons to that panel
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, IntVectorProperty, PointerProperty
from bpy_extras.io_utils import ImportHelper

class MainProperties(PropertyGroup):
    
    # Example property
    example_float: bpy.props.FloatProperty(
        name="Example Float",
        description="This is a test",
        default=1.0,
    )
    
    # Example property
    example_float: bpy.props.BoolProperty(
        name="Data Exists",
        description="This is a test",
        default=1.0,
    )


class MainPanel(bpy.types.Panel):
    bl_label = "Data and Keyframes"
    bl_idname = "OBJECT_PT_accel_anim_main_tools"
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
        row.operator(ImportFile.bl_idname, text="Import Phyphox Data", icon="FILE_NEW") # button that should activate the ImportFile class
        
        
        row = layout.row()
        row.enabled = False
        row.label(text="No data yet...")
        
        # Grey out button based on a condition
        row = layout.row()
        if context.selected_objects == []:
            row.enabled = False  # Disable (grey out) everything inside the layout.row()
            row.operator(ShowInfo.bl_idname, text="Apply to Object", icon="OBJECT_DATA")
        else:
            row.enabled = True  # Enable it
            if len(context.selected_objects) == 1:
                row.operator(ShowInfo.bl_idname, text="Apply to Object", icon="OBJECT_DATA")
            else:
                row.operator(ShowInfo.bl_idname, text=f"Apply to {len(context.selected_objects)} Objects", icon="OBJECT_DATA")
        
        row = layout.row() # new row already resets if its enabled or not
        row.label(text="Test")

        
class ToolPanel(bpy.types.Panel):
    bl_label = "Extra Tools"
    bl_idname = "OBJECT_PT_accel_anim"
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
        row.label(text="Keyframes:", icon='KEYFRAME_HLT')
        
        row = layout.row()
        row.operator(ShowInfo.bl_idname, text="Clear Keyframes", icon="X")
        row = layout.row()
        row.operator(ShowInfo.bl_idname, text="Test Keyframes", icon="KEYFRAME")


def read_some_data(context, filepath, use_some_setting):
    print("running read_some_data...")
    f = open(filepath, 'r', encoding='utf-8')
    data = f.read()
    f.close()

    # would normally load the data here
    print(data)

    return {'FINISHED'}


class ImportFile(Operator, ImportHelper):
    """Import the data from Phyphox""" # this is actually the tooltip
    bl_idname = "import_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Data"

    # ImportHelper mix-in class uses this.
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ('OPT_A', "First Option", "Description one"),
            ('OPT_B', "Second Option", "Description two"),
        ),
        default='OPT_A',
    )

    def execute(self, context):
        return read_some_data(context, self.filepath, self.use_setting)


class ShowInfo(bpy.types.Operator):
    """Just for temp buttons, no actual use""" # description for me I think
    bl_idname = "object.import_file" #make sure to have the "." in the name here
    bl_label = "Friendly Message :)" # description for when the mouse is hovering for a while

    def execute(self, context):
        Properties = context.scene.AccelAnimProperties
        obj = bpy.context.object
        
        # Stuff here to exceute like a regular python file
        # using the Blender API of course
        # Placeholder for now
        self.report({'INFO'}, "Button works!") # this give the little blue info bubble at the bottom of the screen in blender
        # you can use "INFO", "WARNING", "ERROR", and maybe some others that I havent explored
        
        
        return {'FINISHED'} #this just lets blender know the program finished succsesfully


class ClearLightKeyframes(bpy.types.Operator):
    """Clear all Keyframes for working light elements"""
    bl_idname = "object.clear_keyframes" #make sure to have the "." in the name here
    bl_label = "lights working with ThatsLit! will clear keyframes"
    
    def execute(self, context):
        beforeFrameLength = bpy.context.scene.frame_end
        
        bpy.context.scene.frame_end += 5
           
        lightElementNames = ["AR1","AR2","AR3","AR4","AL1","AL2","AL3","AL4","BR1","BR2","BR3","BR4","BL1","BL2","BL3","BL4", "CR1","CR2","CR3","CR4","CL1","CL2","CL3","CL4","DR1","DR2","DR3","DR4","DL1","DL2","DL3","DL4","EL1","EL2","EL3","EL4","ER1","ER2","ER3","ER4","FL1","FL2","FL3","FL4","FR1","FR2","FR3","FR4","GL1","GL2","GL3","GL4","GR1","GR2","GR3","GR4","HL1","HL2","HL3","HL4","HR1","HR2","HR3", "HR4"]
        objectAssignments = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        obj = bpy.data.objects

        for object in obj.items(): #for every object
            if obj[object[0]].get('ThatslitID') is not None: #if the property isnt nothing
                try: #try to find it in the name list and add it in the correct position
                    objectAssignments[lightElementNames.index(obj[object[0]].get('ThatslitID'))] = str(obj[object[0]].name)
                    lightAssignmentsFound += 1
                except: #if we couldnt find it in the list just move on
                    continue

        for i in range(bpy.context.scene.frame_end): #for all the frames...
            for objectName in objectAssignments: #for all the object names...
                if objectName == "": #if theres no name...
                    continue #move on
                else: #if there is a name...
                    try: #remove the keyframe
                        obj[objectName].material_slots[0].material.node_tree.nodes['LitMixer'].inputs[0].keyframe_delete("default_value", frame=i)
                        #not moving on the another frame so all the materials turn on at the same time at the end
                    except: #no material found just move on
                        continue

        for objectName in objectAssignments: #for all the object names...
                if objectName == "": #if theres no name...
                    continue #move on
                else: #if there is a name...
                    try: #remove the keyframe
                        obj[objectName].material_slots[0].material.node_tree.nodes['LitMixer'].inputs[0].default_value = 0
                        #not moving on the another frame so all the materials turn on at the same time at the end
                    except: #no material found just move on
                        continue
        
        bpy.context.scene.frame_end = beforeFrameLength
                    
        return {'FINISHED'} #this just lets blender know the program finished succsesfully


classes = [ #just put all the classes we will be registering here
    MainPanel, #in the register and unregister parts of the code
    MainProperties,
    ImportFile,
    ShowInfo,
    ToolPanel
]


class_register, class_unregister = bpy.utils.register_classes_factory(classes)


def register():
    class_register()
    bpy.types.Scene.AccelAnimProperties = PointerProperty(type=MainProperties)


def unregister():
    class_unregister()


if __name__ == "__main__":
    register()