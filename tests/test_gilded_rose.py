# -*- coding: utf-8 -*-
import unittest
import pytest

from src.gilded_rose import Item, GildedRose

@pytest.fixture
def subject():
    subject = GildedRose([])
    yield subject
    subject.clear()

def test_has_name(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    assert "+5 Dexterity Vest" == subject.items[0].name

def test_has_sellin(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    assert 10 == subject.items[0].sell_in

def test_has_quality(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    assert 20 == subject.items[0].quality

def test_update_quality_lowers_quality_by_1(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].quality == 19

def test_update_quality_lowers_sell_in_by_1(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 9

def test_update_quality_x2_lowers_sell_in_by_2(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    subject.items = items
    subject.update_quality()
    subject.update_quality()
    assert subject.items[0].sell_in == 8

def test_quality_not_below_zero(subject):
    items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=0)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].quality == 0

def test_aged_brie_increases_in_quality(subject):
    items = [Item(name="Aged Brie", sell_in=2, quality=0)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].quality == 1

def test_quality_not_above_50(subject):
    items = [Item(name="Aged Brie", sell_in=2, quality=50)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].quality == 50


# At the end of each day our system lowers both 
# values for every item