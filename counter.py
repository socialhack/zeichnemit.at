import json 

class Counter:
        def __init__(self,number,config=
        {"want":2500,"width":250,"file":"counter.html"}):
                self.number=number
                self.config=config
                self.string="""<html><head>
<link rel="stylesheet" href="style-counter.css" type="text/css" />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
<body>
<div class="counter">
<h1>"Stoppt die Vorratsdatenspeicherung"</h1>
<!--
<div class="wantbar" style="width: %dpx">
</div>
<div class="havebar" style="width: %dpx">
</div>-->
<div class="number">
%d<!--/%d--> Unterschriften 
</div>
<a href="http://zeichnemit.at" target="_new">Jetzt mitzeichnen!</a>
</div>
</body>
</html>"""
        
        def write(self):
                f=open(self.config["file"],"w")
                f.write("%s"%self)
                f.close()

        def __str__(self):
              hw=self.number/self.config["want"]*self.config["width"]
              if hw> self.config["width"]:
                hw=self.config["width"]
              return self.string%(self.config["width"],
              hw, 
              self.number, self.config["want"])

class CounterInternal(Counter):
        def __init__(self,number,config={"want":2500,"width":250,
        "file":"counter-internal.html"}):
                Counter.__init__(self,number,config)
                self.string="""<html><head>
<link rel="stylesheet" href="style-counter.css" type="text/css" />
</head>
<body>
<div class="counter">
Seit 17.10.2011: 
<!--<div class="wantbar" style="width: %dpx">
</div>
<div class="havebar" style="width: %dpx">
</div> -->
<div class="number">%d<!--/%d--> Unterschriften</div>
</div>
</body>
</html>"""
        

if __name__=="__main__":
        import sys
        number=int(sys.argv[1])
        counter=Counter(number)
        counter.write()
        ci=CounterInternal(number)
        ci.write()
        a={"need": 10000, "have": number}
        f=open("counter.json","w")
        json.dump(a,f)
        f.close()
