# -*- coding: utf-8 -*-

# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
import os
import json
import sys
import tempfile
import time
import shutil
import codecs

from Ui_importproject import Ui_ImportProject

class ImportProjectDialog(QDialog, Ui_ImportProject):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.bar = QgsMessageBar(self)
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed) 
        self.gridLayout.addWidget(self.bar, 0, 0 , 0, 1, Qt.AlignTop)        
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Import")
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","Qcadastre")
        self.inputitfpath = QFileInfo(self.settings.value("file/import/inputitfpath")).absolutePath()
        self.provider = self.settings.value("options/db/provider", "")
        if self.provider == "":
            self.provider = "postgres"

        today = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(today)
        self.dateTimeEdit.setCalendarPopup(True)


    def initGui(self):       
        self.lineEditDbSchema.setValidator(QRegExpValidator(QRegExp("[a-z0-9_]+"), self.lineEditDbSchema))
        
        if self.provider == "postgres":
            self.btnProjectName.setText("Check")
            self.lblProjectName.setText("Project name: ")
            self.lblProjectName.setEnabled(True)
            self.lineEditDbSchema.setEnabled(True)
            self.btnProjectName.setEnabled(True)            
        elif self.provider == "sqlite":
            self.lblProjectName.setText("Project file: ")            
            self.btnProjectName.setText("Browse")
            self.lblProjectName.setEnabled(False)
            self.lineEditDbSchema.setEnabled(False)
            self.btnProjectName.setEnabled(False)
 
        try:
            filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/modules.json"))
            self.modules = json.load(open(filename)) 
            if self.modules != None:
                sortedModulesList = sorted(self.modules["modules"], key=lambda k: k['displayname']) 
                self.cmbBoxAppModule.clear()
                for module in sortedModulesList:
                    self.cmbBoxAppModule.insertItem(self.cmbBoxAppModule.count(), unicode(module["displayname"]), module["dirname"])
                self.cmbBoxAppModule.insertItem(0, QCoreApplication.translate("Qcadastre", "Choose module...."), None)
                self.cmbBoxAppModule.setCurrentIndex(1)
        except Exception, e:
            self.bar.pushMessage("Error", str(e), level=QgsMessageBar.CRITICAL)

    @pyqtSignature("on_btnProjectName_clicked()")    
    def on_btnProjectName_clicked(self):
        if self.provider == "postgres":
            self.bar.pushMessage("Warning", "This function is not yet implemented.", level=QgsMessageBar.WARNING, duration=5)
            pass
        elif self.provider == "sqlite":
            self.bar.pushMessage("Warning", "This function is not yet implemented.", level=QgsMessageBar.WARNING, duration=5)            
            # use "options/db/host" as setting parameter 
            pass


        
    @pyqtSignature("on_cBoxAppModule_currentIndexChanged(int)")      
    def on_cBoxAppModule_currentIndexChanged(self,  idx):
        moduleId = str(self.cmbBoxAppModule.itemData(idx).toString())
        
        for module in self.modules["modules"]:
            if moduleId == module["dirname"]:
                try:
                    submodules = module["submodules"]
                    #self.cBoxAppSubModule.clear()
                    #for submodule in submodules:
                        #self.cBoxAppSubModule.insertItem(self.cBoxAppSubModule.count(), str(submodule["displayname"]), QVariant(submodule["dirname"]))
                    #self.cBoxAppSubModule.insertItem(0, QCoreApplication.translate("QGeoApp", "Choose submodule...."), None)
                    #self.cBoxAppSubModule.setCurrentIndex(0)
                    #self.cBoxAppSubModule.setEnabled(True)
                    #self.labelAppSubModule.setEnabled(True)
                except KeyError:
                    pass
                    #self.cBoxAppSubModule.setCurrentIndex(0)
                    #self.cBoxAppSubModule.setEnabled(False)
                    #self.labelAppSubModule.setEnabled(False)
            elif idx == 0:
                    pass
                    #self.cBoxAppSubModule.setCurrentIndex(0)
                    #self.cBoxAppSubModule.setEnabled(False)
                    #self.labelAppSubModule.setEnabled(False)


    @pyqtSignature("on_btnBrowsInputFile_clicked()")    
    def on_btnBrowsInputFile_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QGeoApp", "Choose interlis transfer file"), self.inputitfpath,  "ITF (*.itf *.ITF)")
        fileInfo = QFileInfo(file)
        self.lineEditInputFile.setText(fileInfo.absoluteFilePath())


    def accept(self):
        # save the settings
        self.settings.setValue("import/inputitfpath", self.lineEditInputFile.text())
        self.settings.setValue("import/ili", self.lineEditIliModelName.text())

        # gather all data/information
        self.itf = self.lineEditInputFile.text()
        self.ili = self.lineEditIliModelName.text()
        self.dbschema = self.lineEditDbSchema.text()    
        self.appmodule = self.cBoxAppModule.itemData(self.cBoxAppModule.currentIndex()).toString()
        #self.subappmodule = self.cBoxAppSubModule.itemData(self.cBoxAppSubModule.currentIndex()).toString()
        
        self.dbhost = self.settings.value("db/import/host").toString()
        self.dbname = self.settings.value("db/import/database").toString()
        self.dbport = self.settings.value("db/import/port").toString()
        self.dbuser = self.settings.value("db/import/user").toString()
        self.dbpwd = self.settings.value("db/import/pwd").toString()
        self.dbadmin = self.settings.value("db/import/admin").toString()
        self.dbadminpwd = self.settings.value("db/import/adminpwd").toString()
        
        self.repositories = ""
        size = self.settings.beginReadArray("modelrepositories")
        for i in range(size):
            self.settings.setArrayIndex(i)
            self.repositories = self.repositories + "," + self.settings.value("url").toString()
        self.settings.endArray();
        
        self.projectsdatabase = self.settings.value("projects/database/path").toString()
        self.projectsrootdir = self.settings.value("projects/rootdir").toString()
        
        importjarpath = self.settings.value("java/import/jarpath").toString()
        importvmargs = self.settings.value("java/import/vmarguments").toString()
        
        # check if we have everything
        self.schemaOnly = "false"
        if self.itf == "":
            ret = QMessageBox.question(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "No interlis transfer file chosen.\n"
            "Create empty schema?"), QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                self.schemaOnly = "true"
            else:
                return
        
        if self.ili == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No interlis model name set."))
            return
            
        if self.dbschema == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No database schema set."))
            return
            
        if self.cBoxAppModule.currentIndex() == 0:
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No application module chosen."))
            return
            
        #if self.cBoxAppSubModule.isEnabled() and self.cBoxAppSubModule.currentIndex() == 0:
            #QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No application submodule chosen."))
            #return
    
        if self.dbhost == "" or self.dbname == "" or self.dbport == "" or self.dbuser == "" or self.dbpwd == "" or self.dbadmin == "" or self.dbadminpwd == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "Missing database parameters."))
            return

        if self.repositories == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No interlis models repository found."))
            return
            
        if self.projectsdatabase == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No projects database found. Will create one in project root directory."))
            
        if self.projectsrootdir == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No root directory for projects set."))
            return

        if importjarpath == "":
            QMessageBox.warning(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "No jar file set for import."))
            return
    
        # create java properties file
        tmpPropertiesFile = self.writeJavaPropertiesFile()
        if tmpPropertiesFile == None:
            return

        # clear output textedit
        self.textEditImportOutput.clear()
                
        # import data
        arguments = QStringList()
        
        vmargs = importvmargs.split(" ")
        for i in range(len(vmargs)):
            arguments << vmargs[i]
            
        arguments << "-jar"
        arguments << importjarpath
        arguments << tmpPropertiesFile
        
        self.process = QProcess()
        self.connect(self.process, SIGNAL("readyReadStandardOutput()"), self.readOutput)
        self.connect(self.process, SIGNAL("finished(int)"), self.finishImport)        
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)
        try:
            self.process.start("java", arguments)
        except:
            QApplication.restoreOverrideCursor()
            self.buttonBox.setEnabled(True)            

        
    def readOutput(self):
        self.textEditImportOutput.insertPlainText(QString(self.process.readAllStandardOutput()))
        self.textEditImportOutput.ensureCursorVisible()        


    def finishImport(self,  i):
        # restore gui/cursor
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)

        # update the projects database
        updated = self.updateProjectsDatabase()
        if updated == True:
            pass
        else:
            QMessageBox.critical(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Import process not sucessfully finished.\n\nCould not update projects database."))
            return
            
        # check if there are some errors/fatals in the output
        # Prüfung erst hier, da es einfacher ist den misslungenen Import zu löschen, wenn
        # in der Projektedatenbank bereits ein Eintrag ist.
        output = str(self.textEditImportOutput.toPlainText())
        if output.find("FATAL") > 0 or output.find("ERROR") > 0 or output.strip() == "":
            QMessageBox.critical(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Import process not sucessfully finished."))            
            return            
            
        # create project directory in projects root dir
        dir = self.createProjectDir()
        if dir == True:
            QMessageBox.information(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Import process finished."))
        else:
            QMessageBox.critical(None, "QGeoApp",  QCoreApplication.translate("QGeoApp", "Import process not sucessfully finished. \n\nCould not create project directory."))


    def createProjectDir(self):
        try:
            os.makedirs(str(self.projectsrootdir) + os.sep + str(self.dbschema))
            return True
        except:
            return False


    def writeJavaPropertiesFile(self):
        tmpDir = tempfile.gettempdir()
        tmpPropertiesFile = tmpDir + os.sep + str(time.time()) + ".properties"
        
        try:
            f = codecs.open(tmpPropertiesFile, "w", "utf-8")
        
            try:
                f.write("dbhost = " + self.dbhost + "\n")
                f.write("dbname = " + self.dbname + "\n")
                f.write("dbschema = " + self.dbschema + "\n")
                f.write("dbport = " + self.dbport + "\n")
                f.write("dbuser = " + self.dbuser + "\n")
                f.write("dbpwd = " + self.dbpwd + "\n")
                f.write("dbadmin = " + self.dbadmin + "\n")
                f.write("dbadminpwd = " + self.dbadminpwd + "\n")
                f.write("\n")
                f.write("import = true\n")
                f.write("vacuum = false\n")
                f.write("reindex = false\n")
                f.write("\n")
                f.write("importModelName = " + str(self.ili) + "\n")
                f.write("importItfFile = " + unicode(self.itf) + "\n")
                f.write("\n")
                f.write("schemaOnly = " + str(self.schemaOnly) + "\n")
                f.write("\n")
                f.write("additionalAttributes = false\n")
                f.write("enumerationText = true\n")
                f.write("renumberTid = true\n")
                f.write("\n");
                
                filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+self.appmodule+"/postprocessing/postprocessing.db"))                    
                #if self.subappmodule == None or self.subappmodule == "":
                    #filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+self.appmodule+"/postprocessing/postprocessing.db"))                    
                #else:
                    #filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/modules/"+self.appmodule+"/submodules/"+self.subappmodule+"/postprocessing/postprocessing.db"))
                f.write("postprocess = " + str(filename))
                
            finally:
                f.close()
                return tmpPropertiesFile
        
        except IOError:
            QMessageBox.critical(None, "QGeoApp", QCoreApplication.translate("QGeoApp", "Cannot create: " + tmpPropertiesFile) + "\n\n Import process not completed.")
            return None
        
        return  None
    
    
    def updateProjectsDatabase(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
        
        try:
            if self.projectsdatabase == "":
                srcdatabase = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qgeoapp/templates/template_projects.db"))
                self.projectsdatabase = QDir.convertSeparators(QDir.cleanPath(self.projectsrootdir + "/projekte.db"))
                shutil.copyfile(srcdatabase, self.projectsdatabase)
                self.settings.setValue("projects/database/path", QVariant(self.projectsdatabase))

                 
            self.db.setDatabaseName(self.projectsdatabase) 

            if  self.db.open() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open database:\n") + str(self.db.lastError().driverText()))            
                return 
             
            projectrootdir = QDir.convertSeparators(QDir.cleanPath(self.projectsrootdir + "/" + str(self.dbschema)))
        
            sql = "INSERT INTO projects (id, displayname, dbhost, dbname, dbport, dbschema, dbuser, dbpwd, dbadmin, dbadminpwd, provider, epsg, ilimodelname, appmodule, subappmodule, projectrootdir, projectdir) \
VALUES ('"+str(self.dbschema)+"', '"+str(self.dbschema)+"', '"+str(self.dbhost)+"', '"+str(self.dbname)+"', "+str(self.dbport)+", '"+str(self.dbschema)+"', '"+str(self.dbuser)+"', '"+str(self.dbpwd)+"', \
'"+str(self.dbadmin)+"', '"+str(self.dbadminpwd)+"', 'postgres', 21781, '"+str(self.ili)+"', '"+str(self.appmodule)+"', '"+str("")+"', '"+str(self.projectsrootdir)+"', '"+projectrootdir+"');"

            query = self.db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while updating projects database."))            
                return 
            
            self.db.close()
            self.emit(SIGNAL("projectsFileHasChanged()"))
            return True
        
        except:
            QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not update projects database:\n"))            
            return 
