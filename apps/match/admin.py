"""Admin.py files to register match models."""

from django.contrib import admin
from apps.match.models import (
    Country,
    Venue,
    Team,
    Player,
    Match
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Country Admin model."""


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    """Venue Admin model."""


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Team Admin model."""


class PlayerAdmin(admin.ModelAdmin):
    """Player Admin model."""


class MatchAdmin(admin.ModelAdmin):
    """Match Admin model."""

admin.site.register(Player)
admin.site.register(Match)
