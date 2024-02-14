# coding:utf-8

# Create a database for register cassiopeia project in mysql local server.

import mysql.connector as MC


def Create_data_base():
    try:
        conn = MC.connect(host = 'localhost', user = 'root', password = '')
        cursor = conn.cursor()

#Create Database and use it

        req_database = 'CREATE DATABASE IF NOT EXISTS `CASSIOPEIA`'

        cursor.execute(req_database)
        conn.commit()

        req_use_db = 'USE `CASSIOPEIA`'

        cursor.execute(req_use_db)
        conn.commit

#Create summoners table

        req_summoners = 'CREATE TABLE IF NOT EXISTS `summoners`(\
                    `id_summoner` SMALLINT(5) NOT NULL AUTO_INCREMENT,\
                    `name_summoner` VARCHAR(32) NOT NULL,\
                    `riot_id_summoner` VARCHAR(58),\
                    `region_summoner` CHAR(4),\
                    `usual_lane` CHAR(10),\
                    `league_summoner` CHAR(16),\
                    PRIMARY KEY(`id_summoner`),\
                    UNIQUE (`name_summoner`),\
                    UNIQUE (`riot_is_summoner`)\
                    )\
                    ENGINE = InnoDB\
                    CHARACTER SET utf8mb4\
                    COLLATE utf8mb4_unicode_ci;'
    
        cursor.execute(req_summoners)
        conn.commit()

# Create Matches table

        req_matches ='CREATE TABLE IF NOT EXISTS `matches`(\
                `id_match` MEDIUMINT(7) NOT NULL AUTO_INCREMENT,\
                `red_top` CHAR(16),\
                `red_jun` CHAR(16),\
                `red_mid` CHAR(16),\
                `red_bot` CHAR(16),\
                `red_sup` CHAR(16),\
                `blu_top` CHAR(16),\
                `blu_jun` CHAR(16),\
                `blu_mid` CHAR(16),\
                `blu_bot` CHAR(16),\
                `blu_sup` CHAR(16),\
                `win_side` TINYINT(1),\
                `riot_id_match` BIGINT(15),\
                UNIQUE (`riot_id_match`),\
                `ref_id_summoners` SMALLINT(5) REFERENCES `summoners`(`id_summoner`),\
                PRIMARY KEY(`id_match`)\
                )\
                ENGINE = MyISAM\
                CHARACTER SET utf8mb4\
                COLLATE utf8mb4_unicode_ci;'
    
        cursor.execute(req_matches)
        conn.commit()

# Create Champions_list table
        
        req_Champions = 'CREATE TABLE IF NOT EXISTS `champions_list`(\
                    `id_champion` SMALLINT(3) NOT NULL,\
                    `name_champ` CHAR(16) NOT NULL,\
                    `win_rate` FLOAT(2,2),\
                    PRIMARY KEY (`id_champion`)\
                    )\
                    ENGINE = MyISAM\
                    CHARACTER SET utf8mb4\
                    COLLATE utf8mb4_unicode_ci;'
    
        cursor.execute(req_Champions)
        conn.commit()

# Create Compos table

        req_compos = 'CREATE TABLE IF NOT EXISTS `compos`(\
                    `id_compos` MEDIUMINT(6) NOT NULL AUTO_INCREMENT,\
                    `code_compo` BIGINT(15) NOT NULL,\
                    `win_count` SMALLINT(6),\
                    `lose_count` SMALLINT(6),\
                    PRIMARY KEY (`id_compos`)\
                    )\
                    ENGINE = MyISAM\
                    CHARACTER SET utf8mb4\
                    COLLATE utf8mb4_unicode_ci;'
    
        cursor.execute(req_compos)
        conn.commit()
    
# Show tables

        cursor_b = conn.cursor(buffered=True)

        req_tables = 'SHOW TABLES'
    
        cursor_b.execute(req_tables)
        conn.commit()
        tables = cursor.fetchall()
    
        for table in tables:
            print(table)

    except MC.Error as err:
        print(err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()