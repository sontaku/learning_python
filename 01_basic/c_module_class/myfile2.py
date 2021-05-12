# myfile.py
# from c_module_class.mymodule import get_weather, get_date

# (1) 모듈 전체를 참조할 때
# import mymodule
# today = mymodule.get_weather()
# todayDate = mymodule.get_date()
#
# print('오늘의 날씨는', today)
# print('오늘은 {}요일 입니다'.format(todayDate))


# (2) 모듈 전체를 참조하면서 별칭 부여
# import mymodule as my
# today = my.get_weather()
# todayDate = my.get_date()
#
# print('오늘의 날씨는', today)
# print('오늘은 {}요일 입니다'.format(todayDate))


# (3)전체 모듈 중에서 필요한 것 참조하기(PyCharm 자동완성 가능)
# from mymodule import get_weather, get_date
#
# today = get_weather()
# todayDate = get_date()
#
# print('오늘의 날씨는', today)
# print('오늘은 {}요일 입니다'.format(todayDate))

#[참고]
# import mypackage.mymodule
# print('오늘의 날씨는', mypackage.mymodule.get_weather())
# print('오늘은 {}요일 입니다'.format(mypackage.mymodule.get_date()))

from mypackage import mymodule
print('오늘의 날씨는', mymodule.get_weather())
print('오늘은 {}요일 입니다'.format(mymodule.get_date()))
