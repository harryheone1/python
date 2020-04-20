rate_dict = {('USD', 'CNY'): 6.64, ('CAD', 'CNY'): 4.88}
rate_dict_inverse = {key: 1 / value for (key, value) in rate_dict.items()}


def get_rate(source, target):
    rate_formal = rate_dict.get((source, target))
    return rate_dict_inverse.get(
        (target, source)) if rate_formal is None else rate_formal

count = 0
source_input = input('请输入金额和货币单位, 例如 100CNY, 退出请输入Q : ')
while (source_input != 'Q'):
    target = input('请目标货币, 例如 USD : ')
    source = source_input[-3:]

    rate = get_rate(source, target)
    if rate is not None:
        source_amount = float(source_input[:-3])
        converted_amount = rate * source_amount
        print('转换后的金额是 {}'.format(str(converted_amount) + ' ' + target))
        count = count + 1
    else:
        if len(source) == 0 or len(target) == 0:
            print('没有指定相应的货币单位')
        else:
            print('目前不支持输入的货币')
    print('************************************')
    source_input = input('请输入金额和货币单位, 例如 100CNY, 退出请输入Q : ')

print("转换结束, 祝你愉快")
print("目前为止, 您一共进行了 {} 次转换".format(count))