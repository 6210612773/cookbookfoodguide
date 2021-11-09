from django.db import models

# Create your models here.
# class petition (models.Model):
#     user=models.ForeignKey(User,default=None, on_delete=models.PROTECT)
#     petition = models.TextField(blank=True)
#     date_added =models.DateTimeField(auto_now_add=True)
#     class status(models.TextChoices):
#         no = "no"
#         confirm = "confirm"
#     confirm = models.CharField(max_length=10,
#         choices=status.choices,
#         default=status.confirm.no,
#         )
#     def __str__(self) -> str:
#         return f"{self.user,self.date}"