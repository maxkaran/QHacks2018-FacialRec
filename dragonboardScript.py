import httplib, urllib, base64, json, paramiko, subprocess, os
import computerScript

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '1cad6d9e281e4d09ae69ac6931b68780'
imageVersion = 6
imageVersion2 = 7
# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'eastus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

# The URL of a JPEG image to analyze.
body1 = {'url':'http://easyin.org/apiaccess/image'+str(imageVersion)+'.jpg'}
body = json.dumps(body1)
print body


# Execute the REST API call and get the response.
conn = httplib.HTTPSConnection('eastus.api.cognitive.microsoft.com')
conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()# 'data' contains the JSON data. The following formats the JSON data for display.
parsed = json.loads(data)
print parsed
faceID1 = parsed[0]['faceId']
print(faceID1)
conn.close()


# The URL of a JPEG image to analyze.
body1 = {'url':'http://easyin.org/apiaccess/image'+str(imageVersion2)+'.jpg'}
body = json.dumps(body1)

# Execute the REST API call and get the response.
conn = httplib.HTTPSConnection('eastus.api.cognitive.microsoft.com')
conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()# 'data' contains the JSON data. The following formats the JSON data for display.
parsed = json.loads(data)
print parsed
faceID2 = parsed[0]['faceId']
print(faceID2)
conn.close()

####################################

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'isIdentical': 'true',
    'returnFaceAttributes': 'confidence',
})

# The URL of a JPEG image to analyze.
body1 = {'faceId1':faceID1,'faceId2':faceID2}
body = json.dumps(body1)

# Execute the REST API call and get the response.
conn = httplib.HTTPSConnection('eastus.api.cognitive.microsoft.com')
conn.request("POST", "/face/v1.0/verify?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()# 'data' contains the JSON data. The following formats the JSON data for display.
parsed = json.loads(data )
print(parsed)
match = parsed['isIdentical']

if (match):
	print(match)
	#subprocess.call(["./easy_in_ssh.sh"])
	os.system(".\easy_in_ssh.sh")
	# ssh = paramiko.SSHClient()
	# ssh.load_system_host_keys()
	# ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
	# ssh.connect('10.217.125.153', username='linaro', password='linaro')
	# ssh_stdin,ssh_stdout, ssh_stderr = ssh.exec_command('sudo python ~/mraa/examples/python/custom/OpenDoor.py')
	# #ssh_stdin,ssh_stdout, ssh_stderr = ssh.exec_command('cd ~/mraa/examples/python/custom')
	# #ssh_stdin,ssh_stdout, ssh_stderr = ssh.exec_command('python OpenDoor.py')
	# ssh.close()
	# #sudo python ~/mraa/examples/python/custom/OpenDoor.py | ssh user@192.168.1.101 python -
