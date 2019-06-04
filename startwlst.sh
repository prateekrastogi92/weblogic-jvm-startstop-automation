#!/bin/sh
MW_HOME=/opt/Jenkins/SOA/Oracle_Home
export MW_HOME
. $MW_HOME/osb/tools/configjar/setenv.sh
#${MW_HOME}/osb/tools/configjar/wlst.sh
java weblogic.WLST -i wlststart.py
#depApps1.py maximoui1
