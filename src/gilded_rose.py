# -*- coding: utf-8 -*-

class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Conjured":
                self.update_conjured(item)
            else:
                self.standard_update(item)

    def update_brie(self, item):
        if item.quality < 50 and item.sell_in > 0:
            item.quality += 1
        elif item.quality < 50 and item.sell_in <= 0:
            item.quality += 2
        self.reduce_sell_in(item)

    def update_backstage(self, item):
        if item.quality < 50 and item.sell_in >= 11:
            item.quality += 1
        elif item.quality < 50 and 5 < item.sell_in < 11:
            item.quality += 2
        elif item.quality < 50 and item.sell_in < 6:
            item.quality += 3
        self.reduce_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0

    def standard_update(self, item):
        if 0 < item.quality < 50:
            item.quality -= 1
        self.reduce_sell_in(item)

    def update_conjured(self, item):
        if 0 < item.quality < 50:
            item.quality -= 2
        self.reduce_sell_in(item)       

    def reduce_sell_in(self,item):
        item.sell_in -= 1

    def clear(self):
        self.items = None


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)