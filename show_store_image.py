from scipy import misc 
import matplotlib.pyplot as plt
f = misc.face() 
plt.imsave('jpg.jpg',f)
plt.imshow(f) 
plt.show()