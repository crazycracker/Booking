from datetime import datetime

from django.db import models


# Create your models here.
class UserModel(models.Model):
    id = models.CharField(
        verbose_name="user id",
        max_length=10,
        primary_key=True
    )

    name = models.CharField(
        verbose_name="username",
        max_length=20
    )

    phone = models.CharField(
        verbose_name="Phone",
        max_length=256,
    )

    email = models.EmailField(
        verbose_name="Email",
    )

    type = models.CharField(
        verbose_name="type",
        max_length=10
    )


class requestTable(models.Model):
    block = models.CharField(
        verbose_name="Building name",
        max_length=20
    )

    room_number = models.CharField(
        verbose_name="Room number",
        max_length=10,
    )

    date = models.DateField(
        verbose_name="booking date",
        default=datetime.now().strftime("YYYY-MM-DD")
    )

    time = models.TimeField(
        verbose_name="booking time"
    )

    reserved_by = models.CharField(
        verbose_name="reserver",
        max_length=10
    )

    granter = models.CharField(
        verbose_name="granter",
        max_length=10
    )

    description = models.CharField(
        verbose_name="description",
        max_length=100
    )

    booking_status = models.IntegerField(
        verbose_name="booking status",
    )



class classroom(models.Model):
    block = models.CharField(
        verbose_name="Building name",
        max_length=20
    )

    room_number = models.CharField(
        verbose_name="Room number",
        max_length=10,
        primary_key=True
    )

    floor_number = models.PositiveIntegerField(
        verbose_name="Floor number"
    )

    maximum_capacity = models.PositiveIntegerField(
        verbose_name="Maximum room size",
    )

    projector = models.CharField(
        verbose_name="Projector condition",
        max_length=20
    )

    computer = models.CharField(
        verbose_name="Computer condition",
        max_length=20
    )

    air_conditioner = models.CharField(
        verbose_name="AC condition",
        max_length=20
    )

    speakers = models.CharField(
        verbose_name="Speakes condition",
        max_length=20
    )


class labs(models.Model):
    block = models.CharField(
        verbose_name="Building name",
        max_length=20
    )

    room_number = models.CharField(
        verbose_name="Room number",
        max_length=10,
        primary_key=True
    )

    floor_number = models.CharField(
        verbose_name="Floor number",
        max_length=10
    )

    maximum_capacity = models.CharField(
        verbose_name="Maximum room size",
        max_length=5
    )

    type = models.CharField(
        verbose_name="Type of Lab",
        max_length=20
    )

    air_conditioner = models.CharField(
        verbose_name="AC condition",
        max_length=20
    )
