 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import qcadastre.modules.pnf.tools.utils as utils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
    def run(self):        
        self.settings = QSettings("CatAIS","Qcadastre")
        project_id = (self.settings.value("project/id"))
        epsg = (self.settings.value("project/epsg"))
        
        if not project_id:
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
            return
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = "Lagekontrolle - Bahn" + " (" + str(project_id) + ")"
            
            layer = {}
            layer["type"] = "wms"
            layer["title"] = "Orthofoto CIR"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
            layer["layers"] = "Orthofoto11_CIR"
            layer["format"] = "image/jpeg"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            
            rlayer = utils.loadLayer(self.iface, layer)         
            
            layer = {}
            layer["type"] = "wms"
            layer["title"] = "Orthofoto RGB"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
            layer["layers"] = "Orthofoto_SO"
            layer["format"] = "image/jpeg"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            
            rlayer = utils.loadLayer(self.iface, layer) 
            if rlayer:
                self.iface.legendInterface().setLayerVisible(rlayer, True)     
                
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Gemeindegrenze"
            layer["featuretype"] = "gemeindegrenzen_gemeindegrenze"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
            layer["group"] = group
            layer["style"] = "gemeindegrenze/gemgre_strichliert.qml"

            gemgrelayer = utils.loadLayer(self.iface, layer) 
            if gemgrelayer:
                self.iface.legendInterface().setLayerVisible(gemgrelayer, True)     
              
    #        layer = {}
    #        layer["type"] = "postgres"
    #        layer["title"] = "SBB-Gleisnetz"
    #        layer["featuretype"] = "gleisnetz"
    #        layer["geom"] = "geom"
    #        layer["key"] = "gid"            
    #        layer["sql"] = ""
    #        layer["readonly"] = True
    #        layer["group"] = group
    #        layer["style"] = "sbb/gleisnetz.qml"
    #         
    #        params =  {}
    #        params["appmodule"] = str(self.settings.value("project/active/appmodule").toString())
    #        params["subappmodule"] = str(self.settings.value("project/active/subappmodule").toString())      
    #        params["provider"] = "postgres"
    #        params["dbhost"] = str(self.settings.value("project/active/dbhost").toString())
    #        params["dbport"] = str(self.settings.value("project/active/dbport").toString())
    #        params["dbname"] = "pnf_varia"
    #        params["dbschema"] = "sbb"
    #        params["dbuser"] = str(self.settings.value("project/active/dbuser").toString())
    #        params["dbpwd"] = str(self.settings.value("project/active/dbpwd").toString())
    #        params["dbadmin"] = str(self.settings.value("project/active/dbadmin").toString())
    #        params["dbadminpwd"] = str(self.settings.value("project/active/dbadminpwd").toString())
    #        
    #        layer["params"] = params
    #
    #        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
    #        if vlayer <> False:
    #            self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.BoFlaeche"
            layer["featuretype"] = "bodenbedeckung_boflaeche"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_bahn_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Flaechenelement"
            layer["featuretype"] = "v_einzelobjekte_flaechenelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_fl_bahn_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Linienelement"
            layer["featuretype"] = "v_einzelobjekte_linienelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_li_bahn_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Punktelement"
            layer["featuretype"] = "v_einzelobjekte_punktelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_pk_andere.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"LI.Liegenschaft"
            layer["featuretype"] = "liegenschaften_liegenschaft"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "li/liegenschaft_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, False)    

            if gemgrelayer <> False:
                rect = gemgrelayer.extent()
                rect.scale(1.2)
                self.iface.mapCanvas().setExtent(rect)        
                self.iface.mapCanvas().refresh() 

        except Exception, e:
            QApplication.restoreOverrideCursor()            
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
        QApplication.restoreOverrideCursor()        

        # Workaround for geometryless-tables-wgs84-bug.
        try:
            self.canvas.setMapUnits(0)		
            srs = QgsCoordinateReferenceSystem()
            srs.createFromSrid(int(epsg))
            renderer = self.canvas.mapRenderer()
            renderer.setDestinationCrs(srs)
        except Exception, e:
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
