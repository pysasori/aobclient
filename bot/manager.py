import effortless


class Manager:
    """Клас-менеджер для зберігання та управління динамічними даними."""

    def __init__(self):
        self.image_searcher = effortless.ImageSearcher(threshold=0.84)  # Один екземпляр для всього застосунку
        self.mouse_controller = effortless.MouseController()  # Один екземпляр для всього застосунку
        self.text_extractor = effortless.TextExtractor()
        self.time_sleep_from = 0
        self.time_sleep_to = 0
        self.start_cord = [0,0]
        self.back_row_cord = [0,0]
        self.amount_lots = None
        self.main_list = []
        self.remove_list = []
        self.actual_lot = None
        self.sell_price = None
        self.buy_price = None
        self.buy_order_cord = []
        self.error_count = 0

    def search_image(self, image_path, cords=None, search_time=5):
        return self.image_searcher.search_image(image_path, cords, search_time)

    def checking_image(self, image_path, cords):
        return self.image_searcher.checking_image(image_path, cords)

    def scan_prices(self, cords):
        return self.text_extractor.scan_prices(cords)

    def amount_money(self, cords):
        return self.text_extractor.read_text(cords)


