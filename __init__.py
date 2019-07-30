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

bl_info = {
    "name"        : "Addon Skeleton",
    "author"      : "Christopher Gearhart <chris@bblanimation.com>",
    "version"     : (1, 0, 0),
    "blender"     : (2, 80, 0),
    "description" : "",
    "location"    : "View3D > UI > Addon Skeleton",
    "warning"     : "",  # used for warning icon and text in addons panel
    "wiki_url"    : "",
    "tracker_url" : "",
    "category"    : "Development"}

# System imports
# NONE!

# Blender imports
import bpy
from bpy.types import Scene, Object
from bpy.props import *

# Addon imports
from .operators import *
from .ui import *
from .lib import keymaps, preferences, classes_to_register
from .functions.common import *
from . import addon_updater_ops

# store keymaps here to access after registration
addon_keymaps = []


def register():
    # register classes
    for cls in classes_to_register.classes:
        make_annotations(cls)
        bpy.utils.register_class(cls)

    # # add custom props
    # Scene.skeleton_prop = BoolProperty(
    #     default=False)

    # # register app handlers
    # bpy.app.handlers.load_post.append(handle_something)

    # # register timers
    # if b280():
    #     if not bpy.app.timers.is_registered(sample_timer):
    #         bpy.app.timers.register(sample_timer)

    # handle the keymaps
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon: # check this to avoid errors in background case
        km = wm.keyconfigs.addon.keymaps.new(name="Object Mode", space_type="EMPTY")
        keymaps.add_keymaps(km)
        addon_keymaps.append(km)

    # addon updater code and configurations
    addon_updater_ops.register(bl_info)

def unregister():
    # addon updater unregister
    addon_updater_ops.unregister()

    # handle the keymaps
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

    # # unregister app handlers
    # bpy.app.handlers.load_post.remove(handle_something)

    # # unregister timers
    # if b280():
    #     if bpy.app.timers.is_registered(sample_timer):
    #         bpy.app.timers.unregister(sample_timer)

    # delete custom props
    # del Scene.skeleton_prop

    # unregister classes
    for cls in reversed(classes_to_register.classes):
        bpy.utils.unregister_class(cls)
