# Author: Christopher Gearhart

# System imports
# NONE!

# Blender imports
import bpy
from bpy.props import *
from bpy.types import PropertyGroup

# Module imports
from ...functions.property_callbacks import *


class PropertyGroup(PropertyGroup):
    name = StringProperty(default="")
