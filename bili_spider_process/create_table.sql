#建表语句:
CREATE TABLE test_db.anime_info (
    anime_title varchar(100) NULL,
    anime_order varchar(100) NULL,
    anime_badge varchar(100) NULL,
    anime_index varchar(100) NULL,
    anime_link varchar(100) NULL,
    image_url varchar(100) NULL,
    update_time DATETIME NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci