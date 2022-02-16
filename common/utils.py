from typing import List, Optional

import pandas as pd
from impala.dbapi import connect

import logging
import os ,sys

from pyspark.sql import SparkSession

# 로그 logger = logging.getLogger(
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

IMPALA_HOST: str = '172.30.71.31'
IMPALA_PORT: int = 31055

def query2df(query: str, host: str = IMPALA_HOST, port: int = IMPALA_PORT) -> pd.DataFrame:
    with connect(host=host, port=port) as conn:
        return pd.read_sql_query(query, conn)

def query2exec(query: str):
    conn = connect(host=IMPALA_HOST, port=IMPALA_PORT)
    cursor = conn.cursor()
    for sql in query.split(';'):
        if (len(sql)-sql.count(" ") )> 5:
            print(sql)
            cursor.execute(sql)
    cursor.close()
    conn.close()

def get_column_list(
    table: str,
    exclude_columns: Optional[List[str]] = None,
    impala_host: str = IMPALA_HOST,
    impala_port: int = IMPALA_PORT,
) -> List[str]:
    query = f"""
        describe {table};
    """
    column_list: pd.DataFrame = query2df(query, host=impala_host, port=impala_port)

    column_names: List[str] = column_list['name'].values.tolist()
    if exclude_columns is not None:
        column_names = sorted(list(set(column_names) - set(exclude_columns)))

    logger.info(f'[+] table {table} | number of column names : {len(column_names)}')

    return column_names