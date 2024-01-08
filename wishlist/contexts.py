from .models import Wishlist


def wishlist_counter(request):
    """
    Handles wishlist item count
    """
    if request.user.is_authenticated:
        wishlist_count = (
            Wishlist.objects.filter(user=request.user).count()
        )
    else:
        wishlist_count = 0


    return {
        'wishlist_count': wishlist_count,
    }
