from django.db import models
from django.contrib.auth.models import User


class AgencyModel(models.Model):
    agency = models.CharField(max_length=100, verbose_name="Firma nomi")

    def __str__(self):
        return self.agency


class FacilityModel(models.Model):
    agency = models.ForeignKey(AgencyModel, on_delete=models.CASCADE, verbose_name="Firma nomi")
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()  # bu yerga ma'lumot kiritidadi masalan hajmi umrami Masalan: "Umra safari"
    months = (
        ("yanvar", "yanvar"),
        ("fevral", "fevral"),
        ("mart", "mart"),
        ("april", "april"),
        ("may", "may"),
        ("iyun", "iyun"),
        ("iyul", "iyul"),
        ("avgust", "avgust"),
        ("sentyabr", "sentyabr"),
        ("oktyabr", "oktyabr"),
        ("noyabr", "noyabr"),
        ("dekabr", "dekabr"),
    )
    month = models.CharField(max_length=50, verbose_name="Oy", choices=months)
    days = models.IntegerField(verbose_name="Davomiyligi ")  # necha kunlik umra, masalan 10 kunlik
    _from = models.DateField(max_length=100, verbose_name="Boshlanish sanasi ")
    _to = models.DateField(max_length=100, verbose_name="Tugash sanasi ")
    image = models.ImageField(upload_to='', verbose_name="Lavhalar",
                              blank=True)  # har turfirma baribir birorta umra uchun taklif qilingan qulayliklar haqida tayyorlatdan dizayni bor Masalan " https://images.app.goo.gl/NikZirKMN8dYH66e9 "
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="Narxi")
    included_services = models.TextField(verbose_name="Mavjud xizmatlar ")
    contact = models.IntegerField(verbose_name="Telefon raqami ")
    telegram = models.URLField(verbose_name="Telegram manzili ", blank=True)
    instagram = models.URLField(verbose_name="Instagram manzili ", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.description
