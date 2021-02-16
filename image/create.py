from PIL import Image, ImageDraw, ImageFont
from db.function.Vehicule import *
from image.data import *

class Syno():

    def __init__(self, dispo):
        self.im = Image.open("/Users/Juels/Desktop/Github/csp/image/image1.png")
        self.im2 = Image.open("/Users/Juels/Desktop/Github/csp/image/image2.png")
        self.ims = {1:self.im,2:self.im2}

        self.font = ImageFont.truetype("/Users/Juels/Desktop/Github/csp/image/ARIALBD.ttf", 30, )
        self.font2 = ImageFont.truetype("/Users/Juels/Desktop/Github/csp/image/ARIALBD.ttf", 20, )
        draw = ImageDraw.Draw(self.im2)
        draw.text((130, 5), "Synoptique des moyens 3SM", (255, 255, 255), font = self.font)
        draw.text((130, 106), "Synoptique des moyens COG", (255, 255, 255), font = self.font)
        draw.text((75, 289), f"Synoptique du personnel {dispo[0]}/{dispo[1]}/{dispo[2]} - {dispo[3]}/{dispo[4]} \n     Opérateur CTA disponible : {dispo[5]}", (255, 255, 255), font = self.font)
        draw = ImageDraw.Draw(self.im)
        draw.text((80, 25), "Synoptique des moyens CSP Sète", (255, 255, 255), font = self.font)

        self.im.save("/Users/Juels/Desktop/Github/csp/image/syno1.png", "PNG")
        self.im2.save("/Users/Juels/Desktop/Github/csp/image/syno2.png", "PNG")
    
    def uptade_vhl(self, vhl):
        new_im = Image.new('RGB', (181,50), color[int(vhl.statut)]["fond"])
        draw = ImageDraw.Draw(new_im)
        w, h = draw.textsize(vhl.vehicule, font=self.font2)
        h += int(h*0.21)
        draw.text(((181-w)/2, (50-h)/2), vhl.vehicule,  color[int(vhl.statut)]["text"], font=self.font2)
        cord = (int(vhl.cord.split(',')[0].replace('(','')), int(vhl.cord.split(',')[1].replace(')','')))
        self.ims[vhl.syno].paste(new_im, cord)
        self.im.save("/Users/Juels/Desktop/Github/csp/image/syno1.png", "PNG")
        self.im2.save("/Users/Juels/Desktop/Github/csp/image/syno2.png", "PNG")

    def uptade(self):
        print(get_all_vehicule())
        for v in get_all_vehicule(): v=v[0];print(v);self.uptade_vhl(Vehicule(v))


