from pathlib import Path
import site


def _load_local_venv() -> None:
    root = Path(__file__).resolve().parent
    site_packages = root / ".venv" / "Lib" / "site-packages"
    if site_packages.exists():
        site.addsitedir(str(site_packages))


_load_local_venv()

from app.main import app
