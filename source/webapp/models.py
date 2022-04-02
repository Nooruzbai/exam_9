from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Image(models.Model):
    image = models.ImageField(verbose_name="Image", upload_to="images/", null=False, blank=False)
    sign = models.CharField(max_length=100, null=False, blank=False, verbose_name="Sign")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    author = models.ForeignKey(User, null=False, blank=False, related_name='image_s', on_delete=models.CASCADE,
                               verbose_name='Author')
    gallery = models.ForeignKey('webapp.Gallery', blank=True, on_delete=models.CASCADE, null=True, related_name="images")
    private = models.BooleanField(default=False, verbose_name="Private")
    favourite = models.ManyToManyField(User, related_name="images")
    token = models.UUIDField(blank=True, null=True, verbose_name='token')

    def __str__(self):
        return f"{self.pk}. {self.author} {self.date_created}"

    class Meta:
        db_table = "image"
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Gallery(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Name")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Description")
    author = models.ForeignKey(User, null=False, blank=False, related_name="gallerie_s", on_delete=models.CASCADE,
                               verbose_name="Author")
    private = models.BooleanField(default=False, verbose_name="Private")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    favourite = models.ManyToManyField(User, related_name="Galleries")

    def __str__(self):
        return f"{self.pk}. {self.name} {self.author} {self.date_created}"

    class Meta:
        db_table = "gallery"
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"


