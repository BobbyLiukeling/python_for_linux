from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser


class CRISPR_DATABASE(models.Model):

    '''
    CRISPR 类型选择（暂时没有具体的类型，先用1,2,3,4 代替）
    '''

    CRISPR_Type_Choices = (
        ('一型','第一种类型'),
        ('二型','第二种类型'),
        ('三型', '第三种类型'),
        ('四型', '第四种类型'),
    )

    CRISPR = models.TextField(null = True, blank = True, verbose_name= "CRISPR 序列")
    CRISPR_name = models.CharField(ｍａx_length = 50,null = True, blank = True,verbose_name='CRISPR 名字')
    PI = models.TextField(null = True, blank = True, verbose_name= "PI 序列")
    CRISPR_type = models.CharField(max_length=50,null = True, blank = True, verbose_name= 'CRISPR 类型 ',choices=CRISPR_Type_Choices)
    PAM = models.CharField(max_length=50,null = True, blank = True, verbose_name= 'PAM 序列')

    class Meta:
        verbose_name = 'CRISPR' #备注数据名称
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name