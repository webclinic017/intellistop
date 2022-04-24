from .libs import (
    download_data, calculate_difference_momentum, calculate_momentum,
    ConfigProperties
)

class IntelliStop:
    config: ConfigProperties = {}
    data = {}
    fund_name = ""

    def __init__(self, config: dict = {}):
        self.config = ConfigProperties(config)

    def update_config(self, config: dict = {}):
        self.config = ConfigProperties(config)

    def fetch_data(self, fund: str):
        self.fund_name = fund
        self.data = download_data(fund, self.config)
        return self.data


    def calculate_stops(self):
        fund_momentum = calculate_difference_momentum(self.data[self.fund_name], self.config)
        fund_momentum2 = calculate_momentum(self.data[self.fund_name], self.config)
        print(f"stops {fund_momentum[14]}")
        print(f"momentum2 {fund_momentum2[14]}")
