import rawpy
import imageio
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os #Работа с папками и файлами

def filterphoto(put):
#Создаём классы по которым будем класифицировать фотографии
    className=['Fokus','Geometriy','Horoshie_foto','Miganie','Peresvet','Smazany','Temniy','shum']

    #Размер изображения для НС
    visota=50
    shirina=50
    sloi=3
    xTest = []

    # будем делить вю выборку на обучающую и тестовую в соотношении 90% к 10%
    # также сразу будет поворачивать фотографии и добавлять шума в класс шум
    # решепим фотографии до размера 50*50, иначе не хватает ОЗУ
    #создаем список файлов в директории
    puti = os.listdir(put)
    #обрабатываем каждый файл и добавляем в массив для распознания
    for j in puti:
        with rawpy.imread(put + '\\' + j) as raw:
            thumb = raw.extract_thumb()
        if thumb.format == rawpy.ThumbFormat.JPEG:
            with open('thumb.jpeg', 'wb') as f:
                f.write(thumb.data)
        elif thumb.format == rawpy.ThumbFormat.BITMAP:
            imageio.imsave('thumb.jpeg', thumb.data)

        L = Image.open('thumb.jpeg')
        z = L.resize((visota, shirina))
        x = image.img_to_array(z)
        x = x.reshape(visota, shirina, sloi)
        x /= 255
        xTest.append(x)  # добавляем в обучающую выборку
    #преобразуем в нампай массив
    xTest = np.array(xTest)

    # data_file= open(,'r')
    model1 = load_model('./parserapp/best_model_99.72.h5', compile=False)
#создаем папки по категориям
    for k in className:
        os.mkdir(put + '\\' + k)
#определяем категории фотографий
    prediction = model1.predict(xTest) #Классифицируем каждое изображение
#раскидываем фотографии по папкам
    for i in range(len(puti)): #Проходим по картинкам
      #Вводим результаты на экран

        os.replace(put + '\\' + puti[i], put + '\\' + className[np.argmax(prediction[i])] + '\\' + puti[i])
#удаляем пустые папки с категориями
    for k in className:
        if len(os.listdir(put + '\\' + k)) == 0:
            os.rmdir(put + '\\' + k)
