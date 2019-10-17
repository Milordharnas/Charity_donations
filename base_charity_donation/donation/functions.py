from donation.models import Donation


def count_from_Donation():
    donation = Donation.objects.all()
    quantity_donations = 0
    names_institutions = []
    count_institutions = 0
    for i in donation:
        quantity_donations += i.quantity
        if not i.institution in names_institutions:
            names_institutions.append(i.institution)
            count_institutions += 1

    class a:
        quantity = quantity_donations
        institution = count_institutions

    return a
