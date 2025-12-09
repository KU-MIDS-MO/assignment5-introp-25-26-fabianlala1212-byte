import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    signal = np.array(signal)
    turning_points = []
    
    for i in range(1, len(signal) - 1):
        before = signal[i] - signal[i - 1]
        after  = signal[i + 1] - signal[i]
        
        if before * after < 0:
            turning_points.append(i)
            
    turning_points = np.array(turning_points)
    
    

        
    plt.plot(signal , label="Signal")
    plt.scatter(turning_points, signal[turning_points], 
                color='red', label="Turning Points")
    plt.title("Signal with Turning Points")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()
    plt.show
    
    return turning_points


x = [1, 3, 7, 6, 2, 5, 9]
print(detect_turning_points(x))
