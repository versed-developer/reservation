from django.shortcuts import render
from reservation.models import Reservation


def reservation_list(request):
    reservations = Reservation.objects.order_by("rental__name", "checkin", "checkout")
    prev_reservation = None
    prev_list = []
    for reservation in reservations:
        prev = '-'
        if prev_reservation:
            if prev_reservation.rental.id == reservation.rental.id:
                prev = 'Res-' + str(prev_reservation.id)
        prev_reservation = reservation
        prev_list.append(prev)

    context = {}
    result_list = []
    for reservation, prev in zip(reservations, prev_list):
        result_list.append({'reservation': reservation, 'prev': prev})

    context['object_list'] = result_list
    return render(request, 'reservation/list_view.html', context)

