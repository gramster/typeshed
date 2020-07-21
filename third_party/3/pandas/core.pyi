from __future__ import annotations  # So we don't have to quote forward refs
import datetime
import sys

from typing import (
    Any,
    AnyStr,
    Callable,
    Dict,
    Generator,
    Generic,
    Hashable,
    IO,
    Iterable,
    Iterator,
    List,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol
else:
    from typing_extensions import Literal, Protocol

import numpy as _np
import datetime as _dt
from pathlib import Path
import matplotlib

_str = str  # needed because Series/DataFrame have properties called "str"...
_bool = bool  # ditto
num = Union[int, float]

_SeriesAxisType = Literal["index", 0]  # Restricted subset of _AxisType for series
_AxisType = Literal["columns", "index", 0, 1]
_DType = TypeVar("_DType", bool, int, float, object)
_DTypeNp = TypeVar("_DTypeNp", bound=_np.dtype)
# _ListLike = TypeVar("ListLike", List, Tuple, Set, _np.ndarray, Series)
_StrLike = Union[str, _np.str_]
_Path_or_Buf = Union[str, Path, IO]
_LevelType = Union[int, str]
_Scalar = Union[str, bytes, _dt.date, _dt.datetime, _dt.timedelta, bool, int, float, complex]
# Refine the next 3 in 3.9 to use the specialized type.
_np_ndarray_int64 = NewType("_np_ndarray_int64", _np.ndarray)
_np_ndarray_bool = NewType("_np_ndarray_bool", _np.ndarray)
_np_ndarray_str = NewType("_np_ndarray_str", _np.ndarray)

class StringMethods:
    def contains(
        self, pat: str, case: bool = ..., flags: int = ..., na: float = ..., regex: bool = ...,
    ) -> Series[bool]: ...

_T = TypeVar("_T", str, int)
_U = TypeVar("_U", str, int)

class Int8Dtype(object): ...
class Int16Dtype(object): ...
class Int32Dtype(object): ...
class Int64Dtype(object): ...
class UInt8Dtype(object): ...
class UInt16Dtype(object): ...
class UInt32Dtype(object): ...
class UInt64Dtype(object): ...
class BooleanDtype(object): ...
class StringDtype(object): ...

class SparseDtype(object):
    def __init__(self, dtype: Any = ..., fill_value: Optional[_Scalar] = ...): ...

class CategoricalDtype(object):
    def __init__(self, categories: Optional[Sequence] = ..., ordered: bool = ...): ...
    @property
    def categories(self) -> Index: ...
    @property
    def ordered(self) -> bool: ...

class Timestamp(object):
    def __init__(
        self,
        ts_input: Any,
        freq: Any,
        tz: Any,
        unit: str,
        year: int,
        month: int,
        day: int,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        nanosecond: int = ...,
        tzinfo: Any = ...,
    ): ...
    # Still need to do parameter types
    @property
    def asm8(self) -> int: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def daysinmonth(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def freqstr(self) -> int: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def is_month_end(self) -> bool: ...
    @property
    def is_month_start(self) -> bool: ...
    @property
    def is_quarter_end(self) -> bool: ...
    @property
    def is_quarter_start(self) -> bool: ...
    @property
    def is_year_end(self) -> bool: ...
    @property
    def is_year_start(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    @property
    def tz(self) -> Any: ...
    @property
    def week(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...
    # Class methods
    @staticmethod
    def combine(date, time) -> Timestamp: ...
    @staticmethod
    def fromordinal(ordinal: int, freq: Any = ..., tz: Any = ...) -> Timestamp: ...
    @staticmethod
    def fromtimestamp(ts) -> Timestamp: ...
    @staticmethod
    def now(tz: Any) -> Timestamp: ...
    @staticmethod
    def today(tz: Any) -> Timestamp: ...
    @staticmethod
    def utcfromtimestamp(ts) -> Timestamp: ...
    @staticmethod
    def utcnow() -> Timestamp: ...
    # Methods
    def astimezone(self, tz: Any) -> Timestamp: ...
    def ceil(self, freq: str, ambiguous: str = ..., nonexistent: str = ...) -> Timestamp: ...
    def ctime(self) -> str: ...
    def date(self) -> Any: ...
    def day_name(self, local: Optional[str] = ...) -> str: ...
    def dst(self) -> Timestamp: ...
    def floor(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def fromisoformat(self) -> Any: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...
    def isoweekday(self) -> int: ...
    def monthname(self, local: Any) -> str: ...
    def normalize(self) -> None: ...
    def replace(
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        hour: Optional[int] = ...,
        minute: Optional[int] = ...,
        second: Optional[int] = ...,
        microsecond: Optional[int] = ...,
        nanosecond: Optional[int] = ...,
        tzinfo: Any = ...,
        fold: int = ...,
    ) -> Timestamp: ...
    def round(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def strftime(self) -> str: ...
    def time(self) -> Timestamp: ...
    def timestamp(self) -> float: ...
    def timetuple(self) -> Tuple: ...
    def timetz(self) -> Timestamp: ...
    def to_datetime64(self) -> _np.datetime64: ...
    def to_julian_date(self) -> Any: ...
    def to_numpy(self) -> _np.datetime64: ...
    def to_period(self, freq: Optional[str] = ...) -> Any: ...
    def to_pydatetime(self) -> datetime.datetime: ...
    def toordinal(self) -> Any: ...
    def tz_convert(self, tz: Any) -> Timestamp: ...
    def tz_localize(self, tz: Any, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def tzname(self) -> str: ...
    def utcoffset(self) -> Any: ...
    def utctimetuple(self) -> Any: ...
    def weekday(self) -> int: ...

class Timedelta(object):
    def __init__(self, value: Any, unit: str = ..., **kwargs): ...
    @property
    def asm8(self) -> int: ...
    @property
    def components(self) -> int: ...
    @property
    def days(self) -> int: ...
    @property
    def delta(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    @property
    def nanoseconds(self) -> int: ...
    @property
    def resolution_string(self) -> str: ...
    @property
    def seconds(self) -> int: ...
    max: Timedelta
    min: Timedelta
    resolution: Timedelta
    def ceil(self, freq, **kwargs) -> Timedelta: ...
    def floor(self, freq, **kwargs) -> Timedelta: ...
    def isoformat(self) -> str: ...
    def round(self, freq) -> Timedelta: ...
    def to_numpy(self) -> _np.timedelta64: ...
    def to_pytimedelta(self) -> datetime.timedelta: ...
    def to_timedelta64(self) -> _np.timedelta64: ...
    def total_seconds(self) -> int: ...

class Period(object):
    def __init__(
        self,
        value: Any = ...,
        freqstr: Any = ...,
        ordinal: Any = ...,
        year: Any = ...,
        month: int = ...,
        quarter: Any = ...,
        day: int = ...,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
    ): ...
    @property
    def day(self) -> int: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def end_time(self) -> Timestamp: ...
    @property
    def freq(self) -> Any: ...
    @property
    def freqstr(self) -> str: ...
    @property
    def hour(self) -> int: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def minute(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def ordinal(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    @property
    def qyear(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def start_time(self) -> Timestamp: ...
    @property
    def week(self) -> int: ...
    @property
    def weekday(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...
    @property
    def year(self) -> int: ...
    # Static methods
    @staticmethod
    def now() -> Period: ...
    # Methods
    def asfreq(self, freq: str, how: str = ...) -> Period: ...
    def strftime(self, fmt: str) -> str: ...
    def to_timestamp(self, freq: str, how: str = ...) -> Timestamp: ...

class Interval(object):
    def __init__(self, left: _Scalar, right: _Scalar, closed: str = ...): ...
    @property
    def closed(self) -> bool: ...
    @property
    def closed_left(self) -> bool: ...
    @property
    def closed_right(self) -> bool: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def left(self) -> _Scalar: ...
    @property
    def length(self) -> _Scalar: ...
    @property
    def mid(self) -> _Scalar: ...
    @property
    def open_left(self) -> bool: ...
    @property
    def open_right(self) -> bool: ...
    @property
    def right(self) -> _Scalar: ...
    # Methods
    def overlaps(self, other: Interval) -> bool: ...

class Categorical(object):
    def __init__(
        self,
        values: List,
        categories: Any = ...,
        ordered: bool = ...,
        dtype: Optional[CategoricalDtype] = ...,
        fastpath: bool = ...,
    ): ...
    @property
    def categories(self) -> Any: ...
    @property
    def codes(self) -> List[int]: ...
    @property
    def ordered(self) -> bool: ...
    @property
    def dtype(self) -> CategoricalDtype: ...
    # Static Methods
    @staticmethod
    def from_codes(
        codes: List[int],
        categories: Optional[Index] = ...,
        ordered: bool = ...,
        dtype: Optional[CategoricalDtype] = ...,
    ) -> Categorical: ...

class Index(Generic[_T]):

    # magic methods
    def __init__(
        self, data: Iterable[_T], dtype: Any = ..., copy: bool = ..., name: Any = ..., tupleize_cols: bool = ...,
    ): ...
    def __eq__(self, other: object) -> Series: ...  # type: ignore
    @overload
    def __getitem__(self, idx: Union[int, Series[bool], slice, _np_ndarray_int64]) -> _T: ...
    @overload
    def __getitem__(self, idx: Index[_T]) -> Index[_T]: ...
    @overload
    def __getitem__(self, idx: Tuple[_np_ndarray_int64, ...]) -> _T: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: str) -> Index[_T]: ...  # type: ignore
    #
    # properties
    @property
    def has_duplicates(self) -> bool: ...
    @property
    def has_nans(self) -> bool: ...
    @property
    def is_all_dates(self) -> bool: ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def names(self) -> List[_str]: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    @property
    def str(self) -> StringMethods: ...
    @property
    def values(self) -> Union[_np_ndarray_str, _np_ndarray_int64]: ...
    #
    # methods
    @overload
    def astype(self, dtype: Type[_U]) -> Index[_U]: ...
    @overload
    def astype(self, dtype: _str) -> Index: ...
    def difference(self, other: Union[List[_T], Index[_T]]) -> Index[_T]: ...
    def get_level_values(self, level: _str) -> Index: ...
    def map(self, fn: Callable) -> Index: ...
    def to_frame(self, index: bool = ..., name: Any = ...) -> DataFrame: ...
    def tolist(self) -> List[_T]: ...
    @overload
    def to_numpy(self: Index[_str]) -> _np_ndarray_str: ...
    @overload
    def to_numpy(self: Index[int]) -> _np_ndarray_int64: ...

class Int64Index(Index[_np.int64]): ...
class UInt64Index(Index[_np.uint64]): ...
class Float64Index(Index[_np.float64]): ...
class RangeIndex(Int64Index): ...
class CategoricalIndex(Index[CategoricalDtype]): ...
class IntervalIndex(Index[Any]): ...
class MultiIndex(Index[Any]): ...
class DatetimeIndex(Index[Any]): ...
class TimedeltaIndex(Index[Any]): ...
class PeriodIndex(Index[Any]): ...

class Series(Generic[_DType]):

    _ListLike = Union[_np.ndarray, List[_DType], Dict[_str, _np.ndarray], Sequence, Index]
    def __init__(
        self,
        data: Optional[Union[_ListLike[_DType], Series[_DType], Dict[int, _DType], Dict[_str, _DType]]] = ...,
        index: Union[_str, int, Series, List] = ...,
        dtype: Any = ...,
        name: _str = ...,
        copy: bool = ...,
    ): ...
    # dunder methods
    def __abs__(self) -> Series[_DType]: ...
    def __add__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __and__(self, other: Union[_ListLike, Series[_DType]]) -> Series[_bool]: ...
    # def __array__(self, dtype: Optional[_bool] = ...) -> _np_ndarray
    def __delitem__(self, idx: Union[int, _str]): ...
    def __div__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __eq__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __floordiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[int]: ...
    def __ge__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    @overload
    def __getitem__(self, idx: Union[List[_str], Index[int], Series[_DType], slice]) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[int, _str]) -> _DType: ...
    def __gt__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    # def __iadd__(self, other: _DType) -> Series[_DType]: ...
    # def __iand__(self, other: _DType) -> Series[_bool]: ...
    # def __idiv__(self, other: _DType) -> Series[_DType]: ...
    # def __ifloordiv__(self, other: _DType) -> Series[_DType]: ...
    # def __imod__(self, other: _DType) -> Series[_DType]: ...
    # def __imul__(self, other: _DType) -> Series[_DType]: ...
    # def __ior__(self, other: _DType) -> Series[_bool]: ...
    # def __ipow__(self, other: _DType) -> Series[_DType]: ...
    # def __isub__(self, other: _DType) -> Series[_DType]: ...
    # def __itruediv__(self, other: _DType) -> Series[_DType]: ...
    def __iter__(self) -> Iterator: ...
    # def __itruediv__(self, other: Any) -> None: ...
    # def __ixor__(self, other: _DType) -> Series[_bool]: ...
    def __le__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __mul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __mod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __ne__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __neg__(self) -> None: ...
    def __pow__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __or__(self, other: Union[_ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __radd__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rand__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __rdiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rdivmod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rfloordiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rmod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rmul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rnatmul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rpow__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __ror__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __rsub__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rtruediv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rxor__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __sub__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __truediv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __xor__(self, other: Union[_ListLike, Series[_DType]]) -> Series: ...
    # properties
    # @property
    # def array(self) -> _npndarray
    @property
    def at(self) -> _LocIndexerSeries[_DType]: ...
    @property
    def axes(self) -> List: ...
    # @property
    # def cat(self) -> ?
    @property
    def dt(self) -> Series: ...
    @property
    def dtype(self) -> _DType: ...
    @property
    def dtypes(self) -> _DType: ...
    @property
    def hasnans(self) -> bool: ...
    @property
    def iat(self) -> _iLocIndexerSeries[_DType]: ...
    @property
    def iloc(self) -> _iLocIndexerSeries[_DType]: ...
    @property
    def index(self) -> Index: ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def loc(self) -> _LocIndexerSeries[_DType]: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> Tuple: ...
    @property
    def size(self) -> int: ...
    @property
    def values(self) -> _np.ndarray: ...
    @property
    def T(self) -> Series[_DType]: ...
    # Methods
    def abs(self) -> Series[_DType]: ...
    def add(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Literal[0] = ...,
    ) -> Series[_DType]: ...
    def add_prefix(self, prefix: _str) -> Series[_DType]: ...
    def add_suffix(self, suffix: _str) -> Series[_DType]: ...
    def aggregate(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[_SeriesAxisType, Union[Callable, _str]],],
        axis: _SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def agg(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[_SeriesAxisType, Union[Callable, _str]],],
        axis: _SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def align(
        self,
        other: Union[DataFrame, Series[Any]],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: _SeriesAxisType = ...,
        broadcast_axis: Optional[_SeriesAxisType] = ...,
    ) -> Tuple[Series, Series]: ...
    def all(
        self,
        axis: _SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        **kwargs
    ) -> _bool: ...
    def any(
        self,
        axis: _SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        **kwargs
    ) -> _bool: ...
    def append(
        self,
        to_append: Union[Series[Any], Sequence[Series[Any]]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
    ) -> Series[_DType]: ...
    def apply(
        self, func: Callable, convert_dtype: _bool = ..., args: Tuple = ..., **kwds
    ) -> Union[Series[Any], DataFrame]: ...
    def argmax(self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> _np.ndarray: ...
    def argmin(self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> _np.ndarray: ...
    def argsort(
        self,
        axis: _SeriesAxisType = ...,
        kind: Literal["mergesort", "quicksort", "heapsort"] = ...,
        order: None = ...,
    ) -> Series[int]: ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[_Scalar] = ...,
    ) -> Series[_DType]: ...
    def asof(
        self, where: Union[_Scalar, Sequence[_Scalar]], subset: Optional[Union[_str, Sequence[_str]]] = ...,
    ) -> Union[_Scalar, Series[_DType]]: ...
    def astype(
        self,
        dtype: Union[Type[_str], Type[int], Type[float]],
        copy: _bool = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> Series: ...
    def at_time(
        self, time: Union[_str, datetime.time], asof: _bool = ..., axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def autocorr(self, lag: int = ...) -> float: ...
    def between(
        self, left: Union[_Scalar, Sequence], right: Union[_Scalar, Sequence], inclusive: _bool = ...,
    ) -> Series[_bool]: ...
    def between_time(
        self,
        start_time: Union[_str, datetime.time],
        end_time: Union[_str, datetime.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    @overload
    def bfill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[_DType]: ...
    @overload
    def bfill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    def bool(self) -> _bool: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> Series[_DType]: ...
    def combine(
        self, other: Series[_DType], func: Callable, fill_value: Optional[_Scalar] = ...
    ) -> Series[_DType]: ...
    def combine_first(self, other: Series[_DType]) -> Series[_DType]: ...
    def convert_dtypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert_boolean: _bool = ...,
    ) -> Series[_DType]: ...
    def copy(self, deep: _bool = ...) -> Series[_DType]: ...
    def corr(
        self, other: Series[_DType], method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,
    ) -> float: ...
    @overload
    def count(self, level: None = ...) -> int: ...
    @overload
    def count(self, level: _LevelType) -> Series[_DType]: ...
    def cov(self, other: Series[_DType], min_periods: Optional[int] = ...) -> float: ...
    def cummax(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cummin(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cumprod(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cumsum(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[_DType]]] = ...,
        exclude: Optional[List[_DType]] = ...,
    ) -> Series[_DType]: ...
    def diff(self, periods: int = ...) -> Series[_DType]: ...
    def div(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    def divide(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    def divmod(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    @overload
    def dot(self, other: Union[DataFrame, Series[_DType]]) -> Series[_DType]: ...
    @overload
    def dot(self, other: _ListLike) -> _np.ndarray: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: _SeriesAxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[_LevelType] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> Series: ...
    def drop_duplicates(self, keep: Literal["first", "last", False] = ..., inplace: _bool = ...) -> Series[_DType]: ...
    def droplevel(self, level: _LevelType, axis: _SeriesAxisType = ...) -> DataFrame: ...
    def dropna(
        self, axis: _SeriesAxisType = ..., inplace: _bool = ..., how: Optional[_str] = ...,
    ) -> Series[_DType]: ...
    def duplicated(self, keep: Literal["first", "last", False] = ...) -> Series[_bool]: ...
    def eq(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def equals(self, other: Series[_DType]) -> _bool: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: _SeriesAxisType = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: _SeriesAxisType = ...) -> DataFrame: ...
    def explode(self) -> Series[_DType]: ...
    def factorize(
        self, sort: _bool = ..., na_sentinel: int = ...
    ) -> Tuple[_np.ndarray, Union[_np.ndarray, Index, object]]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType,
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[_DType]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[_DType]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    @overload
    def fillna(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: _SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[_DType]: ...
    @overload
    def fillna(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    def filter(
        self,
        items: Optional[_ListLike] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def first(self, offset: Any) -> Series[_DType]: ...
    def first_valid_index(self) -> _Scalar: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[int]: ...
    def ge(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def get(self, key: object, default: Optional[_DType] = ...) -> _DType: ...
    def groupby(
        self,
        by: Optional[Any] = ...,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> SeriesGroupBy: ...
    def gt(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def head(self, n: int = ...) -> Series[_DType]: ...
    def hist(
        self,
        by: Optional[object] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> matplotlib.axes.SubplotBase: ...
    def idxmax(self, axis: _SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def idxmin(self, axis: _SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def infer_objects(self) -> Series[_DType]: ...
    def interpolate(
        self,
        method: Literal[
            "linear",
            "time",
            "index",
            "values",
            "pad",
            "nearest",
            "slinear",
            "quadratic",
            "cubic",
            "spline",
            "barycentric",
            "polynomial",
            "krogh",
            "pecewise_polynomial",
            "spline",
            "pchip",
            "akima",
            "from_derivatives",
        ] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        limit: Optional[int] = ...,
        inplace: _bool = ...,
        limit_direction: Optional[Literal["forward", "backward", "both"]] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def isin(self, values: Union[Iterable, Series[_DType], Dict]) -> Series[_bool]: ...
    def isna(self) -> Series[_bool]: ...
    def isnull(self) -> Series[_bool]: ...
    def item(self) -> _DType: ...
    def items(self) -> Iterable[Tuple[Union[int, _str], _DType]]: ...
    def iteritems(self) -> Iterable[Tuple[Union[int, _str], _DType]]: ...
    def keys(self) -> List: ...
    @overload
    def kurt(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurt(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Optional[_LevelType],
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    def last(self, offset: Any) -> Series[_DType]: ...
    def last_valid_index(self) -> _Scalar: ...
    def le(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def lt(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    @overload
    def mad(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *, level: Optional[_LevelType], **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mad(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> _Scalar: ...
    def map(self, arg: Any, na_action: Optional[Literal["ignore"]] = ...) -> Series[_DType]: ...
    def mask(
        self,
        cond: Union[Series[_DType], _np.ndarray, Callable],
        other: Union[_Scalar, Series[_DType], DataFrame, Callable] = ...,
        inplace: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["raise", "ignore"] = ...,
        try_cast: _bool = ...,
    ) -> Series[_DType]: ...
    @overload
    def max(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def max(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    @overload
    def mean(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mean(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    @overload
    def median(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def median(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> int: ...
    @overload
    def min(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def min(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    def mod(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def mode(self, dropna: Any) -> Series[_DType]: ...
    def mul(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def multiply(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def ne(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def nlargest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[_DType]: ...
    def notna(self) -> Series[_bool]: ...
    def notnull(self) -> Series[_bool]: ...
    def notnull(self) -> Series[_bool]: ...
    def nsmallest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[_DType]: ...
    def nunique(self, dropna: _bool = ...) -> int: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq: Optional[Any] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def plot(self, **kwargs) -> Union[matplotlib.axes.Axes, _np.ndarray]: ...
    def pop(self, item: _str) -> Series[_DType]: ...
    def pow(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    @overload
    def prod(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def prod(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def product(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def product(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def quantile(
        self, q: float = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> float: ...
    @overload
    def quantile(
        self, q: _ListLike = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series[_DType]: ...
    def radd(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rank(
        self,
        axis: _SeriesAxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> Series: ...
    def ravel(self, order: _str = ...) -> _np.ndarray: ...
    def rdiv(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rdivmod(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def reindex(self, index: Optional[_ListLike] = ..., **kwargs) -> Series[_DType]: ...
    def reindex_like(
        self,
        other: Series[_DType],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[float] = ...,
    ) -> Series: ...
    def rename(
        self,
        index: Optional[Any] = ...,
        *,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["raise", "ignore"] = ...
    ) -> Series: ...
    @overload
    def rename_axis(
        self,
        mapper: Union[_Scalar, _ListLike] = ...,
        index: Optional[Union[_Scalar, _ListLike, Callable, Dict]] = ...,
        columns: Optional[Union[_Scalar, _ListLike, Callable, Dict]] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        mapper: Union[_Scalar, _ListLike] = ...,
        index: Optional[Union[_Scalar, _ListLike, Callable, Dict]] = ...,
        columns: Optional[Union[_Scalar, _ListLike, Callable, Dict]] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> Series: ...
    def reorder_levels(self, order: List) -> Series[_DType]: ...
    def repeat(self, repeats: Union[int, List[int]], axis: Optional[_SeriesAxisType] = ...) -> Series[_DType]: ...
    def replace(
        self,
        to_replace: Optional[Union[str, List, Dict, Series[_DType], int, float]] = ...,
        value: Optional[Union[_Scalar, Dict, List, _str]] = ...,
        inplace: _bool = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: Optional[Literal["pad", "ffill", "bfill"]] = ...,
    ) -> Series[_DType]: ...
    # Next one should return a 'Resampler' object
    def resample(
        self,
        rule: Any,
        axis: _SeriesAxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset: Optional[Any] = ...,
        base: int = ...,
        on: Optional[str] = ...,
        level: Optional[_LevelType] = ...,
    ) -> Any: ...
    def reset_index(
        self, level: Optional[_LevelType] = ..., drop: _bool = ..., name: Optional[object] = ..., inplace: _bool = ...,
    ) -> Series[_DType]: ...
    def rfloordiv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rmod(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rmul(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    # Next one should return a window class
    def rolling(
        self,
        window: Any,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: _SeriesAxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Any: ...
    def round(self, decimals: int = ..., *args, **kwargs) -> Series[_DType]: ...
    def rpow(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rsub(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rtruediv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def sample(
        self,
        n: Optional[int] = ...,
        frac: Optional[float] = ...,
        replace: _bool = ...,
        weights: Optional[Union[_str, _ListLike, _np.ndarray]] = ...,
        random_state: Optional[int] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    @overload
    def searchsorted(
        self, value: _ListLike, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> List[int]: ...
    @overload
    def searchsorted(
        self, value: _Scalar, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> int: ...
    @overload
    def sem(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def sem(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def set_axis(
        self, labels: Union[Index, _ListLike], axis: _SeriesAxisType = ..., *, inplace: Literal[True]
    ) -> None: ...
    @overload
    def set_axis(
        self, labels: Union[Index, _ListLike], axis: _SeriesAxisType = ..., inplace: Literal[False] = ...,
    ) -> Series[_DType]: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: _SeriesAxisType = ...,
        fill_value: Optional[object] = ...,
    ) -> Series[_DType]: ...
    @overload
    def skew(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def skew(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    def slice_shift(self, periods: int = ..., axis: _SeriesAxisType = ...) -> Series[_DType]: ...
    def sort_index(
        self,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
    ) -> Series[_DType]: ...
    def sort_values(
        self,
        axis: _SeriesAxisType = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> Series[_DType]: ...
    def squeeze(self, axis: Optional[_SeriesAxisType] = ...) -> _Scalar: ...
    @overload
    def std(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[float]: ...
    @overload
    def std(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> float: ...
    def str(self) -> _str: ...
    def sub(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> float: ...
    def subtract(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> float: ...
    def sum(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: Optional[_LevelType] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> float: ...
    def swapaxes(self, axis1: _SeriesAxisType, axis2: _SeriesAxisType, copy: _bool = ...) -> Series[_DType]: ...
    def swaplevel(self, i: _LevelType = ..., j: _LevelType = ..., copy: _bool = ...) -> Series[_DType]: ...
    def tail(self, n: int = ...) -> Series[_DType]: ...
    def take(self, indices: List, axis: _SeriesAxisType = ..., is_copy: _bool = ..., **kwargs) -> Series[_DType]: ...
    def to_clipboard(self, excel: _bool = ..., sep: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> None: ...
    @overload
    def to_csv(
        self,
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> _str: ...
    def to_dict(self, into: Hashable = ...) -> Dict[_str, Any]: ...
    def to_excel(
        self,
        excel_writer: Any,
        sheet_name: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Union[_str, Sequence[_str]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[_str] = ...,
        merge_cells: _bool = ...,
        encoding: Optional[_str] = ...,
        inf_rep: _str = ...,
        verbose: _bool = ...,
        freeze_panes: Optional[Tuple[int, int]] = ...,
    ) -> None: ...
    def to_frame(self, name: Optional[object] = ...) -> DataFrame: ...
    def to_hdf(
        self,
        path_or_buf: _Path_or_Buf,
        key: _str,
        mode: _str = ...,
        complevel: Optional[int] = ...,
        complib: Optional[_str] = ...,
        append: _bool = ...,
        format: Optional[_str] = ...,
        index: _bool = ...,
        min_itemsize: Optional[Union[int, Dict[_str, int]]] = ...,
        nan_rep: Optional[Any] = ...,
        dropna: Optional[_bool] = ...,
        data_columns: Optional[List[_str]] = ...,
        errors: _str = ...,
        encoding: _str = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> _str: ...
    @overload
    def to_latex(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_latex(
        self,
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> _str: ...
    def to_list(self) -> List: ...
    @overload
    def to_markdown(self, buf: Optional[_Path_or_Buf], mode: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_markdown(self, mode: Optional[_str] = ...,) -> _str: ...
    def to_numpy(
        self, dtype: Optional[Type[_DTypeNp]] = ..., copy: _bool = ..., na_value: Any = ..., **kwargs
    ) -> _np.ndarray: ...
    def to_period(self, freq: Optional[_str] = ..., copy: _bool = ...) -> DataFrame: ...
    def to_pickle(
        self, path: _str, compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ..., protocol: int = ...,
    ) -> None: ...
    def to_records(
        self,
        index: _bool = ...,
        column_dtypes: Optional[Union[_str, Dict]] = ...,
        index_dtypes: Optional[Union[_str, Dict]] = ...,
    ) -> Any: ...
    def to_sql(
        self,
        name: _str,
        con: Any,
        schema: Optional[_str] = ...,
        if_exists: _str = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        chunksize: Optional[int] = ...,
        dtype: Optional[Union[Dict, _Scalar]] = ...,
        method: Optional[Union[_str, Callable]] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        buf: Optional[_Path_or_Buf],
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    def to_timestamp(
        self, freq: Optional[Any] = ..., how: Literal["start", "end", "s", "e"] = ..., copy: _bool = ...,
    ) -> Series[_DType]: ...
    def to_xarray(self) -> Any: ...  # xarray.DataArray
    def tolist(self) -> List: ...
    def transform(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: _SeriesAxisType = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def transpose(self, *args, **kwargs) -> Series[_DType]: ...
    def truediv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    def truncate(
        self,
        before: Optional[Union[datetime.date, _str, int]] = ...,
        after: Optional[Union[datetime.date, _str, int]] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
    ) -> Series[_DType]: ...
    def tshift(self, periods: int = ..., freq: Any = ..., axis: _SeriesAxisType = ...) -> Series[_DType]: ...
    def tz_convert(
        self, tz: Any, axis: _SeriesAxisType = ..., level: Optional[_LevelType] = ..., copy: _bool = ...,
    ) -> Series[_DType]: ...
    def tz_localize(
        self,
        tz: Any,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        ambiguous: Any = ...,
        nonexistent: _str = ...,
    ) -> Series[_DType]: ...
    def unique(self) -> _np.ndarray: ...
    def unstack(self, level: _LevelType = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,) -> DataFrame: ...
    def update(self, other: Series[_DType]) -> None: ...
    def value_counts(
        self,
        normalize: _bool = ...,
        sort: _bool = ...,
        ascending: _bool = ...,
        bins: Optional[int] = ...,
        dropna: _bool = ...,
    ) -> Series[_DType]: ...
    @overload
    def var(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def var(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    def view(self, dtype: Optional[Any] = ...) -> Series[_DType]: ...
    def where(
        self,
        cond: Union[Series[_DType], Series[_DType], _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> Series[_DType]: ...
    def xs(
        self,
        key: Union[_str, Tuple[_str]],
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        drop_level: _bool = ...,
    ) -> Series[_DType]: ...

class DataFrame:

    _ListLike = Union[
        _np.ndarray, List[_DType], Dict[_str, _np.ndarray], Sequence, Index, Series[_DType],
    ]
    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[_str, Any]]] = ...,
        index: Optional[_ListLike] = ...,
        columns: Optional[_ListLike] = ...,
        dtype: Any = ...,
        copy: bool = ...,
    ): ...
    Name: _str
    #
    # dunder methods
    def __add__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __and__(self, other: Union[num, _ListLike, DataFrame], axis: _SeriesAxisType = ...) -> DataFrame: ...
    def __delitem__(self, key: _str) -> None: ...
    def __div__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __eq__(self, other: Union[float, Series[_DType], DataFrame]) -> DataFrame: ...  # type: ignore
    def __exp__(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: _AxisType = ...,
        level: _LevelType = ...,
        fill_value: Union[None, float] = ...,
    ) -> DataFrame: ...
    def __floordiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _str) -> Series[_DType]: ...
    @overload
    def __getitem__(self, rows: slice) -> DataFrame: ...
    @overload
    def __getitem__(
        self, idx: Union[Series[_bool], DataFrame, List[_str], Index[_str], _np_ndarray_str],
    ) -> DataFrame: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __le__(self, other: float) -> DataFrame: ...
    def __lt__(self, other: float) -> DataFrame: ...
    def __ge__(self, other: float) -> DataFrame: ...
    def __gt__(self, other: float) -> DataFrame: ...
    def __mod__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __mul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __pow__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __ne__(self, other: Union[float, Series[_DType], DataFrame]) -> DataFrame: ...  # type: ignore
    def __or__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __radd__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rand__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rdiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rfloordiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rmod__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rmul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rnatmul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __ror__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rpow__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rsub__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rtruediv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rxor__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __truediv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __mul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __sub__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __xor__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    # properties
    @property
    def at(self) -> Any: ...  # Not sure what to do with this yet; look at source
    @property
    def axes(self) -> Tuple[List[Any], List[Any]]: ...
    @property
    def bool(self) -> _bool: ...
    @property
    def columns(self) -> Index[_str]: ...
    @columns.setter  # setter needs to be right next to getter; otherwise mypy complains
    def columns(self, cols: Union[List[_str], Index[_str]]) -> None: ...
    @property
    def dtypes(self) -> Series[_DType]: ...
    @property
    def empty(self) -> _bool: ...
    @property
    def iat(self) -> Any: ...  # Not sure what to do with this yet; look at source
    @property
    def iloc(self) -> _iLocIndexerFrame: ...
    @property
    def index(self) -> Index[int]: ...
    @index.setter
    def index(self, idx: Index) -> None: ...
    @property
    def loc(self) -> _LocIndexerFrame: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    @property
    def str(self) -> _str: ...
    @property
    def T(self) -> DataFrame: ...
    # this function is deprecated:
    @property
    def values(self) -> _np.ndarray: ...
    # methods
    def abs(self) -> DataFrame: ...
    def add(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def add_prefix(self, prefix: _str) -> DataFrame: ...
    def add_suffix(self, suffix: _str) -> DataFrame: ...
    @overload
    def agg(self, func: Union[Callable, _str], axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    @overload
    def agg(self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, func: Union[Callable, _str], axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    @overload
    def aggregate(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ..., **kwargs
    ) -> DataFrame: ...
    def align(
        self,
        other: Union[DataFrame, Series[_DType]],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: _AxisType = ...,
        broadcast_axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def all(
        self, axis: _AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[_DType]: ...
    @overload
    def all(
        self,
        axis: _AxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def any(
        self, axis: _AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[_DType]: ...
    @overload
    def any(
        self, axis: _AxisType = ..., bool_only: _bool = ..., skipna: _bool = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    def append(
        self,
        other: Union[DataFrame, Series[_DType], Dict[_str, Any]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series[_DType]: ...
    @overload
    def apply(
        self, f: Callable, axis: _AxisType = ..., raw: _bool = ..., result_type: Optional[_str] = ...,
    ) -> DataFrame: ...
    def applymap(self, func: Callable) -> DataFrame: ...
    def asof(self, where: Any, subset: Optional[Union[_str, List[_str]]] = ...) -> DataFrame: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[_Scalar] = ...,
    ) -> DataFrame: ...
    def astype(self, dtype: Union[_str, Dict[_str, _str]], copy: _bool = ..., errors: _str = ...,) -> DataFrame: ...
    def at_time(
        self, time: Union[_str, datetime.time], asof: _bool = ..., axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def between_time(
        self,
        start_time: Union[_str, datetime.time],
        end_time: Union[_str, datetime.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    def boxplot(
        self,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        fontsize: Optional[Union[float, _str]] = ...,
        rot: int = ...,
        grid: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        return_type: Optional[Literal["axes", "dict", "both"]] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> Any: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> DataFrame: ...
    def combine(
        self, other: DataFrame, func: Callable, fill_value: Optional[Any] = ..., overwrite: _bool = ...,
    ) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def convert_dtypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert__boolean: _bool = ...,
    ) -> DataFrame: ...
    def copy(self, deep: _bool = ...) -> DataFrame: ...
    def corr(self, method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,) -> DataFrame: ...
    def corrwith(
        self,
        other: Union[DataFrame, Series[_DType]],
        axis: Optional[_AxisType] = ...,
        drop: _bool = ...,
        method: Literal["pearson", "kendall", "spearman"] = ...,
    ) -> Series: ...
    @overload
    def count(self, axis: _AxisType = ..., numeric_only: _bool = ..., *, level: _LevelType) -> DataFrame: ...
    @overload
    def count(self, axis: _AxisType = ..., level: None = ..., numeric_only: _bool = ...) -> Series[_DType]: ...
    def cov(self, min_periods: Optional[int] = ...) -> DataFrame: ...
    def cummax(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cummin(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumprod(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumsum(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[_DType]]] = ...,
        exclude: Optional[List[_DType]] = ...,
    ) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    def div(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def divide(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def dot(self, other: DataFrame) -> DataFrame: ...
    @overload
    def dot(self, other: Series[_DType]) -> Series[_DType]: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: _AxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[_LevelType] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    def drop_duplicates(
        self,
        subset: Optional[Any] = ...,
        keep: Union[Literal["first", "last"], _bool] = ...,
        inplace: _bool = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def droplevel(self, level: _LevelType = ..., axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def dropna(
        self,
        axis: _AxisType = ...,
        how: Literal["any", "all"] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def dropna(
        self,
        axis: _AxisType = ...,
        how: Literal["any", "all"] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> DataFrame: ...
    def duplicated(
        self,
        subset: Optional[Union[Hashable, Sequence[Hashable]]] = ...,
        keep: Union[Literal["first", "last"], _bool] = ...,
    ) -> Series[_DType]: ...
    def eq(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def equals(self, other: Union[Series[_DType], DataFrame]) -> _bool: ...
    def eval(self, expr: _str, inplace: _bool = ..., **kwargs) -> Any: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: _AxisType = ...,
    ) -> DataFrame: ...
    def exp(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: _AxisType = ...) -> Any: ...  # for now
    def explode(self, column: Union[str, Tuple]) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[_Scalar, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    def filter(
        self,
        items: Optional[List] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def first(self, offset: Any) -> DataFrame: ...
    def first_valid_index(self) -> _Scalar: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # def from_dict
    # def from_records
    def fulldiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ge(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    # def get
    def groupby(
        self,
        by: Optional[Union[List[_str], _str]],
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> DataFrameGroupBy: ...
    def gt(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def hist(
        data,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        sharex: _bool = ...,
        sharey: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        bins: Union[int, List] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> Any: ...
    def idxmax(self, axis: _AxisType, skipna: _bool = ...) -> Series[_DType]: ...
    def idxmin(self, axis: _AxisType, skipna: _bool = ...) -> Series[_DType]: ...
    def infer_objects(self) -> DataFrame: ...
    # def info
    def insert(self, loc: int, column: Any, value: Union[int, _ListLike], allow_duplicates: _bool = ...,) -> None: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: _AxisType = ...,
        limit: Optional[int] = ...,
        limit_direction: Literal["forward", "backward", "both"] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        *,
        inplace: Literal[True],
        **kwargs
    ) -> None: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: _AxisType = ...,
        limit: Optional[int] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit_direction: Literal["forward", "backward", "both"] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        **kwargs
    ) -> DataFrame: ...
    def isin(self, values: Union[Iterable, Series[_DType], DataFrame, Dict]) -> DataFrame: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def items(self) -> Iterable[Tuple[Union[Hashable, None], Series[_DType]]]: ...
    def iteritems(self) -> Iterable[Tuple[Union[Hashable, None], Series[_DType]]]: ...
    def iterrows(self) -> Iterable[Tuple[Union[Hashable, None], Series[_DType]]]: ...
    def itertuples(self, index: _bool = ..., name: Optional[_str] = ...) -> Iterable[Tuple[Union[Hashable, None]]]: ...
    def join(
        self,
        other: Union[DataFrame, Series[_DType], List[DataFrame]],
        on: Optional[Union[_str, List[_str]]] = ...,
        how: Literal["left", "right", "outer", "inner"] = ...,
        lsuffix: _str = ...,
        rsuffix: _str = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def keys(self) -> Index: ...
    @overload
    def kurt(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurt(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def last(self, offset: Any) -> DataFrame: ...
    def last_valid_index(self) -> _Scalar: ...
    def le(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def lookup(self, row_labels: Sequence, col_labels: Sequence) -> _np.ndarray: ...
    def lt(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    @overload
    def mad(
        self, axis: Optional[_AxisType] = ..., skipna: Optional[_bool] = ..., level: None = ...,
    ) -> Series[_DType]: ...
    @overload
    def mad(
        self, axis: Optional[_AxisType] = ..., skipna: Optional[_bool] = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    def mask(
        self,
        cond: Union[Series[_DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mean(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def mean(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def median(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def median(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def melt(
        self,
        id_vars: Optional[Any] = ...,
        value_vars: Optional[Any] = ...,
        var_name: Optional[Any] = ...,
        value_name: Any = ...,
        col_level: Optional[Union[int, _str]] = ...,
    ) -> DataFrame: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> Series[_DType]: ...
    def merge(
        self,
        right: Union[DataFrame, Series[_DType]],
        how: Literal["left", "right", "inner", "outer"] = ...,
        on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        left_on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        right_on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        left_index: _bool = ...,
        right_index: _bool = ...,
        sort: _bool = ...,
        suffixes: Tuple[_str, _str] = ...,
        copy: _bool = ...,
        indicator: Union[_bool, _str] = ...,
        validate: Optional[_str] = ...,
    ) -> DataFrame: ...
    @overload
    def min(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def min(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mode(
        self, axis: _AxisType = ..., skipna: _bool = ..., numeric_only: _bool = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    @overload
    def mode(
        self, axis: _AxisType = ..., skipna: _bool = ..., level: None = ..., numeric_only: _bool = ..., **kwargs
    ) -> Series[_DType]: ...
    def mod(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def mul(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def multiply(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ne(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def nlargest(
        self, n: int, columns: Union[_str, List[_str]], keep: Literal["first", "last", "all"] = ...,
    ) -> DataFrame: ...
    def nsmallest(
        self, n: int, columns: Union[_str, List[_str]], keep: Literal["first", "last", "all"] = ...,
    ) -> DataFrame: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    def nunique(self, axis: _AxisType = ..., dropna=True) -> Series[_DType]: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq: Optional[Any] = ...,
        **kwargs
    ) -> DataFrame: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def pivot(
        self, index: Optional[Any] = ..., columns: Optional[Any] = ..., values: Optional[Any] = ...,
    ) -> DataFrame: ...
    def pivot_table(
        self,
        values: Optional[Any] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        aggfunc: Any = ...,
        fill_value: Optional[Any] = ...,
        margins: _bool = ...,
        dropna: _bool = ...,
        margins_name: _str = ...,
        observed: _bool = ...,
    ) -> DataFrame: ...
    def plot(self, kind: _str, yerr: DataFrame, **kwargs) -> matplotlib.axes.Axes: ...
    def pop(self, item: _str) -> Series[_DType]: ...
    def pow(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series: ...
    def product(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def quantile(
        self,
        q: float = ...,
        axis: _AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series: ...
    @overload
    def quantile(
        self,
        q: List = ...,
        axis: _AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> DataFrame: ...
    def query(self, expr: _str, inplace: _bool = ..., **kwargs) -> DataFrame: ...
    def radd(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rank(
        self,
        axis: _AxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> DataFrame: ...
    def rdiv(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def reindex(
        self,
        labels: Optional[List] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Any = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[Any] = ...,
    ) -> DataFrame: ...
    def reindex_like(
        self,
        other: DataFrame,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[Any] = ...,
    ) -> DataFrame: ...
    # looks like rename is missing an index arg?
    @overload
    def rename(
        self,
        mapper: Optional[Callable],
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def rename(
        self,
        columns: Optional[Dict[_str, _str]],
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def rename_axis(
        self,
        mapper: Optional[Any] = ...,
        index: Optional[_IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        mapper: Optional[Any] = ...,
        index: Optional[_IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> DataFrame: ...
    def reorder_levels(self, order: List, axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def replace(
        self,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: _str = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def replace(
        self,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: _str = ...,
    ) -> DataFrame: ...
    def resample(
        self,
        rule: Any,
        axis: _AxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset: Optional[Any] = ...,
        base: int = ...,
        on: Optional[_str] = ...,
        level: Optional[_LevelType] = ...,
    ) -> Any: ...
    @overload
    def reset_index(
        self,
        level: _LevelType = ...,
        drop: _bool = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: _LevelType = ...,
        drop: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
    ) -> DataFrame: ...
    def rfloordiv(
        self,
        other: Any,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
    ) -> DataFrame: ...
    def rmod(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rmul(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rolling(
        self,
        window: Any,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: _AxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Any: ...  # For now
    def round(self, decimals: Union[int, Dict, Series[_DType]] = ..., *args, **kwargs) -> DataFrame: ...
    def rpow(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rsub(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rtruediv(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # sample is missing a weights arg
    @overload
    def sample(
        self,
        frac: Optional[float],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def sample(
        self,
        n: Optional[int],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def select_dtypes(
        self, include: Optional[Union[_str, List[_str]]] = ..., exclude: Optional[Union[_str, List[_str]]] = ...,
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def set_axis(self, labels: List, inplace: Literal[True], axis: _AxisType = ...) -> None: ...
    @overload
    def set_axis(self, labels: List, axis: _AxisType = ..., inplace: Optional[Literal[False]] = ...,) -> DataFrame: ...
    @overload
    def set_index(
        self,
        keys: List,
        drop: _bool = ...,
        append: _bool = ...,
        verify_integrity: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def set_index(
        self,
        keys: List,
        drop: _bool = ...,
        append: _bool = ...,
        inplace: Optional[Literal[True]] = ...,
        verify_integrity: _bool = ...,
    ) -> DataFrame: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: _AxisType = ...,
        fill_value: Optional[Hashable] = ...,
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def slice_shift(self, periods: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def sort_index(
        self,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def sort_index(
        self,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        axis: _AxisType = ...,
        ascending: _bool = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        axis: _AxisType = ...,
        ascending: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def squeeze(self, axis: Optional[_AxisType] = ...) -> Any: ...
    def stack(self, level: _LevelType = ..., dropna: _bool = ...) -> Union[DataFrame, Series[_DType]]: ...
    @overload
    def std(
        self,
        axis: _AxisType = ...,
        skipna: _bool = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def std(
        self,
        axis: _AxisType = ...,
        skipna: _bool = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def sub(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def subtract(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def swapaxes(self, axis1: _AxisType, axis2: _AxisType, copy: _bool = ...) -> DataFrame: ...
    def swaplevel(self, i: _LevelType = ..., j: _LevelType = ..., axis: _AxisType = ...) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: List, axis: _AxisType = ..., is_copy: Optional[_bool] = ..., **kwargs) -> DataFrame: ...
    def transform(self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ...,) -> DataFrame: ...
    def transpose(self, *args, copy: _bool = ...) -> DataFrame: ...
    T = transpose
    def tshift(self, periods: int = ..., freq: Any = ..., axis: _AxisType = ...) -> DataFrame: ...
    def to_clipboard(self, excel: _bool = ..., sep: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> None: ...
    @overload
    def to_csv(
        self,
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> _str: ...
    @overload
    def to_dict(self) -> Dict[_str, Any]: ...
    @overload
    def to_dict(
        self, orient: Literal["dict", "list", "series", "split", "records", "index"] = ..., into: Hashable = ...,
    ) -> List[Dict[_str, Any]]: ...
    def to_excel(
        self,
        excel_writer: Any,
        sheet_name: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Union[_str, Sequence[_str]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[_str] = ...,
        merge_cells: _bool = ...,
        encoding: Optional[_str] = ...,
        inf_rep: _str = ...,
        verbose: _bool = ...,
        freeze_panes: Optional[Tuple[int, int]] = ...,
    ) -> None: ...
    def to_feather(self, path: _str) -> None: ...
    def to_hdf(
        self,
        path_or_buf: _Path_or_Buf,
        key: _str,
        mode: _str = ...,
        complevel: Optional[int] = ...,
        complib: Optional[_str] = ...,
        append: _bool = ...,
        format: Optional[_str] = ...,
        index: _bool = ...,
        min_itemsize: Optional[Union[int, Dict[_str, int]]] = ...,
        nan_rep: Optional[Any] = ...,
        dropna: Optional[_bool] = ...,
        data_columns: Optional[List[_str]] = ...,
        errors: _str = ...,
        encoding: _str = ...,
    ) -> None: ...
    @overload
    def to_html(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[_str, int]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_html(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[_str, int]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    @overload
    def to_json(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> _str: ...
    @overload
    def to_latex(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_latex(
        self,
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> _str: ...
    @overload
    def to_markdown(self, buf: Optional[_Path_or_Buf], mode: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_markdown(self, mode: Optional[_str] = ..., **kwargs) -> _str: ...
    @overload
    def to_numpy(self) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Optional[Type[_DTypeNp]]) -> _np.ndarray: ...
    def to_parquet(
        self,
        path: _str,
        engine: Literal["auto", "pyarrow", "fastparquet"] = ...,
        compression: Literal["snappy", "gzip", "brotli"] = ...,
        index: Optional[_bool] = ...,
        partition_cols: Optional[List] = ...,
        **kwargs
    ) -> None: ...
    def to_period(self, freq: Optional[_str] = ..., axis: _AxisType = ..., copy: _bool = ...) -> DataFrame: ...
    def to_pickle(
        self, path: _str, compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ..., protocol: int = ...,
    ) -> None: ...
    def to_records(
        self,
        index: _bool = ...,
        column_dtypes: Optional[Union[_str, Dict]] = ...,
        index_dtypes: Optional[Union[_str, Dict]] = ...,
    ) -> Any: ...
    def to_sql(
        self,
        name: _str,
        con: Any,
        schema: Optional[_str] = ...,
        if_exists: _str = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        chunksize: Optional[int] = ...,
        dtype: Optional[Union[Dict, _Scalar]] = ...,
        method: Optional[Union[_str, Callable]] = ...,
    ) -> None: ...
    def to_stata(
        self,
        path: _Path_or_Buf,
        convert_dates: Optional[Dict] = ...,
        write_index: _bool = ...,
        byteorder: Optional[Literal["<", ">", "little", "big"]] = ...,
        time_stamp: Optional[Any] = ...,
        data_label: Optional[_str] = ...,
        variable_labels: Optional[Dict] = ...,
        version: int = ...,
        convert_strl: Optional[List[_str]] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[int] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[int] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    def to_timestamp(
        self,
        freq: Optional[Any] = ...,
        how: Literal["start", "end", "s", "e"] = ...,
        axis: _AxisType = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def to_xarray(self) -> Any: ...
    def transform(self, func: Callable, axis: _AxisType = ..., *args, **kwargs) -> DataFrame: ...
    def truediv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def truncate(
        self,
        before: Optional[Union[datetime.date, _str, int]] = ...,
        after: Optional[Union[datetime.date, _str, int]] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    # def tshift
    def tz_convert(
        self, tz: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., copy: _bool = ...,
    ) -> DataFrame: ...
    def tz_localize(
        self,
        tz: Any,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        ambiguous: Any = ...,
        nonexistent: _str = ...,
    ) -> DataFrame: ...
    def unique(self) -> DataFrame: ...
    def unstack(
        self, level: _LevelType = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,
    ) -> Union[DataFrame, Series[_DType]]: ...
    def update(
        self,
        other: Union[DataFrame, Series[_DType]],
        join: Literal["left"] = ...,
        overwrite: _bool = ...,
        filter_func: Optional[Callable] = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> None: ...
    @overload
    def var(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def where(
        self,
        cond: Union[Series[_DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    def xs(
        self,
        key: Union[_str, Tuple[_str]],
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        drop_level: _bool = ...,
    ) -> DataFrame: ...

_IndexType = Union[slice, _np_ndarray_int64, Index[int], List[int], Series[int]]
_MaskType = Union[Series[bool], _np_ndarray_bool, List[bool]]

class _iLocIndexerFrame:
    @overload
    def __getitem__(self, idx: Tuple[int, int]) -> _DType: ...
    @overload
    def __getitem__(self, idx: Union[_IndexType, slice, Tuple[_IndexType, _IndexType]]) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: Union[int, Tuple[_IndexType, int, Tuple[int, _IndexType]]]) -> Series[_DType]: ...
    def __setitem__(
        self,
        idx: Union[
            int,
            _IndexType,
            Tuple[int, int],
            Tuple[_IndexType, int],
            Tuple[_IndexType, _IndexType],
            Tuple[int, _IndexType],
        ],
        value: Union[float, Series[_DType], DataFrame],
    ) -> None: ...

class _iLocIndexerSeries(Generic[_DType]):
    # get item
    @overload
    def __getitem__(self, idx: int) -> _DType: ...
    @overload
    def __getitem__(self, idx: _IndexType) -> Series[_DType]: ...
    # set item
    @overload
    def __setitem__(self, idx: int, value: _DType) -> None: ...
    @overload
    def __setitem__(self, idx: _IndexType, value: Union[_DType, Series[_DType]]) -> None: ...

class _LocIndexerFrame:
    @overload
    def __getitem__(self, idx: Union[int, slice, _MaskType],) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _StrLike,) -> Series[_DType]: ...
    @overload
    def __getitem__(self, idx: Tuple[_StrLike, _StrLike],) -> float: ...
    @overload
    def __getitem__(self, idx: Tuple[Union[_MaskType, List[str]], Union[_MaskType, List[str]]],) -> DataFrame: ...
    def __setitem__(
        self,
        idx: Union[_MaskType, _StrLike, Tuple[Union[_MaskType, List[str]], Union[_MaskType, List[str]]],],
        value: Union[float, _np.ndarray, Series[_DType], DataFrame],
    ) -> None: ...

class _LocIndexerSeries(Generic[_DType]):
    @overload
    def __getitem__(self, idx: _MaskType,) -> Series[_DType]: ...
    @overload
    def __getitem__(self, idx: Union[int, str],) -> _DType: ...
    @overload
    def __getitem__(self, idx: List[str],) -> Series[_DType]: ...
    @overload
    def __setitem__(self, idx: _MaskType, value: Union[_DType, _np.ndarray, Series[_DType]],) -> None: ...
    @overload
    def __setitem__(self, idx: str, value: _DType,) -> None: ...
    @overload
    def __setitem__(self, idx: List[str], value: Union[_DType, _np.ndarray, Series[_DType]],) -> None: ...

# Incomplete: see https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
class GroupBy:
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]: ...
    @property
    def groups(self) -> Dict[str, str]: ...
    @property
    def indices(self) -> Dict[str, Index]: ...
    def agg(self, func: Optional[Callable] = ..., *args, **kwargs) -> Union[Series, DataFrame]: ...
    def aggregate(self, func: Optional[Callable] = ..., *args, **kwargs) -> Union[Series, DataFrame]: ...
    def all(self, skipna: bool = ...) -> bool: ...
    def any(self, skipna: bool = ...) -> bool: ...
    def apply(self, func: Callable, *args, **kwargs) -> Union[Series, DataFrame]: ...
    def bfill(self, limit: Optional[int] = ...) -> Union[Series, DataFrame]: ...
    def count(self) -> Union[Series, DataFrame]: ...
    def cumcount(self, ascending: bool = ...) -> Series: ...
    def cummax(self, axis: _AxisType = ..., **kwargs) -> Union[Series, DataFrame]: ...
    def cummin(self, axis: _AxisType = ..., **kwargs) -> Union[Series, DataFrame]: ...
    def cumprod(self, axis: _AxisType = ..., **kwargs) -> Union[Series, DataFrame]: ...
    def cumsum(self, axis: _AxisType = ..., **kwargs) -> Union[Series, DataFrame]: ...
    def describe(self, **kwargs) -> Union[Series, DataFrame]: ...
    def ffill(self, limit: Optional[int] = ...) -> Union[Series, DataFrame]: ...
    def first(self, **kwargs) -> Union[Series, DataFrame]: ...
    def get_group(self, name: Any, obj: Optional[DataFrame] = ...) -> DataFrame: ...
    def head(self, n: int = ...) -> Union[Series, DataFrame]: ...
    def last(self, **kwargs) -> Union[Series, DataFrame]: ...
    def max(self, **kwargs) -> Union[Series, DataFrame]: ...
    def mean(self, **kwargs) -> Union[Series, DataFrame]: ...
    def median(self, **kwargs) -> Union[Series, DataFrame]: ...
    def min(self, **kwargs) -> Union[Series, DataFrame]: ...
    def ngroup(self, ascending: bool = ...) -> Series: ...
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> Union[Series, DataFrame]: ...
    def ohlc(self) -> DataFrame: ...
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit: Any = ..., freq: Any = ..., axis: _AxisType = ...,
    ) -> Union[Series, DataFrame]: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def prod(self, **kwargs) -> Union[Series, DataFrame]: ...
    def rank(
        self, method: str = ..., ascending: bool = ..., na_option: str = ..., pct: bool = ..., axis: int = ...,
    ) -> DataFrame: ...
    def sem(self, ddof: int = ...) -> Union[Series, DataFrame]: ...
    def size(self) -> Series: ...
    def std(self, ddof: int = ...) -> Union[Series, DataFrame]: ...
    def sum(self, **kwargs) -> Union[Series, DataFrame]: ...
    def transform(self, func: Callable, *args, **kwargs): ...
    def tail(self, n: int = ...) -> Union[Series, DataFrame]: ...
    def var(self, ddof: int = ...) -> Union[Series, DataFrame]: ...

class Grouper:
    def __init__(
        self,
        key: Optional[str] = ...,
        level: Optional[_LevelType] = ...,
        freq: Optional[str] = ...,
        axis: _AxisType = ...,
        sort: bool = ...,
        *kwargs
    ): ...

# These are missing lots of methods still
class SeriesGroupBy(GroupBy):
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def __getitem__(self, item: str) -> Series[_DType]: ...
    def bfill(self, limit: Optional[int] = ...) -> Series[_DType]: ...
    def count(self) -> Series[_DType]: ...
    def cummax(self, axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    def cummin(self, axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    def cumprod(self, axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    def cumsum(self, axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    def describe(self, **kwargs) -> Series[_np.double64]: ...
    def ffill(self, limit: Optional[int] = ...) -> Series[_DType]: ...
    def first(self, **kwargs) -> Series[_DType]: ...
    def head(self, n: int = ...) -> Series[_DType]: ...
    def last(self, **kwargs) -> Series[_DType]: ...
    def max(self, **kwargs) -> Series[_DType]: ...
    def mean(self, **kwargs) -> Series[_DType]: ...
    def median(self, **kwargs) -> Series[_DType]: ...
    def min(self, **kwargs) -> Series[_DType]: ...
    def nlargest(self, n: int = ..., keep: str = ...) -> Series[_DType]: ...
    def nsmallest(self, n: int = ..., keep: str = ...) -> Series[_DType]: ...
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> Series[_DType]: ...
    def nunique(self, dropna: bool = ...) -> Series: ...
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit: Any = ..., freq: Any = ..., axis: _AxisType = ...,
    ) -> Series[_DType]: ...
    def prod(self, **kwargs) -> Series[_DType]: ...
    def sem(self, ddof: int = ...) -> Series[_DType]: ...
    def std(self, ddof: int = ...) -> Series[_DType]: ...
    def sum(self, **kwargs) -> Series[_DType]: ...
    def tail(self, n: int = ...) -> Series[_DType]: ...
    def value_counts(
        self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins: Any = ..., dropna: bool = ...,
    ) -> DataFrame: ...
    def var(self, ddof: int = ...) -> Series[_DType]: ...

# These are missing lots of methods still
class DataFrameGroupBy(GroupBy):

    ## These are "properties" but properties can't have all these arguments?!
    def corr(self, method: Union[str, Callable], min_periods: int = ...) -> DataFrame: ...
    def cov(self, min_periods: int = ...) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def __getitem__(self, item: str) -> Series[_DType]: ...
    @overload
    def __getitem__(self, item: List[str]) -> DataFrame: ...
    @overload
    def aggregate(self, arg: str, *args, **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, arg: Dict, *args, **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, arg: Callable[[], Any], *args, **kwargs) -> DataFrame: ...
    def bfill(self, limit: Optional[int] = ...) -> DataFrame: ...
    def boxplot(
        self,
        grouped: DataFrame,
        subplots: bool = ...,
        column: Optional[Union[str, Sequence]] = ...,
        fontsize: Union[int, str] = ...,
        rot: float = ...,
        grid: bool = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[str] = ...,
        **kwargs
    ) -> Union[matplotlib.AxesSubplot, List[matplotlib.AxesSubplot]]: ...
    def corrwith(self, other: DataFrame, axis: _AxisType = ..., drop: bool = ..., method: str = ...,) -> Series: ...
    def count(self) -> DataFrame: ...
    def cummax(self, axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    def cummin(self, axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    def cumprod(self, axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    def cumsum(self, axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    def describe(self, **kwargs) -> DataFrame: ...
    def ffill(self, limit: Optional[int] = ...) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Any,
        method: Optional[str] = ...,
        axis: _AxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def fillna(
        self,
        value: Any,
        method: Optional[str] = ...,
        axis: _AxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    def filter(self, func: Callable, dropna: bool = ..., *args, **kwargs) -> DataFrame: ...
    def first(self, **kwargs) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def hist(
        data: DataFrame,
        column: Optional[Union[str, Sequence]] = ...,
        by: Any = ...,
        grid: bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[str] = ...,
        **kwargs
    ) -> Union[matplotlib.AxesSubplot, List[matplotlib.AxesSubplot]]: ...
    def idxmax(self, axis: _AxisType = ..., skipna: bool = ...) -> Series: ...
    def idxmin(self, axis: _AxisType = ..., skipna: bool = ...) -> Series: ...
    def last(self, **kwargs) -> DataFrame: ...
    @overload
    def mad(
        self,
        axis: _AxisType = ...,
        skipna: bool = ...,
        numeric_only: Optional[bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def mad(
        self,
        axis: _AxisType = ...,
        skipna: bool = ...,
        level: None = ...,
        numeric_only: Optional[bool] = ...,
        **kwargs
    ) -> Series: ...
    def max(self, **kwargs) -> DataFrame: ...
    def mean(self, **kwargs) -> DataFrame: ...
    def median(self, **kwargs) -> DataFrame: ...
    def min(self, **kwargs) -> DataFrame: ...
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> DataFrame: ...
    def nunique(self, dropna: bool = ...) -> DataFrame: ...
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit: Any = ..., freq: Any = ..., axis: _AxisType = ...,
    ) -> DataFrame: ...
    def prod(self, **kwargs) -> DataFrame: ...
    def quantile(self, q: float = ..., interpolation: str = ...) -> DataFrame: ...
    def rank(
        self, method: str = ..., ascending: bool = ..., na_option: str = ..., pct: bool = ..., axis: _AxisType = ...,
    ) -> DataFrame: ...
    def resample(self, rule: Any, *args, **kwargs) -> Grouper: ...
    def sem(self, ddof: int = ...) -> DataFrame: ...
    def shift(
        self, periods: int = ..., freq: str = ..., axis: _AxisType = ..., fill_value: Any = ...,
    ) -> DataFrame: ...
    def size(self) -> Series[int]: ...
    @overload
    def skew(
        self, axis: _AxisType = ..., skipna: bool = ..., numeric_only: bool = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    @overload
    def skew(
        self, axis: _AxisType = ..., skipna: bool = ..., level: None = ..., numeric_only: bool = ..., **kwargs
    ) -> Series: ...
    def std(self, ddof: int = ...) -> DataFrame: ...
    def sum(self, **kwargs) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: List, axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    def tshift(self, periods: int, freq: Any = ..., axis: _AxisType = ...) -> DataFrame: ...
    def var(self, ddof: int = ...) -> DataFrame: ...
