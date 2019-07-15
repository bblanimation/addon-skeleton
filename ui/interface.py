# Copyright (C) 2019 Christopher Gearhart
# chris@bblanimation.com
# http://bblanimation.com/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# System imports
# NONE!

# Blender imports
import bpy
from bpy.types import Panel

# Addon imports
from ..functions import *


class VIEW3D_PT_skeleton_interface_1(Panel):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI" if b280() else "TOOLS"
    bl_label       = "Skeleton Interface 1"
    bl_idname      = "VIEW3D_PT_skeleton_interface_1"
    bl_context     = "objectmode"
    bl_category    = "Addon Skeleton"

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        if bpy.data.texts.find("Addon Skeleton log") >= 0:
            split = layout.split(align=True, percentage=0.9)
            col = split.column(align=True)
            row = col.row(align=True)
            row.operator("scene.report_error", text="Report Error", icon="URL")
            col = split.column(align=True)
            row = col.row(align=True)
            row.operator("scene.close_report_error", text="", icon="PANEL_CLOSE")

        col = layout.column(align=True)
        col.label(text="Your interface here!")
        col.operator("skeleton.operator_skeleton")


class VIEW3D_PT_skeleton_interface_2(Panel):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI" if b280() else "TOOLS"
    bl_label       = "Skeleton Interface 2"
    bl_idname      = "VIEW3D_PT_skeleton_interface_2"
    bl_context     = "mesh_edit"
    bl_category    = "Addon Skeleton"

    def draw(self, context):
        layout = self.layout
        layout.operator("skeleton.cc_operator_skeleton")
