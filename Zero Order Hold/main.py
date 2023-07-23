"""
    Zero Order Hold (ZOH) is a method used in signals processing to convert
    Continuous Time Signal into a Discrete Time Signal by holding the value of
    Continuous signal constant over each sampling interval (Samples not all)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft

def ZOH_Equation(ContinuousSignal, tStart, tEnd):
    Samples = int(tEnd / tStart)
    impulse = np.zeros(Samples)
    for i in range(Samples):
        impulse[i] = ContinuousSignal[int( (i*tStart) / tStart)]
    return impulse

def ZOH_FFT(ContinuousSignal, tStart, tEnd):
    Samples = int(tEnd / tStart)
    C_Signal = np.fft.fft(ContinuousSignal)

    Signal_Padd = np.zeros(Samples , dtype=np.complex128)
    Signal_Padd[:Samples//2+1] = C_Signal[:Samples//2+1]      #1st-half = 1st-half
    impulse = np.fft.ifft(Signal_Padd)
    return impulse.real

#Testing
def Test_Continuous_Signal(Signal_Time):
    return np.sin(2 * np.pi * Signal_Time)

Start_Time = 0.1
End_Time = 5.0
Continuous_Time = np.linspace(0, End_Time , 1000)
C_Signal = Test_Continuous_Signal(Continuous_Time)







def Test_ZOH_Equation():
    D_Signal = ZOH_Equation(C_Signal , Start_Time , End_Time)
    Discrete_Time = np.linspace(0 , End_Time, len(D_Signal))
                #print("C_Time:",Continuous_Time)
                #print("C_Signal:",C_Signal)
                #print("D_Time:",Discrete_Time)
                #print("D_Signal:",D_Signal)
    #Plotting Data
    plt.figure(figsize=(10,6))
    plt.plot(Continuous_Time, C_Signal, label='Continuous-Time Signal')
    plt.step(Discrete_Time, D_Signal, label='Discrete-Time Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('ZOH Frequency Response - Equation')
    plt.legend()
    plt.grid(True)
    plt.show()

def Test_ZOH_FFT():
    D_Signal = ZOH_FFT(C_Signal , Start_Time, End_Time)
    Discrete_Time = np.linspace(0, End_Time, len(D_Signal))
            #print("C_Time:", Continuous_Time)
            #print("C_Signal:", C_Signal)
            #print("D_Time:", Discrete_Time)
            #print("D_Signal:", D_Signal)
    # Plotting Data
    plt.figure(figsize=(10, 6))
    plt.plot(Continuous_Time, C_Signal, label='Continuous-Time Signal')
    plt.step(Discrete_Time, D_Signal, label='Discrete-Time Signal')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('ZOH Frequency Response - FFT')
    plt.legend()
    plt.grid(True)
    plt.show()



print('1-Equation (ZOH)')
print('2-Fast Fourier Transform (ZOH)')
choice = int(input())
if choice == 1:
    Test_ZOH_Equation()
if choice == 2:
    Test_ZOH_FFT()