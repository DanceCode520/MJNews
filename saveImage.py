from PIL import Image
import os.path
import glob
import time
def convertjpg(jpgfile,outdir,width=1280,height=720):
    img=Image.open(jpgfile)
    # new_img=img.resize((width,height),Image.BILINEAR)
    now_time = time.strftime('%Y%m%d%H%M%S')
    print('now time ==',now_time)
    imgpath = outdir+now_time+os.path.splitext(jpgfile)[1]
    img.save(imgpath)
for jpgfile in glob.glob("C:/Users/guiwang.su/Desktop/北京.jpg"):
    convertjpg(jpgfile,"./static/newsImages/")