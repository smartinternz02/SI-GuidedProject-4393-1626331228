import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "cvtwoa",
        "typeId": "Device1",
        "deviceId":"mydev123"
    },
    "auth": {
        "token": "123456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    waterlevel=random.randint(0,100)
    lightintensity=random.randint(0,100)
    myData={'WaterLevel':waterlevel, 'LightIntensity':lightintensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
