import nuke

import reset_expose_gain

m_viewer = nuke.menu("Viewer")
m_viewer.addCommand("Zero Viewer", 'reset_expose_gain.reset_expose_gain()', 'alt+e')