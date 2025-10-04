from multimethod import multimethod
class Parqueo:
    def __init__(self,nv,tariho,vehiculo,tiempo):
        self.nv=nv
        self.tariho=tariho
        self.vehiculo=[[""]*2 for i in range(50)]
        self.tiempo=[[0]*2 for j in range(50)]
        for k in range(nv):
            for l in range(2):
                self.vehiculo[k][l]=vehiculo[k][l]
                self.tiempo[k][l]=tiempo[k][l]
    def __add__(self,D):
        P,Z,X,Y=D
        for i in range(50):
            if self.vehiculo[i][0]=="" and self.vehiculo[i][1]=="" and self.tiempo[i][0]==0 and self.tiempo[i][0]==0:
                self.vehiculo[i][0]=P
                self.vehiculo[i][1]=Z
                self.tiempo[i][0]=X
                self.tiempo[i][1]=Y
                self.nv+=1
                break
        else:
            print("hubo un problema ")
        return self
    @multimethod
    def Hallar(self,P:str):
        for i in range (self.nv):
            if self.vehiculo[i][0]==P:
                return self.vehiculo[i][1]
        else:
            return "No  se encontro esa placa"
    @multimethod
    def Hallar(self,P:int):
        c=0
        for i in range(self.nv):
            if self.tiempo[i][1]-self.tiempo[i][0]==P:
                c+=1
        return c
v=[["1245axd","Luis Jairo"],
     ["3456pib","Marcia Lira"],
     ["2576jux","Pablo Rubio"],
     ["3221lip","Rosa Jux"],
     ["3465kik","Saul Lopez"]
   ]
x=["123","luico",7,10]
t=[[2,5],[9,12],[10,12],[10,13],[10,11]]
p1=Parqueo(5,3,v,t)
p1=p1+x
print(p1.vehiculo)

print(p1.Hallar("3456pib"))
print(p1.Hallar(3))
                    
