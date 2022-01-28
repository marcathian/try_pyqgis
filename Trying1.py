import os
from qgis.core import * # QgsApplication
from qgis.server import *
from qgis.utils import * #plugins, available_plugins
from qgis import qgis
from AnotherDXF2Shape.fnc4all import myQGIS_VERSION_INT
import AnotherDXF2Shape
#app =

#plugin1 = qgis.utils.plugins["AnotherDXF2Shape"] 
#plugin1 = available_plugins["AnotherDXF2Shape"]
#plugin1 = available_plugins()
#plugin1.About()

#plgin = myQGIS_VERSION_INT


plgin = qgis.utils.startPlugin(AnotherDXF2Shape)
print(type(plgin))
print(dir(plgin))
#print(type(plugin1))