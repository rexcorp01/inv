

stock = """
    select secucode, secuabbr as secuname from jydb.secumain WHERE SECUCATEGORY IN(1, 8, 13) AND 
    LISTEDSTATE = 1 and listedstate = 1 AND LISTEDSECTOR IN (1, 2, 3, 6, 7)
    UNION ALL
    select secucode, secuabbr as secuname from jydb.hk_secumain where SECUMARKET = 72 and listedstate = 1
"""


# 股票申万行业分类
stock_sw = """
    SELECT
        *
    FROM
        (
        SELECT
            SecuCode,
            FirstIndustryName,
            SecondIndustryName
        FROM
            jydb.secumain s
        JOIN jydb.LC_ExgIndustry m ON
            s.CompanyCode = m.CompanyCode
        WHERE
            m.Standard = 24
            AND m.IFPERFORMED = 1
            AND s.SecuCategory = 1
            AND s.LISTEDSECTOR IN (1, 2, 6, 7)
        ORDER BY
            s.secucode)
    UNION ALL
    SELECT
        s.SECUCODE,
        ls.FIRSTINDUSTRYNAME ,
        ls.SECONDINDUSTRYNAME
    FROM
        JYDB.LC_STIBExgIndustry ls
    JOIN JYDB.SECUMAIN s ON
        ls.COMPANYCODE = s.COMPANYCODE
    WHERE
        ls.STANDARD = 24
        AND ls.IFEXECUTED = 1
        AND s.SecuCategory = 1
        AND s.LISTEDSECTOR IN (1, 2, 6, 7)
"""


# 股票因子暴露度
stock_expose = """
    SELECT
        TRADE_DATE AS "date",
        TICKER_SYMBOL AS secucode,
        BETA,
        MOMENTUM,
        "SIZE" as "size",
        EARNYILD,
        RESVOL,
        GROWTH,
        BTOP,
        LEVERAGE,
        LIQUIDTY,
        SIZENL
    FROM
        DATAYES."dy1d_exposure" dde
    WHERE
        TRADE_DATE >= '<date>'
"""


# 股票收盘价
stock_quote = """
    SELECT
        s.SECUCODE,
        qd.CLOSEPRICE,
        qd.PREVCLOSEPRICE,
        qd.TRADINGDAY AS "date"
    FROM
        JYDB.QT_DAILYQUOTE qd
    JOIN JYDB.SECUMAIN s ON
        qd.INNERCODE = s.INNERCODE
    WHERE
        s.secucategory in (1, 8, 13) and
        qd.TRADINGDAY > TO_DATE('<date>', 'YYYY-MM-DD')
"""

stock_quote_sti = """
    SELECT
        s.SECUCODE,
        qd.CLOSEPRICE,
        qd.PREVCLOSEPRICE,
        qd.TRADINGDAY AS "date"
    FROM
        JYDB.LC_STIBDailyQuote qd
    JOIN JYDB.SECUMAIN s ON
        qd.INNERCODE = s.INNERCODE
    WHERE
        qd.TRADINGDAY > TO_DATE('<date>', 'YYYY-MM-DD')
"""


# 股票收盘价
stock_quote_hk = """
    SELECT
        s.SECUCODE,
        qd.CLOSEPRICE,
        qd.PREVCLOSEPRICE,
        qd.TRADINGDAY AS "date"
    FROM
        JYDB.QT_HKDAILYQUOTE qd
    JOIN JYDB.HK_SECUMAIN s ON
        qd.INNERCODE = s.INNERCODE
    WHERE
        qd.TRADINGDAY > TO_DATE('<date>', 'YYYY-MM-DD')
"""


# 股票资金流动
stock_capital_flow = """
    SELECT
        s.SECUCODE,
        qt.TRADINGDATE AS "date",
        qt.BUYVALUE,
        qt.SELLVALUE,
        (qt.BUYVALUE - qt.SELLVALUE) AS NETVALUE 
    FROM
        JYDB.QT_TRADINGCAPITALFLOW qt
    JOIN JYDB.SECUMAIN s ON
        s.INNERCODE = qt.INNERCODE
    WHERE
        qt.TRADINGDATE > TO_DATE('<date>', 'YYYY-MM-DD')
"""