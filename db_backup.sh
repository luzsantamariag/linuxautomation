#!/bin/bash
# Script to generate a backup of a database

#echo "Generating a backup of the automation database"
sqlfile="/home/user/Documentos/backup/bu_auto_`date '+%Y%m%d_%H%M%S'`.sql"
logfile="/home/user/Documentos/backup/log_`date '+%Y%m%d_%H%M%S'`.txt"

mysqldump automation > $sqlfile

more /var/log/cron* | grep db_backup > $logfile

chown user:user $sqlfile
chown user:user $logfile

/bin/python /home/user/Documentos/backup/Mail.py $logfile $sqlfile
