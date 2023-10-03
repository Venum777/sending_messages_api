from django.db import models
from auths.models import MyCustomUser


class Messages(models.Model):
    """Messages model"""

    ONE_MINUTE = 0
    FIVE_MINUTE = 1
    TEN_MINUTE = 2
    FIFTEEN_MINUTE = 3
    THIRTY_MINUTE = 4
    FORTY_FIVE_MINUTE = 5
    ONE_HOUR = 6
    SIX_HOURS = 7
    TWELVE_HOURS = 8
    TWENTY_FOUR_HOURS = 9

    TIMES_INTERVAL = (
        (ONE_MINUTE, '1 минута'),
        (FIVE_MINUTE, '5 минут'),
        (TEN_MINUTE, '10 минут'),
        (FIFTEEN_MINUTE, '15 минут'),
        (THIRTY_MINUTE, '30 минут'),
        (FORTY_FIVE_MINUTE, '45 минут'),
        (ONE_HOUR, '1 час'),
        (SIX_HOURS, '6 часов'),
        (TWELVE_HOURS, '12 часов'),
        (TWENTY_FOUR_HOURS, '24 часа')
    )

    message = models.TextField(
        verbose_name='сообщение',
        null=False,
        blank=False
    )

    sender: MyCustomUser = models.ForeignKey(
        verbose_name='кто отправил',
        to=MyCustomUser,
        on_delete=models.CASCADE
    )

    recipient = models.EmailField(
        verbose_name='почта получателя',
        max_length=200,
        null=False
    )

    how_many_messages = models.IntegerField(
        verbose_name='сколько отправить сообщений',
        default=1
    )

    interval = models.PositiveSmallIntegerField(
        choices=TIMES_INTERVAL,
        verbose_name='промежуток между сообщениями',
        default=ONE_MINUTE
    )

    class Meta:
        ordering = ['-sender']
        verbose_name = 'Отправка сообщения'
        verbose_name_plural = 'Отправка сообщений'