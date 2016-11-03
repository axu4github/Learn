# -*- coding: UTF-8 -*-
'''
测试try catch
'''
print('start try catch.')
try:
    raise Exception('raise Exception')
except Exception as e:
    print(e.message + ' 123')
else:
    pass
finally:
    print('finally!')
