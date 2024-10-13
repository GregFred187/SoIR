# Rhye's and Fall Redux - edead

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import DynamicCivs
from Consts import *
from StoredData import sd
from RFCUtils import utils

################
### Globals ###
##############

gc = CyGlobalContext()
localText = CyTranslator()
ArtFileMgr = CyArtFileMgr()
PyPlayer = PyHelpers.PyPlayer
DynamicCivs = DynamicCivs.DynamicCivs()

iCheatersPeriod = 12
iBetrayalPeriod = 8
iRebellionDelay = 15

pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
pIndependent3 = gc.getPlayer(iIndependent3)
pIndependent4 = gc.getPlayer(iIndependent4)
pBarbarian = gc.getPlayer(iBarbarian)

teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())
teamIndependent3 = gc.getTeam(pIndependent3.getTeam())
teamIndependent4 = gc.getTeam(pIndependent4.getTeam())
teamBarbarian = gc.getTeam(pBarbarian.getTeam())

bCityRadius = 2

class RiseAndFall:


#################################################
### Secure storage & retrieval of script data ###
#################################################

	def getNewCiv( self ):
		return sd.getNewCiv()

	def setNewCiv( self, iNewValue ):
		sd.setNewCiv(iNewValue)

	def getNewCivFlip( self ):
		return sd.getNewCivFlip()

	def setNewCivFlip( self, iNewValue ):
		sd.setNewCivFlip(iNewValue)

	def getOldCivFlip( self ):
		return sd.getOldCivFlip()

	def setOldCivFlip( self, iNewValue ):
		sd.setOldCivFlip(iNewValue)

	def getSpawnWar( self ):
		return sd.getSpawnWar()

	def setSpawnWar( self, iNewValue ):
		sd.setSpawnWar(iNewValue)

	def getAlreadySwitched( self ):
		return sd.getAlreadySwitched()

	def setAlreadySwitched( self, bNewValue ):
		sd.setAlreadySwitched(bNewValue)

	def getNumCities( self, iCiv ):
		return sd.getNumCities(iCiv)

	def setNumCities( self, iCiv, iNewValue ):
		sd.setNumCities(iCiv, iNewValue)

	def getSpawnDelay( self, iCiv ):
		return sd.getSpawnDelay(iCiv)

	def setSpawnDelay( self, iCiv, iNewValue ):
		sd.setSpawnDelay(iCiv, iNewValue)

	def getFlipsDelay( self, iCiv ):
		return sd.getFlipsDelay(iCiv)

	def setFlipsDelay( self, iCiv, iNewValue ):
		sd.setFlipsDelay(iCiv, iNewValue)

	def getBetrayalTurns( self ):
		return sd.getBetrayalTurns()

	def setBetrayalTurns( self, iNewValue ):
		sd.setBetrayalTurns(iNewValue)

	def getLatestFlipTurn( self ):
		return sd.getLatestFlipTurn()

	def setLatestFlipTurn( self, iNewValue ):
		sd.setLatestFlipTurn

	def getLatestRebellionTurn( self, iCiv ):
		return sd.getLatestRebellionTurn

	def setLatestRebellionTurn( self, iCiv, iNewValue ):
		sd.setLatestRebellionTurn

	def getRebelCiv( self ):
		return sd.getRebelCiv()

	def setRebelCiv( self, iNewValue ):
		sd.setRebelCiv(iNewValue)

	def getExileData( self, i ):
		return sd.getExileData(i)

	def setExileData( self, i, iNewValue ):
		sd.setExileData(i, iNewValue)

	def getTempFlippingCity( self ):
		return sd.getTempFlippingCity()

	def setTempFlippingCity( self, tNewValue ):
		sd.setTempFlippingCity(tNewValue)

	def getCheatersCheck( self, i ):
		return sd.getCheatersCheck(i)

	def setCheatersCheck( self, i, iNewValue ):
		sd.setCheatersCheck(i, iNewValue)

	def getDeleteMode( self, i ):
		return sd.getDeleteMode(i)

	def setDeleteMode( self, i, iNewValue ):
		sd.setDeleteMode(i, iNewValue)

	def getCheatMode( self ):
		return sd.getCheatMode()

	def setCheatMode( self, bNewValue ):
		sd.setCheatMode(bNewValue)

	def setCounter(self, iCounterID, iNewValue):
		sd.setCounter(iCounterID, iNewValue)

	def getCounter( self, iCounterID ):
		return sd.getCounter(iCounterID)

	def setTempPlotList( self, lNewList ):
		sd.setTempPlotList(lNewList)

	def getTempPlotList( self ):
		return sd.getTempPlotList()

	def setStopSpawn(self, iCiv, iNewValue):
		sd.setStopSpawn(iCiv, iNewValue)

	def getStopSpawn( self, iCiv ):
		return sd.getStopSpawn(iCiv)

