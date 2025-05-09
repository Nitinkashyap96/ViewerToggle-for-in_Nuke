####################################--------------------------------------------######################################
# ----- SET 'ALT+E' TO TOGGLE VIEWER EXPOSURE/GAMMA SATURATION----------------
#---------------------Python Update Nuke 15 & 16  version -------------------------#


########################################
#           TO TOGGLE VIEWE            #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#                                      #
#         Author: Nitin Kashyap        #
#                                      #
#                                      #
########################################

import nuke

nuke.tprint('toggle viewer'
            ' loading: Resetviewer')


_viewer_prev_settings = {'gain': 1, 'gamma': 1, 'saturation': 1}

def reset_expose_gain():
    global _viewer_prev_settings

    # Get magic ViewerWindow node
    viewer = nuke.activeViewer()

    # Get regular Viewer node which contains
    # exposure knob and such
    node = viewer.node()


    curgain = node['gain'].value()
    curgamma = node['gamma'].value()
    cursaturation = node['saturation'].value()

    if curgain != 1.0 or curgamma != 1.0 or cursaturation != 1.0:
        # Values are non-default, store them in memory
        _viewer_prev_settings['gain'] = curgain
        _viewer_prev_settings['gamma'] = curgamma
        _viewer_prev_settings['saturation'] = cursaturation

        # Reset to defaults
        node['gain'].setValue(1)
        node['gamma'].setValue(1)
        node['saturation'].setValue(1)
    else:
        # Values are default, restore previous settings if any
        node['gain'].setValue(_viewer_prev_settings['gain'])
        node['gamma'].setValue(_viewer_prev_settings['gamma'])
        node['saturation'].setValue(_viewer_prev_settings['saturation'])
####################################--------------------------------------------######################################
