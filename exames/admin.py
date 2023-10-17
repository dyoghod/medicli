from django.contrib import admin
from .models import TiposExame, PedidoExame, SolicitacaoExame

admin.site.register(TiposExame)
admin.site.register(PedidoExame)
admin.site.register(SolicitacaoExame)

