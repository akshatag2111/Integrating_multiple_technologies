#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess as sp
import cgi

field = cgi.FieldStorage()
task = field.getvalue("task")
field = sp.getoutput("sudo {}".format(task))
print(field)

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
