#!/bin/bash

content=${1}

echo ${content}| mail -s 'third' chao.ma@easystack.cn

datetime=$(date '+%Y-%m-%d %H:%M:%S')

echo "${datetime}" >> /tmp/count.txt
