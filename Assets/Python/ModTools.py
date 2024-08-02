# Console Functions -- Adds various functions for modders to access in the console

from CvPythonExtensions import *
import CvUtil

gc = CyGlobalContext()

#spawns a unit of every unitclass for all civs that are alive in a game
def showUnits():

	for iPlayer in range(0,int(gc.getMAX_PLAYERS())):
		pPlayer = gc.getPlayer(iPlayer)
		if (pPlayer.isAlive() and not pPlayer.isBarbarian()):
			kCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
			for iUnitClass in range( gc.getNumUnitClassInfos() ):
				eLoopUnit = kCivilization.getCivilizationUnits(iUnitClass)
				if (eLoopUnit != -1):
					x = iUnitClass%10 + 1 + iPlayer*12
					y = (iUnitClass/10) + 5
					gc.getMap().plot( x, y ).setTerrainType(CvUtil.findInfoTypeNum(gc.getTerrainInfo, gc.getNumTerrainInfos(), "TERRAIN_OCEAN"), 1, 1)
					pPlayer.initUnit( eLoopUnit, x, y, UnitAITypes.UNITAI_UNKNOWN, DirectionTypes.NO_DIRECTION )


#spawns a unit of the specified unitclass for all civilization in the game
def showUnitClass(UnitClass):

	iUnitClass = gc.getInfoTypeForString(UnitClass)

	for iPlayer in range(0,int(gc.getMAX_PLAYERS())):
		if (gc.getPlayer(iPlayer).isAlive() and not gc.getPlayer(iPlayer).isBarbarian()):
			eUnit = gc.getCivilizationInfo(gc.getPlayer(iPlayer).getCivilizationType()).getCivilizationUnits(iUnitClass)
			if (eUnit != -1):
				x = eUnit%10 + 1 + iPlayer
				y = (eUnit/10) + 5
				gc.getMap().plot( x, y ).setTerrainType(CvUtil.findInfoTypeNum(gc.getTerrainInfo, gc.getNumTerrainInfos(), "TERRAIN_OCEAN"), 1, 1)
				gc.getPlayer(iPlayer).initUnit( eUnit, x, y, UnitAITypes.UNITAI_UNKNOWN, DirectionTypes.NO_DIRECTION )


#Advances all civs 1 era from the era of the most advanced civ
def advanceEra():

	gameEra = 0
	for iPlayer in range(0,int(gc.getMAX_PLAYERS())):
		if (gc.getPlayer(iPlayer).isAlive() and not gc.getPlayer(iPlayer).isBarbarian()):
			teamEra = 0
			pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
			for iTech in range( 0,int(gc.getNumTechInfos()) ):
				if pTeam.isHasTech(iTech) :
					techEra = gc.getTechInfo(iTech).getEra()
					if techEra > teamEra:
						teamEra = techEra
			if teamEra > gameEra:
				gameEra = teamEra
	targetEra = gameEra + 1

	for iPlayer in range(0,int(gc.getMAX_PLAYERS())):
		if (gc.getPlayer(iPlayer).isAlive() and not gc.getPlayer(iPlayer).isBarbarian()):
			pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		if targetEra <= gc.getNumEraInfos():
			for iTech in range( 0,int(gc.getNumTechInfos()) ):
				if gc.getTechInfo(iTech).getEra() <= targetEra:
					pTeam.setHasTech(iTech,True,iPlayer,False,False)
