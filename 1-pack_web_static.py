#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 8 22:25:54 2024
@author: Aman Hablu
"""
from fabric.api import local, put, run, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.158.180.95', '100.26.10.90']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    time_format = '%Y%m%d%H%M%S'
    archive_name = 'web_static_' + datetime.now().strftime(time_format) + '.tgz'
    archive_path = 'versions/' + archive_name

    local('mkdir -p versions')  # Create versions folder if it doesn't exist
    result = local('tar -czvf {} web_static'.format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
