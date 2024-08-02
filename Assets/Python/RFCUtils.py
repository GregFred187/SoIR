# Rhye's and Fall of Civilization - Utilities

from CvPythonExtensions import *
import CvUtil
import CvScreenEnums
import PyHelpers
import Popup
import Consts as con
import UnitArtStyler
import re
from StoredData import sd
from random import shuffle
from operator import itemgetter

# globals
gc = CyGlobalContext()
localText = CyTranslator()
ArtFileMgr = CyArtFileMgr()
PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers
iNumMinorPlayers = con.iNumMinorPlayers
iNumTotalPlayers = con.iBarbarian

tCol = (
'255,255,255',
'200,200,200',
'150,150,150',
'128,128,128')

class RFCUtils:

	bStabilityOverlay = False

	#Rise and fall, stability
	def getLastTurnAlive( self, iCiv ):
		return sd.getLastTurnAlive(iCiv)

	def setLastTurnAlive( self, iCiv, iNewValue ):
		sd.setLastTurnAlive(iCiv, iNewValue)

	#Victory
	def getGoal( self, i, j ):
		return sd.getGoal(i, j)

	def setGoal( self, i, j, iNewValue ):
		sd.setGoal(i, j, iNewValue)

	#Stability
	def getTempFlippingCity( self ):
		return sd.getTempFlippingCity()

	def setTempFlippingCity( self, tNewValue ):
		sd.setTempFlippingCity(tNewValue)

	def getStability( self, iCiv ):
		return sd.getStability(iCiv)

	def setStability( self, iCiv, iNewValue ):
		sd.setStability(iCiv, iNewValue)

	def getBaseStabilityLastTurn( self, iCiv ):
		return sd.getBaseStabilityLastTurn(iCiv)

	def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
		sd.setBaseStabilityLastTurn(iCiv, iNewValue)

	def getStabilityParameters( self, iParameter ):
		return sd.getStabilityParameters(iParameter)

	def setStabilityParameters( self, iParameter, iNewValue ):
		sd.setStabilityParameters(iParameter, iNewValue)

	def getLastRecordedStabilityStuff( self, iParameter ):
		return sd.getLastRecordedStabilityStuff(iParameter)

	def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
		sd.setLastRecordedStabilityStuff(iParameter, iNewValue)

	#Plague
	def getPlagueCountdown( self, iCiv ):
		return sd.getPlagueCountdown(iCiv)

	def setPlagueCountdown( self, iCiv, iNewValue ):
		sd.setPlagueCountdown(iCiv, iNewValue)

	#Religions
	def getBasePiety(self, iCiv):
		return sd.getBasePiety(iCiv)

	def setBasePiety(self, iCiv, iNewValue):
		sd.setBasePiety(iCiv, iNewValue)

	def getPiety(self, iCiv):
		return sd.getPiety(iCiv)

	def getRealPiety(self, iCiv):
		return sd.getPiety(iCiv)

	def setPiety(self, iCiv, iNewValue):
		sd.setPiety(iCiv, iNewValue)

	# edead: Dynamic Civ Names
	def getCivStatus(self, iCiv):
		return sd.getCivStatus(iCiv)

	def setCivStatus(self, iCiv, iNewValue):
		sd.setCivStatus(iCiv, iNewValue)

	# edead: Traits/UPs
	def getNumCrusades(self):
		return sd.getNumCrusades()

	def setNumCrusades(self, iNewValue):
		sd.setNumCrusades(iNewValue)

	def isHasLostCity(self, iCiv):
		return sd.isHasLostCity(iCiv)

	def setHasLostCity(self, iCiv, iNewValue):
		sd.setHasLostCity(iCiv, iNewValue)

	def getLastCrusadeTurn(self, iCiv):
		return sd.getLastCrusadeTurn(iCiv)

	def setLastCrusadeTurn(self, iCiv, iNewValue):
		sd.setLastCrusadeTurn(iCiv, iNewValue)

	def getSeed( self ):
		return sd.getSeed()
	
	def getRandomCivList( self ):
		return sd.getRandomCivList()

