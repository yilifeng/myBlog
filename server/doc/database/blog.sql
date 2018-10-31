--
-- ��SQLiteStudio v3.1.1 �������ļ� ���� ʮ�� 31 15:39:14 2018
--
-- �ı����룺System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- ��t_test_info
DROP TABLE IF EXISTS t_test_info;

CREATE TABLE t_test_info (
    id          INTEGER      PRIMARY KEY ASC,
    username    VARCHAR (32) DEFAULT "",
    password    VARCHAR (64) DEFAULT "",
    create_time DATE         DEFAULT (datetime('now', 'localtime') ),
    update_time DATE         DEFAULT (datetime('now', 'localtime') ) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
