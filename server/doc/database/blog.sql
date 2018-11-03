--
-- ��SQLiteStudio v3.1.1 �������ļ� ���� 11�� 3 21:26:25 2018
--
-- �ı����룺System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- ��db_blog_article
-- 简述表
DROP TABLE IF EXISTS db_blog_article;

CREATE TABLE db_blog_article (
    id         STRING (32)  DEFAULT "",                                -- 简述Id
    contentId  STRING (32)  DEFAULT "",                                -- 内容Id
    title      STRING (255) DEFAULT "",                                -- 标题
    abstr      STRING (511) DEFAULT "",                                -- 简述
    createTime TIME         DEFAULT (datetime('now', 'localtime') ),  -- 创建时间
    updateTime TIME         DEFAULT (datetime('now', 'localtime') ),  -- 最后修改时间
    categoryId STRING (32)  DEFAULT "",                                -- 类别
    hotTag     INTEGER      DEFAULT (0),                              -- 是否热搜 0：否， 1：是
    mainKeyId  STRING (32)  DEFAULT "",                                -- 标签
    author     STRING (32)  DEFAULT "",                                -- 作者
    authorId   STRING (32)  DEFAULT ""                                 -- 作者Id
);


-- ��db_blog_category
-- 类别表
DROP TABLE IF EXISTS db_blog_category;

CREATE TABLE db_blog_category (
    id       STRING (32) DEFAULT "",                                   -- 类别Id
    category STRING (32) DEFAULT ""                                    -- 类别名
);


-- ��db_blog_content
-- 博客内容表
DROP TABLE IF EXISTS db_blog_content;

CREATE TABLE db_blog_content (
    id      STRING (32) PRIMARY KEY,                                   -- 内容Id
    content TEXT        DEFAULT ('')                                    -- 具体内容
);


-- ��db_blog_count
-- 点击量和评论量
DROP TABLE IF EXISTS db_blog_count;

CREATE TABLE db_blog_count (
    id           STRING (32) DEFAULT "",                               -- 表格Id
    contentId    STRING (32) DEFAULT "",                               -- 内容Id
    articleId    STRING (32) DEFAULT "",                               -- 简述Id
    clickCount   INTEGER     DEFAULT (0),                             -- 点击量
    discussCount INTEGER     DEFAULT (0)                              -- 评论量
);


-- ��db_blog_discuss
-- 评论表
DROP TABLE IF EXISTS db_blog_discuss;

CREATE TABLE db_blog_discuss (
    id         STRING (32)  DEFAULT "",                                -- 评论Id
    contentId  STRING (32)  DEFAULT "",                                -- 内容Id
    articleId  STRING (32)  DEFAULT "",                                -- 简述Id
    discuss    STRING (255) DEFAULT "",                                -- 评论
    createTime TIME         DEFAULT (datetime('now', 'localtime') ),   -- 创建时间
    updateTime TIME         DEFAULT (datetime('now', 'localtime') ),   -- 最后修改时间
    author     STRING (32)  DEFAULT "",                                -- 作者
    authorId   STRING (32)  DEFAULT ""                                 -- 作者Id
);


-- ��db_blog_mainkey
-- 标签表
DROP TABLE IF EXISTS db_blog_mainkey;

CREATE TABLE db_blog_mainkey (
    id        STRING (32) DEFAULT "",                                  -- 关键字Id
    contentId STRING (32) DEFAULT "",                                  -- 内容Id
    articleId STRING (32) DEFAULT "",                                  -- 简述Id
    mainKey   STRING (32) DEFAULT ""                                   -- 关键字
);


-- ��db_blog_user
DROP TABLE IF EXISTS db_blog_user;

CREATE TABLE db_blog_user (
    id       STRING (32) DEFAULT "",
    username STRING (64) DEFAULT "",
    passwod  STRING (32) DEFAULT ""
);


-- ��t_test_info
DROP TABLE IF EXISTS t_test_info;

CREATE TABLE t_test_info (
    id          INTEGER      PRIMARY KEY ASC,
    username    VARCHAR (32) DEFAULT "",
    password    VARCHAR (64) DEFAULT "",
    create_time DATE         DEFAULT (datetime('now', 'localtime') ),
    update_time DATE         DEFAULT (datetime('now', 'localtime') ) 
);

INSERT INTO t_test_info (
                            id,
                            username,
                            password,
                            create_time,
                            update_time
                        )
                        VALUES (
                            1,
                            'yyy',
                            'aaabbb',
                            '2018-10-31 16:47:19',
                            '2018-10-31 16:47:19'
                        );

INSERT INTO t_test_info (
                            id,
                            username,
                            password,
                            create_time,
                            update_time
                        )
                        VALUES (
                            2,
                            'ppp',
                            'oooiii',
                            '2018-10-31 18:10:39',
                            '2018-10-31 18:10:39'
                        );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
