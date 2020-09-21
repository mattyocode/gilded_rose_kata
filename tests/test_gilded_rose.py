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

# Sulfuras", being a legendary item, never has 
# to be sold or decreases in Quality

def test_sulfuras_dont_decrease_sell_in_or_quality(subject):
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=25, quality=80)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 25
    assert subject.items[0].quality == 80 

# "Backstage passes", like aged brie, increases in Quality 
# as its SellIn value approaches;
# - Quality increases by 2 when there are 10 days or less 
# and by 3 when there are 5 days or less but
# - Quality drops to 0 after the concert

def test_backstage_pass_quality_increase_by_1(subject):
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 19
    assert subject.items[0].quality == 11

def test_backstage_pass_quality_increase_by_2(subject):
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 9
    assert subject.items[0].quality == 12

def test_backstage_pass_quality_increase_by_3(subject):
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 0
    assert subject.items[0].quality == 13

def test_backstage_pass_quality_drops_to_0(subject):
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=50)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == -1
    assert subject.items[0].quality == 0

def test_backstage_pass_quality_not_above_50(subject):
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)]
    subject.items = items
    subject.update_quality()
    assert subject.items[0].sell_in == 4
    assert subject.items[0].quality == 50

# "Conjured" items degrade in Quality 
# twice as fast as normal items

