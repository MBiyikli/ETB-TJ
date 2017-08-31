import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
import ikpy


tj = ikpy.chain.Chain.from_urdf_file('C:/Users/MUSTAFA/Desktop/'
                                     'tjxml.XML')

ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

tj.plot([0,0,0,0,0,0,0], ax)


tj.plot(tj.inverse_kinematics([
    [1, 0, 0, 0.05],
    [0, 1, 0, 0],
    [0, 0, 1, 0.35],
    [0, 0, 0, 1]
]), ax)

tj.plot(tj.inverse_kinematics([
    [1, 0, 0, 0.05],
    [0, 1, 0, 0],
    [0, 0, 1, 0.30],
    [0, 0, 0, 1]
]), ax)

tj.plot(tj.inverse_kinematics([
    [1, 0, 0, 0.05],
    [0, 1, 0, 0],
    [0, 0, 1, 0.20],
    [0, 0, 0, 1]
]), ax)


tj.plot(tj.inverse_kinematics([
    [1, 0, 0, 0.05],
    [0, 1, 0, 0],
    [0, 0, 1, 0.050],
    [0, 0, 0, 1]
]), ax)

tj.plot(tj.inverse_kinematics([
    [1, 0, 0, 0.1],
    [0, 1, 0, 0.05],
    [0, 0, 1, 0.050],
    [0, 0, 0, 1]
]), ax)

matplotlib.pyplot.show()
























