from django.db import models
from django.db import models
import numpy as np
from rest_framework import serializers
from datetime import datetime, date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import pandas as pd
from django.urls import path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from django.conf import settings
import face_recognition


class Contact(models.Model):
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to='covers/')
    #Output = models.ImageField(upload_to='new/', blank=True)

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)

        if self.Picture:
            #pic = Image.open(self.Picture.path)
            in_image = face_recognition.load_image_file(self.Picture.path)
            out_image = Image.fromarray(in_image)
            out_image_w, out_image_h = out_image.size
            face_locations = face_recognition.face_locations(in_image)
            for (top, right, bottom, left) in face_locations:
                out_image = out_image.crop((left - (out_image_w * .1), top - (out_image_h * .17), right + (out_image_w * .1), bottom + (out_image_h * .1)))

            out_image.save(self.Picture.path)

    def __str__(self):
        return self.Description

# Create your models here.
