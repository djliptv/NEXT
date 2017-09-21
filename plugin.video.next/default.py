# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: NEXT
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.next'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLShKu0sRclF_fn7Yf69tRuq_xcEjEN1wE"
YOUTUBE_CHANNEL_ID_2 = "PLChOO_ZAB22UcOXiE-IO6m7Vm25to6Njg"
YOUTUBE_CHANNEL_ID_3 = "PLO_1AmtK1TMQrdl967xW8z6NiMfuBLdtf"
YOUTUBE_CHANNEL_ID_4 = "PLXLXo07HMXlj6swhszmAX54CNYWRONg76"
YOUTUBE_CHANNEL_ID_5 = "PLwMub1irLfLgV1Wdm09gEEvy-l9iA6KtH"
YOUTUBE_CHANNEL_ID_6 = "PL579BDFCE2C76B890"
YOUTUBE_CHANNEL_ID_7 = "PLIhsN0NS3ECS_N9vIAS6m6v-LkA1WTuEy"
YOUTUBE_CHANNEL_ID_8 = "PLAtuHZ7V5lmvmLtBmU8fQ8rOKLoJz39s4"
YOUTUBE_CHANNEL_ID_9 = "PLFEDB1FF66180AD87"
YOUTUBE_CHANNEL_ID_10 = "PLA_I2ay5YcUUKiZshI4cgp9fTOS-Q6B1E"
YOUTUBE_CHANNEL_ID_11 = "PLSL9DB9AUS4P1v4E1KtXJ1Y2lca7UOdo_"
YOUTUBE_CHANNEL_ID_12 = "PLAFFD17207690FCCB"
YOUTUBE_CHANNEL_ID_13 = "PLF855900B37228AA8" 
YOUTUBE_CHANNEL_ID_14 = "PLlkLqylYSdn8A0NLLeRZPsBPoqPAO4Qu9" 
YOUTUBE_CHANNEL_ID_15 = "PL4iSbgi3WlCpM2bG4ybcZdttLzyWxbEzf"
YOUTUBE_CHANNEL_ID_16 = "PL5viewcavnJRLBTzfr2lotjfbBec_WfsO"
YOUTUBE_CHANNEL_ID_17 = "PLAtuHZ7V5lmuUtrWh3nahsrZIJrZvGnSR" 
YOUTUBE_CHANNEL_ID_18 = "PLDC97A0259A1EFD2E"
YOUTUBE_CHANNEL_ID_19 = "PLeC3KXKbXai5nLfjLi3pVVLIeg58ZaqH5"
YOUTUBE_CHANNEL_ID_20 = "PLBEB584BD45473BDE" 
YOUTUBE_CHANNEL_ID_21 = "PLJaT5gj1oqPRFg3Dd-SV3aQ93EB3kqOxc"
YOUTUBE_CHANNEL_ID_22 = "PLPjGUVv110e9QXFwcPqFaQDwK4YvX56zD"
YOUTUBE_CHANNEL_ID_23 = "PL898D5E9D83F409FA" 
YOUTUBE_CHANNEL_ID_24 = "PLA536BC4F1B31A9C1"
YOUTUBE_CHANNEL_ID_25 = "PL7m5sbJepdm3ockFdYWANXDdAAG7_EdHE"
YOUTUBE_CHANNEL_ID_26 = "PLB9032D4443BB4BC2"
YOUTUBE_CHANNEL_ID_27 = "PLEBC434AD360A2736" 
YOUTUBE_CHANNEL_ID_28 = "PLDC02FA9F86F96406"
YOUTUBE_CHANNEL_ID_29 = "PLpYAMryr-j0U_HN5ekDG47yGZAPp76l6V"
YOUTUBE_CHANNEL_ID_30 = "PL1290CFA5F6423A67"
YOUTUBE_CHANNEL_ID_31 = "PL10100EA06AD634CB"
YOUTUBE_CHANNEL_ID_32 = "PLV4qtz56dfJRpnGD_SYDdaBsIQvmLK8p0"
YOUTUBE_CHANNEL_ID_33 = "PL829D9CD223E56943" 
YOUTUBE_CHANNEL_ID_34 = "PLqK1JpL0Zp67nUaNRno9iVn5nt6IBrAGW"
YOUTUBE_CHANNEL_ID_35 = "PL64953A1F7A8BEB9B"
YOUTUBE_CHANNEL_ID_36 = "PLeMIN33KXnN7MRUXKU7nR_gp1EBBoevxz"
YOUTUBE_CHANNEL_ID_37 = "PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J"
YOUTUBE_CHANNEL_ID_38 = "PL6CM2Se7zfnUtP-AMRsAm-lp-vQ8ZhNeJ" 
YOUTUBE_CHANNEL_ID_39 = "PL69d5IZlV8KHs8xmgpz9B4MbrpSkS8TdO"
YOUTUBE_CHANNEL_ID_40 = "PL5881D08E87DFC944"
YOUTUBE_CHANNEL_ID_41 = "PLVXMccjVOpZrxptx1K9P8-m_2NfkwV2Y4"
YOUTUBE_CHANNEL_ID_42 = "PL0AF81C7A187B0356"
YOUTUBE_CHANNEL_ID_43 = "PL86319EE69F06D828" 
YOUTUBE_CHANNEL_ID_44 = "PL67DF7EA7DDAF6978"
YOUTUBE_CHANNEL_ID_45 = "PLusS9CtXL7ZJELy7rbJ2g3vggC8qVrwOm"
YOUTUBE_CHANNEL_ID_46 = "PLAB1FCDB25219C487"
YOUTUBE_CHANNEL_ID_47 = "PL9FBEE2F34574AF5B"
YOUTUBE_CHANNEL_ID_48 = "PLB90F809164467950"
YOUTUBE_CHANNEL_ID_48 = "PLB90F809164467950"
YOUTUBE_CHANNEL_ID_49 = "PLB495E60E77E742C6"
YOUTUBE_CHANNEL_ID_50 = "PL2F6DF509D3AE319B"
# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]REGGAETON[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ReggaettonThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]2017[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/2017Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HOUSE 2017[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/House2017Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL ULTIMO DE LA FILA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElUltimoDeLaFilaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HOMBRES G[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HombresGThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DANI MARTIN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DaniMartinThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID BISBAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidBisvalThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CAMARÓN DE LA ISLA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CamaronDeLaIslaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CELTAS CORTOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CeltasCortosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FLAMENCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/FlamencoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ESTOPA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EstopaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JOAQUIN SABINA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JoaquinSabinaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL SUEÑO DE MORFEO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElSuenoDeMorfeoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ENRIQUE IGLESIAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EnriqueIglesiasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RAPHAEL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RaphaelThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID BUSTAMANTE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidBustamanteThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ALEJANDRO SANZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AlejandroSanzThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANOLO GARCIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManoloGarciaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ANTONIO OROZCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AntonioOrozcoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ROSARIO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RosarioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANUEL CARRASCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManuelCarrascoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FITO & FITIPALDIS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/FitoYFitipaldisThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MALÚ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MaluThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL BARRIO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElBarrioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MAÍTA VENDE CÁ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MaitaVendeCaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MECANO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MecanoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NAVAJITA PLATEADA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NavajitaPlateadaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DIANA NAVARRO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DianaNavarroThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HUECO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HuecoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MIGUEL BOSÉ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MiguelBoseThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]OBK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ObkThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PABLO ALBORÁN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PabloAlboranThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ANDY & LUCAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AndyYLucasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS DEL RÍO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosDelRioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JOAN MANUEL SERRAT[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JoanManuelSerratThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SERGIO DALMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SergioDalmaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HÉROES DEL SILENCIO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HeroesDelSilencioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RADIO FUTURA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RadioFuturaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DUNCAN DHU[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DuncanDhuThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]M-CLAN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MclanThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MAGO DE OZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MagoDeOzThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EXTREMODURO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ExtremoduroThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOQUILLO Y LOS TROGLODITAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LoquilloYLosTrogloditasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NACHA POP[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NachaPopThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS SECRETOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosSecretosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TRIANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TrianaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS SUAVES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosSuavesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CHAMBAO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ChambaoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JULIO IGLESIAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JulioIglesiasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LA OREJA DE VAN GOGH[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LaOrejaDeVanGoghThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )
run()