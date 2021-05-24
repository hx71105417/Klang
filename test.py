from Klang import (
    C,Klang,
    REF,REFDATE,
    MA,
    HHV,LLV
)

Kl = Klang.Kl
# 设置为隆基
Kl.setcurrent('sh.601012')
print(C)

# 设置为茅台
Kl.setcurrent('sh.600519')
print(C)

Kl.setdate(start='2021-04-26',end='2021-04-29')
print(C)

# 系列比，可以计算出每天的涨幅
print(C.data,C[1].data)
print(C/C[1])

#显示当天TCL的收盘价
Kl.setcurrent('sz.000100')
Kl.setdate()
print(C)

print(REF(C,1))
print(REFDATE(C,'20210429'))

print(MA(C,5))
print(HHV(C,10))
print(LLV(C,10))