#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
db = cgi.FieldStorage()
choice = db.getvalue("choice")
dname = db.getvalue("dname")
pname = db.getvalue("pname")
image = db.getvalue("image")
rno = db.getvalue("rno")
output=""

if choice == "1":
   output = sp.getoutput("sudo kubectl create deployment {} --image={} --kubeconfig admin.conf" .format(dname,image))

elif choice == "2":
   output = sp.getoutput("sudo kubectl get pod --kubeconfig admin.conf")

elif choice == "3":
   output = sp.getoutput("sudo kubectl expose deployment {} --type=NodePort --port={} --kubeconfig admin.conf" .format(dname,port))

elif choice == "4":
   output = sp.getoutput("sudo kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format(dname,rno))

elif choice == "5":
   output = sp.getoutput("sudo kubectl delete deployment {} --kubeconfig admin.conf".format(dname))

elif choice == "6":
   output = sp.getoutput("sudo kubectl delete all --all --kubeconfig admin.conf")

elif choice == "7":
   output = sp.getoutput("sudo kubectl describe pod {} --kubeconfig admin.conf".format(pname))

elif choice == "8":
   output = sp.getoutput("sudo kubectl run {} --image={} --kubeconfig admin.conf".format(pname,image))

elif choice == "9":
   output = sp.getoutput("sudo kubectl delete pod {} --kubeconfig admin.conf".format(pname))

elif choice == "10":
   output = sp.getoutput("sudo kubectl get deployments --kubeconfig admin.conf")

elif choice == "11":
   output = sp.getoutput("sudo kubectl get svc --kubeconfig admin.conf")


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
