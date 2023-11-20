from .models import Wishlist

def wishlist_counter(request):
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0
        
    print(wishlist_count)

    return {
        'wishlist_count': wishlist_count,
        
    }