import pandas as pd
import matplotlib.pyplot as plt

from charts import Chart


class DataPresentation():
    def __init__(self, chart: Chart):
        self._chart = chart

    def draw_plot(self, data: pd.DataFrame, title: str, x_label: str , y_label: str) -> plt.Figure:
        return self._chart.draw_plot(data, title, x_label , y_label)

    def save_plot(self, plot: plt.Figure, path: str, plot_name: str) -> None:
        return self._chart.save_plot(plot, path, plot_name)
    
    def load_data_from_csv(self, data_path: str) -> pd.DataFrame:
        """Method loads data"""
        data = pd.read_csv(data_path)
        return data
