import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def update_yt_dlp() -> None:
    """Upgrade yt-dlp (and uv.lock) to the latest release before downloading.

    Never raises: if the update fails (e.g. offline), continue with the
    installed version.
    """
    print("Checking yt-dlp updates...")
    try:
        result = subprocess.run(
            ["uv", "sync", "-q", "--upgrade-package", "yt-dlp"],
            cwd=PROJECT_ROOT,
            check=False,
            timeout=120,
        )
        if result.returncode == 0:
            return
    except (OSError, subprocess.TimeoutExpired):
        pass
    print("yt-dlp update failed, continuing with the installed version.")
