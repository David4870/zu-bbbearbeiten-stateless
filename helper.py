from dataclasses import dataclass
import datetime
import operator

items = []


@dataclass
class Item:
    text: str
    date: datetime.date
    isCompleted: bool = False


def add(text, date):
    if text == "":
        text = "Todo"
    if len(date) == 0:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    text = text.replace("b", "bbb").replace("B", "Bbb")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    items.append(Item(text, date))
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

def delete(index):
    items.pop(index)
