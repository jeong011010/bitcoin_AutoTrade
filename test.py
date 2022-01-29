import pyupbit

access = "xiGR9gWQxRmTwQ3nE1aI8hNya8yFjByW4O3IHi0z"          # 본인 값으로 변경
secret = "Wdwpa8btDIXoKFimc0bWUd9WllNlzgw6YJdShlYm"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
