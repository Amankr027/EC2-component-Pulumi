from ec2_instance.ec2 import Ec2WithSecurityGroup
import pulumi_aws as aws

ec2 = Ec2WithSecurityGroup("demo", ami_id="ami-084568db4383264d4", instance_type="t2.micro")
