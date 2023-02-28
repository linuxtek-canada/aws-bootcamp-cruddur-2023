from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
import os

class UserActivities:

  def run(user_handle):               
    
    now = datetime.now(timezone.utc).astimezone()
    
    with xray_recorder.in_subsegment('UserData'):
      xray_recorder.current_subsegment().put_metadata('username', user_handle)
      xray_recorder.current_subsegment().put_metadata('timestamp', now.isoformat())
          
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