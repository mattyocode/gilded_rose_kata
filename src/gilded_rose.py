# -*- coding: utf-8 -*-
class GildedRose:

    def __init__(self, items):
        self.items = items
        self.assigner = ItemAssigner()

    def item_to_class(self, items):
        items_reclassed = []
        for item in items:
            item = self.assigner.assign_class(item.name, item.sell_in, item.quality)
            items_reclassed.append(item)
        return items_reclassed

    def update_quality(self):
        self.items = self.item_to_class(self.items)
        for item in self.items:
            item.update_quality()

    def clear(self):
        self.items = None

class ItemAssigner:

    def assign_class(self, name, sell_in, quality):
        if name == "Aged Brie":
            return Brie(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Conjured":
            return Conjured(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def update_quality(self):
        if 0 < self.quality < 50:
            self.quality -= 1
        self.sell_in -= 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Conjured(Item):

    def update_quality(self):
        if 0 < self.quality < 50:
            self.quality -= 2
        self.sell_in -= 1 

class Brie(Item):
    
    def update_quality(self):
        if self.quality < 50 and self.sell_in > 0:
            self.quality += 1
        elif self.quality < 50 and self.sell_in <= 0:
            self.quality += 2
        self.sell_in -= 1

class Backstage(Item):
    
    def update_quality(self):
        if self.quality < 50 and self.sell_in >= 11:
            self.quality += 1
        elif self.quality < 50 and 5 < self.sell_in < 11:
            self.quality += 2
        elif self.quality < 50 and self.sell_in < 6:
            self.quality += 3
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0

class Sulfuras(Item):
    
    def update_quality(self):
        self.quality = 80