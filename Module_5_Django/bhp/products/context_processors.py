from products import models


def available_refunds(request):
    available_refunds_count = None
    if request.user.is_superuser:
        available_refunds_count = models.Refund.objects.all().count()
    return {'AVAILABLE_REFUNDS': available_refunds_count}
