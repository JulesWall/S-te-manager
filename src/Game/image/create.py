from PIL import Image, ImageDraw, ImageFont
import time

from db.function.Vehicule import *
from Game.image.data import *
from config import FILE_PATH

class SynoImages():

    def __init__(self, dispo):
        self.path = FILE_PATH + "/Game/image/"
        self.im = Image.open(self.path + "image1.png")
        self.im2 = Image.open(self.path + "image2.png")
        self.ims = {1:self.im,2:self.im2}

        self.font = ImageFont.truetype(self.path + "font/Segoe UI Bold.ttf", 35)
        self.font2 = ImageFont.truetype(self.path + "font/Segoe UI.ttf", 35)
        self.font3 = ImageFont.truetype(self.path + "font/Segoe UI.ttf", 45)

        draw = ImageDraw.Draw(self.im)
        formatted_date_time = time.strftime("%d/%m/%Y - %H:%M", time.localtime(time.time()))
        draw.text((400, 1400), f"{formatted_date_time}", (255, 255, 255), font = self.font)
        draw.text((20, 1200), f"Personnel CSP Sète : {dispo[2]}/{dispo[1]}/{dispo[0]} \nPersonnel SSSM : {dispo[3]}/{dispo[4]} \nOpérateur CTA disponible : {dispo[5]}", (0, 0, 0), font = self.font3)
        
        self.im.save(self.path + "syno1.png", "PNG")
        self.im2.save(self.path + "syno2.png", "PNG")

    def uptade_vhl(self, vhl):
        new_im = Image.new('RGB', (243,80), color[int(vhl.statut)]["fond"])
        draw = ImageDraw.Draw(new_im)
        w, h = draw.textsize(vhl.vehicule, font=self.font2)
        h += int(h*0.21)
        draw.text(((243-w)/2, (80-h)/2), vhl.vehicule,  color[int(vhl.statut)]["text"], font=self.font2)
        cord = (int(vhl.cord.split(',')[0].replace('(','')), int(vhl.cord.split(',')[1].replace(')','')))
        self.ims[vhl.syno].paste(new_im, cord)
        self.im.save(self.path + "syno1.png", "PNG")
        self.im2.save(self.path + "syno2.png", "PNG")

    def uptade(self):
        for v in get_all_vehicule(): v=v[0];self.uptade_vhl(Vehicule(v))
