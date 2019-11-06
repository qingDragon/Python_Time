def test(*args):
    print(args)
#结果元组格式打印
test(1,2,3,4,5)

test(*[1,2,3,4])