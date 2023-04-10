#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import *
from fabric.operations import put, run
import time
import os

env.hosts = ['52.87.221.0', '18.209.152.146']

def do_pack():
    """creates .tgz archive from web_static folder"""
    timestr = time.strftime("%Y%m%d%H%M")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except:
        return None

def do_deploy(archive_path):
    """distributes archive to web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    full_filename = os.path.basename(archive_path)
    filename, ext = os.path.splitext(full_filename)
    dir_releases = "/data/web_static/releases"
    dir_current = "/data/web_static/current"
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/{}".format(dir_releases, filename))
        run("sudo tar -xzf /tmp/{} -C {}/{}".format(full_filename,
                                                    dir_releases,
                                                    filename))
        run("sudo rm /tmp/{}".format(full_filename))
        run("sudo mv {}/{}/web_static/* {}/{}".format(dir_releases, filename,
                                                      dir_releases, filename))
        run("sudo rm -rf {}/{}/web_static".format(dir_releases, filename))
        run("sudo rm -rf {}".format(dir_current))
        run("sudo ln -s {}/{}/ {}".format(dir_releases, filename, dir_current))
        return True
    except:
        return False

def deploy():
    """packs and deploys archive"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)

