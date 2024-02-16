"""
==================
Rotating a 3D plot
==================

A very simple animation of a rotating 3D plot.

See wire3d_animation_demo for another simple example of animating a 3D plot.

(This example is skipped when building the documentation gallery because it
intentionally takes a long time to run)
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import animation
import imageio

im = imageio.imread('img2020.jpg')/255.0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# load some test data for demonstration and plot a wireframe
xs=im[:,:,0].flatten(order='C')
ys=im[:,:,1].flatten(order='C')
zs=im[:,:,2].flatten(order='C')



def init():
    ax.scatter(xs=xs, ys=ys, zs=zs, c=[(r,g,b) for (r,g,b) in zip(xs,ys,zs)])
    plt.xlabel('R')
    plt.ylabel('G')
    #plt.zlabel('B')
    return fig,



#ax.scatter(xs=xs, ys=ys, zs=zs, c=[(r,g,b) for (r,g,b) in zip(xs,ys,zs)])

#ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)




'''
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
'''
    
def animate(i):
    print(i)
    ax.view_init(elev=10.0, azim=i)
    return fig,

    
# create the animated plot
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
# save as a GIF
anim.save('clusters.gif', fps=30, writer='imagemagick')
