"""Factory Method"""
from abc import ABC, abstractmethod


class Plot(ABC):
    """Plot class declares factory method that returns an Plot objects."""

    @abstractmethod
    def draw_plot(self):
        """Method draws plot"""
        ...

