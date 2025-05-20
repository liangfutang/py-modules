import os.path

import cv2 as cv
import numpy as np
from PIL import Image


# 读取并显示图片
def readPicture():
    img = cv.imread('face01.jpg')
    cv.imshow('主题', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 灰度转化
def changeGray():
    img = cv.imread('face01.jpg')
    cv.imshow('org', img)
    # 转成灰色更方便识别，减少不必要的干扰
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

def resize():
    img = cv.imread('face01.jpg')
    resize_img = cv.resize(img, dsize=(200, 200))
    cv.imshow('org', img)
    cv.imshow('resize', resize_img)

    print('未修改', img.shape)
    print('修改后', resize_img.shape)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 在图像上画图形
def draw():
    img = cv.imread('face01.jpg')
    # 坐标及宽高
    x,y,w,h = 100,100,100,100
    # 绘制矩形
    cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=2)
    # 绘制圆形
    cv.circle(img, center=(x+w, y+h), radius=100, color=(255,0,0), thickness=1)

    cv.imshow('draw', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def faceDetect():
    img = cv.imread('face01.jpg')
    # 灰度处理
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 添加一个分类器
    face_detect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gray_img)
    # face = face_detect.detectMultiScale(gray_img, 1.1, 5, 0, (100,100), (300,300))
    for (x,y,w,h) in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv.putText(img, 'liu', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)  # 添加人名

    cv.imshow('detect', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def dataTrain():
    def getImageAndLabels(path):
        # 储存人脸数据(二维数组)
        faceSamples=[]
        # 储存姓名数据
        ids = []
        # 储存图片信息
        iamgePaths = [os.path.join(path,f) for f in os.listdir(path)]
        # 加载分类器
        face_detect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

        for imagesPath in iamgePaths:
            # 打开图片，灰度化 PIL有九种不同模式：1，L，P，RGB，RGBA，CMYK，YCbCr，I，F
            PIL_img = Image.open(imagesPath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            # 获取图片中人脸特诊
            faces = face_detect.detectMultiScale(img_numpy)
            # 获取每张图片的id和姓名
            id = int(os.path.split(imagesPath)[1].split('.')[0])
            # 预防无面容照片
            for (x,y,w,h) in faces:
                ids.append(id)
                faceSamples.append(img_numpy[y:y+h,x:x+w])
            print('ids:', ids)
            print('fs:', faceSamples)
        return faceSamples, ids

    faces,ids = getImageAndLabels('./data/pic')
    # 加载识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    # 保存训练文件
    recognizer.write('./data/trainer/trainer.yml')

def faceMatch():
    # 加载训练数据集文件
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read('./data/trainer/trainer.yml')
    # 获取用户姓名
    # names = []
    # imagesPath = [os.path.join('./data/pic', f) for f in os.listdir('./data/pic')]
    # for imagesPath in imagesPath:
    #     names.append(str(os.path.split(imagesPath)[1].split('.')[1]))
    names = [f.split('.')[1] for f in os.listdir('./data/pic')]

    def detect(img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # face = face_detect.detectMultiScale(gray)
        face = face_detect.detectMultiScale(gray, 1.1, 5, cv.CASCADE_SCALE_IMAGE,(100,100),(400,400))
        for (x,y,w,h) in face:
            cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,0,255),thickness=1)
            # 人脸识别
            ids, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print('标签id:',ids,'置信评分:',confidence)
            if confidence > 80:
                cv.putText(img, 'unkown', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            else:
                cv.putText(img, f'{str(names[ids-1])} {confidence:.2f}', (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        cv.imshow('face', img)

    detect(cv.imread('face01.jpg'))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    # readPicture()
    # changeGray()
    # resize()
    # draw()
    # faceDetect()
    # dataTrain()
    faceMatch()
