from django.contrib.auth.models import User
from django.db import models
from artifacts.models import Artifact


class Auction(models.Model):
    artifact_id = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
	
    def __str__(self):
        return "ID:" + str(self.pk) + " ARTIFACT_ID:" + str(self.artifact_id)


class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
	
    def __str__(self):
        return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
            str(self.auction_id) + " " + str(self.bid_time) 

class Chat(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()

    def __str__(self):
        return "AUCTION_ID:" + str(self.auction_id) + " USER_ID:" + str(self.user_id)
