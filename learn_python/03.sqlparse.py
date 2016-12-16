# -*- coding: UTF-8 -*-

import sqlparse
from sqlparse.tokens import Keyword

if __name__ == "__main__":
    sql = """
        select 
            *
        from
            (select
                tab1.col3 as t1_col3, count(tab3.col3) as count
            from
                tab1
            where
                tab1.col1 = 'value1' and tab1.col2 = 'value2'
            group by 
                tab1.col3
            order by 
                tab1.col4 desc) as a
        left join
            (select 
                tab2.col1 as t2_col1
            from
                tab2) as b
        on
            a.t1_col3 = b.t2_col1
        group by 
            a.t1_col3
        order by 
            b.t2_col1
    """

    def getTokens(sql): return sqlparse.parse(sql)[0].tokens
    def getKeywords(sql): return [item.value.upper() for item in sqlparse.parse(sql)[0].tokens if item.ttype is Keyword]

    tokens = getTokens(sql)
    kws = getKeywords(sql)
    print(tokens)
    print(kws)
