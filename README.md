# django-server-timing
Django middleware that exposed collected metrics into [HTTP Server Timing](https://www.w3.org/TR/server-timing/) header.

This headers is used by browser to display several metrics into the `Timing` tab of the `Network` interface.
Right now, this header is not supported properlly by all browser. It works pretty good on *Chrome 65+* and on *Firefox* there is a bug [report](https://bugzilla.mozilla.org/show_bug.cgi?id=1403051).

It doesn't effect unsupported browser.

This middleware will send the entire header value since not all browsers supports sending it via [HTTP Trailer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Trailer).

## Example
```python
import time                                                                        
                                                                                     
from django.http import HttpResponse                                               
                                                                                     
from server_timing.middleware import TimedService, timed, timed_wrapper            
                                                                                     
                                                                                     
@timed_wrapper('index', 'Index View')                                              
def index(request):                                                                
    home_service = TimedService('first', 'First service')                          
    home_service.start()                                                           
                                                                                     
    time.sleep(0.3)                                                                
                                                                                     
    home_service.end()                                                             
                                                                                     
    with timed('second', 'Second service'):                                        
        time.sleep(0.5)                                                            
                                                                                     
    return HttpResponse('This page shows a list of most recent posts.')
```

![Server Timing Example](https://raw.githubusercontent.com/vtemian/django-server-timing/master/example/server-timing-example.png)
