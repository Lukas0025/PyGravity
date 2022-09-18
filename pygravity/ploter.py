import matplotlib.pyplot as plt
import matplotlib.collections as collections
import numpy as np
import os

def show3d(motions):
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1, projection='3d')

    xdata = []
    ydata = []
    zdata = []

    distMax = max(_getMax(motions, 0) - _getMin(motions, 0), _getMax(motions, 1) - _getMin(motions, 1), _getMax(motions, 2) - _getMin(motions, 2))

    ybound = [_getMin(motions, 1), _getMin(motions, 1) + distMax]
    xbound = [_getMin(motions, 0), _getMin(motions, 0) + distMax]
    zbound = [_getMin(motions, 2), _getMin(motions, 2) + distMax]

    ax.set_xlim(xbound[0], xbound[1])
    ax.set_ylim(ybound[0], ybound[1])
    ax.set_zlim(zbound[0], zbound[1])

    for motion in motions:
        for index, body in enumerate(motion.bodies):
            if (len(xdata) < (index + 1)):
                xdata.append([])
                ydata.append([])
                zdata.append([])

            xdata[index].append(body.position[0])
            ydata[index].append(body.position[1])
            zdata[index].append(body.position[2])

    for index in range(len(xdata)):
        ax.plot(xdata[index],    ydata[index],    zdata[index])
        
        # draw sphere
        if not(motion.bodies[index].radius is None):
            u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
            x = xdata[index][0] + motion.bodies[index].radius * np.cos(u) * np.sin(v)
            y = ydata[index][0] + motion.bodies[index].radius * np.sin(u) * np.sin(v)
            z = zdata[index][0] + motion.bodies[index].radius * np.cos(v)
            ax.plot_wireframe(x, y, z, color = motion.bodies[index].color)

    plt.show()


def show2d(motions):
    xdata = []
    ydata = []

    for motion in motions:
        for index, body in enumerate(motion.bodies):
            if (len(xdata) < (index + 1)):
                xdata.append([])
                ydata.append([])

            xdata[index].append(body.position[0])
            ydata[index].append(body.position[1])

    fig, ax = plt.subplots()

    dots = []
    for index in range(len(xdata)):
        ax.plot(xdata[index], ydata[index])
        
        if not(motion.bodies[index].radius is None):
            dots.append(plt.Circle((xdata[index][0], ydata[index][0]), radius=motion.bodies[index].radius, color=motion.bodies[index].color))

    c = collections.PatchCollection(dots)
    ax.add_collection(c)

    ax.axis('square')
    plt.show()

def _getMin(motions, axis):
    minimum = motions[0].bodies[0].position[axis]

    for motion in motions:
        for body in motion.bodies:
            if minimum > body.position[axis]:
                minimum = body.position[axis]

    return minimum

def _getMax(motions, axis):
    maximum = motions[0].bodies[0].position[axis]

    for motion in motions:
        for body in motion.bodies:
            if maximum < body.position[axis]:
                maximum = body.position[axis]

    return maximum

def anim2d(motions, history=10, directory=".", space="dynamic"):
    xdata = []
    ydata = []

    offsety = (_getMax(motions, 1) - _getMin(motions, 1)) / 100 
    offsetx = (_getMax(motions, 0) - _getMin(motions, 0)) / 100 

    ybound = [_getMin(motions, 1) - offsety, _getMax(motions, 1) + offsety]
    xbound = [_getMin(motions, 0) - offsetx, _getMax(motions, 0) + offsetx]

    for n, motion in enumerate(motions):

        for index, body in enumerate(motion.bodies):
            if (len(xdata) < (index + 1)):
                xdata.append([])
                ydata.append([])
            elif (len(xdata[index]) > history):
                xdata[index].pop(0)
                ydata[index].pop(0)

            xdata[index].append(body.position[0])
            ydata[index].append(body.position[1])

        fig, ax = plt.subplots()
        
        if space == "static":
            ax.set_xlim(xbound[0], xbound[1])
            ax.set_ylim(ybound[0], ybound[1])
            ax.axis('square')
        
        dots = []
        for index in range(len(xdata)):
            ax.plot(xdata[index], ydata[index])
            
            if not(motion.bodies[index].radius is None):
                dots.append(plt.Circle((xdata[index][-1], ydata[index][-1]), radius=motion.bodies[index].radius, color=motion.bodies[index].color))
            else:
                ax.plot(xdata[index][-1], ydata[index][-1], 'o', color=motion.bodies[index].color)

            ax.annotate(motion.bodies[index].name, (xdata[index][-1], ydata[index][-1]))

        c = collections.PatchCollection(dots)
        ax.add_collection(c)

        if space == "dynamic":
            ax.axis('square')

        plt.savefig(f"{directory}/{n:016}.png")
        plt.close()

def framesDropper(motions, tragetFps=30, tragetDuration=10):
    targetFramesTotal  = tragetFps * tragetDuration
    currentFramesTotal = len(motions)

    droppedTotal       = currentFramesTotal - targetFramesTotal

    if droppedTotal < 0:
        return None

    frames = []

    everyNFrame = int(round(currentFramesTotal / targetFramesTotal))

    index = 0
    while index < len(motions):
        frames.append(motions[index])
        index += everyNFrame

    return frames


def anim2mp4(directory, name, fps=30):
    os.system(f"ffmpeg -r {fps} -f image2 -i {directory}/%016d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p {name}.mp4")

def anim2gif(directory, name, fps=30):
    os.system(f"ffmpeg -r {fps} -i {directory}/*.png -y {name}.gif")
