import boto.ec2
import time
Import subprocess
conn = boto.ec2.connect_to_region("us-west-2")
t=conn.run_instances(image_id='ami-05cf2265', key_name='newkey',instance_type='t2.micro',placement=’us-west-2a’,subnet_id=’subnet-6c788b25’,security_group_ids=[‘sg-48482d30’]]
)
vol = conn.create_volume(1, "us-west-2a")
print 'Volume Id: ', vol.id
#time.sleep(10)
for i in t.instances:
     while i.state != 'running':
        time.sleep(20)
        i.update()
for i in t.instances 
     conn.attach_volume (vol.id, i.id,"/dev/sdf")
subprocess.call(“./lvol.sh”)

