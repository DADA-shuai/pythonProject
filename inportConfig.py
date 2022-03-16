import configparser as cp

config = cp.ConfigParser()

config.read("config_xlsx.ini")

mainSysRouter = config.get("default", "mainSysRouter")
otherSysRouter = config.get("default", "otherSysRouter")
colMap = config.get("default", "colMap")
mainCol = config.get("default", "mainCol")
outSysRouter = config.get("default", "outSysRouter")
Handler = config.get("default", "Handler")

