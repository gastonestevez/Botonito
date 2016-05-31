from django.contrib import admin
from .models import Question, Answer,Personaje
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Personaje)

# @admin.register(models.Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = (
#         'respuesta',
#         'usuario',
#         'pregunta'
#     )
#
#     fieldsets = (
#         ('Respuestas', {
#             'fields': (
#                 'respuseta',
#                 'usuario',
#                 'pregunta',
#             ),
#         }),
#     )
