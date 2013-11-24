CREATE TABLE projects
(
        ogc_fid INTEGER PRIMARY KEY NOT NULL,
        id TEXT,
        displayname TEXT,
        dbhost TEXT,
        dbname TEXT,
        dbport INT,
        dbschema TEXT UNIQUE,
        dbuser TEXT,
        dbpwd TEXT,
        dbadmin TEXT,
        dbadminpwd TEXT,
        provider TEXT,
        epsg INT,
        ilimodelname TEXT,
        appmodule TEXT,
        appmodulename TEXT,	
        projectrootdir TEXT,
        projectdir TEXT,
        datadate DATE,
        importdate DATE DEFAULT (datetime('now','localtime')),
        notes TEXT
);
