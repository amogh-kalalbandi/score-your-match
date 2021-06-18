"""Match related models."""

from django.db import models


class Country(models.Model):
    """Model to store country name."""

    name = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data."""

        app_label = 'match'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Venue(models.Model):
    """Model to Store Venue data."""

    name = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    capacity = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data."""

        app_label = 'match'
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'


class Team(models.Model):
    """Model to store Team playing cricket."""

    # LEAGUE_CHOICES = (
    #     ('Indian Primere League', 'IPL'),
    #     ('Big Bash', 'BB'),
    #     ('Pakistan Super League', 'PSL'),
    #     ('The Hundred', 'TH'),
    #     ('Vitality Blast', 'VB'),
    #     ('Ranji Trophy', 'RH'),
    #     ('Sheffield Shield', 'SH'),
    #     ('Carribean Primere League', 'CPL'),
    #     ('International', 'IN')
    # )

    name = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # associated_league_name = models.CharField(
    #     max_length=255,
    #     null=True,
    #     choices=LEAGUE_CHOICES
    # )
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data."""

        app_label = 'match'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Player(models.Model):
    """Model to store player data."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=255)
    batting_type = models.CharField(max_length=255)
    bowling_type = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data."""

        app_label = 'match'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class Match(models.Model):
    """Model to Store Venue data."""

    match_id = models.IntegerField(null=True)
    season = models.CharField(max_length=255, null=True)
    start_date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    innings = models.IntegerField()
    balls = models.FloatField()
    batting_team = models.ForeignKey(Team, related_name='batting_team', on_delete=models.CASCADE)
    bowling_team = models.ForeignKey(Team, related_name='bowling_team', on_delete=models.CASCADE)
    striker = models.ForeignKey(Player, related_name='striker', on_delete=models.CASCADE)
    non_striker = models.ForeignKey(Player, related_name='non_striker', on_delete=models.CASCADE)
    bowler = models.ForeignKey(Player, related_name='bowler', on_delete=models.CASCADE)
    runs_off_bat = models.IntegerField()
    extras = models.IntegerField()
    wides = models.IntegerField()
    noballs = models.IntegerField()
    byes = models.IntegerField()
    legbyes = models.IntegerField()
    penalty = models.IntegerField()
    wicket_type = models.CharField(max_length=255, null=True)
    player_dismissed = models.CharField(max_length=255, null=True)
    other_wicket_type = models.CharField(max_length=255, null=True)
    other_player_dismissed = models.ForeignKey(
        Player,
        related_name='other_player_dismisse',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta Data."""

        app_label = 'match'
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
