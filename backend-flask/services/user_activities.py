import os
from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class UserActivities:

  def __init__(self, request):
    #self.xray_recorder = xray_recorder
    self.request = request

  def run(self, user_handle):               
    
    # X-Ray Capture Timestamp and User Handle
    now = datetime.now(timezone.utc).astimezone()
    
    with xray_recorder.in_subsegment('user_activities'):
      xray_recorder.current_subsegment().put_metadata('username', user_handle,'userdata')
      xray_recorder.current_subsegment().put_metadata('timestamp', now.isoformat(),'userdata')
      xray_recorder.current_subsegment().put_metadata('method',self.request.method, 'http')
      xray_recorder.current_subsegment().put_metadata('url', self.request.url, 'http')

    model = {
      'errors': None,
      'data': None
    }

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results     
    
    return model