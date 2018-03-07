from robot import robot

t=robot('irb120')
t.BuildKineModules()

a=t.GetEffectorPosition([30,0,20,0,10,0])
print(t.SetEffectorPosition(a[0,0:6]))