import os
import sys
import re
import getopt


def connectToWLST():

        try:
                connect(userConfigFile='/opt/Jenkins/wltserver/config.secure',userKeyFile='/opt/Jenkins/wltserver/key.secure',url='t3://freappd15.oracle.eagle.org:7001')
                print 'Successfully connected to the WLST\n'

        except:
                print 'The domain is unreacheable. Please try again\n'
                exit()

def stopJVM():

        try:
                shutdown("Maximo01")

        except:
                print 'Error stopping\n'
                sys.exit(2)

connectToWLST()
stopJVM()
