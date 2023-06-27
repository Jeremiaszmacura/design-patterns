"""Factory Method"""
import os
from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt


class Chart(ABC):
    """Chart class declares factory method that returns a chart objects."""

    @abstractmethod
    def draw_plot(self, data: pd.DataFrame, title: str, x_label: str , y_label: str) -> plt.Figure:
        """Method draws plot"""

    @abstractmethod
    def save_plot(self, plot: plt.Figure, path: str, plot_name: str) -> None:
        """Method saves plot"""


class LineChart(Chart):
    """Line implementation of Chart"""

    def draw_plot(self, data: pd.DataFrame, title: str, x_label: str , y_label: str) -> plt.Figure:
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.plot(data["AAPL_x"], data["AAPL_y"])
        return fig

    def save_plot(self, plot: plt.Figure, path: str, plot_name: str) -> None:
        current_path = os.path.dirname(os.path.abspath(__file__))
        directory_path = os.path.join(current_path, path)
        file_path = os.path.join(directory_path, plot_name)
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
        plot.savefig(file_path)


def load_data_from_csv(data_path: str) -> pd.DataFrame:
    """Method loads data"""
    data = pd.read_csv(data_path)
    return data


if __name__ == "__main__":
    input_data = load_data_from_csv("factory_method/data.csv")
    line_chart = LineChart()
    sample_plot = line_chart.draw_plot(input_data, "sample title", "sample xlabel", "sample ylabel")
    line_chart.save_plot(sample_plot, "plots", "sample_plot")
