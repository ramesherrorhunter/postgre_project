import logging
import os
import time
import cursor
import subprocess
def post_backup():
    try:
        print("Trying To Connecting With PSQL Database ===>")
        # Database details
        DB_HOST = 'localhost'
        DB_USER = 'postgres'
        DB_PASS = 'rahul123'
        DB_NAME = 'db_student'

        print("Connected With PSQL Database ===>")

        #Define path and time for backup
        BACKUP_PATH = 'C:\\Users\\rahul\\Desktop\\postpre_db\\'
        TIMESTAMP = time.strftime('%Y-%m-%d-%H-%M-%S')
        BACKUP_FILE = DB_NAME + '_' + TIMESTAMP + '.sql'

        print("Creating PSQL Database Backup ===>")
        # Command to take a backup
        command = "pg_dump -h {} -U {} -d {} > {}".format(DB_HOST, DB_USER, DB_NAME, os.path.join(BACKUP_PATH, BACKUP_FILE))
        subprocess.run(command, shell=True)
        print(command)
        # Execute the backup command
        print("Created PSQL Database ===>")
    
    except Exception as e:
        logging.error(e)
        print("Check for Rrror:",e)
        return False
    return True
post_backup()