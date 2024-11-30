class Item:
    def __init__(self, icon, max_item_count: int,
                 min_item_count: int = 0, current_value: int = 0) -> None:
        self.icon = icon
        self.min_value = min_item_count
        self.max_value = max_item_count
        self.current_value = current_value

    @property
    def info_stat(self) -> str:
        return f'{self.icon} {self.min_value}/{self.current_value}/{self.max_value}'

    @property
    def in_min_max(self) -> bool:
        return self.min_value < self.current_value <= self.max_value

    @property
    def is_less_or_equal_than_min(self) -> bool:
        return self.current_value <= self.min_value

    @property
    def is_higher_or_equal_than_max(self) -> bool:
        return self.current_value >= self.max_value


class Statistic:
    def __init__(self, *items: Item) -> None:
        self.items = items

    @property
    def info_stats(self) -> str:
        return ' | '.join(item.info_stat for item in self.items)