#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi,os
import subprocess as sp
db = cgi.FieldStorage()

choice = db.getvalue("choice")
key = db.getvalue("key")

sg = db.getvalue("sg")
Type=db.getvalue("Type")


name = db.getvalue("name")
az=  db.getvalue("az")

volume= db.getvalue("volume")
size = db.getvalue("size")

vid = db.getvalue("vid")
iid= db.getvalue("iid")

image = db.getvalue("image")

bucket = db.getvalue("bucket")
region = db.getvalue("region")

buck = db.getvalue("buck")
obj = db.getvalue("obj")

output=""
if choice =="1" :
     output = sp.getoutput("aws ec2 create-key-pair --key-name {}".format(key))
     output = output + "\n\n<b>key pair created successfully</b>"

elif choice == "2":
   output = sp.getoutput("sudo aws ec2 create-security-group --group-name {} --description {}" .format(sg,Type))
   output = output + "\n\n<b> SG created successfully</b>"

elif choice == "3":
    name = "--tag-specifications " + '"ResourceType = instance , Tags = [{Key=\"Name\",Value=\"' + name +'"}]"'
    az = "--placement " + '"AvailabilityZone='+ az + '"'
    output = sp.getoutput("sudo aws ec2 run-instances --image-id {0} --instance-type {1} --key-name {2} --security-group-ids {3}  {4} {5}".format(image,Type,key,sg,name,az))
    output = output + "\n\n<b>Instance Launched successfully</b>"

elif choice == "4":
    output = sp.getoutput('sudo aws ec2 create-volume --availability-zone "{}" --size {}'.format(volume,size))
    output = output + "\n\n<b> Ebs volume created successfully</b>"

elif choice == "5":
    output = sp.getoutput("sudo aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(iid,vid,volume))
    output = output + "\n\n<b> EBS volume successfully attached to instance </b>"

elif choice == "6":
   output = sp.getoutput("sudo aws  s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint={}" .format(bucket,region))
   output = output + "\n\n<b> bucket created successfully</b>"

elif choice == "7":
   output = sp.getoutput("sudo aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}" .format(buck,obj))
   output = output + "\n\n<b> cloud front is created successfully </b>"

elif choice == "8":
    output = sp.getoutput("sudo aws s3api put-object --bucket {} --key {} --grant-read uri=http://acs.amazonaws.com/groups/global/AllUsers" .format(buck,obj))
    output = output + "\n\n<b> object is uploaded successfully </b>"
else:
    output = "Something went Wrong..."
print("""<style>
   body{
       background-color:#AAB7B8;
      text-align:center;
       justify-content:center;
     }
      pre{
        font-size: 20px;
        color:1B2631;
      font-weight: bold;
      padding -top:0px
}
h1{
color : black;
padding-bottom:0px;
}
</style>""")
print("""
<body>
<pre>
<h1 style = "">OUTPUT</h1>
{}
</pre>
</body>
""".format(output))

