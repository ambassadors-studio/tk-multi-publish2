# Copyright (c) 2017 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk

from .api import PublishManager
from . import base_hooks
from . import util

def show_dialog(app):
    """
    Show the main dialog ui

    :param app: The parent App
    """
    # defer imports so that the app works gracefully in batch modes
    from .dialog import AppDialog

    display_name = sgtk.platform.current_bundle().get_setting("display_name")

    # start ui
    dialog = app.engine.show_dialog(display_name, app, AppDialog)
    # First we display the UI, and we run the _full_rebuild afterwards.
    dialog._full_rebuild()
