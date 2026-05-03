-- 코드를 입력하세요
SELECT
    CONCAT('/home/grep/src/', file.BOARD_ID, '/', file.FILE_ID, file.FILE_NAME, file.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE AS file
JOIN (
    SELECT
        BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
    ) AS board
    ON board.BOARD_ID = file.BOARD_ID
ORDER BY FILE_ID DESC;