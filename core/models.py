from django.db import models
from django.utils import timezone


class BasedModel(models.Model):
    """
    抽象基类，用于封装创建时间和更新时间字段
    """
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="创建时间",
        editable=False
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="更新时间",
        editable=False
    )

    is_effective = models.BooleanField(
        default=True,
        verbose_name="是否生效"
    )
    remark = models.TextField(
        blank=True,
        null=True,
        verbose_name="备注"
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        重写 save 方法，确保更新时间在每次保存时自动更新
        """
        if not self.id:  # 如果是新创建的对象
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