###############
### Popups ###
#############

	def showPopup(self, popupID, title, message, labels):
		"""popupID has to be a registered ID in CvRhyesCatapultEventManager.__init__!"""
		
		popup = Popup.PyPopup(popupID, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(title)
		popup.setBodyString(message)
		for i in labels:
			popup.addButton(i)
		popup.launch(False)


	def newCivPopup(self, iCiv):
		self.showPopup(7614, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), CyTranslator().getText("TXT_KEY_NEWCIV_MESSAGE", (gc.getPlayer(iCiv).getCivilizationDescriptionKey(),)), (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCiv(iCiv)


	def eventApply7614(self, popupReturn):
		if popupReturn.getButtonClicked() == 0: # 1st button
			iOldHandicap = gc.getActivePlayer().getHandicapType()
			gc.getActivePlayer().setHandicapType(gc.getPlayer(sd.getNewCiv()).getHandicapType())
			gc.getGame().setActivePlayer(sd.getNewCiv(), False)
			gc.getPlayer(sd.getNewCiv()).setHandicapType(iOldHandicap)
			utils.setStartingStabilityParameters(sd.getNewCiv())
			for iMaster in range(iNumPlayers):
				if (gc.getTeam(gc.getPlayer(sd.getNewCiv()).getTeam()).isVassal(iMaster)):
					gc.getTeam(gc.getPlayer(sd.getNewCiv()).getTeam()).setVassal(iMaster, False, False)
			sd.setAlreadySwitched(True)
			gc.getPlayer(sd.getNewCiv()).setPlayable(True)


	# edead: Rhye's function modified to use plot lists
	def flipPopup(self, iNewCiv, plotList):
	
		iHuman = gc.getGame().getActivePlayer()
		flipText = CyTranslator().getText("TXT_KEY_FLIPMESSAGE1", ())
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				if (pCurrent.getPlotCity().getOwner() == iHuman):
					if (not (plotList[i] == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
						flipText += (pCurrent.getPlotCity().getName() + "\n")
		flipText += CyTranslator().getText("TXT_KEY_FLIPMESSAGE2", ())
		
		self.showPopup(7615, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), flipText, (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCivFlip(iNewCiv)
		self.setOldCivFlip(iHuman)
		self.setTempPlotList(plotList)


	# edead: Rhye's function modified to use plot lists
	def eventApply7615(self, popupReturn):
	
		iHuman = utils.getHumanID()
		plotList = self.getTempPlotList()
		iNewCivFlip = self.getNewCivFlip()
		
		humanCityList = []
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				city = pCurrent.getPlotCity()
				if (city.getOwner() == iHuman):
					if (not (plotList[i] == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
						humanCityList.append(city)
		
		if popupReturn.getButtonClicked() == 0: # 1st button
			print ("Flip agreed")
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_AGREED", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
			
			if (len(humanCityList)):
				for i in range(len(humanCityList)):
					city = humanCityList[i]
					print ("flipping ", city.getName())
					utils.cultureManager((city.getX(), city.getY()), 100, iNewCivFlip, iHuman, False, False, False)
					utils.flipUnitsInCityBefore((city.getX(), city.getY()), iNewCivFlip, iHuman)
					self.setTempFlippingCity((city.getX(), city.getY()))
					utils.flipCity((city.getX(), city.getY()), 0, 0, iNewCivFlip, [iHuman])
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCivFlip)
					
					#iEra = gc.getPlayer(iNewCivFlip).getCurrentEra()
					#if (iEra >= 2): #medieval
					#		if (city.getPopulation() < iEra):
					#				city.setPopulation(iEra) #causes an unidentifiable C++ exception
					
					#humanCityList[i].setHasRealBuilding(iPlague, False) #buggy
				
			#same code as Betrayal - done just once to make sure human player doesn't hold a stack just outside of the cities
			for i in range(len(plotList)):
				betrayalPlot = gc.getMap().plot(plotList[i][0], plotList[i][1])
				iNumUnitsInAPlot = betrayalPlot.getNumUnits()
				if (iNumUnitsInAPlot):
					for iJ in range(iNumUnitsInAPlot):
						pUnit = betrayalPlot.getUnit(iJ)
						if (pUnit.getOwner() == iHuman):
							rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
							if (rndNum >= self.getBetrayalThreshold()):
								if (pUnit.getDomainType() == 2): #land unit
									iUnitType = pUnit.getUnitType()
									pUnit.kill(False, iNewCivFlip)
									utils.makeUnit(iUnitType, iNewCivFlip, (plotList[i][0], plotList[i][1]), 1)
									iJ = iJ - 1
			
			#edead: extra defenders for cases of flip+war
			if gc.getTeam(gc.getPlayer(iHuman).getTeam()).isAtWar(iNewCivFlip):
				apCityList = PyPlayer(iNewCivFlip).getCityList()
				for pCity in apCityList:
					iFreeUnits = 1
					if pCity.GetCy().plot().getNumUnits() < 2: 
						iFreeUnits = 2
					utils.createGarrisons((pCity.getX(), pCity.getY()), iNewCivFlip, iFreeUnits)
								
			if self.getCheatersCheck(0) == 0:
				self.setCheatersCheck(0, iCheatersPeriod)
				self.setCheatersCheck(1, self.getNewCivFlip())
				
		elif popupReturn.getButtonClicked() == 1: # 2nd button
			print ("Flip disagreed")
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)

			if (len(humanCityList)):
				for iI in range(len(humanCityList)):
					city = humanCityList[iI]
					#city.setCulture(self.getNewCivFlip(), city.countTotalCulture(), True)
					pCurrent = gc.getMap().plot(city.getX(), city.getY())
					oldCulture = pCurrent.getCulture(iHuman)
					pCurrent.setCulture(iNewCivFlip, oldCulture/2, True)
					pCurrent.setCulture(iHuman, oldCulture/2, True)
					iWar = self.getSpawnWar() + 1
					self.setSpawnWar(iWar)
					if self.getSpawnWar() == 1:
						#CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "")
						gc.getTeam(gc.getPlayer(iNewCivFlip).getTeam()).declareWar(iHuman, False, -1) ##True??
						self.setBetrayalTurns(iBetrayalPeriod)
						self.initBetrayal()


	def rebellionPopup(self, iRebelCiv):
		self.showPopup(7622, CyTranslator().getText("TXT_KEY_REBELLION_TITLE", ()), \
			CyTranslator().getText("TXT_KEY_REBELLION_TEXT", (gc.getPlayer(iRebelCiv).getCivilizationAdjectiveKey(),)), \
			(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), \
			CyTranslator().getText("TXT_KEY_POPUP_NO", ())))


	def eventApply7622(self, popupReturn):
		iHuman = utils.getHumanID()
		iRebelCiv = self.getRebelCiv()
		if( popupReturn.getButtonClicked() == 0 ): # 1st button
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).makePeace(iRebelCiv)
		elif( popupReturn.getButtonClicked() == 1 ): # 2nd button
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).declareWar(iRebelCiv, False, -1)


#######################################
### Main methods (Event-Triggered) ###
#####################################


	def setup(self):
	
		self.createEarlyStartingUnits()
		
		for iLoopCiv in range(iNumTotalPlayers):
			gc.getPlayer(iLoopCiv).changeGold(tStartingGold[iLoopCiv]) # edead: set starting gold
		
		for iLoopCiv in range(iNumPlayers):
			if tBirth[iLoopCiv] == iStartYear: # edead: early civs only
				self.assignTechs(iLoopCiv) # assign techs
				utils.revealPlots(iLoopCiv, utils.getRegionPlotList(lRevealRegions[iLoopCiv], True)) 
				
				# reveal holy cites
				iStateReligion = gc.getPlayer(iLoopCiv).getStateReligion()
				if iStateReligion == iSunni:
					utils.revealCity(iLoopCiv, tMecca)
					utils.revealCity(iLoopCiv, tJerusalem)
				elif iStateReligion == iShia:
					utils.revealCity(iLoopCiv, tMecca)
					utils.revealCity(iLoopCiv, tJerusalem)
					utils.revealCity(iLoopCiv, tNajaf)
				elif iStateReligion == iOrthodoxy or iStateReligion == iCatholicism:
					utils.revealCity(iLoopCiv, tConstantinople)
					utils.revealCity(iLoopCiv, tJerusalem)
			
			# look at starting plot for late civs
			elif iLoopCiv == utils.getHumanID():
				gc.getMap().plot(tCapitals[iLoopCiv][0], tCapitals[iLoopCiv][1]).cameraLookAt()


	def checkTurn(self, iGameTurn):
	
		#Trigger betrayal mode
		if (self.getBetrayalTurns() > 0):
			self.initBetrayal()
		
		if (self.getCheatersCheck(0) > 0):
			teamPlayer = gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam())
			if (teamPlayer.isAtWar(self.getCheatersCheck(1))):
				print ("No cheaters!")
				self.initMinorBetrayal(self.getCheatersCheck(1))
				self.setCheatersCheck(0, 0)
				self.setCheatersCheck(1, -1)
			else:
				self.setCheatersCheck(0, self.getCheatersCheck(0)-1)
		
		if (iGameTurn % utils.getTurns(20) == 0):
			for i in range(iIndependent, iIndependent4 + 1):
				if gc.getPlayer(i).isAlive():
					utils.updateMinorTechs(i, iBarbarian)
		
		# conditional spawn - destroy old civs if possible
		iHuman = utils.getHumanID()
		for iCiv in [iAyyubids, iMamluks, iOttomans, iAkKoyunlu, iSafavids]:
			if iGameTurn == getTurnForYear(tBirth[iCiv]) - utils.getTurns(10):
				iCivToDie = None
				if iCiv == iHuman:
					if iCiv == iOttomans:
						if utils.checkRegionOwnedCity(iRum, rThrace) or utils.checkRegionOwnedCity(iRum, rAsia) or gc.getPlayer(iRum).getNumCities > 4:
							iCivToDie = iRum
					elif iCiv == iAkKoyunlu:
						iCivToDie = iZengids
					elif iCiv == iSafavids:
						iCivToDie = iSeljuks
					elif iCiv == iAyyubids or iCiv == iMamluks:
						iCivToDie = iFatimids
				else:
					if iCiv == iOttomans:
						if sd.getStability(iRum) < -10 and iRum != iHuman:
							iCivToDie = iRum
						elif sd.getStability(iRum) < 0 and iRum != iHuman:
							if utils.checkRegionOwnedCity(iRum, rThrace) or utils.checkRegionOwnedCity(iRum, rAsia):
								iCivToDie = iRum
					elif iCiv == iAkKoyunlu:
						if sd.getStability(iZengids) < 0 and iZengids != iHuman:
							iCivToDie = iZengids
					elif iCiv == iSafavids:
						if sd.getStability(iSeljuks) < -10 and iSeljuks != iHuman:
							iCivToDie = iSeljuks
					elif iCiv == iAyyubids or iCiv == iMamluks:
						if sd.getStability(iFatimids) < 0 and iFatimids != iHuman:
							iCivToDie = iFatimids
				if iCivToDie:
					if gc.getPlayer(iHuman).canContact(iCivToDie):
						CyInterface().addMessage(iHuman, False, iDuration, gc.getPlayer(iCivToDie).getCivilizationDescription(0) + " " + \
							CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
					utils.killAndFragmentCiv(iCivToDie, False)
		
		# move Ayyubid capital to Syria or kill them
		if iGameTurn == getTurnForYear(tBirth[iMamluks])-1 and utils.isActive(iAyyubids):
			plotCairo = gc.getMap().plot(tFustat[0],tFustat[1])
			if plotCairo.isCity() and plotCairo.getOwner() == iAyyubids:
				newCapital = None
				newPlot = gc.getMap().plot(tDamascus[0],tDamascus[1])
				if newPlot.isCity() and newPlot.getOwner() == iAyyubids:
					newCapital = newPlot.getPlotCity()
				else:
					apCityList = PyPlayer(iAyyubids).getCityList()
					for pCity in apCityList:
						city = pCity.GetCy()
						if city.plot().getRegionID() in [rSyria, rNorthernSyria]:
							newCapital = city
				if newCapital:			
					plotCairo.getPlotCity().setNumRealBuilding(iPalace, 0)
					newCapital.setNumRealBuilding(iPalace, 1)
				elif iAyyubids != iHuman:
					utils.killAndFragmentCiv(iAyyubids, False)

		# realistic Ottoman start - secede up to 3 Byzantine cities if they're too big
		if iGameTurn == getTurnForYear(tBirth[iOttomans]) - utils.getTurns(8):
			if iHuman != iByzantium:
				iCount = 0
				apCityList = PyPlayer(iByzantium).getCityList()
				for pCity in apCityList:
					if iCount == 3 or (iCount == 2 and gc.getPlayer(iByzantium).getNumCities() < 8):
						break
					city = pCity.GetCy()
					if city.plot().getRegionID() not in [rThrace, rAsia, rLycia, rBithynia, rTrebizond]:
						if gc.getGame().getSorenRandNum(100, 'Secession') < 50:
							if utils.secedeCity(city):
								iCount += 1
					
		# realistic Ottoman start - respawn Byzantines
		if iGameTurn == getTurnForYear(tBirth[iOttomans]) - utils.getTurns(7):
			if not gc.getPlayer(iByzantium).isAlive():
				if iHuman == iOttomans or gc.getMap().plot(tConstantinople[0], tConstantinople[1]).getOwner() >= iNumPlayers:
					self.resurrection(iGameTurn, iByzantium, 0)

		# realistic Ottoman start - respawn Karamanids
		if iGameTurn == getTurnForYear(tBirth[iOttomans]) - utils.getTurns(5):
			if not gc.getPlayer(iRum).isAlive():
				iKaramanChance = 50
				if iHuman == iOttomans: 
					iKaramanChance += 50
				elif iHuman == iAkKoyunlu:
					iKaramanChance += 25
				elif iHuman == iTimurids:
					iKaramanChance -= 10
				elif iHuman == iMamluks:
					iKaramanChance -= 30
				elif iHuman == iSafavids or iHuman == iMughals:
					iKaramanChance -= 40
				if gc.getGame().getSorenRandNum(100, 'Chance for Karaman spawn') < iKaramanChance:
					self.resurrection(iGameTurn, iRum, 0) # Karamanids
		
		# realistic Ottoman start - secede Gallipoli
		if iGameTurn == getTurnForYear(tBirth[iOttomans]) - utils.getTurns(3):
			if iHuman not in [iByzantium, iRum, iOttomans]:
				if gc.getGame().getSorenRandNum(100, 'Secession') < 50:
					plot = gc.getMap().plot(1,61) # Gallipoli
					if plot.isCity() and plot.getOwner() == iByzantium:
						utils.secedeCity(plot.getPlotCity())
		
		# help Armenia out so Cilician Armenia can respawn
		if iGameTurn == getTurnForYear(tRespawn[iArmenia])-10 and iHuman != iArmenia and iHuman != iGeorgia and gc.getPlayer(iArmenia).isAlive():
			iKillChance = -sd.getStability(iArmenia)*2
			if not utils.isActive(iHuman):
				iKillChance += 80
			elif iHuman not in [iByzantium, iSeljuks, iRum]:
				iKillChance += 60
			if gc.getGame().getSorenRandNum(100, 'Should Armenia die?') < iKillChance:
				if gc.getPlayer(iHuman).canContact(iArmenia):
					CyInterface().addMessage(iHuman, False, iDuration, gc.getPlayer(iArmenia).getCivilizationDescription(0) + " " + \
						CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				utils.killAndFragmentCiv(iArmenia, False)
		
		# help Ghorids out so Delhi Sultanate can respawn
		if iGameTurn == getTurnForYear(tRespawn[iGhorids])-2 and iHuman != iGhorids and iHuman != iGhaznavids and gc.getPlayer(iGhorids).isAlive():
			iKillChance = -sd.getStability(iGhorids)*2
			if not utils.isActive(iHuman):
				iKillChance += 90
				if iHuman == iMughals:
					iKillChance = 100
			elif iHuman not in [iChauhan, iGujarat, iSindh]:
				iKillChance += 60
			elif iHuman != gc.getMap().plot(tDelhi[0], tDelhi[1]).getOwner():
				iKillChance += 40
			if gc.getGame().getSorenRandNum(100, 'Should Ghorids die?') < iKillChance:
				if gc.getPlayer(iHuman).canContact(iGhorids):
					CyInterface().addMessage(iHuman, False, iDuration, gc.getPlayer(iGhorids).getCivilizationDescription(0) + " " + \
						CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				utils.killAndFragmentCiv(iGhorids, False)
				sd.setStability(iGhaznavids, sd.getStability(iGhaznavids)-5) # to balance the fact that their bane is gone

		# help Samanids out so Khwarezmshah does better
		if iGameTurn == getTurnForYear(tBirth[iKhwarezm])-10 and iHuman != iKhwarezm and iHuman != iSamanids and gc.getPlayer(iSamanids).isAlive():
			iKillChance = -sd.getStability(iSamanids)*2
			if not utils.isActive(iHuman) or iHuman not in [iSeljuks, iGhaznavids]:
				iKillChance += 40
			if gc.getGame().getSorenRandNum(100, 'Should Samanids die?') < iKillChance:
				if gc.getPlayer(iHuman).canContact(iSamanids):
					CyInterface().addMessage(iHuman, False, iDuration, gc.getPlayer(iSamanids).getCivilizationDescription(0) + " " + \
						CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
				utils.killAndFragmentCiv(iSamanids, False)
				
		# clear Afghanistan before Mughal spawn
		if iGameTurn == getTurnForYear(tBirth[iMughals])-15 and iHuman != iGhorids:
			for tPlot in utils.getRegionPlotList([rBactria]):
				pCurrent = gc.getMap().plot(tPlot[0],tPlot[1])
				if pCurrent.isCity() and pCurrent.getOwner() == iGhorids:
					utils.secedeCity(pCurrent.getPlotCity())
		if iGameTurn == getTurnForYear(tBirth[iMughals])-10 and iHuman != iGhorids:
			for tPlot in utils.getRegionPlotList([rHindukush]):
				pCurrent = gc.getMap().plot(tPlot[0],tPlot[1])
				if pCurrent.isCity() and pCurrent.getOwner() == iGhorids:
					utils.secedeCity(pCurrent.getPlotCity())
		if iGameTurn == getTurnForYear(tBirth[iMughals])-5 and iHuman != iGhorids:
			for tPlot in utils.getRegionPlotList([rEasternKhorasan]):
				pCurrent = gc.getMap().plot(tPlot[0],tPlot[1])
				if pCurrent.isCity() and pCurrent.getOwner() == iGhorids:
					utils.secedeCity(pCurrent.getPlotCity())
		
		# make sure Antioch and Jerusalem are in Muslim hands when crusade comes
		if iGameTurn == getTurnForYear(tBirth[iAntioch])-5:
			city = gc.getMap().plot(tAntioch[0],tAntioch[1]).getPlotCity()
			if city and not city.isNone():
				if gc.getPlayer(city.getOwner()).getStateReligion() == iOrthodoxy:
					utils.secedeCity(city)
		if iGameTurn == getTurnForYear(tBirth[iCrusaders])-5:
			city = gc.getMap().plot(tJerusalem[0],tJerusalem[1]).getPlotCity()
			if city and not city.isNone():
				if gc.getPlayer(city.getOwner()).getStateReligion() == iOrthodoxy:
					utils.secedeCity(city)
		
		# make sure there is at least 1 defender in Antioch and Jerusalem
		if iGameTurn == getTurnForYear(tBirth[iAntioch])-1:
			plot = gc.getMap().plot(tAntioch[0],tAntioch[1])
			if plot.getNumUnits() < 2 and iHuman != plot.getOwner():
				utils.makeUnit(iSpearman, plot.getOwner(), tAntioch, 1)
		if iGameTurn == getTurnForYear(tBirth[iCrusaders])-1:
			plot = gc.getMap().plot(tJerusalem[0],tJerusalem[1])
			if plot.getNumUnits() < 2 and iHuman != plot.getOwner():
				utils.makeUnit(iSpearman, plot.getOwner(), tJerusalem, 1)
		
		# loop through civs and check birth dates - edead
		for iLoopCiv in range(iNumPlayers):
			if tBirth[iLoopCiv] > iStartYear and iGameTurn >= getTurnForYear(tBirth[iLoopCiv]) - 2 and iGameTurn <= getTurnForYear(tBirth[iLoopCiv]) + 6:
				self.initBirth(iGameTurn, tBirth[iLoopCiv], iLoopCiv)
			# flip cities to Abbasids
			elif iLoopCiv == iAbbasids and iGameTurn == 0:
				self.convertSurroundingCities(iLoopCiv, utils.getCorePlotList(iLoopCiv))
				self.convertSurroundingPlotCulture(iLoopCiv, utils.getCorePlotList(iLoopCiv))
		
		# fragment utility
		if iGameTurn >= getTurnForYear(1140) and iGameTurn % utils.getTurns(25) == 6:
			self.fragmentIndependents()
		
		# fall of civs
		if iGameTurn >= getTurnForYear(1030):
			if iGameTurn % utils.getTurns(4) == 0:
				self.collapseByBarbs(iGameTurn)
			if iGameTurn % utils.getTurns(12) == 7:
				self.collapseMotherland(iGameTurn)
		if iGameTurn % utils.getTurns(20) == 0:
			self.collapseGeneric(iGameTurn)
		if iGameTurn % utils.getTurns(8) == 2:
			self.revolt(iGameTurn, -10)
		if iGameTurn % utils.getTurns(8) == 6:
			self.secession(iGameTurn, -20)
		if iGameTurn % utils.getTurns(16) == 14:
			self.secession(iGameTurn, -40)
		
		# historical resurrection
		bFound = False
		for iLoopCiv in range(iNumPlayers):
			if tRespawn[iLoopCiv] == 0:
				continue
			iRespawnTurn = getTurnForYear(tRespawn[iLoopCiv])
			if iGameTurn == iRespawnTurn or iGameTurn == iRespawnTurn + utils.getTurns(10) or iGameTurn == iRespawnTurn + utils.getTurns(20):
				iThreshold = 10
				if iLoopCiv == iArmenia or iLoopCiv == iGhorids:
					iThreshold = 1
				if iGameTurn == iRespawnTurn + utils.getTurns(10):
					iThreshold += 10
				if iGameTurn == iRespawnTurn + utils.getTurns(20):
					iThreshold += 20
				if not gc.getPlayer(iLoopCiv).isAlive() and iGameTurn > sd.getLastTurnAlive(iLoopCiv) + utils.getTurns(iThreshold):
					self.resurrection(iGameTurn, iLoopCiv, iThreshold)
					bFound = True
					break
		
		# random resurrection
		if not bFound:
			iPermaDead = 0
			iCurrentYear = gc.getGame().getGameTurnYear()
			for i in range(len(tFallRespawned)):
				if iCurrentYear > tFallRespawned[i] and not gc.getPlayer(i).isAlive():
					iPermaDead += 1
			iNumDeadCivs1 = max(12, 4 + iPermaDead) # 12
			iNumDeadCivs2 = max(7, 2 + iPermaDead) # 7
			if (gc.getGame().countCivPlayersEverAlive() - gc.getGame().countCivPlayersAlive() > iNumDeadCivs1): 
				if (iGameTurn % utils.getTurns(15) == 10):
					self.resurrection(iGameTurn)
			elif (gc.getGame().countCivPlayersEverAlive() - gc.getGame().countCivPlayersAlive() > iNumDeadCivs2): 
				if (iGameTurn % utils.getTurns(30) == 15):
					self.resurrection(iGameTurn)
		
		# capitals
		self.checkCapitals(iGameTurn)

	# from RFCEurope
	def fragmentIndependents(self): 
		
		for iTest1 in range( iIndependent, iIndependent4 + 1):
			for iTest2 in range( iIndependent, iIndependent4 + 1):
				if ( not (iTest1 == iTest2) ):
					pTest1 = gc.getPlayer( iTest1 )
					pTest2 = gc.getPlayer( iTest2 )
					if ( abs( pTest1.getNumCities() - pTest2.getNumCities() ) > 5 ):
						if ( pTest1.getNumCities() > pTest2.getNumCities() ):
							iBig = iTest1
							pBig = pTest1
							iSmall = iTest2
							pSmall = pTest2
						else:
							iBig = iTest2
							pBig = pTest2
							iSmall = iTest1
							pSmall = pTest1
						apCityList = PyPlayer(iBig).getCityList()
						iDivideCounter = 0
						iCounter = 0
						for pCity in apCityList:
							iDivideCounter += 1
							if (iDivideCounter % 2 == 1):
								city = pCity.GetCy()
								pCurrent = gc.getMap().plot(city.getX(), city.getY())										
								utils.cultureManager((city.getX(),city.getY()), 50, iSmall, iBig, False, True, True)
								utils.flipUnitsInCityBefore((city.getX(),city.getY()), iSmall, iBig)							
								self.setTempFlippingCity((city.getX(),city.getY()))
								utils.flipCity((city.getX(),city.getY()), 0, 0, iSmall, [iBig])   #by trade because by conquest may raze the city
								utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iSmall)
								iCounter += 1
							if ( iCounter == 3 ):
								break


	def collapseByBarbs(self, iGameTurn):
		
		for iCiv in range(iNumPlayers):
			if not utils.canCollapse(iCiv):
				continue
			pCiv = gc.getPlayer(iCiv)
			if not pCiv.isHuman() and pCiv.isAlive():
				if iGameTurn >= getTurnForYear(tBirth[iCiv]) + utils.getTurns(25):
					iNumCities = pCiv.getNumCities()
					iLostCities = 0
					map = CyMap()
					for i in range(map.numPlots()):
						plot = map.plotByIndex(i)
						if plot.isCity():
							city = plot.getPlotCity()
							if city.getOwner() == iBarbarian:
								if city.getOriginalOwner() == iCiv:
									iLostCities = iLostCities + 1
					if iLostCities*2 > iNumCities and iNumCities > 0: #if more than one third is captured, the civ collapses
						print ("COLLAPSE BY BARBS", gc.getPlayer(iCiv).getCivilizationAdjective(0))
						utils.killAndFragmentCiv(iCiv, False)


	def collapseGeneric(self, iGameTurn):
		
		lNumCitiesNew = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for iCiv in range(iNumPlayers):
			if not utils.canCollapse(iCiv):
				continue
			
			# let Ayyubids survive in Syria after Mamluk spawn
			if iCiv == iAyyubids and iGameTurn > getTurnForYear(tBirth[iMamluks]) and iGameTurn <= getTurnForYear(tBirth[iMamluks]) + utils.getTurns(15):
				continue
			
			pCiv = gc.getPlayer(iCiv)
			teamCiv = gc.getTeam(pCiv.getTeam())
			if (pCiv.isAlive()):
				if (iGameTurn >= getTurnForYear(tBirth[iCiv]) + utils.getTurns(25)):
					lNumCitiesNew[iCiv] = pCiv.getNumCities()
					if (lNumCitiesNew[iCiv]*2 <= self.getNumCities(iCiv)): #if number of cities is less than half than some turns ago, the civ collapses
						print ("COLLAPSE GENERIC", pCiv.getCivilizationAdjective(0), lNumCitiesNew[iCiv]*2, "<=", self.getNumCities(iCiv))
						if (gc.getPlayer(iCiv).isHuman() == 0):
							bVassal = False
							for iMaster in range(iNumPlayers):
								if (teamCiv.isVassal(iMaster)):
									bVassal = True
									break
							if (not bVassal):
								utils.killAndFragmentCiv(iCiv, False)
					else:
						self.setNumCities(iCiv, lNumCitiesNew[iCiv])


	def collapseMotherland(self, iGameTurn):
		"""Collapses if completely out of broader areas."""
		
		for iCiv in range(iNumPlayers):
			if not utils.canCollapse(iCiv):
				continue
			pCiv = gc.getPlayer(iCiv)
			teamCiv = gc.getTeam(pCiv.getTeam())
			if not pCiv.isHuman() and pCiv.isAlive():
				if (iGameTurn >= getTurnForYear(tBirth[iCiv]) + utils.getTurns(25)):
					bSafe = False
					plotList = utils.getCorePlotList(iCiv)
					for i in range(len(plotList)):
						pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
						if pCurrent.isCity():
							#print (pCurrent.getPlotCity().getOwner(), pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getX(), pCurrent.getPlotCity().getY())
							if (pCurrent.getPlotCity().getOwner() == iCiv):
								#print ("iCiv", iCiv, "bSafe", bSafe)
								bSafe = True
								break
								break
					if bSafe == False:
						iCitiesOwned = 0
						iCitiesLost = 0
						plotList = utils.getNormalPlotList(iCiv)
						for i in range(len(plotList)):
							pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
							if pCurrent.isCity():
								#print (pCurrent.getPlotCity().getOwner(), pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getX(), pCurrent.getPlotCity().getY())
								if pCurrent.getPlotCity().getOwner() == iCiv:
									iCitiesOwned += 1
								else:
									iCitiesLost += 1
						if iCitiesOwned > iCitiesLost:
							bSafe = True
					#print ("iCiv", iCiv, "bSafe", bSafe)
					if (bSafe == False):
						bVassal = False
						for iMaster in range(iNumPlayers):
							if (teamCiv.isVassal(iMaster)):
								bVassal = True
								break
						if (not bVassal):
							print ("COLLAPSE: MOTHERLAND", gc.getPlayer(iCiv).getCivilizationAdjective(0))
							utils.killAndFragmentCiv(iCiv, False)
						return


	def revolt(self, iGameTurn, iThreshold=-10):
		
		iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
		for j in range(iRndnum, iRndnum + iNumPlayers):
			iPlayer = j % iNumPlayers   
			if gc.getPlayer(iPlayer).isAlive() and iGameTurn >= getTurnForYear(tBirth[iPlayer]) + utils.getTurns(20):
				if sd.getStability(iPlayer) < iThreshold:
					if iPlayer == iFatimids and gc.getGame().getSorenRandNum(100, 'Fatimid UP') < 50:
						continue
					utils.secedeRandomCity(iPlayer, 1 + gc.getGame().getSorenRandNum(3, 'Revolt length')) # second argument: revolt for x turns
					return #just 1 revolt per turn


	def secession(self, iGameTurn, iThreshold=-20):
		
		iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
		for j in range(iRndnum, iRndnum + iNumPlayers):
			iPlayer = j % iNumPlayers   
			if gc.getPlayer(iPlayer).isAlive() and iGameTurn >= getTurnForYear(tBirth[iPlayer]) + utils.getTurns(20):
				if sd.getStability(iPlayer) < iThreshold:
					utils.secedeRandomCity(iPlayer)
					return #just 1 secession per turn


	def resurrection(self, iGameTurn, iForcedCiv = -1, iMinTurns = 20):
		
		iMinNumCities = 3
		iMaxNumCities = 20
		
		if iForcedCiv > -1:
			iRndnum = iForcedCiv
		else:
			iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
		if iForcedCiv == iByzantium: 
			iMinNumCities = 1
		elif iForcedCiv == iCrusaders:
			iMinNumCities = 1
			iMaxNumCities = 2
		elif iForcedCiv == iArmenia:
			iMinNumCities = 2
			iMaxNumCities = 3
		elif iForcedCiv == iRum:
			iMinNumCities = 2
			iMaxNumCities = 2
		
		cityList = []
		bDeadCivFound = False
		for j in range(iRndnum, iRndnum + iNumPlayers):
			iDeadCiv = j % iNumPlayers
			iResurrectionProb = tResurrectionProb[iDeadCiv]
			if iDeadCiv == iRum and iForcedCiv != iRum:
				if utils.getHumanID() != iOttomans:
					iResurrectionProb /= 2
				if utils.getHumanID() in [iMamluks, iSafavids, iMughals]:
					iResurrectionProb = 0
			cityList = []
			if (not gc.getPlayer(iDeadCiv).isAlive() and iGameTurn > getTurnForYear(tBirth[iDeadCiv]) + utils.getTurns(50) and iGameTurn > sd.getLastTurnAlive(iDeadCiv) + utils.getTurns(iMinTurns) and iGameTurn < getTurnForYear(tFallRespawned[iDeadCiv])):
				if gc.getGame().getSorenRandNum(100, 'roll') >= iResurrectionProb and iDeadCiv != iForcedCiv:
					continue
				if iDeadCiv == iKhwarezm and (utils.getHumanID() == iTimurids or iGameTurn < getTurnForYear(1510)): # would be too annoying
					continue
				pDeadCiv = gc.getPlayer(iDeadCiv)
				teamDeadCiv = gc.getTeam(pDeadCiv.getTeam())
				plotList = utils.getRegionPlotList(lRespawnRegions[iDeadCiv]) # edead
				if iDeadCiv == iCrusaders and utils.getYear() >= 1309: # add knights of rhodes
					plotList.extend(utils.getRegionPlotList([rRhodes]))
				if iDeadCiv == iKhwarezm:
					plotList.extend(utils.getRegionPlotList([rKyzylKum, rFarghana]))
				
				for i in range(len(plotList)):
					pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
					if (pCurrent.isCity()):
						city = pCurrent.getPlotCity()
						iOwner = city.getOwner()
						pOwner = gc.getPlayer(iOwner)
						if (iOwner >= iNumPlayers):
							cityList.append(pCurrent.getPlotCity())
							print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "1", cityList)
						else:
							iMinNumCitiesOwner = 3
							iOwnerStability = sd.getStability(iOwner)
							
							# edead: conditional civs are less likely to respawn over their prereqs
							if (iDeadCiv == iOttomans and iOwner == iRum) or (iDeadCiv == iMamluks and iOwner in [iFatimids, iAyyubids]):
								iOwnerStability += 30
							if iDeadCiv == iKhwarezm:
								iOwnerStability -= 20
							
							if not pOwner.isHuman():
								iMinNumCitiesOwner = 2
								iOwnerStability -= 20
							if pOwner.getNumCities() >= iMinNumCitiesOwner:
								if iOwnerStability < -20:
									if not city.isWeLoveTheKingDay() and not city.isCapital():
										cityList.append(pCurrent.getPlotCity())
										print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "2", cityList)
								elif iOwnerStability < 0:
									if not city.isWeLoveTheKingDay() and not city.isCapital():
										if not (city.getX() == tCapitals[iOwner][0] and city.getY() == tCapitals[iOwner][1]) or iDeadCiv == iKhwarezm:
											if pOwner.getNumCities() > 0: #this check is needed, otherwise game crashes
												capital = pOwner.getCapitalCity()
												iDistance = utils.calculateDistance(plotList[i][0], plotList[i][1], capital.getX(), capital.getY())
												if ((iDistance >= 6 and pOwner.getNumCities() >= 4) or \
													city.angryPopulation(0) > 0 or \
													city.healthRate(False, 0) < 0 or \
													city.getReligionBadHappiness() > 0 or \
													city.getHurryAngerModifier() > 0 or \
													city.getNoMilitaryPercentAnger() > 0 or \
													city.getWarWearinessPercentAnger() > 0):
														cityList.append(pCurrent.getPlotCity())
														#print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "3", cityList)
								if (iOwnerStability < 20):
									if (city.getX() == tRespawnCapitals[iDeadCiv][0] and city.getY() == tRespawnCapitals[iDeadCiv][1]):
										#print(pCurrent.getPlotCity(), cityList)
										#if (pCurrent.getPlotCity() not in cityList):  #sadly, this doesn't work
										bAlreadyAdded = False
										for l in range(len(cityList)):
											 if (cityList[l].getName() == city.getName()):
												 bAlreadyAdded = True
												 break
										#print("bAlreadyAdded",bAlreadyAdded)
										if (not bAlreadyAdded):
											cityList.append(pCurrent.getPlotCity())
											#print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "4", cityList)
				#print("len(cityList)",len(cityList))
				if len(cityList) >= iMinNumCities:
					bDeadCivFound = True
					break
		#print ("iDeadCiv", iDeadCiv)
		if (bDeadCivFound):
			
			DynamicCivs.onCivRespawn(iDeadCiv) # edead
			
			# cut off some cities to make sure a civ is not too powerful
			while (len(cityList) > iMaxNumCities):
				cityList.pop()
			
			self.setRebelCiv(iDeadCiv) #for popup and CollapseCapitals()
			for l in range(iNumPlayers):
				teamDeadCiv.makePeace(l)
			self.setNumCities(iDeadCiv, 0) #reset collapse condition

			#reset vassallage
			for iOtherCiv in range(iNumPlayers):
				if (teamDeadCiv.isVassal(iOtherCiv) or gc.getTeam(gc.getPlayer(iOtherCiv).getTeam()).isVassal(iDeadCiv)):
					teamDeadCiv.freeVassal(iOtherCiv)
					gc.getTeam(gc.getPlayer(iOtherCiv).getTeam()).freeVassal(iDeadCiv)
					
			iNewUnits = 2
			if (self.getLatestRebellionTurn(iDeadCiv) > 0):
				iNewUnits = 4
			self.setLatestRebellionTurn(iDeadCiv, iGameTurn)
			bHuman = False
			iHuman = utils.getHumanID()
			print ("RESURRECTION", gc.getPlayer(iDeadCiv).getCivilizationAdjective(0))
			
			for kCity in cityList:
				if kCity.getOwner() == iHuman:
					bHuman = True
					break

			for t in range(iNumTechs - 1): # edead: -1 to skip dummy techs
				if (teamBarbarian.isHasTech(t) or teamIndependent.isHasTech(t) or teamIndependent2.isHasTech(t) or teamIndependent3.isHasTech(t) or teamIndependent4.isHasTech(t)): #remove indep in vanilla
					teamDeadCiv.setHasTech(t, True, iDeadCiv, False, False)

			ownersList = []		
			bAlreadyVassal = False
			for k in range(len(cityList)):
				if (cityList[k] != None): #once happened that it was = none
					#print ("INDEPENDENCE: ", cityList[k].getName()) #may cause a c++ exception									   
					iOwner = cityList[k].getOwner()
					teamOwner = gc.getTeam(gc.getPlayer(iOwner).getTeam())
					bOwnerVassal = teamOwner.isAVassal()
					bOwnerHumanVassal = teamOwner.isVassal(iHuman)

					if iOwner not in ownersList: #assignment of techs must be done before the creation of garrisons
						for t in range(iNumTechs):
							if teamOwner.isHasTech(t): 
								teamDeadCiv.setHasTech(t, True, iDeadCiv, False, False)

					if iOwner == iBarbarian or (iOwner >= iIndependent and iOwner <= iIndependent4):
						utils.cultureManager((cityList[k].getX(),cityList[k].getY()), 100, iDeadCiv, iOwner, False, True, True)
						utils.flipUnitsInCityBefore((cityList[k].getX(),cityList[k].getY()), iDeadCiv, iOwner)
						self.setTempFlippingCity((cityList[k].getX(),cityList[k].getY()))
						utils.flipCity((cityList[k].getX(),cityList[k].getY()), 0, 0, iDeadCiv, [iOwner])
						tCoords = self.getTempFlippingCity()
						utils.flipUnitsInCityAfter(tCoords, iOwner)
						utils.flipUnitsInArea(utils.getAreaPlotList((tCoords[0]-2, tCoords[1]-2), (tCoords[0]+2, tCoords[1]+2)), iDeadCiv, iOwner, True, False)
					else:
						utils.cultureManager((cityList[k].getX(),cityList[k].getY()), 50, iDeadCiv, iOwner, False, True, True)
						utils.pushOutGarrisons((cityList[k].getX(),cityList[k].getY()), iOwner)
						utils.relocateSeaGarrisons((cityList[k].getX(),cityList[k].getY()), iOwner)																		
						self.setTempFlippingCity((cityList[k].getX(),cityList[k].getY()))
						utils.flipCity((cityList[k].getX(),cityList[k].getY()), 0, 0, iDeadCiv, [iOwner])   #by trade because by conquest may raze the city
						utils.createGarrisons(self.getTempFlippingCity(), iDeadCiv, iNewUnits)
						
					#cityList[k].setHasRealBuilding(iPlague, False)

					bAtWar = False #AI won't vassalise if another owner has declared war; on the other hand, it won't declare war if another one has vassalised
					if (iOwner != iHuman and iOwner not in ownersList and iOwner != iDeadCiv and iOwner != iBarbarian): #declare war or peace only once - the 3rd condition is obvious but "vassal of themselves" was happening
						rndNum = gc.getGame().getSorenRandNum(100, 'odds')
						if (rndNum >= tAIStopBirthThreshold[iOwner] and bOwnerHumanVassal == False and bAlreadyVassal == False): #if bOwnerHumanVassal is true, it will skip to the 3rd condition, as bOwnerVassal is true as well
							teamOwner.declareWar(iDeadCiv, False, -1)
							bAtWar = True
						elif (rndNum <= (100-tAIStopBirthThreshold[iOwner])/2):
							teamOwner.makePeace(iDeadCiv)
							if (bAlreadyVassal == False and bHuman == False and bOwnerVassal == False and bAtWar == False): #bHuman == False cos otherwise human player can be deceived to declare war without knowing the new master
								if (iOwner < iNumPlayers): 
									gc.getTeam(gc.getPlayer(iDeadCiv).getTeam()).setVassal(iOwner, True, False)  #remove in vanilla
									bAlreadyVassal = True
						else:
							teamOwner.makePeace(iDeadCiv)
					
					if (iOwner not in ownersList):
						ownersList.append(iOwner) 

			self.moveBackCapital(iDeadCiv)
			
			#add normal regions that are still free
			colonyList = []
			for iIndCiv in range(iIndependent, iBarbarian + 1, 1): #barbarians too
				if (gc.getPlayer(iIndCiv).isAlive()):
					apCityList = PyPlayer(iIndCiv).getCityList()
					for pCity in apCityList:
						indepCity = pCity.GetCy()
						if indepCity.getOriginalOwner() == iDeadCiv or (indepCity.plot().getRegionID() in lRespawnNormalRegions[iDeadCiv] and iDeadCiv == iKhwarezm):
							#print ("colony:", indepCity.getName(), indepCity.getOriginalOwner())
							pCurrent = gc.getMap().plot(indepCity.getX(),indepCity.getY())
							if pCurrent.getRegionID() in lRespawnNormalRegions[iDeadCiv]:
								if (indepCity not in cityList and indepCity not in colonyList):
									colonyList.append(indepCity)
			if (len(colonyList) > 0):
				for k in range(len(colonyList)):
					#print ("INDEPENDENCE: ", colonyList[k].getName())   
					iOwner = colonyList[k].getOwner()
					utils.cultureManager((colonyList[k].getX(),colonyList[k].getY()), 100, iDeadCiv, iOwner, False, True, True)
					utils.flipUnitsInCityBefore((colonyList[k].getX(),colonyList[k].getY()), iDeadCiv, iOwner)
					self.setTempFlippingCity((colonyList[k].getX(),colonyList[k].getY()))
					utils.flipCity((colonyList[k].getX(),colonyList[k].getY()), 0, 0, iDeadCiv, [iOwner])
					tCoords = self.getTempFlippingCity()
					utils.flipUnitsInCityAfter(tCoords, iOwner)
					utils.flipUnitsInArea(utils.getAreaPlotList((tCoords[0]-2, tCoords[1]-2), (tCoords[0]+2, tCoords[1]+2)), iDeadCiv, iOwner, True, False)
			
			if utils.isActive(iHuman):
				textKey = "TXT_KEY_INDEPENDENCE_TEXT"
				if iDeadCiv == iCrusaders:
					textKey = "TXT_KEY_INDEPENDENCE_TEXT_CRUSADE"
				elif iDeadCiv == iArmenia:
					textKey = "TXT_KEY_INDEPENDENCE_TEXT_CILICIA"
				elif iDeadCiv == iKhwarezm:
					textKey = "TXT_KEY_INDEPENDENCE_TEXT_SHAYBANIDS"
				elif iDeadCiv == iGhorids:
					textKey = "TXT_KEY_INDEPENDENCE_TEXT_DELHI"
				CyInterface().addMessage(iHuman, True, iDuration, \
					(CyTranslator().getText(textKey, (pDeadCiv.getCivilizationAdjectiveKey(),))), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
			
			utils.setBaseStabilityLastTurn(iDeadCiv, 0)
			utils.setStability(iDeadCiv, 10) #the new civs start as slightly stable
			if iDeadCiv == iKhwarezm:
				utils.setStability(iDeadCiv, 25) # Uzbeks have issues for some reason
			utils.setPlagueCountdown(iDeadCiv, -10)
			utils.clearPlague(iDeadCiv)
			if iDeadCiv in [iArmenia, iGhorids, iCrusaders, iRum, iAbbasids, iKhwarezm]:
				self.convertBackCulture(iDeadCiv, True)
			else:
				self.convertBackCulture(iDeadCiv)
			
			# Shaybanids - declare war on Timurids
			if iDeadCiv == iKhwarezm:
				utils.flipUnitsInArea(utils.getNormalPlotList(iDeadCiv), iDeadCiv, iBarbarian, True, False)
				if gc.getPlayer(iTimurids).isAlive():
					gc.getTeam(gc.getPlayer(iDeadCiv).getTeam()).declareWar(gc.getPlayer(iTimurids).getTeam(), True, -1)
					# Timurids tend to survive this war too often
					if sd.getStability(iTimurids) > 0:
						sd.setStability(iTimurids, sd.getStability(iTimurids) - 10)
					else:
						sd.setStability(iTimurids, sd.getStability(iTimurids) - 5)
			
			# Karamanids - make them more tame
			if iDeadCiv == iRum:
				for i in range(iIndependent, iIndependent4 + 1):
					teamDeadCiv.makePeace(i)
			
			# Armenian Cilicia - religion & attitude
			elif iDeadCiv == iArmenia:
				if pDeadCiv.getStateReligion() != iOrthodoxy:
					pDeadCiv.setLastStateReligion(iOrthodoxy)
				if pDeadCiv.AI_getAttitudeExtra(iCrusaders) < 1:
					pDeadCiv.AI_changeAttitudeExtra(iCrusaders, 1)
				if gc.getPlayer(iCrusaders).AI_getAttitudeExtra(iArmenia) < 1:
					gc.getPlayer(iCrusaders).AI_changeAttitudeExtra(iArmenia, 1)
				pCapital = gc.getPlayer(iDeadCiv).getCapitalCity()
				if not pCapital.isHasReligion(iOrthodoxy):
					pCapital.setHasReligion(iOrthodoxy, True, True, True)
				else:
					apCityList = PyPlayer(iDeadCiv).getCityList()
					for pCity in apCityList:
						if not pCity.GetCy().isHasReligion(iOrthodoxy):
							pCity.GetCy().setHasReligion(iOrthodoxy, True, True, True)
							break
			
			# Delhi Sultanate - religion
			elif iDeadCiv == iGhorids:
				if pDeadCiv.getStateReligion() != iSunni:
					pDeadCiv.setLastStateReligion(iSunni)
				pCapital = gc.getPlayer(iDeadCiv).getCapitalCity()
				if not pCapital.isHasReligion(iSunni):
					pCapital.setHasReligion(iSunni, True, True, True)
				else:
					apCityList = PyPlayer(iDeadCiv).getCityList()
					for pCity in apCityList:
						if not pCity.GetCy().isHasReligion(iSunni):
							pCity.GetCy().setHasReligion(iSunni, True, True, True)
							break
			
			# Gujarat, Malwa and Sindhi Sultanates - religion
			elif iDeadCiv in [iGujarat, iMalwa, iSindh] and utils.getYear() > 1290:
				pDeadCiv.setLastStateReligion(iSunni)
				gc.getLeaderHeadInfo(pDeadCiv.getLeaderType()).setFavoriteReligion(iSunni)
				pCapital = gc.getPlayer(iDeadCiv).getCapitalCity()
				if not pCapital.isHasReligion(iSunni):
					pCapital.setHasReligion(iSunni, True, True, True)
				else:
					apCityList = PyPlayer(iDeadCiv).getCityList()
					for pCity in apCityList:
						if not pCity.GetCy().isHasReligion(iSunni):
							pCity.GetCy().setHasReligion(iSunni, True, True, True)
							break
			
			# Cyprus - religion & free buildings
			if iDeadCiv == iCrusaders:
				gc.getMap().plot(15,47).setBonusType(iSugar)
				if pDeadCiv.getStateReligion() != iCatholicism:
					pDeadCiv.setLastStateReligion(iCatholicism)
				pCapital = gc.getPlayer(iDeadCiv).getCapitalCity()
				if pCapital and not pCapital.isHasReligion(iCatholicism):
					pCapital.setHasReligion(iCatholicism, True, True, True)
				if pCapital:
					pCapital.setNumRealBuilding(iAqueduct, 1)
					pCapital.setNumRealBuilding(iHospital, 1)
					pCapital.setNumRealBuilding(iWalls, 1)
					pCapital.setNumRealBuilding(iCastle, 1)
					pCapital.setNumRealBuilding(iBlacksmith, 1)
					pCapital.setNumRealBuilding(iCatholicTemple, 1)
					pCapital.setNumRealBuilding(iCatholicMonastery, 1)
					pCapital.setNumRealBuilding(iBarracks, 1)
					pCapital.setNumRealBuilding(iArcheryRange, 1)
					pCapital.setNumRealBuilding(iLighthouse, 1)
					pCapital.setNumRealBuilding(iHarbor, 1)
					utils.makeUnit(iMarksman, iCrusaders, (pCapital.getX(), pCapital.getY()), 1, UnitAITypes.UNITAI_CITY_DEFENSE, (iCityGarrison1, ))
					tSeaPlot = utils.findSeaPlots((pCapital.getX(), pCapital.getY()), 1, iCrusaders)
					utils.makeUnit(iWarGalley, iCrusaders, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK_SEA, (iCombat1, ))
				pRhodes = gc.getMap().plot(tRhodes[0],tRhodes[1]).getPlotCity()
				if pRhodes and not pRhodes.isNone() and pRhodes.getOwner() == iCrusaders:
					if not pRhodes.isHasReligion(iCatholicism):
						pRhodes.setHasReligion(iCatholicism, True, True, True)
					if not pRhodes.isHasCorporation(iHospitallers):
						pRhodes.setHasCorporation(iHospitallers, True, True, True)
					pRhodes.setNumRealBuilding(iAqueduct, 1)
					pRhodes.setNumRealBuilding(iHospital, 1)
					pRhodes.setNumRealBuilding(iWalls, 1)
					pRhodes.setNumRealBuilding(iCastle, 1)
					pRhodes.setNumRealBuilding(iBlacksmith, 1)
					pRhodes.setNumRealBuilding(iBarracks, 1)
					pRhodes.setNumRealBuilding(iLighthouse, 1)
					pRhodes.setNumRealBuilding(iHarbor, 1)
					utils.makeUnit(iHospitaller, iCrusaders, (pRhodes.getX(), pRhodes.getY()), 1, UnitAITypes.UNITAI_CITY_DEFENSE, (iCombat1, iCombat2))
			
			# update the name again after flip & religion changes
			DynamicCivs.onCivRespawn(iDeadCiv)
			
			# rebellion popup moved to the end to make sure the name is right
			if bHuman:
				self.rebellionPopup(iDeadCiv)
			
			# update leader
			# if len(tLeaders[iDeadCiv]) > 0:
				# iNewLeader = CvUtil.findInfoTypeNum(gc.getLeaderHeadInfo, gc.getLeaderHeadInfos(), tLeaders[iDeadCiv][0])
				# if pDeadCiv.getCurrentEra() >= tLeaders[iDeadCiv][1] and pDeadCiv.getLeader() != iNewLeader:
					# pDeadCiv.setLeader(iNewLeader)
			return


	def moveBackCapital(self, iCiv):
		apCityList = PyPlayer(iCiv).getCityList()
		if (gc.getMap().plot(tRespawnCapitals[iCiv][0], tRespawnCapitals[iCiv][1]).isCity()):
			oldCapital = gc.getMap().plot(tRespawnCapitals[iCiv][0], tRespawnCapitals[iCiv][1]).getPlotCity()
			if (oldCapital.getOwner() == iCiv):
				if oldCapital.getNumRealBuilding(iPalace) < 1:
					for pCity in apCityList:
						pCity.GetCy().setNumRealBuilding(iPalace, 0)
					oldCapital.setNumRealBuilding(iPalace, 1)
		else:
			iMaxValue = 0
			bestCity = None
			for pCity in apCityList:
				loopCity = pCity.GetCy()
				#loopCity.AI_cityValue() doesn't work as area AI types aren't updated yet
				loopValue = max(0,500-loopCity.getGameTurnFounded()) + loopCity.getPopulation()*10
				#print ("loopValue", loopCity.getName(), loopCity.AI_cityValue(), loopValue) #causes C++ exception
				if (loopValue > iMaxValue):
					iMaxValue = loopValue
					bestCity = loopCity
			if (bestCity != None):
				for pCity in apCityList:
					loopCity = pCity.GetCy()
					if (loopCity != bestCity):
						loopCity.setNumRealBuilding(iPalace, 0)
				bestCity.setNumRealBuilding(iPalace, 1)


	def convertBackCulture(self, iCiv, bMoved = False): # bMoved = True for civs that spawn in another area
		plotList = []
		if bMoved: 
			plotList.extend(utils.getRegionPlotList(lRespawnRegions[iCiv]))
			plotList.extend(utils.getRegionPlotList(lRespawnNormalRegions[iCiv]))
		newAreaIdx = len(plotList)
		plotList.extend(utils.getNormalPlotList(iCiv))
		plotList = utils.uniq(plotList)
		cityList = []
		#collect all the cities in the region
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if (pCurrent.isCity()):
				bOldArea = False
				if bMoved and i >= newAreaIdx:
					bOldArea = True
				for ix in range(pCurrent.getX()-1, pCurrent.getX()+2):		# from x-1 to x+1
					for iy in range(pCurrent.getY()-1, pCurrent.getY()+2):	# from y-1 to y+1
						pCityArea = gc.getMap().plot( ix, iy )
						if bMoved and bOldArea:
							iCivCulture = pCityArea.getCulture(iCiv) / 4
						else:
							iCivCulture = pCityArea.getCulture(iCiv)
						iLoopCivCulture = 0
						for iLoopCiv in range(iIndependent, iBarbarian + 1, 1): #barbarians too
							if bMoved and bOldArea:
								iLoopCivCulture += pCityArea.getCulture(iLoopCiv)/4
								pCityArea.setCulture(iLoopCiv, pCityArea.getCulture(iLoopCiv)*3/4, True)
							else:
								iLoopCivCulture += pCityArea.getCulture(iLoopCiv)
								pCityArea.setCulture(iLoopCiv, 0, True)
						pCityArea.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)
				city = pCurrent.getPlotCity()
				if bMoved and bOldArea:
					iCivCulture = city.getCulture(iCiv) / 4
				else:
					iCivCulture = city.getCulture(iCiv)
				iLoopCivCulture = 0
				for iLoopCiv in range(iIndependent, iBarbarian + 1, 1): #barbarians too
					if bMoved and bOldArea:
						iLoopCivCulture += city.getCulture(iLoopCiv)/4
						city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*3/4, True)
					else:
						iLoopCivCulture += city.getCulture(iLoopCiv)  
						city.setCulture(iLoopCiv, 0, True)
				city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True) 


	def initBirth(self, iCurrentTurn, iBirthYear, iCiv):
		
		iHuman = utils.getHumanID()
		iBirthTurn = getTurnForYear(iBirthYear)
		print("iBirthTurn:%d, iCurrentTurn:%d" %(iBirthTurn, iCurrentTurn))
		#print("getSpawnDelay:%d, getFlipsDelay:%d" %(self.getSpawnDelay(iCiv), self.getFlipsDelay(iCiv)))
		
		if self.getStopSpawn(iCiv) > 0: return
		
		# Ayyubid & Mamluk conditional spawn
		if utils.isActive(iFatimids) and iCiv in [iAyyubids, iMamluks]:
			self.setStopSpawn(iCiv, 1)
			print ("stopSpawn", gc.getPlayer(iCiv).getCivilizationShortDescription(0))
			return
		
		# Ottoman conditional spawn
		if iCiv == iOttomans:
			if utils.checkRegionOwnedCity(iRum, rThrace) or utils.checkRegionOwnedCity(iRum, rAsia) or gc.getPlayer(iRum).getNumCities() > 6:
				self.setStopSpawn(iCiv, 1)
				print ("stopSpawn", gc.getPlayer(iCiv).getCivilizationShortDescription(0))
				return
		
		if iCurrentTurn == iBirthTurn and iHuman != iCiv and utils.isActive(iHuman):
			self.showBirthMessage(iCiv, iHuman)
		
		if (iCurrentTurn == iBirthTurn-1 + self.getSpawnDelay(iCiv) + self.getFlipsDelay(iCiv)):
				tCapital = tCapitals[iCiv]
				if (self.getFlipsDelay(iCiv) == 0): #city hasn't already been founded)
					
					#this may fix the -1 bug
					if (iCiv == iHuman): 
						killPlot = gc.getMap().plot(tCapital[0], tCapital[1])
						iNumUnitsInAPlot = killPlot.getNumUnits()
						if (iNumUnitsInAPlot):
							for i in range(iNumUnitsInAPlot):
								unit = killPlot.getUnit(i)
								if (unit.getOwner() != iCiv):
									unit.kill(False, iBarbarian)
					
					# conditional spawn - if applicable, will convert one city instead of spawning the settler
					if tNoSettler[iCiv] > 0 and gc.getMap().plot(tCapital[0], tCapital[1]).isCity():
						if iCiv in [iAyyubids, iMamluks, iOttomans]:
							self.birthConditional(iCiv, tCapital, utils.getCorePlotList(iCiv))
							return
						elif iCiv == iAntioch or iCiv == iCrusaders:
							self.birthInvasion(iCiv, tCapital, utils.getCorePlotList(iCiv))
							return
						elif iCiv == iTimurids:
							capital = gc.getMap().plot(tCapitals[iTimurids][0], tCapitals[iTimurids][1])
							if not (capital.isCity() and capital.getOwner() == utils.getHumanID()):
								self.birthConditional(iCiv, tCapital, utils.getCorePlotList(iCiv))
								return
					
					bDeleteEverything = False
					pCapital = gc.getMap().plot(tCapital[0], tCapital[1])
					if (pCapital.isOwned()):
						if (iCiv == iHuman or not gc.getPlayer(iHuman).isAlive()):
							bDeleteEverything = True
							print ("bDeleteEverything 1")
						else:
							bDeleteEverything = True
							for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-1 to x+1
								for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-1 to y+1
									pCurrent=gc.getMap().plot(x, y)
									if (pCurrent.isCity() and pCurrent.getPlotCity().getOwner() == iHuman):
										bDeleteEverything = False
										print ("bDeleteEverything 2")
										break
										break
					if iCiv in [iAntioch, iCrusaders, iZengids]:
						bDeleteEverything = False # military spawn, spare Antioch/Jerusalem/Mosul
					print ("bDeleteEverything", bDeleteEverything)
					if (not gc.getMap().plot(tCapital[0], tCapital[1]).isOwned()):
						if iCiv in [iCrusaders, iGhorids, iSafavids, iMughals, iRum, iOttomans, iTimurids]: #dangerous starts
							self.setDeleteMode(0, iCiv)
						self.birthInFreeRegion(iCiv, tCapital, utils.getCorePlotList(iCiv))
					elif (bDeleteEverything):
						self.setDeleteMode(0, iCiv)
						# edead: part 1 - cities
						for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-2 to x+2
							for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
								#print ("deleting cities", x, y)
								pCurrent = gc.getMap().plot(x, y)
								if (pCurrent.isCity()):
									pCurrent.eraseAIDevelopment() #new function, similar to erase but won't delete rivers, resources and features()
						# edead: part 2 - units & culture
						for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
							for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
								#print ("deleting everything else", x, y)
								pCurrent = gc.getMap().plot(x, y)
								for iLoopCiv in range(iBarbarian+1): #Barbarians as well
									if (iCiv != iLoopCiv):
										utils.flipUnitsInArea([(x,y)], iCiv, iLoopCiv, True, False)
								for iLoopCiv in range(iBarbarian+1): #Barbarians as well
									if (iCiv != iLoopCiv):
										pCurrent.setCulture(iLoopCiv, 0, True)
								pCurrent.setOwner(-1)
						plotList = utils.getCorePlotList(iCiv)
						for iLoopCiv in range(iBarbarian+1): #Barbarians as well
							if (iCiv != iLoopCiv):
								utils.flipUnitsInArea(plotList, iCiv, iLoopCiv, True, False, True) # skip AI units within borders
						self.birthInFreeRegion(iCiv, tCapital, utils.getCorePlotList(iCiv))
					else:
						self.birthInForeignBorders(iCiv, utils.getCorePlotList(iCiv), utils.getBroaderPlotList(iCiv))
				else:
					print ( "setBirthType again: flips" )
					self.birthInFreeRegion(iCiv, tCapital, utils.getCorePlotList(iCiv))
		
		# war on spawn and reveal moved from here to after unit creation - edead
		
		if (iCurrentTurn == iBirthTurn + sd.getSpawnDelay(iCiv)) and (gc.getPlayer(iCiv).isAlive()) and (self.getAlreadySwitched() == False) and (iHuman + tDifference[iHuman] < iCiv) and (gc.getPlayer(iCiv).isPlayable()):
			self.newCivPopup(iCiv)

	def deleteMode(self, iCurrentPlayer):
		
		iCiv = self.getDeleteMode(0)
		#if tNoSettler[iCiv] > 0: return # skip
		
		print ("deleteMode after", iCurrentPlayer)
		tCapital = tCapitals[iCiv]
		if (iCurrentPlayer == iCiv):
			for x in range(tCapital[0] - 2, tCapital[0] + 3):		# from x-2 to x+2
				for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
					pCurrent=gc.getMap().plot(x, y)
					pCurrent.setCulture(iCiv, 300, True)
			for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
				for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
					pCurrent=gc.getMap().plot(x, y)
					utils.convertPlotCulture(pCurrent, iCiv, 100, True)
					if (pCurrent.getCulture(iCiv) < 3000):
						pCurrent.setCulture(iCiv, 3000, True)
					pCurrent.setOwner(iCiv)
			self.setDeleteMode(0, -1)
			return
		
		print ("iCurrentPlayer", iCurrentPlayer, "iCiv", iCiv)
		if (iCurrentPlayer != iCiv-1):
			return
		
		bNotOwned = True
		for x in range(tCapital[0] - 1, tCapital[0] + 2):		# from x-1 to x+1
			for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
				print ("deleting again", x, y)
				pCurrent=gc.getMap().plot(x, y)
				if (pCurrent.isOwned()):
					bNotOwned = False
					for iLoopCiv in range(iBarbarian): #Barbarians as well
						if(iLoopCiv != iCiv):
							pCurrent.setCulture(iLoopCiv, 0, True)
						#else:
						#		if (pCurrent.getCulture(iCiv) < 4000):
						#				pCurrent.setCulture(iCiv, 4000, True)
					#pCurrent.setOwner(-1)
					pCurrent.setOwner(iCiv)
		
		print ("bNotOwned loop executed OK")
		
		for x in range(tCapital[0] - 11, tCapital[0] + 12):		# must include the distance from Sogut to the Caspius
			for y in range(tCapital[1] - 11, tCapital[1] + 12):
				print ("units", x, y, gc.getMap().plot(x, y).getNumUnits(), tCapital[0], tCapital[1])
				if (x != tCapital[0] or y != tCapital[1]):
					pCurrent=gc.getMap().plot(x, y)
					if (pCurrent.getNumUnits() > 0 and not pCurrent.isWater()):
						unit = pCurrent.getUnit(0)
						print ("units2", x, y, gc.getMap().plot(x, y).getNumUnits(), unit.getOwner(), iCiv)
						if (unit.getOwner() == iCiv):
							print ("moving starting units from", x, y, "to", (tCapital[0], tCapital[1]))
							for i in range(pCurrent.getNumUnits()):
								unit = pCurrent.getUnit(0)
								unit.setXY(tCapital[0], tCapital[1], False, False, False)
							#may intersect plot close to tCapital
