from django.db import models
from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo
from apps.node_mgmt.models.cloud_region import CloudRegion


class EnvVariable(TimeInfo, MaintainerInfo):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    description = models.TextField(blank=True, verbose_name="描述")
    cloud_region = models.ForeignKey(CloudRegion, on_delete=models.CASCADE, verbose_name="云区域")

    class Meta:
        verbose_name = "环境变量"
        db_table = "env_variable"
        verbose_name_plural = "环境变量"
        unique_together = ('key', 'cloud_region')
