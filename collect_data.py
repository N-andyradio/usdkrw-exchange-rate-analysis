"""원/달러 환율(KRW=X) 일별 데이터를 수집해 data/ 폴더에 CSV로 저장한다."""
import yfinance as yf

TICKER = "KRW=X"
START = "2021-01-01"
END = "2026-10-01"  # yfinance의 end는 포함되지 않으므로 9/30까지 받으려면 10/01로 지정
OUTPUT = "data/usdkrw_2021_2026.csv"

df = yf.download(TICKER, start=START, end=END, auto_adjust=False)

# 최신 yfinance는 컬럼이 2단(MultiIndex)으로 나올 수 있어 1단으로 정리
if hasattr(df.columns, "levels"):
    df.columns = df.columns.get_level_values(0)

df.index.name = "Date"
df.to_csv(OUTPUT)

print(f"저장 완료: {OUTPUT}")
print(f"기간: {df.index.min().date()} ~ {df.index.max().date()}")
print(f"데이터 수: {len(df)}개")
print(df.head())
