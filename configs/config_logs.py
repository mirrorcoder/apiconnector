from configs.config import PROD

if PROD:
    LOG_CONFIG_CALLBACKS_SERVER_PATH = ""
else:
    LOG_CONFIG_CALLBACKS_SERVER_PATH = "/home/PycharmProjects/apiconnector/configs/logs/webserver/test_config.yaml"
