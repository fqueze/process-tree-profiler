# process-tree-profiler
Visualize in the Firefox Profiler the processes that are running, along with resource use.

This repository extracts the [mozilla-central resource monitoring code](https://searchfox.org/mozilla-central/source/testing/mozbase/mozsystemmonitor/mozsystemmonitor/resourcemonitor.py) so that it can be used outside Mozilla builds.

# Usage

- Ensure psutil is available (`pip install psutil` if needed).
- Start the profiler: `python process-tree-profiler.py`
- Do whatever it is you want to profile.
- Stop the profiler using Ctrl-c to capture the profile. A Firefox Profiler tab will open in the default browser with the data that was recorded.

Example profile: https://share.firefox.dev/44wq7EH
