
from db.function.ExistProfil import ExistProfil
from db.function.Vehicule import Vehicule, get_all_vehicule
from db.function.Querry import Querry
from image.create import SynoImages

class Syno():

    def __init__(self):
        self.csp = "Sète"
        self.syno = [0, 0, 0, 0, 0, 0] # [HDR, SOFF, OFF, MED, INF, CTA]
    
    def update_syno(self):
        service = Querry("SELECT * FROM service")     
        for data in service:
            i, uid, name, starttime, cta = data
            player = ExistProfil(uid)
            if not cta:self.syno[player.hierarchie-1] += 1
            if cta: self.syno[5] += 1
        return self
    
    def updatevhl(self, vhl):
        vhl = Vehicule(vhl)
        if vhl.statut != 0 and vhl.statut != 1: return vhl.statut
        vhl.calculator = list(vhl.calculator.split(" "))    
        ii = 0
        for i in vhl.calculator : vhl.calculator[ii] = i.split("+"); ii += 1
        syno_vhl = [0, 0, 0, 0, 0, 0]
        for i in vhl.calculator:
            for ii in i:
                syno_vhl[vhl.calculator.index(i)] += self.syno[int(ii)]

        unitnumer = 0
        for i in syno_vhl : unitnumer += i

        number_needed = eval(str(vhl.required))
        syno_required = list(vhl.required.split(" + "))
        for i in range(len(syno_required)) : syno_required[i] = int(syno_required[i])
        
        def get_powermax(syno):
            power_max = 0
            for i in syno :
                if i != 0 : 
                    power_max = syno.index(i)
            return power_max

        print(syno_vhl)
        print(syno_required)

        if get_powermax(syno_vhl) >= get_powermax(syno_required):
            if number_needed <= unitnumer:vhl.statut = 1
            else:vhl.statut = 0
        else:vhl.statut = 0

        vhl.save()

    def updatevhls(self):
        for vhl in get_all_vehicule(): self.updatevhl(vhl[0])
    
    def createsyno(self):
        SynoImages(self.syno).uptade()

    def run(self):
        self.update_syno()
        self.updatevhls()
        self.createsyno()






