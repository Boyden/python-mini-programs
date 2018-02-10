#Additive white Gaussian noise
import PIL.Image
import scipy.misc
import numpy as np


def convert_2d(r):
    # 添加均值为 0, 标准差为 64 的加性高斯白噪声
    s = r + np.random.normal(0, 64, r.shape)
    if np.min(s) >= 0 and np.max(s) <= 255:
        return s
    # 对比拉伸
    s = s - np.full(s.shape, np.min(s))
    s = s * 255 / np.max(s)
    s = s.astype(np.uint8)
    return s


def convert_3d(r):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = convert_2d(rr)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s


im = PIL.Image.open('/img/jp.jpg')
im = im.convert('RGB')
im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.show()
