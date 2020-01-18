#!/bin/bash

mv /home/cjling/data/log/job.html /home/cjling/data/log/bak/html/job.`date -d yesterday '+%Y_%m'`.html && \
mv /home/cjling/data/log/job.log /home/cjling/data/log/bak/log/job.`date -d yesterday '+%Y_%m'`.log