#######################################

	# Stability, RiseNFall, CvFinanceAdvisor
	def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
		if (gc.getPlayer(iPlayer).isHuman()):
			if (bPreviousAmount):
				self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
			else:
				self.setStabilityParameters(iParameter, 0 + iAmount)


	def setStartingStabilityParameters(self, iCiv):
		
		iHandicap = gc.getGame().getHandicapType()
		
		for i in range(con.iNumStabilityParameters):
			self.setStabilityParameters(i, 0)
		
		if (iHandicap == 0):
			self.setStability(iCiv, 20)
			self.setParameter(iCiv, con.iParCitiesE, True, 4)
			self.setParameter(iCiv, con.iParCivicsE, True, 4)
			self.setParameter(iCiv, con.iParDiplomacyE, True, 4)
			self.setParameter(iCiv, con.iParEconomyE, True, 4)
			self.setParameter(iCiv, con.iParExpansionE, True, 4) 
		elif (iHandicap == 1):
			self.setStability(iCiv, 5)
			self.setParameter(iCiv, con.iParCitiesE, True, 1)
			self.setParameter(iCiv, con.iParCivicsE, True, 1)
			self.setParameter(iCiv, con.iParDiplomacyE, True, 1)
			self.setParameter(iCiv, con.iParEconomyE, True, 1)
			self.setParameter(iCiv, con.iParExpansionE, True, 1) 
		elif (iHandicap == 2):
			self.setStability(iCiv, -10)
			self.setParameter(iCiv, con.iParCitiesE, True, -2)
			self.setParameter(iCiv, con.iParCivicsE, True, -2)
			self.setParameter(iCiv, con.iParDiplomacyE, True, -2)
			self.setParameter(iCiv, con.iParEconomyE, True, -2)
			self.setParameter(iCiv, con.iParExpansionE, True, -2) 


	# CvFinanceAdvisor
	def getParCities(self):
		if (self.getStabilityParameters(con.iParCitiesE) > 7):
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParCitiesE) < -7):
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE)


	def getParCivics(self):
		if (self.getStabilityParameters(con.iParCivicsE) > 7):
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParCivicsE) < -7):
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE)


	def getParDiplomacy(self):
		if (self.getStabilityParameters(con.iParDiplomacyE) > 7):
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParDiplomacyE) < -7):
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE)


	def getParEconomy(self):
		#print ("ECO", self.getStabilityParameters(con.iParEconomy3), self.getStabilityParameters(con.iParEconomy1), self.getStabilityParameters(con.iParEconomyE))
		if (self.getStabilityParameters(con.iParEconomyE) > 7):
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParEconomyE) < -7):
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE)


	def getParExpansion(self):
		if (self.getStabilityParameters(con.iParExpansionE) > 7):
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) - gc.getActivePlayer().getCurrentEra()
		elif (self.getStabilityParameters(con.iParExpansionE) < -7):
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) + gc.getActivePlayer().getCurrentEra()
		else:
			return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE)


	def getArrow(self, iParameter):
		if (iParameter == 0):
			if (self.getStability(self.getHumanID()) >= self.getLastRecordedStabilityStuff(iParameter) + 6):
				return 1
			elif (self.getStability(self.getHumanID()) <= self.getLastRecordedStabilityStuff(iParameter) - 6):
				return -1
			else:
				return 0
		else:
			if (iParameter == 1):
				iNewValue = self.getParCities()
			elif (iParameter == 2):
				iNewValue = self.getParCivics()
			elif (iParameter == 3):
				iNewValue = self.getParEconomy()
			elif (iParameter == 4):
				iNewValue = self.getParExpansion()
			elif (iParameter == 5):
				iNewValue = self.getParDiplomacy()
			if (iNewValue >= self.getLastRecordedStabilityStuff(iParameter) + 4):
				return 1
			elif (iNewValue <= self.getLastRecordedStabilityStuff(iParameter) - 4):
				return -1
			else:
				return 0


	#Victory
	def countAchievedGoals(self, iPlayer):
		iResult = 0
		for j in range(3):                        
			#iTemp = self.getGoal(iPlayer, j)
			#if (iTemp < 0):
			#        iTemp = 0
			#iResult += iTemp
			if (self.getGoal(iPlayer, j) == 1):
					iResult += 1
		return iResult

	def getGoalsColor(self, iPlayer): #by CyberChrist
		iCol = 0
		for j in range(3):
			if (self.getGoal(iPlayer, j) == 0):
				iCol += 1
		return tCol[iCol]


	def showPopup(self, popupID, title, message, labels):
		"""popupID has to be a registered ID in CvRhyesCatapultEventManager.__init__!"""
		
		popup = Popup.PyPopup(popupID, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(title)
		popup.setBodyString(message)
		for i in labels:
			popup.addButton(i)
		popup.launch(False)


	def getYear(self):
		return gc.getGame().getGameTurnYear()


	def getTurns(self, turns):
			"""Returns the amount of turns modified adequately for the game's speed.
			Values are based on CIV4GameSpeedInfos.xml. Use this only for durations, intervals etc.; 
			for year->turn conversions, use the DLL function getTurnForYear(int year)."""
			iGameSpeed = gc.getGame().getGameSpeedType()
			if iGameSpeed == 1: return turns # normal
			elif iGameSpeed == 0: # epic
					if turns == 3: return 5 # getTurns(6) must be a multiple of getTurns(3) for turn divisors in Stability.py
					elif turns == 6: return 10
					else: return turns*3/2
			#elif iGameSpeed == 0: return turns*3 # marathon
			#elif iGameSpeed == 3: return turns*2/3 # quick
			return turns


	def isActive(self, iPlayer):
		"""Returns true if the player is spawned and alive."""
		
		if gc.getPlayer(iPlayer).getNumCities() < 1: return False
		if not gc.getPlayer(iPlayer).isAlive: return False
		if self.getYear() < con.tBirth[iPlayer]: return False
		return True


	# from SdToolkit
	def echo(self, echoString):
		printToScr = True
		printToLog = True
		message = "%s" %(echoString)
		if (printToScr):
			CyInterface().addImmediateMessage(message,"")
		if (printToLog):
			CvUtil.pyPrint(message)
		return 0

		
	def getCoreRegions(self, iCiv):
		if sd.getCivStatus(iCiv) > 0:
			return con.lRespawnRegions[iCiv][:]
		return con.lCoreRegions[iCiv][:]

		
	def getNormalRegions(self, iCiv):
		if sd.getCivStatus(iCiv) > 0:
			return con.lRespawnNormalRegions[iCiv][:]
		return con.lNormalRegions[iCiv][:]
		
		
	def getBroaderRegions(self, iCiv):
		if sd.getCivStatus(iCiv) > 0:
			result = con.lRespawnBroaderRegions[iCiv][:]
		else: 
			result = con.lBroaderRegions[iCiv][:]
		if gc.getTeam(gc.getPlayer(iCiv).getTeam()).getProjectCount(con.iRaja) > 0 and gc.getPlayer(iCiv).getStateReligion() == con.iHinduism:
			result.extend(con.lTitleRegions[con.iRaja])
			self.uniq(result)
		return result

	
	# Temp function for compatibility with some RFC routines
	def getAreaPlotList(self, tTopLeft, tBottomRight):
		"""Converts the RFC-style rectangular area to a list of tuples."""
		
		map = CyMap()
		plotList = []
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				if map.isPlot(x, y):
					plotList.append((x, y))
		return plotList


	def getRegionPlotList(self, lRegions, bBorder = False):
		"""Returns a list of all plots in listed regions, optionally with borders for visible coastline."""
		
		plotList = []
		map = CyMap()
		for i in range(map.numPlots()):
			plot = map.plotByIndex(i)
			if plot.getRegionID() in lRegions:
				px = plot.getX()
				py = plot.getY()
				if not bBorder:
					plotList.append((px, py))
				else:
					for x in range(px-1, px+2):
						for y in range(py-1, py+2):
							if (x, y) not in plotList: 
								plotList.append((x, y))
		return plotList


	def getCorePlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core regions."""

		return self.getRegionPlotList(self.getCoreRegions(iCiv), bBorder)


	def getNormalPlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core + normal regions."""
		
		return self.getRegionPlotList(self.getCoreRegions(iCiv) + self.getNormalRegions(iCiv), bBorder)


	def getBroaderPlotList(self, iCiv, bBorder = False):
		"""Returns a list of all plots in core + normal + broader regions."""
		
		return self.getRegionPlotList(self.getCoreRegions(iCiv) + self.getNormalRegions(iCiv) + self.getBroaderRegions(iCiv), bBorder)


	def coverPlots(self, plotX, plotY, iCiv):
		"""Covers the plots revealed by RFC catapult and flipped units."""
		
		for x in range(plotX-1, plotX+2):
			for y in range(plotY-1, plotY+2):
				gc.getMap().plot(x, y).setRevealed(iCiv, False, True, -1)

				
	def revealPlots(self, iCiv, plotList):
		"""Reveals all plots on the list."""
		
		iTeam = gc.getPlayer(iCiv).getTeam()
		for i in range(len(plotList)):
			gc.getMap().plot(plotList[i][0], plotList[i][1]).setRevealed(iTeam, True, False, -1)


	def revealCity(self, iCiv, tCoords):
		"""Reveals the specified city plot and its fat cross."""
		
		iTeam = gc.getPlayer(iCiv).getTeam()
		for x in range(tCoords[0]-2, tCoords[0]+3):
			for y in range(tCoords[1]-2, tCoords[1]+3):
				gc.getMap().plot(x, y).setRevealed(iTeam, True, False, -1)
				

	def getRegionStabilityLevel(self, iCiv, iRegionID):
		"""Returns stability level for the given region."""
		
		if iRegionID in con.lCoreRegions[iCiv]:
			return 4 # core
		elif iRegionID in self.getNormalRegions(iCiv) or iRegionID in self.getBroaderRegions(iCiv):
			for iLoopCiv in range(con.iNumPlayers):
				if iLoopCiv != iCiv and iRegionID in self.getCoreRegions(iLoopCiv):
					if gc.getGame().getGameTurn() >= getTurnForYear(con.tBirth[iLoopCiv]) and gc.getGame().getGameTurn() <= getTurnForYear(con.tFall[iLoopCiv]):
						return 2 # contested
			return 3 # border
		else:
			for iLoopCiv in range(con.iNumPlayers):
				if iLoopCiv != iCiv and iRegionID in self.getCoreRegions(iLoopCiv):
					if gc.getGame().getGameTurn() >= getTurnForYear(con.tBirth[iLoopCiv]) and gc.getGame().getGameTurn() <= getTurnForYear(con.tFall[iLoopCiv]):
						return 0 # foreign
			return 1 # none


	def getRandomMinorCiv(self):
		"""Returns a random minor civilization."""
		
		return con.iIndependent + gc.getGame().getSorenRandNum(iNumMinorPlayers, 'Random minor civilization')


	# Religions
	def getFavorLevel(self, iPlayer):
		"""Returns the appropriate level (0-10) for piety amount (0-100)."""
		
		iPiety = self.getPiety(iPlayer)
		if iPiety < 0:
			return -1
		elif iPiety == 100:
			return 10
		
		for i in range(len(con.lFavorLevels)):
			if iPiety < con.lFavorLevels[i]:
				break
		
		return i-1


	# Religions
	def getFavorLevelText(self, iPlayer):
		"""Returns the description for a given favor level."""
		
		iFavorLevel = self.getFavorLevel(iPlayer)
		if iFavorLevel < 0:
			return -1
		else:
			return localText.getText(con.lFavorLevelsText[iFavorLevel], ())


# RFCUtils

	#AIWars
	def checkUnitsInEnemyTerritory(self, iCiv1, iCiv2): 
		unitList = PyPlayer(iCiv1).getUnitList()
		if(len(unitList)):
			for unit in unitList:
				iX = unit.getX()
				iY = unit.getY()
				if (gc.getMap().plot( iX, iY ).getOwner() == iCiv2):
					return True
			return False


	#AIWars
	def restorePeaceAI(self, iMinorCiv, bOpenBorders):
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		for iActiveCiv in range( iNumPlayers ):
			if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
				if (teamMinor.isAtWar(iActiveCiv)):
					bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
					bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)
					if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):
						teamMinor.makePeace(iActiveCiv)
						#print ("Minor peace", gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))
						if (bOpenBorders):
							teamMinor.signOpenBorders(iActiveCiv)


	#AIWars
	def restorePeaceHuman(self, iMinorCiv, bOpenBorders): 
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		for iActiveCiv in range( iNumPlayers ):
			if (gc.getPlayer(iActiveCiv).isHuman()):
				if (gc.getPlayer(iActiveCiv).isAlive()):
					if (teamMinor.isAtWar(iActiveCiv)):
						bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
						bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)
						if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):
							teamMinor.makePeace(iActiveCiv)
					return


	#AIWars
	def minorWars(self, iMinorCiv):
		teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
		apCityList = PyPlayer(iMinorCiv).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			x = city.getX()
			y = city.getY()
			for iActiveCiv in range( iNumPlayers ):
				if gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman():
					if iActiveCiv == con.iRum and sd.getCivStatus(iActiveCiv) > 0: # skip Karamanids to make them more passive
						continue
					regionList = []
					regionList.extend(self.getCoreRegions(iActiveCiv))
					regionList.extend(self.getNormalRegions(iActiveCiv))
					regionList.extend(self.getBroaderRegions(iActiveCiv))
					if gc.getMap().plot(x, y).getRegionID() in regionList:
						if (not teamMinor.isAtWar(iActiveCiv)):
							teamMinor.declareWar(iActiveCiv, False, WarPlanTypes.WARPLAN_LIMITED)
							#print ("Minor war", city.getName(), gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))


	# RiseAndFall, Stability
	def calculateDistance(self, x1, y1, x2, y2):
		dx = abs(x2-x1)
		dy = abs(y2-y1)
		return max(dx, dy)


	# RiseAndFall
	def updateMinorTechs(self, iMinorCiv, iMajorCiv):
		"""Gives all techs of iMajorCiv to iMinorCiv."""
		
		for t in range(con.iNumTechs):
			if (gc.getTeam(gc.getPlayer(iMajorCiv).getTeam()).isHasTech(t)):
				gc.getTeam(gc.getPlayer(iMinorCiv).getTeam()).setHasTech(t, True, iMinorCiv, False, False)


	# RiseAndFall, Religions, Barbs
	def makeUnit(self, iUnit, iPlayer, tCoords, iNum, eUnitAIType = UnitAITypes.NO_UNITAI, tPromotions = False, prefix = False): #by LOQ/edead
		"""Makes iNum units for player iPlayer of the type iUnit at tCoords."""
		
		if iUnit == -1: return None # edead
		
		pUnit = None
		for i in range(iNum):
			pUnit = gc.getPlayer(iPlayer).initUnit(iUnit, tCoords[0], tCoords[1], eUnitAIType, DirectionTypes.DIRECTION_SOUTH)
			if pUnit:
				UnitArtStyler.checkUnitArt(pUnit) # update unit art
				if tPromotions:
					for j in tPromotions:
						pUnit.setHasPromotion(j, True)
				if prefix:
					pUnit.setName("%s %s" %(prefix, pUnit.getName()))
		return pUnit


	# RiseAndFall, Religions
	def getHumanID(self):
		return gc.getGame().getActivePlayer()


	# RiseAndFall
	def flipUnitsInCityBefore(self, tCityPlot, iNewOwner, iOldOwner):
		#print ("tCityPlot Before", tCityPlot)
		plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
		city = plotCity.getPlotCity()
		iNumUnitsInAPlot = plotCity.getNumUnits()
		j = 0
		for i in range(iNumUnitsInAPlot):
			unit = plotCity.getUnit(j)
			unitType = unit.getUnitType()
			if (unit.getOwner() == iOldOwner):
				unit.kill(False, con.iBarbarian)
				if (iNewOwner < con.iNumPlayers or unitType > con.iSettler):
					self.makeUnit(self.getBaseUnit(unitType, iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1) # edead
			else:
				j += 1


	# RiseAndFall
	def flipUnitsInCityAfter(self, tCityPlot, iCiv):
		#moves new units back in their place
		print ("tCityPlot After", tCityPlot)
		tempPlot = gc.getMap().plot(con.iFlipX, con.iFlipY)
		if (tempPlot.getNumUnits() != 0):
			iNumUnitsInAPlot = tempPlot.getNumUnits()
			#print ("iNumUnitsInAPlot", iNumUnitsInAPlot)
			for i in range(iNumUnitsInAPlot):
				unit = tempPlot.getUnit(0)
				unit.setXY(tCityPlot[0], tCityPlot[1], False, False, False)
		#cover plots revealed
		self.coverPlots(con.iFlipX, con.iFlipY, iCiv)


	# Leaving it as it is, since it's only used for the whole map
	def killUnitsInArea(self, tTopLeft, tBottomRight, iCiv):
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				killPlot = gc.getMap().plot(x,y)
				iNumUnitsInAPlot = killPlot.getNumUnits()
				if (iNumUnitsInAPlot):
					for i in range(iNumUnitsInAPlot):
						unit = killPlot.getUnit(0)
						if (unit.getOwner() == iCiv):
							unit.kill(False, con.iBarbarian)


	# RiseAndFall
	def flipUnitsInArea(self, plotList, iNewOwner, iOldOwner, bSkipPlotCity, bKillSettlers, bSkipOwned=False):
				"""Deletes, recreates units in 0,67 and moves them to the previous tile.
				If there are units belonging to others in that plot and the new owner is barbarian, the units aren't recreated.
				Settlers aren't created.
				If bSkipPlotCity is True, units in a city won't flip. This is to avoid converting barbarian units that would capture a city before the flip delay"""
				
				for iLoop in range(len(plotList)):
					killPlot = gc.getMap().plot(plotList[iLoop][0], plotList[iLoop][1])
					if bSkipOwned and killPlot.getOwner() < iNumPlayers and killPlot.getOwner() != utils.getHumanID(): # edead
						continue
					iNumUnitsInAPlot = killPlot.getNumUnits()
					if (iNumUnitsInAPlot):
						bRevealedZero = False
						if (gc.getMap().plot(con.iFlipX, con.iFlipY).isRevealed(iNewOwner, False)):
							bRevealedZero = True
						#print ("killplot", plotList[iLoop][0], plotList[iLoop][1])
						if (bSkipPlotCity == True) and (killPlot.isCity()):
							#print (killPlot.isCity())
							#print 'do nothing'
							pass
						else:
							j = 0
							for i in range(iNumUnitsInAPlot):
								unit = killPlot.getUnit(j)
								#print ("killplot", plotList[iLoop][0], plotList[iLoop][1], unit.getUnitType(), unit.getOwner(), "j", j)
								if (unit.getOwner() == iOldOwner):
									unit.kill(False, con.iBarbarian)
									if (bKillSettlers):
										if ((unit.getUnitType() > con.iSettler)):
											if unit.getUnitType() not in [con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight, con.iManAtArms, con.iKnightOfJerusalem, con.iNormanKnight, con.iVarangianGuard, con.iGreekFlamethrower]: # edead
												self.makeUnit(self.getBaseUnit(unit.getUnitType(), iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1)
									else:
										if ((unit.getUnitType() >= con.iSettler)): #skip animals
											if unit.getUnitType() not in [con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight, con.iManAtArms, con.iKnightOfJerusalem, con.iNormanKnight, con.iVarangianGuard, con.iGreekFlamethrower]: # edead
												self.makeUnit(self.getBaseUnit(unit.getUnitType(), iNewOwner), iNewOwner, [con.iFlipX, con.iFlipY], 1)
								else:
										j += 1
							tempPlot = gc.getMap().plot(con.iFlipX, con.iFlipY)
							#moves new units back in their place
							if (tempPlot.getNumUnits() != 0):
								iNumUnitsInAPlot = tempPlot.getNumUnits()
								for i in range(iNumUnitsInAPlot):
									unit = tempPlot.getUnit(0)
									#print ("Moving unit from ", unit.getNameNoDesc(), con.iFlipX, con.iFlipY)
									#print ("Moving unit to ", plotList[iLoop][0], plotList[iLoop][1])
									unit.setXY(plotList[iLoop][0], plotList[iLoop][1], False, False, False)
								iCiv = iNewOwner
								if (bRevealedZero == False):
									self.coverPlots(con.iFlipX, con.iFlipY, iCiv)


	# RiseAndFall
	def flipCity(self, tCityPlot, bFlipType, bKillUnits, iNewOwner, iOldOwners):
		"""Changes owner of city specified by tCityPlot.
		bFlipType specifies if it's conquered or traded.
		If bKillUnits != 0 all the units in the city will be killed.
		iRetainCulture will determine the split of the current culture between old and new owner. -1 will skip
		iOldOwners is a list. Flip happens only if the old owner is in the list.
		An empty list will cause the flip to always happen."""
		pNewOwner = gc.getPlayer(iNewOwner)
		city = gc.getMap().plot(tCityPlot[0], tCityPlot[1]).getPlotCity()
		if (gc.getMap().plot(tCityPlot[0], tCityPlot[1]).isCity()):
			if not city.isNone():
				iOldOwner = city.getOwner()
				if (iOldOwner in iOldOwners or not iOldOwners):
					if (bKillUnits):
						killPlot = gc.getMap().plot( tCityPlot[0], tCityPlot[1] )
						for i in range(killPlot.getNumUnits()):
							unit = killPlot.getUnit(0)
							unit.kill(False, iNewOwner)
					
					if (bFlipType): #conquest
						if (city.getPopulation() == 2):
							city.setPopulation(3)
						if (city.getPopulation() == 1):
							city.setPopulation(2)
						pNewOwner.acquireCity(city, True, False)
					else: #trade
						pNewOwner.acquireCity(city, False, True)
					
					return True
		return False


	#Congresses, RiseAndFall
	def cultureManager(self, tCityPlot, iCulturePercent, iNewOwner, iOldOwner, bBarbarian2x2Decay, bBarbarian2x2Conversion, bAlwaysOwnPlots):
				"""Converts the culture of the city and of the surrounding plots to the new owner of a city.
				iCulturePercent determine the percentage that goes to the new owner.
				If old owner is barbarian, all the culture is converted"""
				
				pCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
				city = pCity.getPlotCity()
				
				#city
				if (pCity.isCity()):
						iCurrentCityCulture = city.getCulture(iOldOwner)
						city.setCulture(iOldOwner, iCurrentCityCulture*(100-iCulturePercent)/100, False)
						if (iNewOwner != con.iBarbarian):
								city.setCulture(con.iBarbarian, 0, True)
						city.setCulture(iNewOwner, iCurrentCityCulture*iCulturePercent/100, False)
						if (city.getCulture(iNewOwner) <= 10):
								city.setCulture(iNewOwner, 20, False)
				
				#halve barbarian culture in a broader area
				if (bBarbarian2x2Decay or bBarbarian2x2Conversion):
					if (iNewOwner < iNumPlayers):
						for x in range(tCityPlot[0]-2, tCityPlot[0]+3):		# from x-2 to x+2
							for y in range(tCityPlot[1]-2, tCityPlot[1]+3):	# from y-2 to y+2
								iPlotBarbCulture = gc.getMap().plot(x, y).getCulture(con.iBarbarian)
								if (iPlotBarbCulture > 0):
									if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
										if (bBarbarian2x2Decay):
											gc.getMap().plot(x, y).setCulture(con.iBarbarian, iPlotBarbCulture/4, True)
										if (bBarbarian2x2Conversion):
											gc.getMap().plot(x, y).setCulture(con.iBarbarian, 0, True)
											gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotBarbCulture, True)
								# loop through minors - edead
								for offset in range(con.iNumMinorPlayers):
									iMinorCiv = con.iIndependent + offset
									iPlotIndependentCulture = gc.getMap().plot(x, y).getCulture(iMinorCiv)
									if (iPlotIndependentCulture > 0):
										if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
											if (bBarbarian2x2Decay):
												gc.getMap().plot(x, y).setCulture(iMinorCiv, iPlotIndependentCulture/4, True)
											if (bBarbarian2x2Conversion):
												gc.getMap().plot(x, y).setCulture(iMinorCiv, 0, True)
												gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependentCulture, True)
				
				#plot
				for x in range(tCityPlot[0]-1, tCityPlot[0]+2):		# from x-1 to x+1
					for y in range(tCityPlot[1]-1, tCityPlot[1]+2):	# from y-1 to y+1
						pCurrent = gc.getMap().plot(x, y)
						
						iCurrentPlotCulture = pCurrent.getCulture(iOldOwner)
						
						if (pCurrent.isCity()):
							pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/100, True)
							pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent)/100, True)
						else:
							pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/3/100, True)
							pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent/3)/100, True)
						
						#cut other players culture
