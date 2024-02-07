# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SmartSDI
                                 A QGIS plugin
 Description
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-07-19
        copyright            : (C) 2023 by Geo-System
        email                : geo-system@geo-system.com.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SmartSDI class from file SmartSDI.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .smartsdi import SmartSDI
    return SmartSDI(iface)
