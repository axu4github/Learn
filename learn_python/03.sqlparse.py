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

    def getTokens(sql):
        return sqlparse.parse(sql)[0].tokens

    def getKeywords(sql):
        return [item.value.upper() for item in sqlparse.parse(sql)[0].tokens if item.ttype is Keyword]

    def existsKeywords(sql, kws, levels=1):
        print(kws.split(" "))
        for kw in kws.split(" "):
            if not (kw == " " or kw == ""):
                if kw.upper() not in getKeywords(sql):
                    return False

        return True

    tokens = getTokens(sql)
    kws = getKeywords(sql)
    print(tokens)
    print(kws)
    print(existsKeywords(sql, ""))

    sql = '''
    select d_week_seq1
       ,round(sun_sales1/sun_sales2,2)
       ,round(mon_sales1/mon_sales2,2)
       ,round(tue_sales1/tue_sales2,2)
       ,round(wed_sales1/wed_sales2,2)
       ,round(thu_sales1/thu_sales2,2)
       ,round(fri_sales1/fri_sales2,2)
       ,round(sat_sales1/sat_sales2,2)
     from
     (select wswscs.d_week_seq d_week_seq1
            ,sun_sales sun_sales1
            ,mon_sales mon_sales1
            ,tue_sales tue_sales1
            ,wed_sales wed_sales1
            ,thu_sales thu_sales1
            ,fri_sales fri_sales1
            ,sat_sales sat_sales1
      from wswscs,date_dim 
      where date_dim.d_week_seq = wswscs.d_week_seq and
            d_year = [YEAR]) y,
     (select wswscs.d_week_seq d_week_seq2
            ,sun_sales sun_sales2
            ,mon_sales mon_sales2
            ,tue_sales tue_sales2
            ,wed_sales wed_sales2
            ,thu_sales thu_sales2
            ,fri_sales fri_sales2
            ,sat_sales sat_sales2
      from wswscs
          ,date_dim 
      where date_dim.d_week_seq = wswscs.d_week_seq and
            d_year = [YEAR]+1) z
     where d_week_seq1=d_week_seq2-53
     order by d_week_seq1;
    '''

    print "*" * 40
    print getTokens(sql)
    print "*" * 40

    sql = '''
    select 
        *, 
        (select sa.script_id from test.scripts_app as sa where sa.id = s.id) as script_id
    from 
        test.scripts as s 
    '''

    print getTokens(sql)
    print "*" * 40

