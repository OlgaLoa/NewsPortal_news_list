from django import template


register = template.Library()

censor_list = ['Biology','Ecology','Finance']
# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    for word in censor_list:
        value = value.replace(word[1:], '*' * len(word[1:])) #Строковый метод str.replace(old, new[, count]) вернет копию строки,
        # в которой все подстроки old будут заменены на new.
    return value # Возвращаемое функцией значение подставится в шаблон.



# Декоратор register.filter() указывает Django, что нужно запомнить про существование нового фильтра.
# Название фильтра по умолчанию берется равным названию функции, то есть в шаблонах мы можем писать
# {{ price|currency }}. Однако Django дает нам возможность самим указать название фильтра.
# Например, если бы мы указали register.filter(name=’currency_rub’),
# а название функции не меняли, тогда в шаблонах мы вызывали фильтр следующим образом
# {{ price|currency_rub }}.
#
# Результат этой функции и будет подставлен у нас в шаблоне.
#
# нужно сказать,что мы хотим подключить свои фильтры. Сделать это можно с помощью указания тега
# {% load custom_filters %}.
# Где сustom_filters — это название Python файла, который мы создали в папке simpleapp/templatetags/.