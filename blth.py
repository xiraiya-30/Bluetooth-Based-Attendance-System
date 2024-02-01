import bluetooth
import time

def scan():
    end_time=time.time()+10
    y=[]
    print('------Scanning for devices...------')
    while time.time()<end_time:
        x=bluetooth.discover_devices(duration=10,flush_cache=True,lookup_class=False,lookup_names=False)
        for i in x:
            if i not in y:
                y.append(i)
        x=None

    return y

