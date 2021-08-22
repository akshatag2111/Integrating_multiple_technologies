#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi,os
import subprocess as sp

db = cgi.FieldStorage()

choice = db.getvalue("choice")
disk1= db.getvalue("disk1")

vg = db.getvalue("vg")
disk1 = db.getvalue("disk1")
disk2 = db.getvalue("disk2")

lv = db.getvalue("lv")
lvsize = db.getvalue("lvsize")

fold = db.getvalue("fold")

exsize = db.getvalue("exsize")

output = ""
if choice =="1" :
     output = sp.getoutput("sudo fdisk -l")
     output = output

elif choice == "2":
    output = sp.getoutput("sudo pvcreate {}" .format(disk1))
    output = sp.getoutput("sudo pvdisplay {}" .format(disk1))
    output = output + "\n\n<b> Physical Volume Created Successfully</b>"

elif choice == "3":
    output = sp.getoutput("sudo vgcreate {} {} {}" .format(vg,disk1,disk2))
    output = sp.getoutput("sudo vgdisplay {}" .format(vg))
    output = output + "\n\n<b> Volume Group Created Successfully </b>"

elif choice == "4":
    output = sp.getoutput("sudo lvcreate --size {} --name {} {}" .format(lvsize,lv,vg))
    output = sp.getoutput("sudo lvdisplay {}/{}" .format(vg,lv))
    output = output + "\n\n<b> Logical Volume Created Successfully </b>"

elif choice == "5":
    output = sp.getoutput("sudo mkfs.ext4 /dev/{}/{}" .format(vg,lv))
    output = output + "\n\n<b> Logical Volume Formatted Successfully </b>"

elif choice == "6":
    output = sp.getoutput("sudo mkdir {}" .format(fold))
    output = sp.getoutput("sudo mount /dev/{}/{} {}" .format(vg,lv,fold))
    output = sp.getoutput("sudo df -h")
    output = output + "\n\n<b> Logical Volume Mounted Successfully </b>"

elif choice == "7":
    output = sp.getoutput("sudo lvextend --size +{} /dev/{}/{}" .format(exsize,vg,lv))
    output = sp.getoutput("sudo lvdisplay {}/{}" .format(vg,lv))
    output = output + "\n\n<b> Logical Volume Extended Successfully </b>"

elif choice == "8":
    output = sp.getoutput("sudo resize2fs /dev/{}/{}" .format(vg,lv))
    output = output + "\n\n<b> Newly Extended Partition Formatted Successfully </b>"

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