from django.contrib import admin
from .models import Auction, Chat, Watchlist, Bid

admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)
