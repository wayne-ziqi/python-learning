> 文章来源：https://www.cnblogs.com/yinxiangnan-charles/p/5928689.html

## [python 读取并显示图片的两种方法](https://www.cnblogs.com/yinxiangnan-charles/p/5928689.html)

在 python 中除了用 opencv，也可以用 matplotlib 和 PIL 这两个库操作图片。本人偏爱 matpoltlib，因为它的语法更像 matlab。

# 一、matplotlib

## 1. 显示图片



```python
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

lena = mpimg.imread('lena.png') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
lena.shape #(512, 512, 3)

plt.imshow(lena) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
```



## 2. 显示某个通道

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

```
# 显示图片的第一个通道
lena_1 = lena[:,:,0]
plt.imshow('lena_1')
plt.show()
# 此时会发现显示的是热量图，不是我们预想的灰度图，可以添加 cmap 参数，有如下几种添加方法：
plt.imshow('lena_1', cmap='Greys_r')plt.show()img = plt.imshow('lena_1')img.set_cmap('gray') # 'hot' 是热量图
plt.show()
```

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

## 3. 将 RGB 转为灰度图

matplotlib 中没有合适的函数可以将 RGB 图转换为灰度图，可以根据公式自定义一个：

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

```
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray = rgb2gray(lena)    
# 也可以用 plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.imshow(gray, cmap='Greys_r')plt.axis('off')
plt.show()
```

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

## 4. 对图像进行放缩

这里要用到 scipy

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

```
from scipy import misc
lena_new_sz = misc.imresize(lena, 0.5) # 第二个参数如果是整数，则为百分比，如果是tuple，则为输出图像的尺寸
plt.imshow(lena_new_sz)
plt.axis('off')
plt.show()
```

[![复制代码](python图片处理.assets/copycode.gif)](javascript:void(0);)

## 5. 保存图像

5.1 保存 matplotlib 画出的图像

该方法适用于保存任何 matplotlib 画出的图像，相当于一个 screencapture。

```
plt.imshow(lena_new_sz)
plt.axis('off')
plt.savefig('lena_new_sz.png')
```

5.2 将 array 保存为图像

```
from scipy import misc
misc.imsave('lena_new_sz.png', lena_new_sz)
```

5.3 直接保存 array

读取之后还是可以按照前面显示数组的方法对图像进行显示，这种方法完全不会对图像质量造成损失

```
np.save('lena_new_sz', lena_new_sz) # 会在保存的名字后面自动加上.npy
img = np.load('lena_new_sz.npy') # 读取前面保存的数组
```

 

 

# 二、PIL 

## 1. 显示图片

```
from PIL import Image
im = Image.open('lena.png')
im.show()
```

## 2. 将 PIL Image 图片转换为 numpy 数组

```
im_array = np.array(im)
# 也可以用 np.asarray(im) 区别是 np.array() 是深拷贝，np.asarray() 是浅拷贝
```

## 3. 保存 PIL 图片

直接调用 Image 类的 save 方法

```
from PIL import Image
I = Image.open('lena.png')
I.save('new_lena.png')
```

## 4. 将 numpy 数组转换为 PIL 图片

这里采用 matplotlib.image 读入图片数组，注意这里读入的数组是 float32 型的，范围是 0-1，而 PIL.Image 数据是 uinit8 型的，范围是0-255，所以要进行转换：

```
import matplotlib.image as mpimg
from PIL import Image
lena = mpimg.imread('lena.png') # 这里读入的数据是 float32 型的，范围是0-1
im = Image.fromarray(np.uinit8(lena*255))
im.show()
```

##  5. RGB 转换为灰度图

```python
from PIL import Image
I = Image.open('lena.png')
I.show()
L = I.convert('L')
L.show()
```

 