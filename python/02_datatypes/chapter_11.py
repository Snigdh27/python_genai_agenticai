import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/London")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile",["flavour","aroma"])
print(chaiProfile(flavour="spicy",aroma="strong"))