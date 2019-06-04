#!/bin/sh
MW_HOME=/opt/Jenkins/SOA/Oracle_Home
export MW_HOME
. $MW_HOME/osb/tools/configjar/setenv.sh
#${MW_HOME}/osb/tools/configjar/wlst.sh
java weblogic.WLST -i wlststop.py
#depApps1.py maximoui1
#${MW_HOME}/osb/tools/configjar/wlst.sh /opt/Jenkins/SOA/Middleware/wlserver/common/wlst/bin/import.py ./sbconfig/import_int.properties
