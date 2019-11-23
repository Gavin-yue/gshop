from django.db import models

# Create your models here.
class Type(models.Model):
    class Meta():
        verbose_name = "商品类型"
        verbose_name_plural = "商品类型"
    type_name = models.CharField(max_length=50,verbose_name = '商品类别名称')
    date = models.DateTimeField(auto_now_add = True,verbose_name = '更新时间')
    def __str__(self):
        return self.type_name


class Manager(models.Model):
    class Meta():
        verbose_name = "商家"
        verbose_name_plural = "商家"
    manager_name = models.CharField(max_length=50,verbose_name='商家姓名')
    email = models.EmailField("商家邮箱")
    password = models.CharField(max_length=32,verbose_name="商家密码")
    image = models.ImageField(upload_to='media/manage/image',default="https://source.unsplash.com/QAB-WJcbgJk/60x60")
    is_login = models.BooleanField(default=0)