# coding=utf-8
import logging

from flask import Flask

app = Flask(__name__)
a1 =app.logger

@app.route('/')
def root():

    a1.debug('app.logger.debug')
    a1.info('app.logger.info')
    a1.warning('app.logger.warning')
    a1.error('app.logger.error')
    a1.critical('app.logger.critical')
    print a1.level
    return 'ok'
fileHandler = logging.FileHandler('log.log',encoding='UTF-8')

#控制总级别
a1.setLevel(logging.INFO)
#控制每个handler级别（总级别一定要比每个级别低）
fileHandler.setLevel(logging.ERROR)

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
fileHandler.setFormatter(log_formatter)
a1.addHandler(fileHandler)
print a1.level
if __name__ == '__main__':
    app.debug=True
    app.run()
