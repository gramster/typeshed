from typing import Any, Dict, List, Optional, Tuple, Union

from .core import DataFrame, Series, Index

import matplotlib
import numpy as np

def andrews_curves(
    frame: DataFrame,
    class_column: str,
    ax: Optional[matplotlib.axes.Axes] = ...,
    samples: int = ...,
    color: Optional[Union[List[str], Tuple[str]]] = ...,
    colormap: Any = ...,
) -> matplotlib.axes.Axes: ...
def autocorrelation_plot(series: Series, ax: Optional[matplotlib.axes.Axes] = ...,) -> matplotlib.axes.Axes: ...
def bootstrap_plot(
    series: Series, fig: Optional[matplotlib.pyplot.Figure] = ..., size: int = ..., samples: int = ...,
) -> matplotlib.pyplot.Figure: ...
def boxplot(
    data: DataFrame,
    column: Optional[Union[str, List[str]]] = ...,
    by: Optional[Union[str, List[str]]] = ...,
    ax: Optional[matplotlib.axes.Axes] = ...,
    fontsize: Optional[Union[float, str]] = ...,
    rot: float = ...,
    grid: bool = ...,
    figsize: Optional[Tuple[float, float]] = ...,
    layout: Optional[Tuple[int, int]] = ...,
    return_type: Optional[str] = ...,
) -> Any: ...
def deregister_matplotlib_converters() -> None: ...
def lag_plot(series: Series, lag: int = ..., ax: Optional[matplotlib.axes.Axes] = ...,) -> matplotlib.axes.Axes: ...
def parallel_coordinates(
    frame: DataFrame,
    class_column: str,
    cols: Optional[List[str]] = ...,
    ax: Optional[matplotlib.axes.Axes] = ...,
    color: Optional[Union[List[str], Tuple[str]]] = ...,
    use_columns: bool = ...,
    xticks: Optional[Union[List, Tuple]] = ...,
    colormap: Any = ...,
    axvlines: bool = ...,
    axvlines_kwds: Any = ...,
    sort_labels: bool = ...,
) -> matplotlib.axes.Axes: ...
def table(ax, data, rowLabels=None, colLabels=None,) -> Any: ...  # table
def radviz(
    frame: DataFrame,
    class_column: str,
    ax: Optional[matplotlib.axes.Axes] = ...,
    color: Optional[Union[List[str], Tuple[str]]] = ...,
    colormap: Any = ...,
) -> matplotlib.axes.Axes: ...
def register_matplotlib_converters() -> None: ...
def scatter_matrix(
    frame: DataFrame,
    alpha: float = ...,
    figsize: Optional[Tuple[float, float]] = ...,
    ax: Optional[matplotlib.axes.Axes] = ...,
    grid: bool = ...,
    diagonal: str = ...,
    marker: str = ...,
    density_kwds: Any = ...,
    hist_kwds: Any = ...,
    range_padding: float = ...,
) -> np.ndarray: ...

plot_params: Dict[str, Any]
