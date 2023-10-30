import os
import json
import logging


with open(os.path.join(os.getcwd(), "data", "statistics_parameters.json"), "r") as st_f:
    stat_prmtrs = json.load(st_f)


logging.basicConfig(
    # filename=os.path.join(PROJECT_ROOT_DIR, "data", "expert_bot_update.logs"),
    # filemode='a',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', )

logger = logging.getLogger()
logger.setLevel(logging.INFO)