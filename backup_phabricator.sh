#!/bin/bash

date=$(date +"%Y-%m-%d")
backup_dir='/home/cjling/package/phabricator/backup'
backed_num=$(find $backup_dir -type f|wc -l)
backed_plan=4
back_bin='/home/cjling/package/phabricator/phabricator/bin/storage'

if [ $backed_num -ge $backed_plan ]
then
    find $backup_dir -name "*.gz" | xargs ls -rt | head -n1 | xargs -i rm {}
fi

$back_bin dump | gzip > $backup_dir/$date.mysql.gz

