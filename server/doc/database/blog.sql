--
-- 由SQLiteStudio v3.1.1 产生的文件 周三 十月 31 15:39:14 2018
--
-- 文本编码：System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：t_test_info
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
