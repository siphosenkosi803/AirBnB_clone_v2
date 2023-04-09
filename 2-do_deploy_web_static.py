#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import env, put, run
import os

env.hosts = ['52.87.221.0', '18.209.152.146']

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        remote_path = "/tmp/{}".format(file_name)
        data_path = "/data/web_static/releases/{}".format(file_name_no_ext)

        put(archive_path, remote_path)
        run("mkdir -p {}".format(data_path))
        run("tar -xzf {} -C {}".format(remote_path, data_path))
        run("rm {}".format(remote_path))
        run("mv {}/web_static/* {}".format(data_path, data_path))
        run("rm -rf {}/web_static".format(data_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(data_path))

        return True
    except:
        return False

