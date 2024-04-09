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
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
