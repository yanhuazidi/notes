# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
wav.py 基于傅里叶变换的频域滤波
'''
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf
import numpy.fft as nf

sample_rate, noised_sigs = \
    wf.read('../data/noised.wav')
print(sample_rate, noised_sigs.shape)
# 声音在存储时放大了2**15, 所以处理时先除去
noised_sigs = noised_sigs / 2**15
# 绘制声音图像
times = np.arange(
    len(noised_sigs)) / sample_rate
mp.figure('Filter', facecolor='lightgray')

mp.subplot(221)
mp.title('Noised', fontsize=16)
mp.xlabel('Times', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],
        color='dodgerblue', label='Signal')
mp.tight_layout()
mp.legend()

# 第二步
# 通过采样个数与周期 得到频率数组
freqs = nf.fftfreq(times.size,
                   1 / sample_rate)
# 获取每个频率对应的能量值
noised_fft = nf.fft(noised_sigs)
noised_pow = np.abs(noised_fft)
mp.subplot(222)
mp.title('Frequency', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(
    freqs[freqs > 0], noised_pow[freqs > 0],
    color='orangered', label='Frequency')
mp.tight_layout()

# 将低频噪声去除后绘制音频频率的:频率/能量图
fund_freq = freqs[noised_pow.argmax()]
# 找到不是高能信号的噪声信号
noised_inds = np.where(freqs != fund_freq)
# 把fft得到的复数数组中所有噪声信号的值
# 改为0
filter_fft = noised_fft.copy()
filter_fft[noised_inds] = 0
filter_pow = np.abs(filter_fft)
mp.subplot(224)
mp.title('Filter Frequency', fontsize=16)
mp.xlabel('Filter Frequency', fontsize=12)
mp.ylabel('Filter Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(
    freqs[freqs > 0], filter_pow[freqs > 0],
    color='orangered', label='Filter Frequency')
mp.tight_layout()

# 第四步
filter_sigs = nf.ifft(filter_fft).real
mp.subplot(223)
mp.title('Filter', fontsize=16)
mp.xlabel('Times', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],
        color='dodgerblue', label='Signal')
mp.tight_layout()
mp.legend()

# 第五步
wf.write(
    '../data/filter.wav', sample_rate,
    (filter_sigs * 2**15).astype('int16'))

mp.show()
