from django.utils import timezone
from django.contrib import messages

from datetime import datetime

from products import models


class MakeRefundTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            purchases = models.Purchase.objects.filter(user_id=request.user, make_refund_status=False)
            for purchase in purchases:
                now = datetime.now(timezone.utc)
                dif = (now - purchase.created_at).seconds
                if dif > 180:
                    purchase.make_refund_status = True
                    purchase.save()
            messages.add_message(request, messages.INFO, 'You cannot return a product.')
        response = self.get_response(request)
        return response
