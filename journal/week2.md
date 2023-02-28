# Week 2 — Distributed Tracing

## Required Homework

### Video Review
* Watched [FREE AWS Cloud Project Bootcamp - Update 2023-02-23 Video](https://youtu.be/gQxzMvk6BzM).
* Watched [Week 2 – Live Streamed Video – Honeycomb.io Setup](https://www.youtube.com/live/2GD9xCzRId4?feature=share)
* Watched [Week 2 – Instrument X-Ray Video](https://youtu.be/n2DTsuBrD_A)


### Actions

* Completed all steps during the livestream to set up Honeycomb distributed tracing.
* Completed all steps to implement AWS X-Ray
  * Note:  The X-Ray Trace Groups are under **X-Ray > New Console > CloudWatch > Settings > Traces > View Settings > Groups**.
  * [Github - AWS X-Ray SDK Python](https://github.com/aws/aws-xray-sdk-python)

## Spending Considerations

## Security Considerations

## Stretch Homework

### Got AWS X-Ray logging metadata properly via a subsegment in user_activities.py

* From troubleshooting after watching the video, I tried defining a segment and subsegment, and kept running into errors.
* Reviewed [this documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-subsegments.html) with examples repeatedly, but I couldn't get a segment definition to work.
* After working on this a while, I managed to get the data I wanted to submit to X-Ray without exception using a defined subsegment only.
* This uses the following definition to capture the user_handle and timestamp:

```
now = datetime.now(timezone.utc).astimezone()
    
with xray_recorder.in_subsegment('UserData'):
  xray_recorder.current_subsegment().put_metadata('username', user_handle)
  xray_recorder.current_subsegment().put_metadata('timestamp', now.isoformat())
```

* By defining it this way, you don't have to use begin_subsegment(), current_subsegment(), end_subsegment() functions.
* Was able to get this to output to X-Ray as metadata.  For example, going to the ```/api/activities/@andrewbrown``` endpoint would push the following to X-Ray:

![image](../_docs/assets/week2/X-Ray-UserData.png)
