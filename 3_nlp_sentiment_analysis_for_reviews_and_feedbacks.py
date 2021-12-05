# -*- coding: utf-8 -*-
"""3 NLP sentiment analysis for reviews and feedbacks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qAeEkUIspDEvxRQNXZ8fxM8utmICRAOd
"""

!pip install fastai --upgrade

from fastai.text.all import *
dls = TextDataLoaders.from_folder(untar_data(URLs.IMDB),
valid='test')
learn = text_classifier_learner(dls, AWD_LSTM,
drop_mult=0.5, metrics=accuracy)
learn.fine_tune(4, 1e-2)

learn.predict("I really hated that movie!")