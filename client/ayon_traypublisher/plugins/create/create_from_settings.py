import os
from ayon_core.lib import Logger
from ayon_core.settings import get_project_settings

log = Logger.get_logger(__name__)


def initialize():
    from ayon_traypublisher.api.plugin import SettingsCreator

    project_name = os.environ["AYON_PROJECT_NAME"]
    project_settings = get_project_settings(project_name)

    simple_creators = project_settings["traypublisher"]["create"]["simple_creators"]

    global_variables = globals()
    for item in simple_creators:
        dynamic_plugin = SettingsCreator.from_settings(item)
        global_variables[dynamic_plugin.__name__] = dynamic_plugin


initialize()
