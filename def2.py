#s24010
#関数で消費税を計算するコード

def postTaxPrice(price):
    ans = price * 1.1
    return ans

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
