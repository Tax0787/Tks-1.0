tks = []
nom = -1 
class Tks:
    def __init__(self,name,title,geometry,prints):
        global tks
        global nom
        nom += 1
        if prints: print(str(nom) + "is this Tks object's Memory code.")
        tks.append({'name' : name, 'title' : '\'' +  title + '\'' , 'geometry' : '\'' + geometry + '\''})
    @classmethod
    def wiget(cls,name,command,option,memory_code):
        global tks
        objects = tks[memory_code]
        return "{} = {}({}{});{}.pack()\n".format(name,command,objects['name'],option,name)
    @classmethod
    def sose(cls,option,wiget,sose,memory_code):
        global tks
        objects = tks[memory_code]
        return '''try:
    from Tkinter import *
except:
    from tkinter import *
{} = Tk()
{}.title({})
{}.geometry({})
{}
{}
{}
{}.mainloop()'''.format(objects['name'],objects['name'],objects['title'],objects['name'],objects['geometry'],option,wiget,sose,objects['name'])
