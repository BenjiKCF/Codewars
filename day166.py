def tribonacci(signature,n):
    if n == 1:
        return [signature[0]]
    elif n ==0:
        return []
    k = 0
    while k < n-3:
        signature.append(sum(signature[k:k+3]))
        k += 1
    return signature
print tribonacci([1,1,1],10)#,[1,1,1,3,5,9,17,31,57,105])

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3):
    res.append(sum(res[-3:]))
  return res
