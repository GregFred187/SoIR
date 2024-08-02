# DLL Data Loader by edead

from CvPythonExtensions import *
import Consts as con
import Maps as maps
import SorenRand as random

gc = CyGlobalContext()

def setup():
	"""Loads the data from Consts.py and Maps.py into appriopriate objects within CvGameCoreDLL."""
	
	# Rhye's Catapult
	gc.getGame().setCatapultXY(con.iCatapultX, con.iCatapultY)
	
	# Region (province) and art style maps
	map = CyMap()
	for y in range(len(maps.regions)):
		for x in range(len(maps.regions[y])):
			plot = map.plot(x, len(maps.regions) - 1 - y) # because Civ4 maps are reversed on Y-axis
			if plot:
				plot.setRegionID(maps.regions[y][x])
				if len(maps.artStyles) > y and len(maps.artStyles[y]) > x:
					# Set the value in CvPlot instance
					plot.setArtStyleType(maps.artStyles[y][x])
	
	# Settlers maps
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		if len(maps.settlersMaps) > iLoopPlayer:
			for y in range(len(maps.settlersMaps[iLoopPlayer])):
				for x in range(len(maps.settlersMaps[iLoopPlayer][y])):
					plot = map.plot(x, len(maps.settlersMaps[iLoopPlayer]) - 1 - y) # because Civ4 maps are reversed on Y-axis
					if plot:
						iValue = maps.settlersMaps[iLoopPlayer][y][x]
						# Randomize found modifiers (0-50 in RFC, only for values >= 150)
						if iValue >= 400:
							iValue += random.randint(-90, 90)
						elif iValue >= 300:
							iValue += random.randint(-80, 80)
						elif iValue >= 150:
							iValue += random.randint(-60, 60)
						elif iValue >= 60:
							iValue += random.randint(-30, 30)
						elif iValue >= 40:
							iValue += random.randint(-20, 20)
						# Set the value in CvPlot instance
						plot.setFoundModifier(iLoopPlayer, iValue)
	
	# RFC Borders & Permanent Attitude Modifiers
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()): 
		player = gc.getPlayer(iLoopPlayer)
		if len(con.tBorders) > iLoopPlayer:
			for iOtherPlayer in range(gc.getMAX_CIV_PLAYERS()): 
				if len(con.tBorders[iLoopPlayer]) > iOtherPlayer:
					player.setBorders(iOtherPlayer, con.tBorders[iLoopPlayer][iOtherPlayer])
		if len(con.tAttitudeModifier) > iLoopPlayer:
			for iOtherPlayer in range(gc.getMAX_CIV_PLAYERS()): 
				if len(con.tAttitudeModifier[iLoopPlayer]) > iOtherPlayer:
					player.setAttitudeModifier(iOtherPlayer, con.tAttitudeModifier[iLoopPlayer][iOtherPlayer])	
	
	# Start Year & RFC Balance
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()): 
		player = gc.getPlayer(iLoopPlayer)
		if len(con.tBirth) > iLoopPlayer:
			player.setStartYear(con.tBirth[iLoopPlayer])
		if len(con.tInflationPercent) > iLoopPlayer:
			player.changeInflationModifier(-(100 - con.tInflationPercent[iLoopPlayer]))
		if len(con.tGrowthPercent) > iLoopPlayer:
			player.setGrowthPercent(con.tGrowthPercent[iLoopPlayer])
		if len(con.tProductionPercent) > iLoopPlayer:
			player.setProductionPercent(con.tProductionPercent[iLoopPlayer])
		if len(con.tResearchPercent) > iLoopPlayer:
			player.setResearchPercent(con.tResearchPercent[iLoopPlayer])
		if len(con.tEspionagePercent) > iLoopPlayer:
			player.setEspionagePercent(con.tEspionagePercent[iLoopPlayer])
		if len(con.tGreatPeoplePercent) > iLoopPlayer:
			player.setGreatPeoplePercent(con.tGreatPeoplePercent[iLoopPlayer])
		if len(con.tCulturePercent) > iLoopPlayer:
			player.setCulturePercent(con.tCulturePercent[iLoopPlayer])			
		if len(con.tNumCitiesMaintenancePercent) > iLoopPlayer:
			player.changeNumCitiesMaintenanceModifier(-(100 - con.tNumCitiesMaintenancePercent[iLoopPlayer]))
		if len(con.tDistanceMaintenancePercent) > iLoopPlayer:
			player.changeDistanceMaintenanceModifier(-(100 - con.tDistanceMaintenancePercent[iLoopPlayer]))
		if len(con.tCompactEmpireModifier) > iLoopPlayer:
			player.AI_setCompactEmpireModifier(con.tCompactEmpireModifier[iLoopPlayer])
		if len(con.tMassacreProb) > iLoopPlayer:
			player.AI_setMassacreProb(con.tMassacreProb[iLoopPlayer])
		if len(con.tBuildPersecutorProb) > iLoopPlayer:
			player.AI_setBuildPersecutorProb(con.tBuildPersecutorProb[iLoopPlayer])
		if len(con.tWarDistanceModifier) > iLoopPlayer:
			player.AI_setWarDistanceModifier(con.tWarDistanceModifier[iLoopPlayer])
		if len(con.tWarCoastalModifier) > iLoopPlayer:
			player.AI_setWarCoastalModifier(con.tWarCoastalModifier[iLoopPlayer])
		if len(con.tMaxTakenTiles) > iLoopPlayer:
			player.AI_setMaxTakenTiles(con.tMaxTakenTiles[iLoopPlayer])
		# Religion spreads
		for iReligion in range(len(con.tReligionSpreadPercent[iLoopPlayer])):
			player.setReligionSpreadPercent(iReligion, con.tReligionSpreadPercent[iLoopPlayer][iReligion])