# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Leaderboard(models.Model):
    user_id = models.IntegerField()
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()


class LeaderboardArchive(models.Model):
    lb_id = models.IntegerField(db_index=True)
    user_id = models.IntegerField(db_index=True)
    score = models.IntegerField(db_index=True)
    rank = models.IntegerField(db_index=True)

    class Meta:
        unique_together = ('lb_id', 'user_id')
