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
from bpy.types import Operator

# Addon imports
from ..functions import *


class SKELETON_OT_operator_skeleton(Operator):
    """ Operator skeleton """
    bl_idname = "skeleton.operator_skeleton"
    bl_label = "Operator Skeleton"
    bl_options = {"REGISTER", "UNDO"}

    ################################################
    # Blender Operator methods

    @classmethod
    def poll(self, context):
        """ ensures operator can execute (if not, returns false) """
        return True

    def modal(self, context, event):
        if event.type in {"ESC"}:
            return{"CANCELLED"}
        return{"PASS_THROUGH"}

    def execute(self, context):
        try:
            # create timer for modal
            wm = context.window_manager
            self._timer = wm.event_timer_add(0.1, context.window)
            wm.modal_handler_add(self)
            return{"RUNNING_MODAL"}
        except:
            addon_skeleton_handle_exception()
            return{"CANCELLED"}

    def cancel(self, context):
        pass

    ################################################
    # initialization method

    def __init__(self):
        pass

    ###################################################
    # class variables

    # NONE!

    #############################################
    # class methods

    # NONE!

    #############################################
