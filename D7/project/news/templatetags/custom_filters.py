from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать, и фильтры потеряются

@register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        list = ['ух', 'ор', 'ах', 'ай', 'бля', 'сука', 'хуй', 'дебил', 'пизд', 'зда', ] # Список нецензурных слов
        for A in list:
            value = value.replace(A, '#') # Замена совпадений подстроки на @!#%
        return str(value)
    else:
        raise ValueError(f'Нельзя преобразовать {type(value)}')
