from django.db import models

class BookingRecords(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_name = models.CharField(max_length=100)
    booking_email = models.EmailField()
    booking_contact = models.CharField(max_length=15)

    def __str__(self):
        return "%s " % (self.booking_name)

    class Meta:
        db_table = "bookingrecords"
