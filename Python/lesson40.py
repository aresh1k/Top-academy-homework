from jinja2 import Template

print("Задание №1")

links = [
    {'href': 'Алексей', 'text': 'Главная', 'class': 'active'},
    {'href': 'Никита', 'text': 'Новости'},
    {'href': 'Виталий', 'text': 'О компании'},
    {'href': 'Виталий', 'text': 'Магазин'},
    {'href': 'Виталий', 'text': 'Контакты'}
]

menu = """<ul>
{% for i in links -%}
    {% if i.text == 'Главная' -%}
        <li><a href="{{ i['href'] }} class={{ i['class'] }}>{{ i['text'] }}</a></li>
    {% else -%}
        <li><a href="{{ i['href'] }}>{{ i['text'] }}</a></li>
    {% endif -%}
{% endfor -%}
</ul>"""

tm = Template(menu)
msg = tm.render(links=links)

print(msg)

print("-"*50)
print("Задание №2")

html = """
{% macro text_input(name, placeholder, type='text') %}
    <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
{% endmacro %}

<p>{{ text_input('firstname', 'Имя') }}</p>
<p>{{ text_input('lastname', 'Фамилия') }}</p>
<p>{{ text_input('address', 'Адрес') }}</p>
<p>{{ text_input('phone', 'Телефон', type='tel') }}</p>
<p>{{ text_input('email', 'Почта', type='email') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)


