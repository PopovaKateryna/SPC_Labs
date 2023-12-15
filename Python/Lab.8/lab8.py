import pandas as pd
import matplotlib.pyplot as plt
import logging

class DataVisualizer:
    def __init__(self, csv_file):
        try:
            self.data = pd.read_csv(csv_file, delimiter=';')
        except FileNotFoundError as e:
            print(f"Помилка: файл '{csv_file}' не знайдено.")
            logging.error(f"Помилка: файл '{csv_file}' не знайдено.")
            self.data = None

    def describe_data(self):
        if self.data is not None:
            return self.data.describe()
        else:
            print("Дані не завантажено.")
            return None

    def find_extremes(self, column):
        if self.data is not None and column in self.data.columns:
            min_value = self.data[column].min()
            max_value = self.data[column].max()
            print(f"Мінімальне значення в стовпці '{column}': {min_value}")
            print(f"Максимальне значення в стовпці '{column}': {max_value}")
            return min_value, max_value
        else:
            print(f"Стовпець '{column}' не знайдено.")
            return None, None

    def plot_line_chart(self, x, y):
        if self.data is not None and self._check_columns(x, y):
            plt.figure()
            plt.plot(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'{y} over {x}')
            plt.grid(True)
            plt.show(block=True)

    def plot_bar_chart(self, x, y):
        if self.data is not None and self._check_columns(x, y):
            plt.figure()
            plt.bar(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'{y} by {x}')
            plt.show(block=True)

    def multiple_subplots(self, x, y):
        if self.data is not None and self._check_columns(x, y):
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            ax[0].plot(self.data[x], self.data[y])
            ax[0].set_title(f'Line Chart: {y} over {x}')
            ax[1].bar(self.data[x], self.data[y], color='orange')
            ax[1].set_title(f'Bar Chart: {y} by {x}')
            plt.tight_layout()
            plt.show(block=True)

    def _check_columns(self, x, y):
        if x not in self.data.columns or y not in self.data.columns:
            print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
            logging.error(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
            return False
        return True

def main():
    visualizer = DataVisualizer('/Users/popovakatusha/LPNU/3 курс/Спеціалізовані мови програмування/Python/Lab.8/table.csv')
    if visualizer.describe_data() is not None:
        visualizer.find_extremes('Score')
        visualizer.find_extremes('Year')
        visualizer.plot_line_chart('Score', 'Year')
        visualizer.plot_bar_chart('Score', 'Year')
        visualizer.multiple_subplots('Score', 'Year')

if __name__ == '__main__':
    main()