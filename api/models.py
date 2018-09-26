from django.db import models
from jsonfield import JSONField


class DateTimeCheckModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class KakaoUser(DateTimeCheckModel):
    user_key = models.CharField(
        max_length=190,
        primary_key=True,
        unique=True,
    )
    context = JSONField()

    def __str__(self):
        return self.user_key


class PackageQuery(DateTimeCheckModel):
    PACKAGE_QUERY_TYPES = (
        ('HBL', 'HBL / 운송장번호'),
        ('MBL', 'MBL'),
        ('CRG', '화물관리번호'),
    )

    user = models.ForeignKey(KakaoUser,
                             on_delete=models.CASCADE,
                             db_index=True)
    type = models.CharField(max_length=3,
                            choices=PACKAGE_QUERY_TYPES,
                            db_index=True)
    tracking_number = models.CharField(max_length=190)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user_id} / {self.type} / {self.tracking_number}'
