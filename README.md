# 数字图像处理笔记及其算法实现

sample.jpg &nbsp;示例图片 <br>
![示例图片](https://github.com/chinoll/digital_image_processing/raw/master/sample.jpg)
sample_gray.jpg &nbsp;灰度图 <br>
![灰度图](https://github.com/chinoll/digital_image_processing/raw/master/sample_gray.jpg)
sample2.jpg &nbsp;示例图片2 <br>
![示例图片2](https://github.com/chinoll/digital_image_processing/raw/master/sample2.jpg)

## gray/ &nbsp;&nbsp;灰度变换算法

inversion.py &nbsp;&nbsp; 反色算法 <br>
pow.py &nbsp;&nbsp; 幂律变换算法 <br>
histogram_equalization.py &nbsp;&nbsp; 直方图均衡化算法 <br>
histogram_specification.py &nbsp;&nbsp; 直方图匹配算法 <br>

## spatial_filtering/ &nbsp;&nbsp;空间滤波算法
box_kernel.py &nbsp;&nbsp; 盒状卷积核 <br>
gauss_kernel.py &nbsp;&nbsp; 高斯卷积核 <br>
laplace_kernel.py &nbsp;&nbsp; 拉普拉斯卷积核 <br>
Unsharpening_Mask.py &nbsp;&nbsp; 钝化掩蔽和高提升滤波算法 <br>
roberts_kernel.py &nbsp;&nbsp; 罗伯特卷积核 <br>
sobel_kernel.py &nbsp;&nbsp; sobel卷积核 <br>

## frequency_filtering/ &nbsp;&nbsp;频域滤波算法
ILPF.py &nbsp;&nbsp; 理想低通滤波器 <br>
GLPF.py &nbsp;&nbsp; 高斯低通滤波器 <br>
BLPF.py &nbsp;&nbsp; 巴特沃斯低通滤波器 <br>
IHPF.py &nbsp;&nbsp; 理想高通滤波器 <br>
GHPF.py &nbsp;&nbsp; 高斯高通滤波器 <br>
BHPF.py &nbsp;&nbsp; 巴特沃斯高通滤波器 <br>
laplace.py &nbsp;&nbsp; 频域拉普拉斯滤波器 <br>
homomorphic.py &nbsp;&nbsp; 同态滤波器 <br>
IBRF.py &nbsp;&nbsp; 理想带阻滤波器 <br>
GBRF.py &nbsp;&nbsp; 高斯带阻滤波器 <br>
BBRF.py &nbsp;&nbsp; 巴特斯沃带阻滤波器 <br>