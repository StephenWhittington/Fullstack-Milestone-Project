from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentPostForm


def get_comments(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'commentposts.html' template
    """
    comments = Comment.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "commentposts.html", {'comments': comments})


def comment_detail(request, pk):
    """
    Create's a view that returns a single
    Comment object based on the post ID (pk) and
    render it to the 'commentdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.views += 1
    comment.save()
    return render(request, "commentdetail.html", {'comment': comment})


def create_or_edit_comment(request, pk=None):
    """
    Create's a view that allows us to create
    or edit a comment depending if the Post ID
    is null or not
    """
    comment = get_object_or_404(Comment, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentPostForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(comment_detail, comment.pk)
    else:
        form = CommentPostForm(instance=comment)
    return render(request, 'commentpostform.html', {'form': form})