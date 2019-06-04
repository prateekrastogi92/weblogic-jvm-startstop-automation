import sys

import os

import re

from java.lang import System

import getopt

#========================

#Usage Section

#========================

def usage():



	print "Usage:"

	print "java weblogic.WLST depApps1.py -n deploymentName\n"

	sys.exit(2)

#========================

#Connect To Domain

#========================



def connectToDomain():



	try:

		connect(userConfigFile='userConfig.secure', userKeyFile='userKey.secure', url='t3://'+cname+':7001')

		print 'Successfully connected to the domain\n'



	except:

		print 'The domain is unreacheable. Please try again\n'

		exit()

#========================

#Checking Application Status Section

#========================



def appstatus(deploymentName, deploymentTarget):



	try:

		domainRuntime()

		cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')

		currentState = cmo.getCurrentState(deploymentName, deploymentTarget)

		return currentState

	except:

		print 'Error in getting current status of ' +deploymentName+ '\n'

		exit()

#========================

#Application undeployment Section

#========================



def undeployApplication():



	try:

		print 'stopping and undeploying ..' +deploymentName+ '\n'

		stopApplication(deploymentName, targets=deploymentTarget)

		undeploy(deploymentName, targets=deploymentTarget)

	except:

		print 'Error during the stop and undeployment of ' +deploymentName+ '\n'

#========================

#Applications deployment Section

#========================



def deployApplication():



	try:

		print 'Deploying the application ' +deploymentName+ '\n'

		deploy(deploymentName,deploymentFile,targets=deploymentTarget)

		startApplication(deploymentName)

	except:

		print 'Error during the deployment of ' +deploymentName+ '\n'

		exit()



#========================

#Input Values Validation Section

#========================



cfg = ConfigParser()

cfg.read('/opt/Oracle/wlst/domain.properties')

cname = cfg.get("config", "cname")

domain= cfg.get("config", "domain")





deploymentName=sys.argv[1]

print sys.argv[1]





if deploymentName == 'freedom':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/freedom.war'

	deploymentTarget = 'freedom_cluster'

elif deploymentName == 'freedom-ws':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/freedom-ws.war'

	deploymentTarget = 'freedom_cluster'

elif deploymentName == 'ABSCertificateWS':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/ABSCertificateWS.war'

	deploymentTarget = 'freedom_cluster'

elif deploymentName == 'workpackage-ws':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/workpackage-ws.war'

	deploymentTarget = 'freedom_cluster'

elif deploymentName == 'maximoui':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/maximoui.ear'

	deploymentTarget = 'maximo_cluster'

elif deploymentName == 'maximocron':

	deploymentFile = '/webadmin/Stage/'+ domain +'/maximo/stage/maximocron.ear'

	deploymentTarget = 'maxcron_cluster'



#========================

#Main Control Block For Operations

#========================



def deployUndeployMain():



		appList = re.findall(deploymentName, ls('/AppDeployments'))

		if len(appList) >= 1:

    			print 'Application'+deploymentName+' Found on server '+deploymentTarget+', undeploying application..'

			print '=============================================================================='

			print 'Application Already Exists, Undeploying...'

			print '=============================================================================='

    			undeployApplication()

			print '=============================================================================='

    			print 'Redeploying Application '+deploymentName+' on '+deploymentTarget+' server...'

			print '=============================================================================='

			deployApplication()

	   	else:

			print '=============================================================================='

			print 'No application with same name...'

    			print 'Deploying Application '+deploymentName+' on '+deploymentTarget+' server...'

			print '=============================================================================='

			deployApplication()

#========================

#Execute Block

#========================

print '=============================================================================='

print 'Connecting to Admin Server...'

print '=============================================================================='

connectToDomain()

print '=============================================================================='

print 'Starting Deployment...'

print '=============================================================================='

deployUndeployMain()

print '=============================================================================='

print 'Execution completed...'

print '=============================================================================='

disconnect()

exit()
