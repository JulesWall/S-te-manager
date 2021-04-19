
from db.function.ExistProfil import ExistProfil
from db.function.Vehicule import Vehicule, get_all_vehicule
from db.function.Querry import Querry
from image.create import SynoImages
from db.files.vhl import required, calculation

class Syno():

    def __init__(self):
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
        
        vhl_required = required[vhl.vehicule]
        vhl_calcualtion = calculation[vhl.vehicule]
        syno_dict = {"hdr":self.syno[0], "soff":self.syno[1], "off":self.syno[2], "inf":self.syno[3], "med":self.syno[4], "":0}
        syno_vhl = {"hdr":0, "soff":0, "off":0, "inf":0, "med":0}
        for key in vhl_calcualtion.keys():
            for i in range(len(vhl_calcualtion[key])):
                syno_vhl[key] += syno_dict[vhl_calcualtion[key][i]]
        
        number_required, number_unit = 0, 0
        for i in vhl_required.values(): number_required += i 
        for i in syno_vhl.values(): number_unit += i

        if number_required <= number_unit:
            syno_vhl_inverted = []
            for a in syno_vhl.items():
                syno_vhl_inverted.insert(0, (a[0], a[1]))
            syno_vhl_inverted = dict(syno_vhl_inverted)

            result = 0
            for i in syno_vhl_inverted.keys():
                result = syno_vhl[i] - (vhl_required[i] - result)
                if result < 0:
                    vhl.statut = 0
                    break
                else:
                    continue
            vhl.statut = 1

        else:
            vhl.statut = 0
        
        vhl.save()

    def updatevhls(self):
        for vhl in get_all_vehicule(): self.updatevhl(vhl[0])
    
    def createsyno(self):
        SynoImages(self.syno).uptade()

    def run(self):
        self.update_syno()
        self.updatevhls()
        self.createsyno()






