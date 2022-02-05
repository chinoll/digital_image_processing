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

## image_restoration_and_reconstruction/ &nbsp;&nbsp; 图像复原和重建
geometric_mean.py &nbsp;&nbsp; 几何均值滤波器 <br>
harmonic_mean.py &nbsp;&nbsp; 谐波平均滤波器 <br>
contra_harmonic_mean.py &nbsp;&nbsp; 反谐波平均滤波器 <br>
median.py &nbsp;&nbsp; 中值滤波器 <br>
minimum.py &nbsp;&nbsp; 最小值滤波器 <br>
maximum.py &nbsp;&nbsp; 最大值滤波器 <br>
alpha_trimmed_mean.py &nbsp;&nbsp; 修正阿尔法均值滤波器 <br>
midpoint.py &nbsp;&nbsp; 中点滤波器 <br>
adaptive_local.py &nbsp;&nbsp; 自适应局部降噪滤波器 <br>
adaptive_median.py &nbsp;&nbsp; 自适应中值滤波器 <br>
TBLPF.py &nbsp;&nbsp; 传递巴特斯沃滤波器 <br>
Wiener.py &nbsp;&nbsp; 维纳滤波器 <br>
const_ls.py &nbsp;&nbsp; 约束最小二乘滤波器 <br>

## color_image_processing/ &nbsp;&nbsp; 彩色图像处理
color_layer.py &nbsp;&nbsp; 彩色分层 <br>
rgb_hsi.py &nbsp;&nbsp; RGB和HSI相互转换 <br>

## morphological/ &nbsp;&nbsp; 形态学处理
dilation.py &nbsp;&nbsp; 膨胀 <br>
erosion.py &nbsp;&nbsp; 腐蚀 <br>
morphological.py &nbsp;&nbsp; 形态学函数 <br>
close.py &nbsp;&nbsp; 闭运算 <br>
open.py &nbsp;&nbsp; 开运算 <br>
hmt.py &nbsp;&nbsp; 击中-击不中变换 <br>