#!/usr/bin/python3
"""
generates a .tgz archive
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        result = local("tar -czvf {} web_static".format(archive_path))
        if result.failed:
            print("Error: Failed to create archive")
            return None
        return archive_path
    except Exception as e:
        print("Error: {}".format(e))
        return None
