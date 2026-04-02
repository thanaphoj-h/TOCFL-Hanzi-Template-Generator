from datetime import datetime, timezone, timedelta

class AppDatetimeProvider():

    TZ = timezone(timedelta(hours=7))

    @classmethod
    def now(cls) -> datetime:
        return datetime.now(cls.TZ)

    @classmethod
    def now_str(cls) -> str:
        return cls.now().isoformat(timespec="milliseconds")

    @classmethod
    def parse_str(cls, value: str) -> datetime:

        if value.endswith("Z"):
            value = value.replace("Z", "+00:00")

        try:
            dt = datetime.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Invalid ISO datetime format: {value}")

        if dt.tzinfo is None:
            return dt.replace(tzinfo=cls.TZ)
        
        return dt.astimezone(cls.TZ)