##								for farX in range(x - 6, x + 7):
##									for farY in range(y - 6, y + 7):
##										pCurrentFar = gc.getMap().plot(farX, farY)
##										if (pCurrentFar.getNumUnits() == 0):
##											pCurrentFar.setRevealed(iCiv, False, True, -1);


	def birthConditional(self, iCiv, tCapital, plotList):
		
		print("birthConditional, FlipsDelay=%d" %(self.getFlipsDelay(iCiv)))
		
		startingPlot = (tCapital[0], tCapital[1])
		iOwner = gc.getMap().plot(tCapital[0], tCapital[1]).getOwner()
		if self.getFlipsDelay(iCiv) == 0:
			iFlipsDelay = self.getFlipsDelay(iCiv) + 2
			if iFlipsDelay > 0:
				
				# pre-spawn a catapult to revive the player
				#gc.getPlayer(iCiv).revive() # forces alive status
				#print ("revived")
				pCatapult = utils.makeUnit(iCatapult, iCiv, (iCatapultX, iCatapultY), 1)
				#print ("catapult: ", pCatapult.getName())
				
				# flip capital instead of spawning starting units
				utils.cultureManager(startingPlot, 100, iCiv, iOwner, True, False, False)
				utils.flipUnitsInCityBefore(startingPlot, iCiv, iOwner)
				self.setTempFlippingCity(startingPlot) #necessary for the (688379128, 0) bug
				utils.flipCity(startingPlot, 0, 0, iCiv, [iOwner])
				utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iCiv)
				
				#print ("starting units in", tCapital[0], tCapital[1])
				print ("birthConditional: starting units in", tCapital[0], tCapital[1])
				self.createStartingUnits(iCiv, (tCapital[0], tCapital[1]))
				utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
				utils.clearPlague(iCiv)
				print ("flipping remaining units")
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iCiv, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iCiv, iFlipsDelay) #save
				
				# kill the catapult and cover the plots
				plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
				if (plotZero.getNumUnits()):
					catapult = plotZero.getUnit(0)
					catapult.kill(False, iCiv)
				utils.coverPlots(iCatapultX, iCatapultY, iCiv) # edead
				print ("Plots covered")
		
		else: #starting units have already been placed, now the second part
			iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, plotList)
			self.convertSurroundingPlotCulture(iCiv, plotList)
			
			# extra help for the post-barbarian invasion AI
			if iCiv != utils.getHumanID() and iCiv in [iSeljuks, iRum, iTimurids, iAkKoyunlu, iSafavids]:
				iNumAICitiesConverted += self.convertSurroundingCities(iCiv, utils.getNormalPlotList(iCiv), True) # barbs only
			
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iCiv, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			#print ("utils.flipUnitsInArea()")
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iCiv)
			utils.coverPlots(iCatapultX, iCatapultY, iCiv) # edead
			#print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iCiv).getNumCities() > 0:
				capital = gc.getPlayer(iCiv).getCapitalCity()
				self.createStartingWorkers(iCiv, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iCiv, plotList)
			
			# move AI capital
			#if tNoSettler[iCiv] > 0:
			if not self.moveCapital(tCapital, iCiv):
				self.moveCapital(tBackupCapitals[iCiv], iCiv)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iCiv)


	def birthInvasion(self, iCiv, tCapital, plotList):
		
		print("birthInvasion, FlipsDelay=%d" %(self.getFlipsDelay(iCiv)))
		
		if self.getFlipsDelay(iCiv) == 0:
			iFlipsDelay = self.getFlipsDelay(iCiv) + 2
			if iFlipsDelay > 0:
				
				# declare war on the capital's owner
				iCapitalOwner = gc.getMap().plot(tCapital[0],tCapital[1]).getOwner()
				if not gc.getTeam(gc.getPlayer(iCiv).getTeam()).isAtWar(gc.getPlayer(iCapitalOwner).getTeam()):
					gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(gc.getPlayer(iCapitalOwner).getTeam(), True, -1)
				
				# traitors open the gates...
				city = gc.getMap().plot(tCapital[0],tCapital[1]).getPlotCity()
				if city:
					city.changeCultureUpdateTimer(3);
					city.changeOccupationTimer(3);
					CyInterface().addMessage(city.getOwner(), False, iDuration, localText.getText("TXT_KEY_TRAITOR_REVOLT", (city.getName(),)), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(iRed), city.getX(), city.getY(), True, True);
				
				# find a spot for the siege
				for tPlot in ((tCapital[0], tCapital[1]+1), (tCapital[0]+1, tCapital[1]+1), (tCapital[0]+1, tCapital[1])):
					pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
					if pPlot.getOwner() < 0 or gc.getTeam(gc.getPlayer(iCiv).getTeam()).isAtWar(gc.getPlayer(pPlot.getOwner()).getTeam()):
						break
				
				startingPlot = gc.getMap().plot(tPlot[0], tPlot[1])
				
				# clear the spot
				iNumUnitsInAPlot = startingPlot.getNumUnits()
				if iNumUnitsInAPlot:
					for i in range(iNumUnitsInAPlot):
						unit = startingPlot.getUnit(0)
						if unit.getOwner() != iCiv:
							unit.kill(False, iBarbarian)
				
				print ("birthInvasion: starting units in", tPlot[0], tPlot[1])
				self.createStartingUnits(iCiv, (tPlot[0], tPlot[1]))
				utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
				utils.clearPlague(iCiv)
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iCiv, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iCiv, iFlipsDelay) #save
		
		else: #starting units have already been placed, now the second part
			iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, plotList)
			
			# extra help for the post-barbarian invasion AI
			if iCiv != utils.getHumanID() and iCiv in [iSeljuks, iRum, iTimurids, iAkKoyunlu, iSafavids]:
				iNumExtraCities, dummy = self.convertSurroundingCities(iCiv, utils.getNormalPlotList(iCiv), True) # barbs only
				iNumAICitiesConverted += iNumExtraCities
			
			self.convertSurroundingPlotCulture(iCiv, plotList)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iCiv, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			print ("utils.flipUnitsInArea()")
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iCiv)
			utils.coverPlots(iCatapultX, iCatapultY, iCiv) # edead
			print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iCiv).getNumCities() > 0:
				capital = gc.getPlayer(iCiv).getCapitalCity()
				self.createStartingWorkers(iCiv, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iCiv, plotList)
			
			# move AI capital
			#if tNoSettler[iCiv] > 0:
			if not self.moveCapital(tCapital, iCiv):
				self.moveCapital(tBackupCapitals[iCiv], iCiv)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iCiv)


	def birthInFreeRegion(self, iCiv, tCapital, plotList):
		
		print("birthInFreeRegion, FlipsDelay=%d" %(self.getFlipsDelay(iCiv)))
		
		startingPlot = gc.getMap().plot(tCapital[0], tCapital[1])
		if self.getFlipsDelay(iCiv) == 0:
			iFlipsDelay = self.getFlipsDelay(iCiv) + 2
			if iFlipsDelay > 0:
				print ("birthInFreeRegion: starting units in", tCapital[0], tCapital[1])
				self.createStartingUnits(iCiv, (tCapital[0], tCapital[1]))
				utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
				utils.clearPlague(iCiv)
				for i in range(iIndependent, iBarbarian+1):
					utils.flipUnitsInArea(utils.getAreaPlotList((tCapital[0]-2, tCapital[1]-2), (tCapital[0]+2, tCapital[1]+2)), iCiv, i, True, True) #This is for AI only. During Human player spawn, that area is already cleaned
				self.setFlipsDelay(iCiv, iFlipsDelay) #save
		
		else: #starting units have already been placed, now the second part
			iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, plotList)
			
			# extra help for the post-barbarian invasion AI
			if iCiv != utils.getHumanID() and iCiv in [iSeljuks, iRum, iTimurids, iAkKoyunlu, iSafavids]:
				iNumExtraCities, dummy = self.convertSurroundingCities(iCiv, utils.getNormalPlotList(iCiv), True) # barbs only
				iNumAICitiesConverted += iNumExtraCities
			
			self.convertSurroundingPlotCulture(iCiv, plotList)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(plotList, iCiv, i, False, True) #remaining barbs/indeps in the region now belong to the new civ   
			print ("utils.flipUnitsInArea()")
			
			# kill the catapult & cover the plots
			plotZero = gc.getMap().plot(iCatapultX, iCatapultY)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iCiv)
			utils.coverPlots(iCatapultX, iCatapultY, iCiv) # edead
			print ("Plots covered")
			
			# create workers
			if gc.getPlayer(iCiv).getNumCities() > 0:
				capital = gc.getPlayer(iCiv).getCapitalCity()
				self.createStartingWorkers(iCiv, (capital.getX(), capital.getY()))
			
			# convert human cities
			if iNumHumanCitiesToConvert > 0:
				self.flipPopup(iCiv, plotList)
			
			# move AI capital
			#if tNoSettler[iCiv] > 0:
			if not self.moveCapital(tCapital, iCiv):
				self.moveCapital(tBackupCapitals[iCiv], iCiv)
			
			# extra units in flipped cities
			self.createPostFlipUnits(iCiv)


	def birthInForeignBorders(self, iCiv, lCorePlots, lBroaderPlots):
		
		iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, lCorePlots)
		self.convertSurroundingPlotCulture(iCiv, lCorePlots)
		
		# extra help for the post-barbarian invasion AI
		if iCiv != utils.getHumanID() and iCiv in [iSeljuks, iRum, iTimurids, iAkKoyunlu, iSafavids]:
			iNumExtraCities, dummy = self.convertSurroundingCities(iCiv, utils.getNormalPlotList(iCiv), True) # barbs only
			iNumAICitiesConverted += iNumExtraCities

		#now starting units must be placed
		if (iNumAICitiesConverted > 0):
			#utils.debugTextPopup( 'iConverted OK for placing units' )
			dummy1, plotList = utils.plotListSearch( lCorePlots, utils.ownedCityPlots, iCiv )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching any city just flipped')
			#print ("rndNum for starting units", rndNum)
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iCiv, result)
					utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
					utils.clearPlague(iCiv)
					#gc.getPlayer(iCiv).changeAnarchyTurns(1)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(lCorePlots, iCiv, i, False, False) #remaining barbs in the region now belong to the new civ 
			
			# move AI capital
			#if tNoSettler[iCiv] > 0:
			if not self.moveCapital(tCapitals[iCiv], iCiv):
				self.moveCapital(tBackupCapitals[iCiv], iCiv)
		
		else:   #search another place
			dummy, plotList = utils.plotListSearch( lCorePlots, utils.goodPlots, [] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching another free plot')
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iCiv, result)
					utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
					utils.clearPlague(iCiv)
			else:
				dummy1, plotList = utils.plotListSearch( lBroaderPlots, utils.goodPlots, [] )
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching other good plots in a broader region')
				if (len(plotList)):
					result = plotList[rndNum]
					if (result):
						self.createStartingUnits(iCiv, result)
						self.createStartingWorkers(iCiv, result)
						utils.setPlagueCountdown(iCiv, -utils.getTurns(iImmunity))
						utils.clearPlague(iCiv)
			for i in range(iIndependent, iBarbarian+1):
				utils.flipUnitsInArea(lCorePlots, iCiv, i, True, True) #remaining barbs in the region now belong to the new civ 
		
		if (iNumHumanCitiesToConvert > 0):
			self.flipPopup(iCiv, lCorePlots)
		
		# extra units in flipped cities
		self.createPostFlipUnits(iCiv)


	def convertSurroundingCities(self, iCiv, plotList, fBarbOnly = False):
			
			iConvertedCitiesCount = 0
			iNumHumanCities = 0
			cityList = []
			self.setSpawnWar(0)
			
			#collect all the cities in the spawn region
			for i in range(len(plotList)):
				pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().getOwner() != iCiv:
						if not fBarbOnly or pCurrent.getPlotCity().getOwner() == iBarbarian:
							cityList.append(pCurrent.getPlotCity())

			#print ("Birth", iCiv)
			#print (cityList)

			#for each city
			if len(cityList):
					for i in range(len(cityList)):
							loopCity = cityList[i]
							loopX = loopCity.getX()
							loopY = loopCity.getY()
							#print ("cityList", loopCity.getName(), (loopX, loopY))
							iHuman = utils.getHumanID()
							iOwner = loopCity.getOwner()
							iCultureChange = 0 #if 0, no flip; if > 0, flip will occur with the value as variable for utils.CultureManager()
							
							#case 1: barbarian/independent city
							if (iOwner >= iNumPlayers):
								#utils.debugTextPopup( 'BARB' )
								iCultureChange = 100
							#case 2: human city
							#elif (iOwner == iHuman and not loopCity.isCapital()): #exploitable
							elif (iOwner == iHuman and not (loopX == tCapitals[iHuman] and loopY == tCapitals[iHuman]) and not gc.getPlayer(iHuman).getNumCities() <= 1 and not (self.getCheatMode() == True and loopCity.isCapital())):
								
								#utils.debugTextPopup( 'HUMAN' )
	##							bForeigners = False
	##							cityPlot = gc.getMap().plot(cityList[i].getX(), cityList[i].getY())
	##							cityCulture = cityList[i].countTotalCulture()
	##							iCultureThreshold = 10
	##							for j in range(iNumPlayers+1):
	##								if (cityList[i].getCulture(j)*100 / cityCulture >= iCultureThreshold) and (j != iHuman):
	##									bForeigners = True
	##							humanCapital = gc.getPlayer(iHuman).getCapitalCity()
	##							iDistance = gc.getMap().calculatePathDistance(cityPlot, gc.getMap().plot(humanCapital.getX(),humanCapital.getY()))
	##							if (cityList[i].isOccupation()) or (cityList[i].isDisorder()) or (bForeigners == True) or (not cityPlot.getNumUnits()) or ((not cityList[i].isGovernmentCenter()) and (iDistance >= 8) and (gc.getPlayer(iHuman).getNumCities() >= 5)):
								if (iNumHumanCities == 0):
									iNumHumanCities += 1
									#iConvertedCitiesCount += 1
									#self.flipPopup(iCiv, plotList)
							#case 3: other
							elif (not loopCity.isCapital()):   #utils.debugTextPopup( 'OTHER' )
								if (iConvertedCitiesCount < 6): #there won't be more than 5 flips in the area
									#utils.debugTextPopup( 'iConvertedCities OK' )
									iCultureChange = 50
									if (gc.getGame().getGameTurn() <= getTurnForYear(tBirth[iCiv]) + 5): #if we're during a birth
										rndNum = gc.getGame().getSorenRandNum(100, 'odds')
										if (rndNum >= tAIStopBirthThreshold[iOwner]):
											print (iOwner, "stops birth", iCiv, "rndNum:", rndNum, "threshold:", tAIStopBirthThreshold[iOwner])
											if (not gc.getTeam(gc.getPlayer(iOwner).getTeam()).isAtWar(iCiv)):																		
												gc.getTeam(gc.getPlayer(iOwner).getTeam()).declareWar(iCiv, False, -1)
												if (gc.getPlayer(iCiv).getNumCities() > 0): #this check is needed, otherwise game crashes
													print ("capital:", gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY())
													if (gc.getPlayer(iCiv).getCapitalCity().getX() != -1 and gc.getPlayer(iCiv).getCapitalCity().getY() != -1):
														self.createAdditionalUnits(iCiv, (gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY()))
													else:
														self.createAdditionalUnits(iCiv, tCapitals[iCiv])
							
							if (iCultureChange > 0):
								#print ("flipping ", cityList[i].getName())
								utils.cultureManager((loopX, loopY), iCultureChange, iCiv, iOwner, True, False, False)
								#gc.getMap().plot(cityList[i].getX(),cityList[i].getY()).setImprovementType(-1)
								
								utils.flipUnitsInCityBefore((loopX, loopY), iCiv, iOwner)
								self.setTempFlippingCity((loopX, loopY)) #necessary for the (688379128, 0) bug
								utils.flipCity((loopX, loopY), 0, 0, iCiv, [iOwner])
								#print ("cityList[i].getXY", cityList[i].getX(), cityList[i].getY()) 
								utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iCiv)

								#iEra = gc.getPlayer(iCiv).getCurrentEra()
								#if (iEra >= 2): #medieval
								#		if (loopCity.getPopulation() < iEra):
								#				loopCity.setPopulation(iEra) #causes an unidentifiable C++ exception
										#doesn't work (assigns UBs too)
										#for iLoopBuilding in range(iNumBuildingsPlague):
										#		if (gc.getBuildingInfo(iLoopBuilding).getFreeStartEra() >= 0):
										#				if (iEra >= gc.getBuildingInfo(iLoopBuilding).getFreeStartEra()):
										#						print (iEra, iLoopBuilding, gc.getBuildingInfo(iLoopBuilding).getFreeStartEra(), loopCity.canConstruct(iLoopBuilding, False, False, False))
										#						if (loopCity.canConstruct(iLoopBuilding, False, False, False)):
										#								if (not loopCity.hasBuilding(iLoopBuilding)):
										#										loopCity.setHasRealBuilding(iLoopBuilding, True)

								#cityList[i].setHasRealBuilding(iPlague, False)   #buggy
								
								iConvertedCitiesCount += 1
								print ("iConvertedCitiesCount", iConvertedCitiesCount)

			if (iConvertedCitiesCount > 0):
				if (gc.getPlayer(iCiv).isHuman()):
					CyInterface().addMessage(iCiv, True, iDuration, CyTranslator().getText("TXT_KEY_FLIP_TO_US", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)

			#print( "converted cities", iConvertedCitiesCount)
			return (iConvertedCitiesCount, iNumHumanCities)



	def convertSurroundingPlotCulture(self, iCiv, plotList):
	
		for i in range(len(plotList)):
			pCurrent = gc.getMap().plot(plotList[i][0], plotList[i][1])
			if not pCurrent.isCity():
				utils.convertPlotCulture(pCurrent, iCiv, 100, False)


	def immuneMode(self, argsList): 
		
		pWinningUnit,pLosingUnit = argsList
		iLosingPlayer = pLosingUnit.getOwner()
		iUnitType = pLosingUnit.getUnitType()
		if (iLosingPlayer < iNumPlayers):
			if (gc.getGame().getGameTurn() >= getTurnForYear(tBirth[iLosingPlayer]) and gc.getGame().getGameTurn() <= getTurnForYear(tBirth[iLosingPlayer])+2):
				if (pLosingUnit.getX() == tCapitals[iLosingPlayer][0] and pLosingUnit.getY() == tCapitals[iLosingPlayer][1]):
					print("new civs are immune for now")
					if (gc.getGame().getSorenRandNum(100, 'immune roll') >= 50):
						utils.makeUnit(iUnitType, iLosingPlayer, (pLosingUnit.getX(), pLosingUnit.getY()), 1)


	def initMinorBetrayal(self, iCiv):
		
		iHuman = utils.getHumanID()
		dummy, plotList = utils.plotListSearch(utils.getCorePlotList(iCiv), utils.outerInvasion, [])
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players borders')
		if len(plotList):
			result = plotList[rndNum]
			if result:
				self.createAdditionalUnits(iCiv, result)
				self.unitsBetrayal(iCiv, iHuman, utils.getCorePlotList(iCiv), result)


	def initBetrayal(self):
		
		iHuman = utils.getHumanID()
		turnsLeft = self.getBetrayalTurns()
		dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.outerInvasion, [] )
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players (or in general, the old civ if human player just swtiched) borders')
		if (not len(plotList)):
			dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.innerSpawn, [self.getOldCivFlip(), self.getNewCivFlip()] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border but distant from units')
		if (not len(plotList)):
			dummy, plotList = utils.plotListSearch( self.getTempPlotList(), utils.innerInvasion, [self.getOldCivFlip(), self.getNewCivFlip()] )
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border')
		if (len(plotList)):
			result = plotList[rndNum]
			if (result):
				if (turnsLeft == iBetrayalPeriod):
					self.createAdditionalUnits(self.getNewCivFlip(), result)
				self.unitsBetrayal(self.getNewCivFlip(), self.getOldCivFlip(), self.getTempPlotList(), result)
		self.setBetrayalTurns(turnsLeft - 1)


	def unitsBetrayal(self, iNewOwner, iOldOwner, plotList, tPlot):
		
		#print ("iNewOwner", iNewOwner, "iOldOwner", iOldOwner, "tPlot", tPlot)
		if (gc.getPlayer(self.getOldCivFlip()).isHuman()):
			CyInterface().addMessage(self.getOldCivFlip(), False, iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL", ()), "", 0, "", ColorTypes(iRed), -1, -1, True, True)
		elif (gc.getPlayer(self.getNewCivFlip()).isHuman()):
			CyInterface().addMessage(self.getNewCivFlip(), False, iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL_NEW", ()), "", 0, "", ColorTypes(iGreen), -1, -1, True, True)
		for i in range(len(plotList)):
			killPlot = gc.getMap().plot(plotList[i][0], plotList[i][1])
			iNumUnitsInAPlot = killPlot.getNumUnits()
			if (iNumUnitsInAPlot):
				iStateReligion = gc.getPlayer(iNewOwner).getStateReligion()
				for i in range(iNumUnitsInAPlot):
					unit = killPlot.getUnit(i)
					if (unit.getOwner() == iOldOwner):
						rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
						if (rndNum >= self.getBetrayalThreshold()):
							if (unit.getDomainType() == 2): #land unit
								iUnitType = unit.getUnitType()
								if utils.canBetray(iUnitType, iStateReligion):
									unit.kill(False, iNewOwner)
									utils.makeUnit(iUnitType, iNewOwner, tPlot, 1)
									i = i - 1


	def createAdditionalUnits( self, iCiv, tPlot ):
			
		if iCiv == iSamanids:
			utils.makeUnit(iDihqanArcher, iCiv, tPlot, 2)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			
		if iCiv == iKhanids:
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)

		if iCiv == iBuyids:
			utils.makeUnit(iDaylamiTribesman, iCiv, tPlot, 2)
			utils.makeUnit(iDaylamiInfantry, iCiv, tPlot, 1)
			utils.makeUnit(iGhulamLancer, iCiv, tPlot, 1)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 1)
			
		if iCiv == iArmenia:
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iAxeman, iCiv, tPlot, 3)
			
		if iCiv == iAlans:
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iHorseman, iCiv, tPlot, 3)   
			
		if iCiv == iMalwa:
			utils.makeUnit(iKshatriyaArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			
		if iCiv == iFatimids:
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iBerberCavalry, iCiv, tPlot, 2)
			
		if iCiv == iGhaznavids:
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 3)
			
		if iCiv == iGujarat:
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iKshatriya, iCiv, tPlot, 3)
			
		if iCiv == iChalukya:
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 3)
			utils.makeUnit(iSpearman, iCiv, tPlot, 3)
			
		if iCiv == iGeorgia:
			utils.makeUnit(iArcher, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseman, iCiv, tPlot, 2)
			
		if iCiv == iSeljuks:
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSeljukHorseArcher, iCiv, tPlot, 4)
			
		if iCiv == iSindh:
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseman, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			
		if iCiv == iRum:
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iGhazi, iCiv, tPlot, 4)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 4)
			
		if iCiv == iKhwarezm:
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 3)
			utils.makeUnit(iKhwarezmianLancer, iCiv, tPlot, 2)
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			
		if iCiv == iAntioch:
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iNormanKnight, iCiv, tPlot, 2)
			utils.makeUnit(iAxeman, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 1)
			
		if iCiv == iCrusaders:
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iLancer, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iAxeman, iCiv, tPlot, 1)
			
		if iCiv == iGhorids:
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iMujahid, iCiv, tPlot, 4)
			utils.makeUnit(iLancer, iCiv, tPlot, 2)
			
		if iCiv == iOman:
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySwordsman, iCiv, tPlot, 4)
		
		if iCiv == iAyyubids:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iTawashiLancer, iCiv, tPlot, 3)
		
		if iCiv == iMongols:
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 6)
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 4)
		
		if iCiv == iMamluks:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 3)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 3)
			
		if iCiv == iGolden:
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iHeavySwordsman, iCiv, tPlot, 3)
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 4)
			
		if iCiv == iChagatai:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 3)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 3)
		
		if iCiv == iOttomans:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 4)
		
		if iCiv == iBahmanids:
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iLancer, iCiv, tPlot, 4)
		
		if iCiv == iTimurids:
			utils.makeUnit(iSiegeEngineer, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 6)
		
		if iCiv == iAkKoyunlu:
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 4)
			utils.makeUnit(iTurkomanRaider, iCiv, tPlot, 2)
		
		if iCiv == iSafavids:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iQizilbash, iCiv, tPlot, 4)
		
		if iCiv == iMughals:
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 4)


	def createStartingUnits(self, iCiv, tPlot):
		"""Creates starting units for initBirth."""
		
		iHandicap = gc.getGame().getHandicapType()
		
		if iCiv == iMakuria:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iJavelinman, iCiv, tPlot, 1)
			utils.makeUnit(iOrthodoxMissionary, iCiv, tPlot, 2)
			utils.makeUnit(iWorker, iCiv, tPlot, 1)
		
		if iCiv == iAbbasids:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iWorker, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iHorseman, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iAbnaSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			
		if iCiv == iKhazars:
			utils.makeUnit(iSettler, iCiv, tPlot, 4)
			utils.makeUnit(iWorker, iCiv, tPlot, 5)
			utils.makeUnit(iArcher, iCiv, tPlot, 6)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 4)
			
		if iCiv == iChauhan:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iArcher, iCiv, tPlot, 1)
			utils.makeUnit(iJavelinman, iCiv, tPlot, 1)
			utils.makeUnit(iHinduMissionary, iCiv, tPlot, 1)
			
		if iCiv == iMalwa:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iKshatriyaArcher, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 1)
			utils.makeUnit(iHinduMissionary, iCiv, tPlot, 1)
			
		if iCiv == iSamanids:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			if iCiv == utils.getHumanID():
				utils.makeUnit(iSettler, iCiv, tPlot, 1) # AI settler spawned with workers
			utils.makeUnit(iDihqanArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSkirmisher, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 1)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			
		if iCiv == iKhanids:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iHorseArcherChig, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 4)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iArcher, iCiv, tPlot, 1)
			gc.getPlayer(iSamanids).AI_changeAttitudeExtra(iKhanids, -4)
			gc.getPlayer(iSeljuks).AI_changeAttitudeExtra(iKhanids, -3)
			gc.getPlayer(iGhaznavids).AI_changeAttitudeExtra(iKhanids, -4)
			gc.getPlayer(iGhorids).AI_changeAttitudeExtra(iKhanids, -4)
			gc.getPlayer(iKhwarezm).AI_changeAttitudeExtra(iKhanids, -3)
			gc.getPlayer(iGolden).AI_changeAttitudeExtra(iKhanids, -2)
			gc.getPlayer(iKypchaks).AI_changeAttitudeExtra(iKhanids, -2)
			gc.getPlayer(iMongols).AI_changeAttitudeExtra(iKhanids, -2)
			gc.getPlayer(iChagatai).AI_changeAttitudeExtra(iKhanids, -2)
			
		if iCiv == iOghuz:
			utils.makeUnit(iSettler, iCiv, tPlot, 4)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 4)
			utils.makeUnit(iArcher, iCiv, tPlot, 6)
			utils.makeUnit(iAxeman, iCiv, tPlot, 2)
			if iKhanids != utils.getHumanID() and iSamanids != utils.getHumanID():
				utils.makeUnit(iSettler, iCiv, tPlot, 2)
				utils.makeUnit(iArcher, iCiv, tPlot, 4)
			
		if iCiv == iBuyids:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 1)
			utils.makeUnit(iDaylamiTribesman, iCiv, tPlot, 2 + iHandicap)
			utils.makeUnit(iDaylamiInfantry, iCiv, tPlot, 1)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			
		if iCiv == iArmenia:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iJavelinman, iCiv, tPlot, 1)
			utils.makeUnit(iOrthodoxMissionary, iCiv, tPlot, 2)
			
		if iCiv == iKiev:
			utils.makeUnit(iSettler, iCiv, tPlot, 4)
			utils.makeUnit(iArcher, iCiv, tPlot, 7)
			utils.makeUnit(iAxeman, iCiv, tPlot, 4)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			
		if iCiv == iAlans:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 6)
			utils.makeUnit(iAxeman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 3)
			if gc.getPlayer(iCiv).getNumCities() == 0:
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
			
		if iCiv == iYemen:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSkirmisher, iCiv, tPlot, 1)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			
		if iCiv == iFatimids:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iBerberCavalry, iCiv, tPlot, 3)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			gc.getPlayer(iFatimids).AI_changeAttitudeExtra(iMakuria, 1)
			gc.getPlayer(iMakuria).AI_changeAttitudeExtra(iFatimids, 1)
			
		if iCiv == iGhaznavids:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 3)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 3)
			if iCiv != utils.getHumanID() and iHandicap:
				utils.makeUnit(iHorseArcher, iCiv, tPlot, iHandicap)
			
		if iCiv == iGujarat:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iKshatriya, iCiv, tPlot, 1)
			utils.makeUnit(iHinduMissionary, iCiv, tPlot, 2)
			
		if iCiv == iChalukya:
			utils.makeUnit(iSettler, iCiv, tPlot, 4)
			utils.makeUnit(iArcher, iCiv, tPlot, 9)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 5)
			utils.makeUnit(iSpearman, iCiv, tPlot, 6)
			utils.makeUnit(iHinduMissionary, iCiv, tPlot, 4)
			gc.getPlayer(iMalwa).AI_changeAttitudeExtra(iChalukya, -2)
			gc.getPlayer(iChauhan).AI_changeAttitudeExtra(iChalukya, -2)
			gc.getPlayer(iGujarat).AI_changeAttitudeExtra(iChalukya, -2)
			gc.getPlayer(iMughals).AI_changeAttitudeExtra(iChalukya, -3)
			gc.getPlayer(iBahmanids).AI_changeAttitudeExtra(iChalukya, -3)
			gc.getPlayer(iGhorids).AI_changeAttitudeExtra(iChalukya, -3)
			gc.getPlayer(iSindh).AI_changeAttitudeExtra(iChalukya, -1)
			
		if iCiv == iGeorgia:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iJavelinman, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 1)
			utils.makeUnit(iOrthodoxMissionary, iCiv, tPlot, 2)
			
		if iCiv == iSeljuks:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iSeljukHorseArcher, iCiv, tPlot, 6)
			if iCiv != utils.getHumanID() and iHandicap:
				utils.makeUnit(iSeljukHorseArcher, iCiv, tPlot, iHandicap * 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			gc.getPlayer(iZengids).AI_changeAttitudeExtra(iSeljuks, 2)
			gc.getPlayer(iSeljuks).AI_changeAttitudeExtra(iZengids, 2)
			
		if iCiv == iSindh:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iSkirmisher, iCiv, tPlot, 1)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			gc.getPlayer(iAbbasids).AI_changeAttitudeExtra(iSindh, 1)
			gc.getPlayer(iSindh).AI_changeAttitudeExtra(iAbbasids, 1)
			gc.getPlayer(iFatimids).AI_changeAttitudeExtra(iSindh, 1)
			gc.getPlayer(iSindh).AI_changeAttitudeExtra(iFatimids, 1)
			
		if iCiv == iRum:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iGhazi, iCiv, tPlot, 1)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 6)
			if iByzantium == utils.getHumanID() and iHandicap:
				utils.makeUnit(iHorseArcher, iCiv, tPlot, iHandicap)
				utils.makeUnit(iGhazi, iCiv, tPlot, iHandicap)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 3)
			gc.getPlayer(iRum).AI_changeAttitudeExtra(iSeljuks, 2)
			gc.getPlayer(iSeljuks).AI_changeAttitudeExtra(iRum, 2)
			gc.getPlayer(iZengids).AI_changeAttitudeExtra(iRum, 1)
			gc.getPlayer(iRum).AI_changeAttitudeExtra(iZengids, 1)
			
		if iCiv == iKhwarezm:
			utils.makeUnit(iSettler, iCiv, tPlot, 3)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iHorseArcher, iCiv, tPlot, 4)
			utils.makeUnit(iKhwarezmianLancer, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 3)
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iCaravan, iCiv, tPlot, 1, UnitAITypes.UNITAI_EXPLORE)
			if iCiv != utils.getHumanID() and iHandicap:
				utils.makeUnit(iKhwarezmianLancer, iCiv, tPlot, iHandicap)
				utils.makeUnit(iHorseArcher, iCiv, tPlot, iHandicap)
			
		if iCiv == iAntioch:
			utils.makeUnit(iArcher, iCiv, tPlot, 2)
			utils.makeUnit(iNormanKnight, iCiv, tPlot, 4)
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 2)
			utils.makeUnit(iCatapult, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 4)
			utils.makeUnit(iAxeman, iCiv, tPlot, 3)
			# Antioch UP
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setExperience(5, -1)
			
		if iCiv == iCrusaders:
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iLancer, iCiv, tPlot, 4)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 4)
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 2)
			utils.makeUnit(iCatapult, iCiv, tPlot, 2)
			gc.getPlayer(iCrusaders).AI_changeAttitudeExtra(iAntioch, 2)
			gc.getPlayer(iAntioch).AI_changeAttitudeExtra(iCrusaders, 2)
			
		if iCiv == iKhitai:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iLancer, iCiv, tPlot, 3)
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 6)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 3)
			
		if iCiv == iGhorids:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iArcher, iCiv, tPlot, 3)
			utils.makeUnit(iMujahid, iCiv, tPlot, 3)
			utils.makeUnit(iLancer, iCiv, tPlot, 2)
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 3)
			
		if iCiv == iOman:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iSwordsman, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			utils.makeUnit(iCaravan, iCiv, tPlot, 1, UnitAITypes.UNITAI_EXPLORE)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iCiv)
			if tSeaPlot:
				utils.makeUnit(iDhow, iCiv, tSeaPlot, 1, UnitAITypes.UNITAI_SETTLER_SEA)
				utils.makeUnit(iWarGalley, iCiv, tSeaPlot, 1, UnitAITypes.UNITAI_ESCORT_SEA)
				utils.makeUnit(iSettler, iCiv, tSeaPlot, 1)
				utils.makeUnit(iArcher, iCiv, tSeaPlot, 1)
		
		if iCiv == iAyyubids:
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iSpearman, iCiv, tPlot, 2)
			utils.makeUnit(iTawashiLancer, iCiv, tPlot, 3)
			utils.makeUnit(iCatapult, iCiv, tPlot, 1)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)

			if gc.getPlayer(iCiv).getNumCities() == 0: 
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
		if iCiv == iMongols:
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 8)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iFormation, True)
				unit.setHasPromotion(iFeintAttack, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 8)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iMarksman, iCiv, tPlot, 9)
			if iCiv == utils.getHumanID():
				utils.makeUnit(iTrebuchet, iCiv, tPlot, 7)
	
		if iCiv == iGolden:
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 8)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iFormation, True)
				unit.setHasPromotion(iFeintAttack, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 6)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iMarksman, iCiv, tPlot, 9)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 4)
			utils.makeUnit(iSettler, iCiv, tPlot, 4)
			if iCiv != utils.getHumanID():
				utils.makeUnit(iSettler, iCiv, tPlot, 2)
				utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			if gc.getPlayer(iCiv).getNumCities() == 0:
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
			if iSafavids == utils.getHumanID() or iMughals == utils.getHumanID() or iPortugal == utils.getHumanID():
				utils.makeUnit(iSettler, iCiv, tPlot, 3)
				utils.makeUnit(iMarksman, iCiv, tPlot, 6)
		
		
		if iCiv == iMamluks:
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 2)
			utils.makeUnit(iMamluk, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			if gc.getPlayer(iCiv).getNumCities() == 0: 
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
				
		if iCiv == iChagatai:
			utils.makeUnit(iMongolHorseArcher, iCiv, tPlot, 6)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iFormation, True)
				unit.setHasPromotion(iFeintAttack, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 6)
			pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
			iNumUnitsInAPlot = pPlot.getNumUnits()
			for i in range(iNumUnitsInAPlot):
				unit = pPlot.getUnit(i)
				unit.setHasPromotion(iCombat1, True)
				unit.setHasPromotion(iCombat2, True)
				unit.setHasPromotion(iMobility, True)
			utils.makeUnit(iMarksman, iCiv, tPlot, 7)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 5)
			if gc.getPlayer(iCiv).getNumCities() == 0:
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
		
		if iCiv == iOttomans:
			utils.makeUnit(iMarksman, iCiv, tPlot, 4)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 3)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySwordsman, iCiv, tPlot, 3)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 4)
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 3)
			if iCiv != utils.getHumanID() and iHandicap:
				utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, iHandicap)
			if gc.getPlayer(iCiv).getNumCities() == 0: 
				utils.makeUnit(iSettler, iCiv, tPlot, 1)
		
		if iCiv == iBahmanids:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iLancer, iCiv, tPlot, 2 + iHandicap)
			utils.makeUnit(iDakhani, iCiv, tPlot, 4 + iHandicap)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			utils.makeUnit(iCaravan, iCiv, tPlot, 1, UnitAITypes.UNITAI_EXPLORE)
		
		if iCiv == iTimurids:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyLancer, iCiv, tPlot, 4)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 6)
			utils.makeUnit(iSiegeEngineer, iCiv, tPlot, 2)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
			utils.makeUnit(iCaravan, iCiv, tPlot, 1, UnitAITypes.UNITAI_EXPLORE)
			if iCiv != utils.getHumanID():
				if iHandicap == 1:
					utils.makeUnit(iMarksman, iCiv, tPlot, 1)
					utils.makeUnit(iSiegeEngineer, iCiv, tPlot, 1)
					utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 3)
				elif iHandicap == 2:
					utils.makeUnit(iMarksman, iCiv, tPlot, 1)
					utils.makeUnit(iSiegeEngineer, iCiv, tPlot, 2)
					utils.makeUnit(iHeavyLancer, iCiv, tPlot, 1)
					utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 4)
		
		if iCiv == iAkKoyunlu:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 3)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 4)
			utils.makeUnit(iTurkomanRaider, iCiv, tPlot, 2)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 2)
			gc.getPlayer(iTimurids).AI_changeAttitudeExtra(iAkKoyunlu, 1)
			gc.getPlayer(iMughals).AI_changeAttitudeExtra(iTimurids, 2)
			gc.getPlayer(iRum).AI_changeAttitudeExtra(iAkKoyunlu, 1)
			gc.getPlayer(iAkKoyunlu).AI_changeAttitudeExtra(iRum, 1)

		
		if iCiv == iSafavids:
			utils.makeUnit(iSettler, iCiv, tPlot, 2)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 1)
			utils.makeUnit(iQizilbash, iCiv, tPlot, 5)
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iShiaMissionary, iCiv, tPlot, 3)
			if iCiv != utils.getHumanID() and iHandicap:
				utils.makeUnit(iQizilbash, iCiv, tPlot, iHandicap)
				utils.makeUnit(iTrebuchet, iCiv, tPlot, iHandicap)
		
		if iCiv == iPortugal:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iArquebusier, iCiv, tPlot, 2)
			utils.makeUnit(iPikeman, iCiv, tPlot, 1)
			utils.makeUnit(iCatholicMissionary, iCiv, tPlot, 1)
			tSeaPlot = utils.findSeaPlots(tPlot, 1, iCiv)
			if tSeaPlot:
				utils.makeUnit(iCarrack, iCiv, tSeaPlot, 1, UnitAITypes.UNITAI_EXPLORE_SEA)
		
		if iCiv == iMughals:
			utils.makeUnit(iSettler, iCiv, tPlot, 1)
			utils.makeUnit(iMarksman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavySpearman, iCiv, tPlot, 2)
			utils.makeUnit(iHeavyHorseArcher, iCiv, tPlot, 5)
			utils.makeUnit(iTrebuchet, iCiv, tPlot, 1)
			utils.makeUnit(iSunniMissionary, iCiv, tPlot, 2)
		
		# init contacts
		pPlayer = gc.getPlayer(iCiv)
		pTeam = gc.getTeam(pPlayer.getTeam())
		for i in range(len(lContactCivsOnSpawn[iCiv])):
			iCivToMeet = lContactCivsOnSpawn[iCiv][i]
			if gc.getTeam(gc.getPlayer(iCivToMeet).getTeam()).isAlive() and not pTeam.isHasMet(iCivToMeet):
				pTeam.meet(iCivToMeet, True)
		
		# edead: war on spawn I - declare war on civs from the list
		# for i in range(len(lEnemyCivsOnSpawn[iCiv])):
			# gc.getTeam(pPlayer.getTeam()).declareWar(lEnemyCivsOnSpawn[iCiv][i], False, -1)
		for iEnemyCiv in lEnemyCivsOnSpawn[iCiv]:
			if utils.isActive(iEnemyCiv):
				gc.getTeam(pPlayer.getTeam()).declareWar(iEnemyCiv, False, -1)
		
		# edead: war on spawn II - randomly declare war on civs in normal regions
		# plotList = utils.getNormalPlotList(iCiv)
		# for i in range(len(plotList)):
			# if gc.getMap().plot(plotList[i][0], plotList[i][1]).isCity():
				# city = gc.getMap().plot(plotList[i][0], plotList[i][1]).getPlotCity()
				# iRandNum = gc.getGame().getSorenRandNum(100, 'war on spawn')
				# if iRandNum < 25: # 25% chance per city
					# gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(city.getOwner(), False, -1)
		
		# edead: reveal some map
		utils.revealPlots(iCiv, utils.getRegionPlotList(lRevealRegions[iCiv], True)) 
		
		iStateReligion = pPlayer.getStateReligion()
		if iStateReligion == iSunni or iStateReligion == iShia:
			utils.revealCity(iCiv, tMecca)
			utils.revealCity(iCiv, tJerusalem)
		elif iStateReligion == iOrthodoxy or iStateReligion == iCatholicism:
			utils.revealCity(iCiv, tConstantinople)
			utils.revealCity(iCiv, tJerusalem)
		if iStateReligion == iShia:
			utils.revealCity(iCiv, tNajaf)
		
		# set piety - for late game civs that start with state religion
		if iStateReligion >= 0:
			utils.setBasePiety(iCiv, 40)
			utils.setPiety(iCiv, 40)
		
		self.assignTechs(iCiv)
		self.hitNeighboursStability(iCiv)


	def createPostFlipUnits(self, iCiv):
		"""Creates extra units in flipped cities."""
		
		if iCiv == iAyyubids:
			if gc.getMap().plot(22,43).isCity() and gc.getMap().plot(22,43).getOwner() == iAyyubids:
				utils.makeUnit(iSpearman, iCiv, (22,43), 1)
				utils.makeUnit(iLancer, iCiv, (22,43), 1)
			if gc.getMap().plot(17,31).isCity() and gc.getMap().plot(17,31).getOwner() == iAyyubids:
				utils.makeUnit(iMarksman, iCiv, (17,31), 1)
			if gc.getMap().plot(23,47).isCity() and gc.getMap().plot(23,47).getOwner() == iAyyubids:
				utils.makeUnit(iSpearman, iCiv, (23,47), 1)
			
		if iCiv == iBuyids:
			if gc.getMap().plot(49,39).isCity() and gc.getMap().plot(49,39).getOwner() == iBuyids:
				utils.makeUnit(iGhulamLancer, iCiv, (49,39), 1)
				utils.makeUnit(iDaylamiTribesman, iCiv, (49,39), 1)
		
		if utils.getHumanID() in lEnemyCivsOnSpawn[iCiv]:
			apCityList = PyPlayer(iCiv).getCityList()
			for pCity in apCityList:
				utils.createGarrisons((pCity.getX(), pCity.getY()), iCiv, 1)


	def createStartingWorkers(self, iCiv, tPlot):
		"""Creates workers for the specified civ."""
		
		iNumWorkers = 2
		if utils.getYear() > 1250: iNumWorkers = 4
		elif utils.getYear() > 1000: iNumWorkers = 3
		utils.makeUnit(iWorker, iCiv, tPlot, iNumWorkers)
		
		if iCiv == iSamanids and iCiv != utils.getHumanID():
			utils.makeUnit(iSettler, iCiv, tPlot, 1) # fixes weird Samanid settler behaviour


	def createEarlyStartingUnits(self):
		"""Creates a settler and a scout for early start civs and the human player."""
		
		iHuman = utils.getHumanID()
		if tBirth[iHuman] > iStartYear:
			utils.makeUnit(iCatapult, iHuman, (iCatapultX, iCatapultY), 1)
		
		for iCiv in range(iNumPlayers):
			if tBirth[iCiv] == iStartYear:
				self.createStartingUnits(iCiv, tCapitals[iCiv])
			else:
				break


	def assignTechs(self, iCiv):
		"""Assigns techs to the specific civ based on the starting tech table."""
		
		pTeam = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		for iLoopTech in range(len(lStartingTechs[iCiv])):
			pTeam.setHasTech(lStartingTechs[iCiv][iLoopTech], True, iCiv, False, False)


	def hitNeighboursStability( self, iCiv ):
		
		if (len(lOlderNeighbours[iCiv])):
			bHuman = False
			for iLoop in lOlderNeighbours[iCiv]:
				if (gc.getPlayer(iLoop).isAlive()):
					if (iLoop == utils.getHumanID()):
						bHuman = True
					utils.setStability(iLoop, sd.getStability(iLoop)-3)
			if (bHuman):
				utils.setStabilityParameters(iParDiplomacyE, utils.getStabilityParameters(iParDiplomacyE)-3)


	def moveCapital (self, tCoords, iPlayer, bHuman=False):
		"""Moves the AI's capital to the specified city."""
		
		if tCoords[0] == -1 or tCoords[1] == -1:
			return False
		
		pNewCapital = gc.getMap().plot(tCoords[0], tCoords[1]).getPlotCity()
		if pNewCapital and not pNewCapital.isNone(): 
			if pNewCapital.getNumRealBuilding(iPalace) > 0:
				return True
			if pNewCapital.getOwner() == iPlayer and (bHuman or pNewCapital.getOwner() != utils.getHumanID()):
				apCityList = PyPlayer(iPlayer).getCityList()
				for pyCity in apCityList:
					city = gc.getMap().plot(pyCity.getX(), pyCity.getY()).getPlotCity()
					if city.getNumRealBuilding(iPalace) > 0 and city.getX() != pNewCapital.getX() and city.getY() != pNewCapital.getY():
						city.setNumRealBuilding(iPalace, 0)
						break
				pNewCapital.setNumRealBuilding(iPalace, 1)
				return True
		return False


	def checkCapitals (self, iGameTurn):
		"""If applicable, moves the non-human player's capital to the historical location for free."""
		
		for iCiv in range(iNumPlayers):
			if tNewCapitals[iCiv][0] > -1:
				counter = self.getCounter(iCiv)
				if counter == 1:
					self.setCounter(iCiv, 0)
					self.moveCapital(tNewCapitals[iCiv], iCiv)
				elif counter > 1:
					self.setCounter(iCiv, counter - 1)


	def checkCapitalsOnCapture (self, pCity, iCiv):
		"""Sets the new capital counter when a new historical capital is captured by a non-human player."""
		
		if iCiv != utils.getHumanID() and iCiv < iNumPlayers:
			if (pCity.getX(), pCity.getY()) == tNewCapitals[iCiv]:
				self.setCounter(iCiv, utils.getTurns(10+gc.getGame().getSorenRandNum(10, 'New Capital')))


	def getBetrayalThreshold(self):
		if gc.getGame().getHandicapType() == 0:
			return 85
		return 80


	def showBirthMessage(self, iCiv, iHuman):
		
		textKey = ""
		
		if iCiv == iSamanids and iHuman in [iByzantium, iAbbasids]:
			textKey = "TXT_KEY_CIV_BIRTH_SAMANIDS"
		
		elif iCiv == iArmenia and iHuman in [iByzantium, iAbbasids]:
			textKey = "TXT_KEY_CIV_BIRTH_ARMENIA"
		
		elif iCiv == iYemen and iHuman in [iAbbasids]:
			textKey = "TXT_KEY_CIV_BIRTH_YEMEN"
		
		elif iCiv == iSamanids and iHuman in [iAbbasids, iSamanids, iArmenia, iYemen]:
			textKey = "TXT_KEY_CIV_BIRTH_BUYIDS"
		
		elif iCiv == iGujarat and iHuman in [iChauhan, iMalwa]:
			textKey = "TXT_KEY_CIV_BIRTH_SOLANKI"
		
		elif iCiv == iGhaznavids and iHuman in [iByzantium, iAbbasids, iSamanids, iChauhan, iGujarat]:
			textKey = "TXT_KEY_CIV_BIRTH_GHAZNAVIDS"
		
		elif iCiv == iFatimids and iHuman in [iByzantium, iMakuria, iAbbasids, iYemen, iArmenia]:
			textKey = "TXT_KEY_CIV_BIRTH_FATIMIDS"
		
		elif iCiv == iGeorgia and iHuman in [iByzantium, iAbbasids, iArmenia]:
			textKey = "TXT_KEY_CIV_BIRTH_GEORGIA"
		
		elif iCiv == iSeljuks and iHuman in [iByzantium, iAbbasids, iSamanids, iArmenia, iGhaznavids, iFatimids, iGeorgia]:
			textKey = "TXT_KEY_CIV_BIRTH_SELJUKS"
		
		elif iCiv == iSindh and iHuman in [iAbbasids, iFatimids, iSamanids, iGhaznavids, iSeljuks, iChauhan, iGujarat]:
			textKey = "TXT_KEY_CIV_BIRTH_SINDH"
		
		elif iCiv == iRum and iHuman in [iByzantium, iAbbasids, iSamanids, iArmenia, iGhaznavids, iFatimids, iGeorgia, iSeljuks]:
			textKey = "TXT_KEY_CIV_BIRTH_RUM"
		
		elif iCiv == iKhwarezm and iHuman in [iByzantium, iAbbasids, iSamanids, iGhaznavids, iSeljuks]:
			textKey = "TXT_KEY_CIV_BIRTH_KHWAREZM"
		
		elif iCiv == iAntioch and iHuman in [iByzantium, iAbbasids, iArmenia, iGeorgia, iSeljuks, iRum, iFatimids]:
			textKey = "TXT_KEY_CIV_BIRTH_ANTIOCH"
		
		elif iCiv == iCrusaders and iHuman in [iByzantium, iAntioch, iAbbasids, iYemen, iArmenia, iGeorgia, iSeljuks, iRum, iFatimids]:
			textKey = "TXT_KEY_CIV_BIRTH_JERUSALEM"
		
		elif iCiv == iZengids and iHuman in [iByzantium, iAbbasids, iYemen, iArmenia, iGeorgia, iSeljuks, iRum, iCrusaders, iFatimids]:
			textKey = "TXT_KEY_CIV_BIRTH_ZENGIDS"
		
		elif iCiv == iGhorids and iHuman in [iAbbasids, iSeljuks, iKhwarezm, iGhaznavids, iChauhan, iGujarat, iSindh]:
			textKey = "TXT_KEY_CIV_BIRTH_GHORIDS"
		
		elif iCiv == iOman and iHuman in [iAbbasids, iYemen, iSeljuks, iSindh]:
			textKey = "TXT_KEY_CIV_BIRTH_OMAN"
		
		elif iCiv == iAyyubids and iHuman in [iByzantium, iMakuria, iAbbasids, iYemen, iArmenia, iGeorgia, iSeljuks, iRum, iCrusaders]:
			textKey = "TXT_KEY_CIV_BIRTH_AYYUBIDS"
		
		elif iCiv == iMamluks and iHuman in [iByzantium, iMakuria, iAbbasids, iYemen, iArmenia, iGeorgia, iSeljuks, iRum, iCrusaders]:
			textKey = "TXT_KEY_CIV_BIRTH_MAMLUKS"
		
		elif iCiv == iOttomans and iHuman in [iByzantium, iAbbasids, iArmenia, iGeorgia, iCrusaders, iSeljuks, iRum, iTimurids, iKhwarezm, iFatimids, iAyyubids, iMamluks]:
			textKey = "TXT_KEY_CIV_BIRTH_OTTOMANS"
		
		elif iCiv == iAkKoyunlu and iHuman in [iByzantium, iAbbasids, iArmenia, iGeorgia, iCrusaders, iSeljuks, iRum, iTimurids, iKhwarezm, iFatimids, iAyyubids, iMamluks, iOttomans]:
			textKey = "TXT_KEY_CIV_BIRTH_AKKOYUNLU"
		
		elif iCiv == iSafavids and iHuman not in [iMakuria, iChauhan, iGujarat]:
			textKey = "TXT_KEY_CIV_BIRTH_SAFAVIDS"
		
		elif iCiv == iSafavids and iHuman in [iChauhan, iGujarat, iSindh, iGhaznavids, iGhorids, iSamanids, iKhwarezm, iTimurids, iOman, iSafavids, iSeljuks]:
			textKey = "TXT_KEY_CIV_BIRTH_MUGHALS"
		
		if textKey:
			CyInterface().addMessage(iHuman, True, iDuration, CyTranslator().getText(textKey, ()), "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getCivilizationInfo(iCiv).getButton(), ColorTypes(iGreen), tCapitals[iCiv][0], tCapitals[iCiv][1], True, True)
