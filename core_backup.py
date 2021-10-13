import os
import shutil
import json
import traceback
from datetime import datetime
import logging

source_folder = r"C:\MC_Cluster\Cluster"
destination_folder = r"C:\MC_Cluster\Cluster_Backup"

text = "SYSTEM: backed up files @"
data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
log_file = r"C:\MC_Cluster\Logs.json"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)


logging.basicConfig(filename=log_file,
                            filemode='a',
                            format='%(message)s%(asctime)s',
                            datefmt='%d/%m/%Y %H:%M:%S',
                            level=logging.DEBUG)

logging.info(text)
logger = logging.getLogger('urbanGUI')


