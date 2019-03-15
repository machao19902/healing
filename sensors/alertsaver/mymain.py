import os

import yaml

VERSION = '1.0'


class RuleConfig(object):
    ACTION_CONFIG_KEY = 'alertsaver_action'
    COMMON_PUBLISHERS = 'common_publishers'

    def __init__(self, log, configName='alertsaver_action.yaml'):
        self.log = log
        self.configName = configName

    # TODO(),test the path of alertsaver_action.yaml
    def readConfig(self):
        if not os.path.exists(self.configName):
            curFile = os.path.realpath(__file__)
            curDir = os.path.dirname(curFile)
            info = '##### current file: {file}, current dir: {dir}'.format(
                file=curFile,
                dir=curDir
            )
            self.log.info(info)
            self.configName = os.path.join(curDir, 'etc', 'alertsaver_action.yaml')
            self.log.info('find file path: {realFile}'.format(realFile=self.configName))
        if not os.path.exists(self.configName):
            self.log.info("can not find file: {name}".format(
                name=self.configName
            ))
            return ""
        with open(self.configName) as fr:
            data = fr.read()
        try:
            dataConfig = yaml.safe_load(data)
        except Exception as ex:
            info = "read config : {name}, exception: {exp}, message: {mes}".format(
                self.configName, ex.__class__.__name__, ex
            )
            print info
            return info
        else:
            return dataConfig