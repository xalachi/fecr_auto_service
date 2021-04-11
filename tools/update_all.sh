#!/bin/bash

repos=(
    'fecr'
    'fecr_pos'
    'fecr_auto_service'
)
REPOS_PATH='/root/dockers/local/addons'
for repo in ${repos[@]}; do
    git -C $REPOS_PATH/$repo checkout .
    git -C $REPOS_PATH/$repo pull
done;

docker restart local

docker exec local python3 /mnt/extra-addons/fecr_auto_service/tools/db.py
