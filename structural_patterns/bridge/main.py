from charts import LineChart
from data_presentation import DataPresentation


if __name__ == "__main__":
    line_chart = LineChart()
    data_presentation = DataPresentation(line_chart)
    input_data = data_presentation.load_data_from_csv("structural_patterns/bridge/data.csv")
    sample_plot = data_presentation.draw_plot(input_data, "sample title", "sample xlabel", "sample ylabel")
    data_presentation.save_plot(sample_plot, "plots", "sample_plot")
