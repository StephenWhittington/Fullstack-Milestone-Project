from django.shortcuts import render
from django.utils import timezone
from artifacts.models import Artifact
from .models import Auction, Watchlist, Bid, Chat

def index(request):
    """
    The main page of the website
    Returns
    -------
    HTTPResponse
        The index page with the current and future auctions.
    """
    auctions = Auction.objects.filter(time_ending__gte=datetime.now()).order_by('time_starting')

    try:
        if request.session['username']:
            user = User.objects.get(username=request.session['username'])

            w = Watchlist.objects.filter(user_id=user)
            watchlist = Auction.objects.none()
            for item in w:
                a = Auction.objects.filter(id=item.auction_id.id)
                watchlist = list(chain(watchlist, a))

            userDetails = UserDetails.objects.get(user_id=user.id)
            return render(request, 'index.html',
                {'auctions': auctions, 'balance': userDetails.balance, 'watchlist': watchlist})
    except KeyError:
        return render(request, 'index.html', {'auctions': auctions})

    return render(request, 'index.html', {'auctions': auctions})

def bid_page(request, auction_id):
    """
    Returns the bid page for the
    selected auction.
    Parametes
    ---------
    auction_id : class 'int'
    Returns
    -------
    HTTPResponse
        Return the bidding page for the selected auction.
    Function : index(request)
        If the user is not logged in.
    """
    print(type(auction_id))
    try:
        # if not logged in return to the index page.
        if request.session['username']:
            # If the auction hasn't started return to the index page.
            auction = Auction.objects.filter(id=auction_id)
            if auction[0].time_starting > timezone.now():
                return index(request)
            user = User.objects.filter(username=request.session['username'])

            stats = []
            time_left, expired = remaining_time(auction[0])
            stats.append(time_left) # First element in stats list

            current_cost = 0.20 + (auction[0].number_of_bids * 0.20)
            current_cost = "%0.2f" % current_cost
            stats.append(current_cost)

            # Second element in stats list
            if expired < 0: # if auction ended append false.
                stats.append(False)
            else:
                stats.append(True)

            # Third element in stats list
            latest_bid = Bid.objects.all().order_by('-bid_time')
            if latest_bid:
                winner = User.objects.filter(id=latest_bid[0].user_id.id)
                stats.append(winner[0].username)
            else:
                stats.append(None)

            # Fourth element in stats list
            chat = Chat.objects.all().order_by('time_sent')
            stats.append(chat)

            # Getting user's watchlist.
            w = Watchlist.objects.filter(user_id=user[0])
            watchlist = Auction.objects.none()
            for item in w:
                a = Auction.objects.filter(id=item.auction_id.id)
                watchlist = list(chain(watchlist, a))

            return render(request, 'bid.html',
            {
                'auction': auction[0],
                'user': user[0],
                'stats': stats,
                'watchlist':watchlist
            })
    except KeyError:
        return index(request)

    return index(request)

def comment(request, auction_id):
    """
    Comment on an auction.
    Returns
    -------
    Function : bid_page(request, auction_id)
        Return the
    Function : index(request)
        If the user is not logged in.
    """
    try:
        if request.session['username']:
            user = User.objects.filter(username=request.session['username'])
            auction = Auction.objects.filter(id=auction_id)
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    msg = Chat()
                    msg.user_id = user[0]
                    msg.auction_id = auction[0]
                    msg.message = form.cleaned_data['comment']
                    msg.time_sent = timezone.now()
                    msg.save()
                    return bid_page(request, auction_id)

            return index(request)
    except KeyError:
        return index(request)

    return index(request)

def raise_bid(request, auction_id):
    """
    Increases the bid of the selected auction
    and returns to the bidding page.
    Parametes
    ---------
    auction_id : class 'int'
    Returns
    -------
    Function : bid_page(request, auction_id)
        Return the bidding page for the selected auction.
    Function : index(request)
        If the user is not logged in.
    """
    auction = Auction.objects.get(id=auction_id)
    if auction.time_ending < timezone.now():
        return bid_page(request, auction_id)
    elif auction.time_starting > timezone.now():
        return index(request)

    try:
        if request.session['username']:
            user = User.objects.get(username=request.session['username'])
            userDetails = UserDetails.objects.filter(user_id=user.id)
            if userDetails.balance > 0.0:
                latest_bid = Bid.objects.filter(auction_id=auction.id).order_by('-bid_time')
                if not latest_bid:
                    increase_bid(user, auction)
                else:
                    current_winner = User.objects.filter(id=latest_bid[0].user_id.id)
                    if current_winner[0].id != user.id:
                        increase_bid(user, auction)

            return bid_page(request, auction_id)
    except KeyError:
        return index(request)

    return bid_page(request, auction_id)


