menu = [{'title': "Про нас", 'url_name': 'about'},
        {'title': "Послуги", 'url_name': 'services'},
        {'title': "Контактні данні", 'url_name': 'contacts'},
]

class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                context['menu'] = menu
                context['phonenumber'] = '+1 (234) 567 89 00'
                context['email'] = 'yourmail@gmail.com'
                context['location'] = 'м.Одеса, вул.Дерібасівська, буд.1/2,'

                return context