##						for iCiv in range(iNumPlayers):
##							if (iCiv != iNewOwner and iCiv != iOldOwner):
##								iPlotCulture = gc.getMap().plot(x, y).getCulture(iCiv)
##								if (iPlotCulture > 0):
##									gc.getMap().plot(x, y).setCulture(iCiv, iPlotCulture/3, True)
						
						if (not pCurrent.isCity()):
							if (bAlwaysOwnPlots):
								pCurrent.setOwner(iNewOwner)
							else:
								if (pCurrent.getCulture(iNewOwner)*4 > pCurrent.getCulture(iOldOwner)):
									pCurrent.setOwner(iNewOwner)



	# handler
	def spreadMajorCulture(self, iMajorCiv, iX, iY):
		for x in range(iX-4, iX+5):		# from x-4 to x+4
			for y in range(iY-4, iY+5):	# from y-4 to y+4
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					city = pCurrent.getPlotCity()
					if (city.getOwner() >= iNumPlayers):
						iMinor = city.getOwner()
						iDen = 25
						if gc.getMap().plot(iX, iY).getRegionID() in self.getCoreRegions(iMajorCiv):
							iDen = 10
						elif gc.getMap().plot(iX, iY).getRegionID() in self.getNormalRegions(iMajorCiv):
							iDen = 15
						
						iMinorCityCulture = city.getCulture(iMinor)
						city.setCulture(iMajorCiv, iMinorCityCulture/iDen, True)
						
						iMinorPlotCulture = pCurrent.getCulture(iMinor)
						pCurrent.setCulture(iMajorCiv, iMinorPlotCulture/iDen, True)


	# RiseAndFall
	def convertPlotCulture(self, pCurrent, iCiv, iPercent, bOwner):
		
		if (pCurrent.isCity()):
			city = pCurrent.getPlotCity()
			iCivCulture = city.getCulture(iCiv)
			iLoopCivCulture = 0
			for iLoopCiv in range(iNumTotalPlayers):
				if (iLoopCiv != iCiv):
					iLoopCivCulture += city.getCulture(iLoopCiv)
					city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*(100-iPercent)/100, True)
			city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)  
		
		iCivCulture = pCurrent.getCulture(iCiv)
		iLoopCivCulture = 0
		for iLoopCiv in range(iNumTotalPlayers):
			if (iLoopCiv != iCiv):
				iLoopCivCulture += pCurrent.getCulture(iLoopCiv)
				pCurrent.setCulture(iLoopCiv, pCurrent.getCulture(iLoopCiv)*(100-iPercent)/100, True)
		pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)
		if (bOwner == True):
			pCurrent.setOwner(iCiv)


	# RiseAndFall
	def pushOutGarrisons(self, tCityPlot, iOldOwner):
		tDestination = (-1, -1)
		for x in range(tCityPlot[0]-2, tCityPlot[0]+3):
			for y in range(tCityPlot[1]-2, tCityPlot[1]+3):
				pDestination = gc.getMap().plot(x, y)
				if (pDestination.getOwner() == iOldOwner and (not pDestination.isWater()) and (not pDestination.isImpassable())):
					tDestination = (x, y)
					break
					break
		if (tDestination != (-1, -1)):
			plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
			iNumUnitsInAPlot = plotCity.getNumUnits()
			j = 0
			for i in range(iNumUnitsInAPlot):
				unit = plotCity.getUnit(j)
				if (unit.getDomainType() == 2): #land unit
					unit.setXY(tDestination[0], tDestination[1], False, False, False)
				else:
					j = j + 1


	# RiseAndFall
	def relocateSeaGarrisons(self, tCityPlot, iOldOwner):
				tDestination = (-1, -1)
				cityList = PyPlayer(iOldOwner).getCityList()
				for pyCity in cityList:
						if (pyCity.GetCy().isCoastal(0)):
								tDestination = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
				if (tDestination == (-1, -1)):
						for x in range(tCityPlot[0]-12, tCityPlot[0]+12):
								for y in range(tCityPlot[1]-12, tCityPlot[1]+12):
										pDestination = gc.getMap().plot(x, y)
										if (pDestination.isWater()):
												tDestination = (x, y)
												break
												break
				if (tDestination != (-1, -1)):
						plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
						iNumUnitsInAPlot = plotCity.getNumUnits()
						j = 0
						for i in range(iNumUnitsInAPlot):
								unit = plotCity.getUnit(j)
								if (unit.getDomainType() == 0): #sea unit
										unit.setXY(tDestination[0], tDestination[1], False, False, False)
								else:
										j = j + 1


	# RiseAndFall
	def createGarrisons(self, tCityPlot, iNewOwner, iNumUnits):
		pTeam = gc.getTeam(gc.getPlayer(iNewOwner).getTeam())
		
		if pTeam.isHasTech(con.iFlintlock):
			iUnitType = con.iMusketman
		elif pTeam.isHasTech(con.iMatchlock):
			iUnitType = con.iArquebusier
		elif pTeam.isHasTech(con.iMilitaryDrill):
			iUnitType = con.iPikeman
		elif pTeam.isHasTech(con.iGuilds):
			iUnitType = con.iMarksman
		elif pTeam.isHasTech(con.iLevyArmies):
			iUnitType = con.iHeavySpearman
		else:
			iUnitType = con.iArcher
		
		self.makeUnit(iUnitType, iNewOwner, [tCityPlot[0], tCityPlot[1]], iNumUnits)


	# RiseAndFall, Stability
	def killCiv(self, iCiv, iNewCiv):
		self.clearPlague(iCiv)
		for pyCity in PyPlayer(iCiv).getCityList():
			tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
			self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
			self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv]) #by trade because by conquest may raze the city
		
		self.flipUnitsInArea(self.getAreaPlotList([0,0], [gc.getMap().getGridWidth(), gc.getMap().getGridHeight()]), iNewCiv, iCiv, False, True)
		self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())
		self.resetUHV(iCiv)


	def killAndFragmentCiv(self, iCiv, bAssignOneCity):
		
		self.clearPlague(iCiv)
		iNumLoyalCities = 0
		iCounter = gc.getGame().getSorenRandNum(6, 'random start')
		iNumPlayerCities = len(PyPlayer(iCiv).getCityList()) #needs to be assigned cause it changes dinamically
		for pyCity in PyPlayer(iCiv).getCityList():
			#print("iCounter",iCounter)
			tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
			pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
			#loyal cities for the human player
			#print(bAssignOneCity,iNumLoyalCities,1+(iNumPlayerCities-1)/6,pyCity.GetCy().isCapital(),iCounter%6 == 0)
			if (bAssignOneCity and iNumLoyalCities <= 1+(iNumPlayerCities-1)/6 and (pyCity.GetCy().isCapital() or iCounter%6 == 0)):
					iNumLoyalCities += 1
					if (iNumLoyalCities == 1):
						for offset in range(con.iNumMinorPlayers):
							gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(con.iIndependent + offset, False, -1) #too dangerous?
					iCounter += 1
					#print(pyCity.GetCy().getName(), "loyal")
					continue
			#assign to neighbours first
			bNeighbour = False
			iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
			
			# edead - minors fix + efficiency
			plotCulture = pCurrent.getCulture(iCiv) + pCurrent.getCulture(con.iBarbarian)
			for offset in range(iNumMinorPlayers):
				plotCulture += pCurrent.getCulture(con.iIndependent + offset)
			
			for j in range(iRndnum, iRndnum + iNumPlayers): #only major players
				iLoopCiv = j % iNumPlayers
				if (gc.getPlayer(iLoopCiv).isAlive() and iLoopCiv != iCiv and not gc.getPlayer(iLoopCiv).isHuman()):
					regionList = []
					regionList.extend(self.getCoreRegions(iLoopCiv))
					regionList.extend(self.getNormalRegions(iLoopCiv))
					regionList.extend(self.getBroaderRegions(iLoopCiv))
					if pCurrent.getCulture(iLoopCiv) > 0 and pCurrent.getRegionID() in regionList: # make sure to skip random culture in far away cities
						if (pCurrent.getCulture(iLoopCiv)*100 / (pCurrent.getCulture(iLoopCiv) + plotCulture) >= 5): #change in vanilla
							self.flipUnitsInCityBefore(tCoords, iLoopCiv, iCiv)
							self.setTempFlippingCity((tCoords[0],tCoords[1]))
							self.flipCity(tCoords, 0, 0, iLoopCiv, [iCiv])
							#self.flipUnitsInCityAfter(self.getTempFlippingCity(), iLoopCiv) # edead - buggy for some reason
							self.flipUnitsInCityAfter(tCoords, iLoopCiv) # edead
							self.flipUnitsInArea(self.getAreaPlotList([tCoords[0]-2,tCoords[1]-2], [tCoords[0]+2,tCoords[1]+2]), iLoopCiv, iCiv, False, True)
							bNeighbour = True
							break
			if (bNeighbour):
				iCounter += 1
				continue
			iNewCiv = self.getRandomMinorCiv()
			self.flipUnitsInCityBefore(tCoords, iNewCiv, iCiv)
			self.setTempFlippingCity(tCoords) # edead
			self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
			self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
			self.flipUnitsInCityAfter(tCoords, iNewCiv) # edead
			iCounter += 1
			self.flipUnitsInArea(self.getAreaPlotList([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1]), iNewCiv, iCiv, False, True)
			
			# free vassals - edead
			for i in range(iNumPlayers):
				if i != iCiv:
					pTeam = gc.getTeam(i)
					if pTeam.isAlive() and pTeam.isVassal(iCiv):
						pTeam.setVassal(iCiv, False, False)
			
		if (bAssignOneCity == False):
			self.killUnitsInArea([0,0], [gc.getMap().getGridWidth(), gc.getMap().getGridHeight()], iCiv)
			self.resetUHV(iCiv)
		self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())


	# edead: only used for Barbs
	def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
		"""Searches all tile in the square from tTopLeft to tBottomRight and calls function for
		every tile, passing argsList. The function called must return a tuple: (1) a result, (2) if
		a plot should be painted and (3) if the search should continue.
		"""
		tPaintedList = []
		result = None
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1, -1): # edead: added -1, not sure why it didn't work before
				result, bPaintPlot, bContinueSearch = function((x, y), result, argsList)
				if bPaintPlot: # paint plot
					tPaintedList.append((x, y))
				if not bContinueSearch: # goal reached, so stop
					return result, tPaintedList
		return result, tPaintedList


	# edead: replaces squareSearch for RiseAndFall
	def plotListSearch(self, plotList, function, argsList):
		"""Searches all tiles in the plotList and calls function for every tile, passing argsList. 
		The function called must return a tuple: (1) a result, (2) if a plot should be painted and 
		(3) if the search should continue.
		"""
		tPaintedList = []
		result = None
		for i in range(len(plotList)):
			result, bPaintPlot, bContinueSearch = function((plotList[i][0], plotList[i][1]), result, argsList)
			if bPaintPlot: # paint plot
				tPaintedList.append((plotList[i][0], plotList[i][1]))
			if not bContinueSearch: # goal reached, so stop
				return result, tPaintedList
		return result, tPaintedList


	# functions for plotListSearch & squareSearch


	# Barbs, RiseAndFall
	def outerInvasion( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					#if (pCurrent.countTotalCulture() == 0 ):
					if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def innerSeaSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's water and it isn't occupied by any unit. Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isWater() and not pCurrent.isLake(): # edead: no barbs in lakes!
			if not pCurrent.isCity() and not pCurrent.isUnit():
				bClean = True
				for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
					for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
						if gc.getMap().plot(x,y).isUnit():
							bClean = False
							break
				if bClean:   
					# this is a good plot, so paint it and continue search
					return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def outerSeaSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's water and it isn't occupied by any unit and if it isn't a civ's territory. Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if len(argsList) > 0 and pCurrent.getPlotType() not in argsList: # edead: extra condition to allow only certain terrains
			return (None, not bPaint, bContinue)
		if pCurrent.isWater() and not pCurrent.isLake(): # edead: no barbs in lakes!
			if not pCurrent.isCity() and not pCurrent.isUnit():
				if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# Barbs
	def outerSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory.
		Unit check extended to adjacent plots"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	# RiseAndFall
	def innerInvasion( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					if pCurrent.getOwner() >= 0 and pCurrent.getOwner() < con.iNumPlayers: #if (pCurrent.getOwner() in argsList ):
						# this is a good plot, so paint it and continue search
						return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def innerSpawn( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getTerrainType() != con.iWetland:
				if not pCurrent.isCity() and not pCurrent.isUnit():
					bClean = True
					for x in range(tCoords[0] - 1, tCoords[0] + 2):		# from x-1 to x+1
						for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
							if gc.getMap().plot(x,y).isUnit():
								bClean = False
								break
					if bClean:
						if pCurrent.getOwner() in argsList:
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def goodPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands, it isn't desert, tundra, marsh or jungle; it isn't occupied by a unit or city and if it isn't a civ's territory.
		Unit check extended to adjacent plots.
		"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if not pCurrent.isImpassable():
				if not pCurrent.isUnit():
					if pCurrent.getTerrainType() not in [con.iDesert, con.iSemidesert, con.iTundra, con.iWetland]:
						if pCurrent.calculateCulturalOwner() == -1: # edead: bugfix
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedCityPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ.
		"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.getOwner() == argsList:
			if pCurrent.isCity():
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedCityPlotsAdjacentArea( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		#print(tCoords[0], tCoords[1], pCurrent.isCity(), pCurrent.getOwner() == argsList[0], pCurrent.isAdjacentToArea(gc.getMap().plot(argsList[1][0],argsList[1][1]).area()))
		if pCurrent.getOwner() == argsList[0] and pCurrent.isAdjacentToArea(gc.getMap().plot(argsList[1][0],argsList[1][1]).area()):
			if pCurrent.isCity():
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def foundedCityPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isCity():
			if pCurrent.getPlotCity().getOriginalOwner() == argsList:
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def ownedPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it is in civ's territory."""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.getOwner() == argsList:
			# this is a good plot, so paint it and continue search
			return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def goodOwnedPlots( self, tCoords, result, argsList ):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it's hill or flatlands; it isn't marsh or jungle, it isn't occupied by a unit and if it is in civ's territory."""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if pCurrent.isHills() or pCurrent.isFlatlands():
			if pCurrent.getFeatureType() not in [con.iMarsh, con.iJungle]:
				if not pCurrent.isCity() and not pCurrent.isUnit():
						if pCurrent.getOwner() == argsList:
							# this is a good plot, so paint it and continue search
							return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)


	def resetUHV(self, iPlayer):
		if iPlayer < iNumPlayers:
			if self.getGoal(iPlayer, 0) == -1:
				self.setGoal(iPlayer, 0, 0)
			if self.getGoal(iPlayer, 1) == -1:
				self.setGoal(iPlayer, 1, 0)
			if self.getGoal(iPlayer, 2) == -1:
				self.setGoal(iPlayer, 2, 0)


	def clearPlague(self, iCiv):
		for pyCity in PyPlayer(iCiv).getCityList():
			if (pyCity.GetCy().getNumRealBuilding(con.iPlague) > 0):
				pyCity.GetCy().setNumRealBuilding(con.iPlague, 0)


	#AIWars, by CyberChrist

	def isNoVassal(self, iCiv):
		iMaster = 0
		for iMaster in range (iNumTotalPlayers):
			if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster):
				if gc.getPlayer(iMaster).isAlive(): # edead: occasional CIV4 bug makes dead masters
					return False
		return True


	def isAVassal(self, iCiv):
		iMaster = 0
		for iMaster in range (iNumTotalPlayers):
			if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster):
				if gc.getPlayer(iMaster).isAlive(): # edead: occasional CIV4 bug makes dead masters
					return True
		return False


	#Plague, Religions
	def getRandomCity(self, iPlayer):
		
		cityList = []
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			cityList.append(pCity.GetCy())
		if (len(cityList)):
			return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
		else:
			return -1


	def getRandomCiv( self ):
		
		civList = []
		for i in range(con.iNumPlayers):
			if gc.getPlayer(i).isAlive() and self.getYear() >= con.tBirth[i]:
				civList.append(i)
				
		return civList[gc.getGame().getSorenRandNum(len(civList), 'random civ')]


	def isMortalUnit(self, unit):
		
		if unit.isHasPromotion(con.iLeader): #leader
			if not gc.getPlayer(unit.getOwner()).isHuman():
				return False
		iUnitType = unit.getUnitType()
		if iUnitType >= con.iWorkBoat:
			return False
		return True


	def secedeCity(self, city, bSilent=False):
		"""Makes a specific city declare independence."""
		
		if city.isWeLoveTheKingDay() or city.isCapital():
			return False
		
		iPlayer = city.getOwner()
		iNewCiv = self.getRandomMinorCiv()
		iOldX = city.getX()
		iOldY = city.getY()
		self.cultureManager((city.getX(),city.getY()), 50, iNewCiv, iPlayer, False, True, True)
		self.flipUnitsInCityBefore((city.getX(),city.getY()), iNewCiv, iPlayer)
		self.setTempFlippingCity((city.getX(),city.getY()))
		self.flipCity((city.getX(),city.getY()), 0, 0, iNewCiv, [iPlayer])   #by trade because by conquest may raze the city
		self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
		city = gc.getMap().plot(iOldX,iOldY).getPlotCity()
		output = True
		if iPlayer == self.getHumanID() and not city is None:
			if bSilent:
				output = city.getName()
			else:
				CyInterface().addMessage(iPlayer, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_SECESSION", (city.getName(), )), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(con.iRed), city.getX(), city.getY(), True, True)
		self.setStability(iPlayer, self.getStability(iPlayer) + 3) #to counterbalance the stability hit on city acquired event, leading to a chain reaction
		self.setParameter(iPlayer, con.iParExpansionE, True, 3)
		return output


	def secedeRandomCity(self, iPlayer, iRevoltTurns = 0):
		"""Makes one semi-random city declare independence."""
		
		if gc.getPlayer(iPlayer).getNumCities() > 0: #this check is needed, otherwise game crashes
			return False
		
		cityList = []
		secondPass = []
		apCityList = PyPlayer(iPlayer).getCityList()
		shuffle(apCityList)
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		
		for pCity in apCityList:
			city = pCity.GetCy()
			iRegion = gc.getMap().plot(city.getX(), city.getY()).getRegionID()
			
			# skip capitals and core cities
			if city.isWeLoveTheKingDay() or city.isCapital():
				continue
			if city.getX() == con.tCapitals[iPlayer][0] and city.getY() == con.tCapitals[iPlayer][1]:
				continue
			if sd.getCivStatus(iPlayer) == 1 and city.getX() == con.tRespawnCapitals[iPlayer][0] and city.getY() == con.tRespawnCapitals[iPlayer][1]:
				continue
			if iRegion in self.getCoreRegions(iPlayer): # spare the core cities instead of iDistance > 3
				continue
			
			# add up unrest points from various sources
			iTotalUnrest = city.angryPopulation(0)
			if city.healthRate(False, 0) < 0: iTotalUnrest += 1
			if city.getReligionBadHappiness() > 0: iTotalUnrest += 1 
			if city.getHurryAngerModifier() > 0: iTotalUnrest += 1
			if city.getNoMilitaryPercentAnger() > 0: iTotalUnrest += 1
			if city.getWarWearinessPercentAnger() > 0: iTotalUnrest += 1
			if city.isOccupation() or city.isDisorder(): iTotalUnrest += 1
			
			iDistance = self.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY())
			
			# if really bad city is found, take it and break the loop, otherwise store them in first & second pass lists
			if iRegion not in self.getNormalRegions(iPlayer) and (iRegion in con.lUnrulyRegions or city.isOccupation() or city.isDisorder()):
				cityList = [city]
				break
			if iRegion not in self.getNormalRegions(iPlayer) and iRegion not in self.getBroaderRegions(iPlayer) and (iTotalUnrest > 0 or iDistance > 40):
				cityList = [city]
				break
			if iRegion not in self.getNormalRegions(iPlayer) and iTotalUnrest > 1:
				cityList = [city]
				break
			if iTotalUnrest > 3 or (iRegion in con.lUnrulyRegions and iTotalUnrest > 0):
				cityList = [city]
				break
			if iRegion in con.lUnrulyRegions:
				cityList.append(city)
			elif iRegion not in self.getNormalRegions(iPlayer) and iRegion not in self.getBroaderRegions(iPlayer):
				cityList.append(city)
			elif iRegion not in self.getNormalRegions(iPlayer) and iTotalUnrest > 0:
				cityList.append(city)
			elif iTotalUnrest > 1:
				cityList.append(city)
			elif iTotalUnrest > 0:
				secondPass.append(city)
			else:
				pCurrent = gc.getMap().plot(city.getX(), city.getY())
				for iLoop in range(iNumTotalPlayers+1):
					if iLoop != iPlayer:
						if pCurrent.getCulture(iLoop) > 0:
							secondPass.append(city)
							break
		
		if not cityList:
			cityList = secondPass
		
		if cityList:
			splittingCity = cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
			
			# Stationed garrison can turn the secession into a revolt (10% chance per normal unit, 20% per mercenary)
			if iRevoltTurns == 0:
				iNumUnitsInAPlot = splittingCity.plot().getNumUnits()
				iRevoltProtection = iNumUnitsInAPlot * 10
				if iNumUnitsInAPlot:
					for i in range(iNumUnitsInAPlot):
						iRevoltProtection += splittingCity.plot().getUnit(i).getRevoltProtection()
				iStability = self.getStability(iPlayer)
				if iStability < 0:
					iRevoltProtection = max(0, iRevoltProtection + iStability)
				if gc.getGame().getSorenRandNum(100, 'Revolt test') < iRevoltProtection:
					iRevoltTurns = gc.getGame().getSorenRandNum(4, 'Revolt turns')
			if iRevoltTurns > 0:
				splittingCity.changeCultureUpdateTimer(iRevoltTurns)
				splittingCity.changeOccupationTimer(iRevoltTurns)
				CyInterface().addMessage(iPlayer, False, con.iDuration, localText.getText("TXT_KEY_STABILITY_REVOLT", (splittingCity.getName(),)), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(con.iRed), splittingCity.getX(), splittingCity.getY(), True, True)
			else:
				return self.secedeCity(splittingCity)
			
		return False


	# edead
	def showPersecutionPopup(self):
		"""Asks the human player to select a religion to persecute."""
		
		popup = Popup.PyPopup(7626, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString("Religious Persecution")
		popup.setBodyString("Choose a religious minority to deal with...")
		religionList = sd.getPersecutionReligions()
		for iReligion in religionList:
			strIcon = gc.getReligionInfo(iReligion).getType()
			strIcon = "[%s]" %(strIcon.replace("RELIGION_", "ICON_"))
			strButtonText = "%s %s" %(localText.getText(strIcon, ()), gc.getReligionInfo(iReligion).getText())
			popup.addButton(strButtonText)
		popup.launch(False)


	def doPersecution(self, iX, iY, iUnitID, iReligion=None):
		"""Removes one religion from the city and handles the consequences."""
		
		pCity = gc.getMap().plot(iX, iY).getPlotCity()
		if pCity.isNone(): return False
		
		iOwner = pCity.getOwner()
		pPlayer = gc.getPlayer(iOwner)
		pUnit = pPlayer.getUnit(iUnitID)
		
		#utils.echo("doPersecution (%s)" %(pPlayer.getCivilizationShortDescription(0)))
		
		# chance to work: 65-90 based on piety
		iChance = 65 + min(25, self.getPiety(iOwner)/2)
		if gc.getGame().getSorenRandNum(100, "purge chance") < iChance:
			
			iStateReligion = pPlayer.getStateReligion()
			
			# sanity check
			if iStateReligion == -1:
				return False
			
			# determine the target religion, if not supplied by the popup decision
			if not iReligion:
				for iReligion in con.tPersecutionOrder[iStateReligion]:
					if iReligion != iStateReligion and not pCity.isHolyCityByType(iReligion): # spare holy cities
						if pCity.isHasReligion(iReligion):
							break
			
			# remove a single non-state religion and its buildings from the city, count the loot
			iLootModifier = 2 * pCity.getPopulation() / pCity.getReligionCount() + 1
			iLoot = 2 + iLootModifier
			pCity.setHasReligion(iReligion, 0, 0, 0)
			for iBuildingLoop in range(gc.getNumBuildingInfos()):
				if iBuildingLoop < con.iPlague:
					if pCity.getNumRealBuilding(iBuildingLoop):
						if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == iReligion:
							pCity.setNumRealBuilding(iBuildingLoop, 0)
							iLoot += iLootModifier
			if iReligion == con.iJudaism:
				iLoot = iLoot*3/2
			
			# kill / expel some population
			if pCity.getPopulation() > 14 and pCity.getReligionCount() < 2:
				pCity.changePopulation(-3)
			elif pCity.getPopulation() > 9 and pCity.getReligionCount() < 3:
				pCity.changePopulation(-2)
			elif pCity.getPopulation() > 3:
				pCity.changePopulation(-1)
			
			# distribute the loot
			iLoot = iLoot/2 + gc.getGame().getSorenRandNum(iLoot/2, 'random loot')
			pPlayer.changeGold(iLoot)
			
			# apply diplomatic penalty
			for iLoopPlayer in range(con.iNumPlayers):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive() and iLoopPlayer != iOwner:
					if pLoopPlayer.getStateReligion() == iReligion:
						pLoopPlayer.AI_changeAttitudeExtra(iOwner, -1)
			
			# add piety
			self.setPiety(iOwner, self.getRealPiety(iOwner) + 1)
			
			CyInterface().addMessage(iOwner, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_INQUISITION", (pCity.getName(), gc.getReligionInfo(iReligion).getDescription(), iLoot)), "AS2D_PLAGUE", InterfaceMessageTypes.MESSAGE_TYPE_INFO, pUnit.getButton(), ColorTypes(con.iGreen), iX, iY, True, True)
		
		else: # fail
			CyInterface().addMessage(iOwner, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_INQUISITION_FAIL", (pCity.getName(), )), "AS2D_SABOTAGE", InterfaceMessageTypes.MESSAGE_TYPE_INFO, pUnit.getButton(), ColorTypes(con.iRed), iX, iY, True, True)
		
		# start a small revolt
		pCity.changeCultureUpdateTimer(1);
		pCity.changeOccupationTimer(1);
		
		# consume the inquisitor
		pUnit.kill(0, -1)
		
		# Unhappiness from persecution
		pCity.changeHurryAngerTimer(pCity.flatHurryAngerLength())
		
		return True


	# edead
	def doGreatSaintEffect(self, unit):
		"""Spreads state religion to up to 5 surrounding cities and consumes the unit."""
		
		iPlayer = unit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		iReligion = pPlayer.getStateReligion()
		
		# loop through all cities and save city+distance tuples for those that don't have the religion
		cityValueList = []
		for iLoopPlayer in range(iNumTotalPlayers+1): # include barbarians
			apCityList = PyPlayer(iLoopPlayer).getCityList()
			for pCity in apCityList:
				city = pCity.GetCy()
				if city.isHasReligion(iReligion) or city.isNone():
					continue
				iDistance = self.calculateDistance(unit.getX(), unit.getY(), city.getX(), city.getY())
				cityValueList.append((city, iDistance))
		
		# sort cities from closest to farthest to the unit
		cityValueList.sort(key=itemgetter(1))
		
		# loop through the new city list and spread the religion 3-5 times
		iCount = 0
		for tCity in cityValueList:
			city = tCity[0]
			iDistance = tCity[1]
			if gc.getPlayer(city.getOwner()).getCivics(4) != con.iPersecutionCivic:
				city.setHasReligion(iReligion, True, True, True)
				iCount += 1
				if iCount == 6 or (iCount == 5 and iDistance > 30) or (iCount == 4 and iDistance > 55) or (iCount == 3 and iDistance > 70):
					break
		
		# piety bonus like for normal missionary
		sd.changePiety(iPlayer, iCount * 2)
		
		# interface message
		if iCount > 0:
			szText = localText.getText("TXT_KEY_MINOR_EVENT_GREAT_SAINT_SUCCESS", (unit.getName(), iCount))
			CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iGreen), -1, -1, False, False)
		else:
			szText = localText.getText("TXT_KEY_MINOR_EVENT_GREAT_SAINT_FAILURE", (unit.getName(), ))
			CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
		
		# consume the Great Saint
		unit.kill(0, -1)



	# edead
	def doPilgrimageSuccess(self, iX, iY, iPlayer, iUnitID):
		
		pPlayer = gc.getPlayer(iPlayer)
		pUnit = pPlayer.getUnit(iUnitID)
		
		pCapital = gc.getPlayer(iPlayer).getCapitalCity()
		iDistance = self.calculateDistance(pCapital.getX(), pCapital.getY(), iX, iY)
		iBonus = 1 + iDistance/10 + gc.getGame().getSorenRandNum(5, 'Determining the bonus amount.')
		
		# piety bonus
		self.setPiety(iPlayer, self.getRealPiety(iPlayer) + iBonus)
		
		iRandNum = gc.getGame().getSorenRandNum(100, 'Checking whether to generate a relic.')
		
		# make a relic
		if iRandNum < iBonus * 2:
			pPlayer.initUnit(con.iRelic, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			szText = localText.getText("TXT_KEY_MINOR_EVENT_PILGRIM_FOUND_RELIC", ())
			CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getUnitInfo(con.iRelic).getButton(), ColorTypes(con.iGreen), iX, iY, True, True)
		
		# convert some culture in the holy city
		pPlot = gc.getMap().plot(iX, iY)
		pCity = pPlot.getPlotCity()
		iOwner = pCity.getOwner()
		iRandNum = 1 + gc.getGame().getSorenRandNum(3, 'Convert from 1% to 3% culture.')
		
		iOldCulture = pCity.getCulture(iPlayer)
		iOwnerCulture = pCity.getCulture(iOwner)
		iAmount = iOwnerCulture * iRandNum / 100
		pCity.setCulture(iPlayer, iOldCulture + iAmount, True)
		pCity.setCulture(iOwner, iOwnerCulture - iAmount, True)
		
		iOldCulture = pPlot.getCulture(iPlayer)
		iOwnerCulture = pPlot.getCulture(iOwner)
		iAmount = iOwnerCulture * iRandNum / 100
		pPlot.setCulture(iPlayer, iOldCulture + iAmount, True)
		pPlot.setCulture(iOwner, iOwnerCulture - iAmount, True)
		
		# spread religion if not present
		iReligion = pPlayer.getStateReligion()
		if iReligion >= 0 and not pCity.isHasReligion(iReligion):
			pCity.setHasReligion(iReligion, True, True, True)
		
		# consume the pilgrim
		pUnit.kill(0, -1)


	# modified from CvExoticForeignAdvisor.py - edead
	def calculateRelations(self, nPlayer, nTarget):
		"""Returns the total value of diplomatic relations between nPlayer and nTarget."""
		
		if (nPlayer != nTarget and gc.getTeam(gc.getPlayer(nPlayer).getTeam()).isHasMet(gc.getPlayer(nTarget).getTeam())):
			nAttitude = 0
			szAttitude = CyGameTextMgr().getAttitudeString(nPlayer, nTarget)
			ltPlusAndMinuses = re.findall ("[-+][0-9]+\s?: ", szAttitude)
			for i in range (len (ltPlusAndMinuses)):
				nAttitude += int (ltPlusAndMinuses[i][:-2])
			return nAttitude
		else:
			return 0


	def getPilgrimageSite(self, iPlayer):
		iReligion = gc.getPlayer(iPlayer).getStateReligion()
		if iReligion == con.iCatholicism or iReligion == con.iOrthodoxy:
			return con.tJerusalem
		elif iReligion == con.iSunni or iReligion == con.iShia:
			return con.tMecca
		elif iReligion == con.iHinduism:
			return con.tDwarka
		else:
			return con.tJerusalem


	def findSeaPlots( self, tCoords, iRange, iCiv):
		"""Searches a sea plot that isn't occupied by a unit and isn't a civ's territory surrounding the starting coordinates."""
		
		seaPlotList = []
		for x in range(tCoords[0] - iRange, tCoords[0] + iRange+1):
			for y in range(tCoords[1] - iRange, tCoords[1] + iRange+1):	
				pCurrent = gc.getMap().plot( x, y )
				if ( pCurrent.isWater()):
					if ( not pCurrent.isUnit() ):
						#if (pCurrent.countTotalCulture() == 0 ):
						if (not (pCurrent.isOwned() and pCurrent.getOwner() != iCiv)):
							seaPlotList.append(pCurrent)
							# this is a good plot, so paint it and continue search
		if (len(seaPlotList) > 0):
			rndNum = gc.getGame().getSorenRandNum(len(seaPlotList), 'sea plot')
			result = seaPlotList[rndNum]
			if (result):
				return ((result.getX(), result.getY()))
		return (None)


	def checkRegionOwnedCity(self, iPlayer, regionID, bCoastal = False):
		"""Returns True if the region has a city owned by iPlayer."""
		
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().getOwner() == iPlayer:
						if bCoastal:
							if pCurrent.getPlotCity().isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								return True
						else:
							return True
		return False


	def checkRegionControl(self, iPlayer, regionID, bVassal = False):
		"""Returns True if the region has no cities other than iPlayer's.
		if bVassal is True, vassal cities are counted as iPlayer's."""
		
		bFound = False
		plotList = self.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					iOwner = pCurrent.getPlotCity().getOwner()
					if iOwner != iPlayer:
						if bVassal:
							if gc.getTeam(gc.getPlayer(iOwner).getTeam()).isVassal(iPlayer):
								bFound = True
							else:
								return False
						else:
							return False
					else:
						bFound = True
		if bFound:
			return True
		else:
			return False


	def canCollapse(self, iPlayer):
		
		if iPlayer == con.iPortugal:
			return False
		
		# stops rare cases of civs collapsing instantly after resurrection
		if gc.getGame().getGameTurn() < sd.getLatestRebellionTurn(iPlayer) + self.getTurns(20):
			return False
		
		if self.isTitleValid(iPlayer, con.iRomanEmperor):
			return False
		
		return True


	def isTitleValid(self, iPlayer, iTitle):
		
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		if iTitle == con.iRomanEmperor:
			if pTeam.getProjectCount(iTitle):
				if gc.getMap().plot(con.tConstantinople[0],con.tConstantinople[1]).getOwner() == iPlayer:
					return True
			return False
		return pTeam.getProjectCount(iTitle)


	def getBaseUnit(self, iUnit, iNewOwner):
		
		iStateReligion = gc.getPlayer(iNewOwner).getStateReligion()
		
		if iUnit in [con.iItalianMaceman, con.iItalianCrossbowman, con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight, con.iManAtArms, con.iKnightOfJerusalem, con.iNormanKnight, con.iVarangianGuard, con.iGreekFlamethrower]:
			if iStateReligion == con.iCatholicism or iStateReligion == con.iOrthodoxy:
				return iUnit
			else: 
				return -1
		
		if iUnit in [con.iGhulamLancer, con.iGhulamHorseArcher, con.iGhulamGuard, con.iMaceman_Harafisha, con.iMaceman_Turkish]:
			if iStateReligion == con.iSunni or iStateReligion == con.iShia:
				return iUnit
			else: 
				return -1
		
		# get base unit class using Delhi Sultanate (no UUs)
		iUnitClass = gc.getUnitInfo(iUnit).getUnitClassType()
		iBaseUnit = gc.getCivilizationInfo(gc.getInfoTypeForString("CIVILIZATION_DELHI")).getCivilizationUnits(iUnitClass)

		# fix for classes not included in Delhi XML
		if iUnit == con.iBerberCavalry:
			return con.iHorseman
		elif iUnit == con.iArabianSheikh:
			return con.iMountedInfantry
		
		if iBaseUnit == -1:
			return iUnit
		else:
			return iBaseUnit

			
	def getRandomCityByRegion(self, lRegions):
		"""Returns a city located in any of the listed regions."""
		
		cityList = []
		for iPlayer in range(iNumTotalPlayers):
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCurrent = gc.getMap().plot(pyCity.getX(), pyCity.getY())
				if pCurrent.getRegionID() in lRegions:
					cityList.append(pyCity.GetCy())
		if len(cityList):
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None

	
	# From RFCE
	def getRandomCityByReligion(self, iReligion):
		
		if (gc.getGame().isReligionFounded(iReligion)):
			cityList = []
			for iPlayer in range(iNumTotalPlayers):
				for pyCity in PyPlayer(iPlayer).getCityList():
					if pyCity.GetCy().isHasReligion(iReligion):
						cityList.append(pyCity.GetCy())
			iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
			return cityList[iCity]
		return None


	def getCaliphController(self):
		iOwner = None
		for iPlayer in range(iNumPlayers):
			pPlayer = gc.getPlayer(iPlayer)
			if gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iCaliph) > 0:
				iOwner = iPlayer
				for iMaster in range(iNumPlayers):
					if iPlayer != iMaster and gc.getTeam(pPlayer.getTeam()).isVassal(iMaster):
						if pPlayer.getStateReligion() == con.iShia or pPlayer.getStateReligion() == con.iSunni:
							iOwner = iMaster
							break
						else:
							iOwner = None
							break
		return iOwner
					
	
	def getHolyWarTargets(self, iPlayer):
		"""Returns a list of tuples containing targets' IDs, reason for war, and AI weights."""
		
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		targetList = [] 
		for iTarget in range(iNumPlayers):
			if iTarget != iPlayer and self.isActive(iTarget) and pTeam.isAtWar(iTarget): # base condition: alive and at war
				iWeight, szText = self.getHolyWarTargetInfo(iPlayer, iTarget)
				if iWeight > 0:
					targetList.append((iTarget, szText, iWeight))
		return targetList


	def getHolyWarTargetInfo(self, iPlayer, iTarget):
		"""Returns a tuple containing AI weight and reason for war."""
	
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		holyCityOwners = []
		holyCityOwners.append(gc.getMap().plot(con.tJerusalem[0],con.tJerusalem[1]).getOwner())
		holyCityOwners.append(gc.getMap().plot(con.tMedina[0],con.tMedina[1]).getOwner())
		holyCityOwners.append(gc.getMap().plot(con.tMecca[0],con.tMecca[1]).getOwner())
		if iStateReligion == con.iShia:
			holyCityOwners.append(gc.getMap().plot(con.tNajaf[0],con.tNajaf[1]).getOwner())
		targetPlayer = gc.getPlayer(iTarget)
		targetReligion = targetPlayer.getStateReligion()
		iWeight = 0
		szText = ""
		# War against disbelievers
		if targetReligion == -1:
			iWeight += 10
			szText = con.lHolyWarTypes[1]
		elif targetReligion in [con.iOrthodoxy, con.iCatholicism, con.iHinduism]:
			iWeight += 6
			szText = con.lHolyWarTypes[1]
		# War against heretics
		elif targetReligion != iStateReligion:
			if self.getFavorLevel(iTarget) == 0:
				iWeight += 20
				szText = con.lHolyWarTypes[2]
			elif self.getFavorLevel(iTarget) == 1:
				iWeight += 10
				szText = con.lHolyWarTypes[2]
			else:
				iWeight += 2
				szText = con.lHolyWarTypes[2]
		else:
			if self.getFavorLevel(iTarget) == 0:
				iWeight += 20
				szText = con.lHolyWarTypes[2]
			elif self.getFavorLevel(iTarget) == 1:
				iWeight += 10
				szText = con.lHolyWarTypes[2]
		# War against whoever occupies our holy cities
		if iTarget in holyCityOwners and targetReligion not in [con.iSunni, con.iShia]:
			if iTarget == holyCityOwners[0]:
				iWeight += 2
			else:
				iWeight += 40
			szText = con.lHolyWarTypes[0]
		# Add attitude
		if iWeight > 0:
			iWeight += -self.calculateRelations(iPlayer, iTarget)
			if iTarget == utils.getHumanID():
				iWeight += 2 * gc.getGame().getHandicapType()
		return (iWeight, szText)
	
	
	def getHolyWarParticipants(self, iPlayer, iTarget):
		
		playerList = []
		iReligion = gc.getPlayer(iPlayer).getStateReligion()
		for iLoopPlayer in range(iNumPlayers):
			if iLoopPlayer != iPlayer and iLoopPlayer != iTarget and gc.getPlayer(iLoopPlayer).getStateReligion() == iReligion and self.isActive(iLoopPlayer):
				pLoopTeam = gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam())
				if not pLoopTeam.isAtWar(iTarget) and pLoopTeam.isHasMet(iTarget):
					playerList.append(iLoopPlayer)
		return playerList
	
	
	def canBetray(self, iUnitType, iReligion):
	
		if iUnitType in [con.iItalianMaceman, con.iItalianCrossbowman, con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight, con.iManAtArms, con.iKnightOfJerusalem, con.iNormanKnight] and iReligion not in [con.iCatholicism, con.iOrthodoxy]:
			return False
		if iUnitType in [con.iGhulamLancer, con.iGhulamHorseArcher, con.iGhulamGuard, con.iMaceman_Harafisha, con.iMaceman_Turkish] and iReligion not in [con.iSunni, con.iShia]:
			return False
		if iUnitType in [con.iSunniMissionary, con.iShiaMissionary, con.iCatholicMissionary, con.iOrthodoxMissionary, con.iHinduMissionary, con.iInquisitor]:
			return False
		if iUnitType >= con.iRelic1:
			return False
		return True
	
	
	def toggleStabilityOverlay(self):
		
		engine = CyEngine()
		map = CyMap()
		
		# clear the highlight
		engine.clearColoredPlots(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_WORLD_BUILDER)
		
		if self.bStabilityOverlay:
			self.bStabilityOverlay = False
			CyGInterfaceScreen("MainInterface", CvScreenEnums.MAIN_INTERFACE).setState("StabilityOverlay", False)
			return
		
		self.bStabilityOverlay = True
		CyGInterfaceScreen("MainInterface", CvScreenEnums.MAIN_INTERFACE).setState("StabilityOverlay", True)
		
		# set up colors
		colors = []
		colors.append("COLOR_HIGHLIGHT_FOREIGN")
		colors.append("COLOR_HIGHLIGHT_OUTSIDE")
		colors.append("COLOR_HIGHLIGHT_CONTESTED")
		colors.append("COLOR_HIGHLIGHT_BORDER")
		colors.append("COLOR_HIGHLIGHT_CORE")
		
		iHuman = self.getHumanID()
		iHumanTeam = gc.getPlayer(iHuman).getTeam()
		
		# apply the highlight
		for i in range(map.numPlots()):
			plot = map.plotByIndex(i)
			if gc.getGame().isDebugMode() or plot.isRevealed(iHumanTeam, False):
				if plot.isWater():
					szColor = "COLOR_GREY"
				else:
					szColor = colors[self.getRegionStabilityLevel(iHuman, plot.getRegionID())]
				engine.addColoredPlotAlt(plot.getX(), plot.getY(), int(PlotStyles.PLOT_STYLE_BOX_FILL), int(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_WORLD_BUILDER), szColor, .2)
	
	
	def launchDebugScreen(self):
		
		map = CyMap()
		output = "RELICS\n\n"
		hiddenRelics = sd.getVal('hiddenRelics')
		for iRelic in con.relics.keys():
			bFound = False
			szName = gc.getBuildingInfo(iRelic).getText()
			for i in range(map.numPlots()):
				plot = map.plotByIndex(i)
				if plot.isCity():
					if plot.getPlotCity().getNumRealBuilding(iRelic):
						output += szName + ' is safely kept in ' + plot.getPlotCity().getName() + ' (' + str(unit.getX()) + ',' + str(unit.getY()) + ')'
						bFound = True
						break
				for j in range(plot.getNumUnits()):
					unit = plot.getUnit(j)
					if unit.getUnitType() == con.relics[iRelic][0]:
						if plot.isCity():
							output += szName + ' is located in ' + plot.getPlotCity().getName() + ' (' + str(unit.getX()) + ',' + str(unit.getY()) + ')'
						else:
							output += szName + ' is located at (' + str(unit.getX()) + ',' + str(unit.getY()) + ')'
						bFound = True
						break
						break
			if not bFound:
				if iRelic in hiddenRelics.keys():
					szProvince = '????'
					for i in range(map.numPlots()):
						plot = map.plotByIndex(i)
						if plot.getRegionID() == hiddenRelics[iRelic]:
							szProvince = plot.getRegionName(False)
							break
					output += szName + ' is hidden somewhere in ' + szProvince
				else:
					output += szName + ' is lost'
			output += "\n"
		
		popup = Popup.PyPopup(-1)
		popup.setPosition(240, 150)
		popup.setSize(800, 550)
		popup.setHeaderString("The Sword of Islam Debug Screen")
		popup.setBodyString(output)
		popup.launch(True, PopupStates.POPUPSTATE_QUEUED)
		
	
	def getMaster(self, iCiv):
		team = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		for iMaster in range(iNumTotalPlayers):
			if team.isVassal(iMaster):
				return iMaster
	
	
	def getRegionName(self, regionID):
		'Returns the region name of a plot.'
		map = gc.getMap()
		for i in range(map.numPlots()):
			plot = map.plotByIndex(i)
			if plot.getRegionID() == regionID:
				return plot.getRegionName(False)
		return ""
	
	
	def getPlotRegion(self, plot):
		'Returns the region ID of a plot.'
		if (plot.getX(), plot.getY()) == con.tConstantinople:
			return con.rConstantinople
		return plot.getRegionID()
	
	
	def uniq(self, alist):
		'Returns a copy of alist with duplicate elements removed.'
		set = {}
		return [set.setdefault(e,e) for e in alist if e not in set]


# singleton for use by all modules

utils = RFCUtils()