# Author: Wei Zhenhuan, Xidian University
# Email: zhenhuan2002@163.com
# All rights reserved
# License: No License. Feel free to modify or publish it!

import time

import Settings
import Runner

def main():
    hour = int(time.strftime("%H", time.localtime()))
    hour = (hour + 8) % 24

    if hour <= 12:
        Runner.exec("晨检")
    else:
        Runner.exec("午检")

if __name__ == '__main__':
    if Settings.run:
        main()
