# Religions

from CvPythonExtensions import *
import CvUtil
import Consts as con
from CvMainInterface import CvMainInterface
from PyHelpers import PyPlayer
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()


class Religions:


#######################################
### Main methods (Event-Triggered) ###
#####################################


	def setup(self):
		
		# Piety
		for iPlayer in range(con.iNumPlayers):
			if con.tBirth[iPlayer] <= con.iStartYear and gc.getPlayer(iPlayer).getStateReligion() > 0:
				iBasePiety = self.calcBasePiety(iPlayer)
				if iBasePiety < 40: iBasePiety = 40
				sd.setBasePiety(iPlayer, iBasePiety)
				sd.setPiety(iPlayer, iBasePiety)
		
		# Relics
		hiddenRelics = {}
		for iRelic in con.relics.keys():
			iJerusalemCount = iByzantiumCount = 0 # used to make sure there's max. 2 relics in these cities
			validLocations = con.relics[iRelic][1]
			iProvince = validLocations[gc.getGame().getSorenRandNum(len(validLocations), 'Random location')]
			# If it's Thrace, make it Constantinople; if it's Palestine, make it Jerusalem; otherwise use random city
			if iProvince == con.rThrace:
				if iByzantiumCount == 2:
					if con.rThrace in validLocations:
						validLocations.remove(con.rThrace)
					iProvince = validLocations[gc.getGame().getSorenRandNum(len(validLocations), 'Random location')]
					city = utils.getRandomCityByRegion([iProvince])
				else:
					iByzantiumCount += 1
					city = gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getPlotCity()
			elif iProvince == con.rPalestine:
				if iJerusalemCount == 2:
					if con.rPalestine in validLocations:
						validLocations.remove(con.rPalestine)
					iProvince = validLocations[gc.getGame().getSorenRandNum(len(validLocations), 'Random location')]
					city = utils.getRandomCityByRegion([iProvince])
				else:
					iJerusalemCount += 1
					city = gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1]).getPlotCity()
			else:
				city = utils.getRandomCityByRegion([iProvince])
			if city:
				# this check makes sure that relics from the holy land aren't instantly grabbed by muslims
				# and hauled to Egypt/Iraq; they remain hidden instead until the crusaders arrive
				# if city.getOwner() >= con.iNumPlayers:
					# if iRelic in [con.iTrueCross, con.iHolyLance]:
						# if iProvince in [con.rPalestine, con.rNorthernSyria]:
							# hiddenRelics[iRelic] = iProvince
							# continue
				city.setNumRealBuilding(iRelic, 1)
			else:
				hiddenRelics[iRelic] = iProvince
		sd.setVal('hiddenRelics', hiddenRelics)


	def eventApply7624(self, popupReturn):
		"""Holy war popup event."""
		iPlayer = utils.getCaliphController()
		targetList = utils.getHolyWarTargets(iPlayer)
		if popupReturn.getButtonClicked() < len(targetList):
			tTarget = targetList[popupReturn.getButtonClicked()]
			CyInterface().addMessage(iPlayer, False, con.iDuration, localText.getText("TXT_KEY_HOLY_WAR_CALLED", (gc.getPlayer(iPlayer).getName(), gc.getPlayer(tTarget[0]).getCivilizationDescription(0))), "AS2D_DECLAREWAR", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
			sd.setVal('iLastHolyWarTurn', gc.getGame().getGameTurn())
			sd.setVal('iHolyWarTarget', tTarget[0])


	def eventApply7625(self, popupReturn):
		"""Holy war call."""
		iHuman = utils.getHumanID()
		if popupReturn.getButtonClicked() == 0: # YES
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).declareWar(sd.getVal('iHolyWarTarget'), False, -1)
			sd.changePiety(iHuman, max(5, (100 - sd.getPiety(iHuman)) / 5))
		else:
			sd.changePiety(iHuman, min(-10, -(sd.getPiety(iHuman) * 2 / 5)))
		CvMainInterface().updateGameDataStrings()


	def eventApply7626(self, popupReturn):
		"""Persecution popup event."""
		iUnitX, iUnitY, iUnitID = sd.getPersecutionData()
		religionList = sd.getPersecutionReligions()
		utils.doPersecution(iUnitX, iUnitY, iUnitID, religionList[popupReturn.getButtonClicked()])


	def changePiety(self, iPlayer, iChange):
		
		if iPlayer < con.iNumPlayers:
			iPiety = sd.getPiety(iPlayer)
			if iPiety >= 0:
				iPreviousPiety = iPiety
				iPiety += iChange
				sd.setPiety(iPlayer, iPiety)


	def checkTurn(self, iGameTurn):
		
		iHuman = utils.getHumanID()
		
		# Relic Respawn: every 40 turns one random lost relic will be respawned in an independent or barbarian city
		if iGameTurn % utils.getTurns(40) == 0:
			relicList = con.relics.keys() # list of all relics
			# exclude hidden relics
			hiddenRelics = sd.getVal('hiddenRelics')
			for iRelic in hiddenRelics.keys():
				if iRelic in relicList:
					relicList.remove(iRelic)
			# exclude relics that are active as units or buildings
			map = CyMap()
			for i in range(map.numPlots()):
				plot = map.plotByIndex(i)
				if plot.isCity():
					for iRelic in list(relicList):
						if plot.getPlotCity().getNumRealBuilding(iRelic):
							relicList.remove(iRelic)
				for j in range(plot.getNumUnits()):
					unitType = plot.getUnit(j).getUnitType()
					if unitType >= con.iRelic1:
						for iRelic in con.relics.keys():
							if con.relics[iRelic][0] == unitType:
								if iRelic in relicList:
									relicList.remove(iRelic)
								break
			# proceed if there are any relics remaining on the list (i.e. those that are lost)
			if relicList:
				iRelic = relicList[gc.getGame().getSorenRandNum(len(relicList), "random relic")]
				# for realistic locations, narrow the list of valid cities to those in specified provinces
				if gc.getBuildingInfo(iRelic).getStateReligion() in [con.iCatholicism, con.iOrthodoxy]:
					regionList = con.relicRegionsChristian
				else:
					regionList = con.relicRegionsIslamic
				cityList = []
				# make a list of valid independent and barbarian cities
				playerList = range(con.iIndependent, con.iBarbarian + 1, 1)
				for iPlayer in playerList:
					if gc.getPlayer(iPlayer).getNumCities() > 0:
						for pyCity in PyPlayer(iPlayer).getCityList():
							plot = map.plot(pyCity.getX(), pyCity.getY())
							if plot.getRegionID() in regionList:
								cityList.append(pyCity.GetCy())
				# respawn the relic
				if cityList:
					iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
					city = cityList[iCity]
					city.setNumRealBuilding(iRelic, 1)
					debugMsg = str(gc.getGame().getGameTurnYear()) + ' AD: ' + gc.getBuildingInfo(iRelic).getText() + ' respawned in ' + city.getName()
					print debugMsg
		
		# Holy Wars
		iCaliphPlayer = utils.getCaliphController()
		if iGameTurn > getTurnForYear(1000) and iGameTurn % utils.getTurns(15) == 0:
			if iCaliphPlayer and utils.getHumanID() != iCaliphPlayer:
				if iGameTurn - sd.getVal('iLastHolyWarTurn') - 100 >= 0:
					self.checkAIHolyWar(iCaliphPlayer)
		if iCaliphPlayer and iGameTurn == sd.getVal('iLastHolyWarTurn') + 1:
			iTarget = sd.getVal('iHolyWarTarget')
			civList = utils.getHolyWarParticipants(iCaliphPlayer, iTarget)
			for iCiv in civList:
				iChance, szText = utils.getHolyWarTargetInfo(iCiv, iTarget)
				if iCiv != iHuman:
					if iChance > 0: iChance *= 5
					if utils.getYear() > 1050 and utils.getYear() < 1250:
						iChance += 10
					iChance += utils.calculateRelations(iCiv, iCaliphPlayer) * 2
					iChance -= utils.calculateRelations(iCiv, iTarget) * 2
					iPowerRatio = 100 * gc.getPlayer(iTarget).getPower() / gc.getPlayer(iCaliphPlayer).getPower()
					iChance = iChance * iPowerRatio / 100
					if iPowerRatio <= 100 and iCaliphPlayer == iHuman: 
						iChance -= 10 * (gc.getGame().getHandicapType() + 1)
					elif iTarget == iHuman:
						iChance += 10 * (gc.getGame().getHandicapType() + 1)
					#utils.echo("%s, %d" %(gc.getPlayer(iCiv).getName(), iChance))
					if gc.getGame().getSorenRandNum(100, 'Answer the call?') < iChance:
						gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iTarget, False, -1)
						sd.changePiety(iCiv, max(10, (100 - sd.getPiety(iCiv)) / 5))
					else:
						iPenalty = min(-10, -(sd.getPiety(iCiv) * 2 / 5))
						if iPowerRatio <= 100:
							iPenalty = iPenalty * iPowerRatio / 100
						sd.changePiety(iCiv, iPenalty)
				else:
					iReligion = gc.getPlayer(iTarget).getStateReligion()
					if iReligion == -1:
						szReligion = localText.getText("TXT_KEY_HOLY_WAR_PAGAN", ())
					elif iReligion == con.iCatholicism or iReligion == con.iOrthodoxy:
						szReligion = localText.getText("TXT_KEY_HOLY_WAR_CHRISTIAN", ())
					else:
						szReligion = gc.getReligionInfo(iReligion).getAdjectiveKey()
					szText = localText.getText(szText, (szReligion, ))
					utils.showPopup(7625, localText.getText("TXT_KEY_HOLY_WAR_POPUP_TITLE", ()), localText.getText("TXT_KEY_HOLY_WAR_CALL", (gc.getPlayer(iCaliphPlayer).getName(), gc.getPlayer(iTarget).getCivilizationDescription(0), szText)), (localText.getText("TXT_KEY_HOLY_WAR_YES", ()), localText.getText("TXT_KEY_HOLY_WAR_NO", ())))
		
		# Piety rise/decay
		if iGameTurn % utils.getTurns(5) == 1:
			for iPlayer in range(con.iNumPlayers):
				if gc.getPlayer(iPlayer).isAlive():
					iBasePiety = self.calcBasePiety(iPlayer)
					sd.setBasePiety(iPlayer, iBasePiety)
					iPiety = sd.getPiety(iPlayer)
					if iPiety < 0:
						sd.setPiety(iPlayer, iBasePiety)
					elif iPiety > iBasePiety:
						self.changePiety(iPlayer, -1)
					elif iPiety < iBasePiety:
						self.changePiety(iPlayer, min(5, (iBasePiety + 1) / (iPiety + 1)))
			# Piety effects
			for iPlayer in range(con.iNumPlayers):
				if gc.getPlayer(iPlayer).isAlive():
					self.doPietyEffects(iPlayer)
		
		# Zoroastrianism
		if iGameTurn == getTurnForYear(821):
			self.spreadReligion(utils.getRandomCityByRegion([con.rBactria]), con.iZoroastrianism)
		if iGameTurn == getTurnForYear(850):
			self.spreadReligion(utils.getRandomCityByRegion([con.rEasternKhorasan]), con.iZoroastrianism)
			self.spreadReligion(utils.getRandomCityByRegion([con.rGujarat]), con.iZoroastrianism)
		if iGameTurn == getTurnForYear(935 + sd.getSeed() % 30):
			self.spreadReligion(utils.getRandomCityByRegion([con.rLuristan, con.rKurdistan, con.rJibal]), con.iZoroastrianism)
		if iGameTurn == getTurnForYear(990):
			self.spreadReligion(utils.getRandomCityByRegion([con.rYazd]), con.iZoroastrianism)
		
		# Nestorianism
		if iGameTurn == getTurnForYear(930 + sd.getSeed() % 40):
			self.spreadReligion(utils.getRandomCityByRegion([con.rAsuristan, con.rKurdistan, con.rLuristan, con.rTaklaMakan]), con.iOrthodoxy)

		# Religions in Egypt
		if iGameTurn == getTurnForYear(con.tBirth[con.iFatimids] + sd.getSeed() % 15) + 1:
			self.spreadReligion(utils.getRandomCityByRegion([con.rLowerEgypt]), con.iSunni)
		if iGameTurn == getTurnForYear(con.tBirth[con.iFatimids] + sd.getSeed() % 50) + 1:
			self.spreadReligion(utils.getRandomCityByRegion([con.rLowerEgypt, con.rPalestine, con.rUpperEgypt]), con.iOrthodoxy)
			
		# Decline of Buddhism
		if iGameTurn == getTurnForYear(1150 + sd.getSeed() % 20) or iGameTurn == getTurnForYear(1180 + sd.getSeed() % 20):
			self.removeReligion(utils.getRandomCityByReligion(con.iBuddhism), con.iBuddhism)
			
		# Islam in Afghanistan
		if iGameTurn == getTurnForYear(1000 + sd.getSeed() % 20):
			self.spreadReligion(utils.getRandomCityByRegion([con.rHindukush]), con.iSunni)
		
		# Seljuks in Iran
		if iGameTurn == getTurnForYear(1036):
			self.spreadReligion(utils.getRandomCityByRegion([con.rKurdistan, con.rLuristan, con.rWesternKhorasan, con.rEasternKhorasan]), con.iSunni)
		
		# Seljuks in Anatolia
		if iGameTurn == getTurnForYear(1064):
			self.spreadReligion(utils.getRandomCityByRegion([con.rVaspurakan, con.rLesserArmenia]), con.iSunni)
		if iGameTurn == getTurnForYear(1070)-1:
			self.spreadReligion(utils.getRandomCityByRegion([con.rGalatia, con.rCappadocia]), con.iSunni)
		if iGameTurn == getTurnForYear(1100) or iGameTurn == getTurnForYear(1130) or iGameTurn == getTurnForYear(1160):
			self.spreadReligion(utils.getRandomCityByRegion([con.rCappadocia, con.rGalatia, con.rBithynia, con.rAsia, con.rLycia, con.rPaphlagonia, con.rPontus, con.rLesserArmenia]), con.iSunni)
		if iGameTurn == getTurnForYear(1270 + sd.getSeed() % 20):
			self.spreadReligion(utils.getRandomCityByRegion([con.rAsia, con.rBithynia, con.rLycia]), con.iSunni)
		if iGameTurn == getTurnForYear(1185 + sd.getSeed() % 15) or iGameTurn == getTurnForYear(1290 + sd.getSeed() % 10):
			self.spreadReligion(utils.getRandomCityByRegion([con.rCappadocia, con.rGalatia, con.rLesserArmenia, con.rVaspurakan]), con.iShia)
		
		# Armenian refugees in Cilicia
		if iGameTurn == getTurnForYear(1078):
			self.spreadReligion(utils.getRandomCityByRegion([con.rCilicia]), con.iOrthodoxy)

		# Catholics in Northern Syria
		if iGameTurn == getTurnForYear(1050):
			city = gc.getMap().plot(con.tTripoli[0], con.tTripoli[1]).getPlotCity()
			if city and not city.isNone() and not city.isHasReligion(con.iCatholicism):
				city.setHasReligion(con.iCatholicism, True, True, True)
		if iGameTurn == getTurnForYear(con.tBirth[con.iAntioch]) + 1 or iGameTurn == getTurnForYear(con.tBirth[con.iAntioch]) + 2:
			city = gc.getMap().plot(con.tAntioch[0], con.tAntioch[1]).getPlotCity()
			if city and not city.isNone() and not city.isHasReligion(con.iCatholicism) and city.getOwner() == con.iAntioch:
				city.setHasReligion(con.iCatholicism, True, True, True)
		
		# Make sure there is Islam in the Levant
		if iGameTurn == getTurnForYear(1080):
			self.spreadReligion(utils.getRandomCityByRegion([con.rNorthernSyria]), con.iSunni)
		if iGameTurn == getTurnForYear(1160):
			self.spreadReligion(utils.getRandomCityByRegion([con.rSyria]), con.iSunni)
		
		# Zengids
		if iGameTurn == getTurnForYear(1127)-5:
			self.spreadReligion(utils.getRandomCityByRegion([con.rAsuristan]), con.iSunni)
		
		# Shiites in Northern Iran and Azerbaijan
		if iGameTurn == getTurnForYear(950 + sd.getSeed() % 40):
			self.spreadReligion(utils.getRandomCityByRegion([con.rAsuristan, con.rLuristan, con.rKurdistan]), con.iShia)
		if iGameTurn == getTurnForYear(1160):
			self.spreadReligion(utils.getRandomCityByRegion([con.rShirvan, con.rAzerbaijan]), con.iShia)
		
		# Islam in India
		if iGameTurn == getTurnForYear(1012 + sd.getSeed() % 5):
			self.spreadReligion(utils.getRandomCityByRegion([con.rSindh, con.rPunjab]), con.iSunni)
		if iGameTurn == getTurnForYear(1020 + sd.getSeed() % 10):
			self.spreadReligion(utils.getRandomCityByRegion([con.rSindh, con.rPunjab]), con.iSunni)
		if iGameTurn == getTurnForYear(1100 + sd.getSeed() % 3):
			if gc.getGame().getSorenRandNum(100, 'Random religion') > 50:
				self.spreadReligion(utils.getRandomCityByRegion([con.rPunjab]), con.iShia)
			elif gc.getGame().getSorenRandNum(100, 'Random religion') > 50:
				self.spreadReligion(utils.getRandomCityByRegion([con.rSindh, con.rPunjab]), con.iSunni)
			else:
				self.spreadReligion(utils.getRandomCityByRegion([con.rSindh, con.rPunjab]), con.iHinduism)
		if iGameTurn == getTurnForYear(1150 + sd.getSeed() % 3):
			if iHuman != con.iChauhan and iHuman != con.iGhorids:
				self.spreadReligion(utils.getRandomCityByRegion([con.rUttarBharat]), con.iSunni)
		if iGameTurn == getTurnForYear(1220 + sd.getSeed() % 3):
			self.spreadReligion(utils.getRandomCityByRegion([con.rMalwa]), con.iSunni)
		if iGameTurn == getTurnForYear(1280 + sd.getSeed() % 4):
			self.spreadReligion(utils.getRandomCityByRegion([con.rSindh, con.rPunjab, con.rGujarat]), con.iSunni)
		if iGameTurn == getTurnForYear(1320):
			self.spreadReligion(utils.getRandomCityByRegion([con.rGujarat, con.rMalwa]), con.iSunni)
		if iGameTurn == getTurnForYear(1330):
			self.spreadReligion(utils.getRandomCityByRegion([con.rSindh]), con.iSunni)
		if iGameTurn == getTurnForYear(1350):
			self.spreadReligion(utils.getRandomCityByRegion([con.rGujarat, con.rUttarBharat]), con.iSunni)
		
		# Islam in Nubia
		if iGameTurn == getTurnForYear(1250 + sd.getSeed() % 20):
			self.spreadReligion(utils.getRandomCityByRegion([con.rUpperEgypt, con.rNobatia]), con.iSunni)
		if iGameTurn == getTurnForYear(1280 + sd.getSeed() % 40):
			self.spreadReligion(utils.getRandomCityByRegion([con.rNobatia, con.rMakuria]), con.iSunni)
		if iGameTurn == getTurnForYear(1325 + sd.getSeed() % 30):
			self.spreadReligion(utils.getRandomCityByRegion([con.rMakuria, con.rAlodia]), con.iSunni)
		
		# Himyarite Jews
		if iGameTurn == getTurnForYear(901):
			self.spreadReligion(utils.getRandomCityByRegion([con.rYemen]), con.iJudaism)
		# Other Jews
		if iGameTurn % utils.getTurns(50) == 16:
			if iGameTurn <= getTurnForYear(1200):
				self.spreadReligion(utils.getRandomCityByRegion(con.jewsEarlyRegions), con.iJudaism)
			else:
				self.spreadReligion(utils.getRandomCityByRegion(con.jewsMiddleRegions), con.iJudaism)


	def spreadReligion(self, city, iReligion, textKey=False):
		
		if city is None or city.isNone():
			return -1
		
		# do not spread the religion if the city already has it, or the owner is using Persecution civic
		if city.isHasReligion(iReligion) or gc.getPlayer(city.getOwner()).getCivics(4) == con.iPersecutionCivic:
			return -1
		
		# show the message about Jewish refugess if the religion is Judaism
		if iReligion == con.iJudaism:
			city.setHasReligion(iReligion, True, False, False)
			if not textKey:
				textKey = "TXT_KEY_MINOR_EVENT_JEWS"
			szText = localText.getText(textKey, (city.getName(), ))
			CyInterface().addMessage(city.getOwner(), False, con.iDuration, szText, "AS2D_BUILD_JEWISH", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, gc.getReligionInfo(iReligion).getButton(), ColorTypes(con.iWhite), city.getX(), city.getY(), True, True)
		else:
			city.setHasReligion(iReligion, True, True, True)
		return True


	def removeReligion(self, city, iReligion):
		
		if city is None: return -1
		elif city.isNone(): return -1
		elif not city.isHasReligion(iReligion): return -1
		
		city.setHasReligion(iReligion, False, True, True)
		return True


	def onPlayerChangeStateReligion(self, argsList):
		'Player changes his state religion'
		iPlayer, iNewReligion, iOldReligion = argsList
		
		if iPlayer >= con.iNumPlayers: return
		
		pPlayer = gc.getPlayer(iPlayer)
		iBasePiety = self.calcBasePiety(iPlayer)
		sd.setBasePiety(iPlayer, iBasePiety)
		sd.setPiety(iPlayer, iBasePiety)
		
		# eject all relics if needed
		for tReligionGroup in ([con.iSunni, con.iShia], [con.iCatholicism, con.iOrthodoxy]):
			if iOldReligion in tReligionGroup and iNewReligion not in tReligionGroup:
				apCityList = PyPlayer(iPlayer).getCityList()
				for pCity in apCityList:
					for iRelic in con.relics.keys():
						if pCity.getNumBuilding(iRelic):
							pCity.GetCy().setNumRealBuilding(iRelic, 0)
							utils.makeUnit(con.relics[iRelic][0], iPlayer, (pCity.getX(), pCity.getY()), 1, UnitAITypes.UNITAI_MERCHANT)
		
		# add/remove Islamic tech to turn pork consumption on/off
		if iNewReligion in [con.iSunni, con.iShia]:
			gc.getTeam(pPlayer.getTeam()).setHasTech(con.iIslamTech, True, pPlayer.getTeam(), False, False)
		else:
			gc.getTeam(pPlayer.getTeam()).setHasTech(con.iIslamTech, False, pPlayer.getTeam(), False, False)
		
		# reset diplomatic penalty from persecution
		for iLoopPlayer in range(con.iNumPlayers):
			if gc.getPlayer(iLoopPlayer).isAlive() and iLoopPlayer != iPlayer:
				pPlayer.AI_setAttitudeExtra(iLoopPlayer, 0)
		
		# punishment for switching between Islam and Christianity
		iTurmoilLevel = 0
		testList = [] # 25% chance leaving
		killList = [] # 100% chance of leaving
		
		if iOldReligion in [con.iCatholicism, con.iOrthodoxy]:
			iTurmoilLevel = 1
			testList.extend([con.iManAtArms, con.iNormanKnight, con.iLancer, con.iHeavyLancer, con.iHeavyCavalry, con.iHeavySwordsman])
			killList.extend([con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight])
			if iNewReligion in [con.iSunni, con.iShia, con.iHinduism, -1]:
				iTurmoilLevel = 2
				testList.extend([con.iCataphract, con.iMonaspaLancer, con.iVishapInfantry, con.iSwordsman, con.iAxeman])
				killList.extend([con.iItalianMaceman, con.iItalianCrossbowman, con.iKnightOfJerusalem, con.iHospitallerSergeant, con.iHospitallerCanon, con.iHospitallerKnight, con.iTemplarSergeant, con.iTemplarKnight, con.iManAtArms, con.iNormanKnight, con.iVarangianGuard])
		
		if iOldReligion in [con.iSunni, con.iShia]:
			if iNewReligion in [con.iCatholicism, con.iOrthodoxy, con.iHinduism, -1]:
				iTurmoilLevel = 2
				testList.extend([con.iAbnaSpearman, con.iTawashiLancer, con.iMamluk])
				killList.extend([con.iGhulamGuard, con.iGhulamLancer, con.iGhulamHorseArcher, con.iMujahid, con.iGhazi])
		
		if iTurmoilLevel > 0:
			unitList = PyPlayer(iPlayer).getUnitList()
			for unit in unitList:
				if unit.getUnitType() in killList:
					unit.kill(True, -1)
				elif unit.getUnitType() in testList and gc.getGame().getSorenRandNum(100, 'Kill?') < iTurmoilLevel * 33:
					if not unit.isHasPromotion(con.iMercenary):
						unit.kill(True, -1)
			cityList = PyPlayer(iPlayer).getCityList()
			for pCity in cityList:
				city = pCity.GetCy()
				if city.isHasReligion(iOldReligion) and city.getPopulation() > 1:
					iPop = max(1, city.getPopulation() / city.getReligionCount() / 2)
					if iTurmoilLevel == 1:
						iPop -= 1
					city.changePopulation(-iPop)
					iRevoltTurns = gc.getGame().getSorenRandNum(iPop, 'Revolt Turns')
					city.changeCultureUpdateTimer(iRevoltTurns)
					city.changeOccupationTimer(iRevoltTurns)
			CyInterface().addMessage(iPlayer, True, con.iDuration, localText.getText("TXT_KEY_RELIGIOUS_TURMOIL", ()), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)


	def calcBasePiety(self, iPlayer):
		"""Calculates base piety level for a given player."""
		
		# Set the building variables
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		if iStateReligion == con.iCatholicism:
			iTemple = con.iCatholicTemple
			iMonastery = con.iCatholicMonastery
			iCathedral = con.iCatholicCathedral
			iShrine = con.iCatholicShrine
			lWonders = []
		elif iStateReligion == con.iOrthodoxy:
			iTemple = con.iOrthodoxTemple
			iMonastery = con.iOrthodoxMonastery
			iCathedral = con.iOrthodoxCathedral
			iShrine = con.iOrthodoxShrine
			lWonders = [con.iBagratiCathedral, con.iNarekavank]
		elif iStateReligion == con.iSunni:
			iTemple = con.iSunniTemple
			iMonastery = con.iSunniMonastery
			iCathedral = con.iSunniCathedral
			iShrine = con.iSunniShrine
			lWonders = [con.iDomeOfTheRock, con.iSpiralMinaret, con.iMinaretOfJam, con.iQutbMinar, con.iBlueMosque, con.iProphetsMosque]
		elif iStateReligion == con.iShia:
			iTemple = con.iShiaTemple
			iMonastery = con.iShiaMonastery
			iCathedral = con.iShiaCathedral
			iShrine = con.iShiaShrine
			lWonders = [con.iDomeOfTheRock, con.iAlAzhar, con.iShahMosque, con.iProphetsMosque, con.iSunniShrine, con.iImamRezaShrine]
		elif iStateReligion == con.iHinduism:
			iTemple = con.iHinduTemple
			iMonastery = con.iHinduMonastery
			iCathedral = con.iHinduCathedral
			iShrine = con.iHinduShrine
			lWonders = [con.iTowerOfVictory, con.iRaniKiVav]
		else:
			return -1
		
		apCityList = PyPlayer(iPlayer).getCityList()
		iNumCities = len(apCityList)
		if iNumCities < 1: return -1
		
		iNumTemples = 0
		iNumMonasteries = 0
		iNumCathedrals = 0
		iNumStateReligions = 0
		iNumNonStateReligions = 0
		iNumWonders = 0
		iNumShrines = 0
		
		# Loop through the city list and count all religions and religious buildings
		for pyCity in apCityList:
			pCity = pyCity.GetCy()
			for iReligion in range(con.iNumReligions):
				if pCity.isHasReligion(iReligion):
					if iReligion == iStateReligion: 
						iNumStateReligions += 1
					else: 
						iNumNonStateReligions += 1
						# count christian and muslim denominations as one
						if  (iStateReligion == con.iCatholicism and iReligion == con.iOrthodoxy) or \
							(iStateReligion == con.iOrthodoxy and iReligion == con.iCatholicism) or \
							(iStateReligion == con.iSunni and iReligion == con.iShia) or \
							(iStateReligion == con.iShia and iReligion != con.iSunni):
								iNumNonStateReligions -= 1
			if pCity.getNumRealBuilding(iTemple) > 0 or (iStateReligion == con.iCatholicism and pCity.getNumRealBuilding(con.iNormanChapel) > 0): 
				iNumTemples += 1
			if pCity.getNumRealBuilding(iMonastery) > 0: 
				iNumMonasteries += 1
			if pCity.getNumRealBuilding(iCathedral) > 0: 
				iNumCathedrals += 1
			for iWonder in lWonders:
				if pCity.getNumRealBuilding(iWonder) > 0: 
					iNumWonders += 1
			if pCity.getNumRealBuilding(iShrine) > 0: 
				iNumShrines += 1
			if iStateReligion == con.iSunni or iStateReligion == con.iShia:
				if pCity.getNumRealBuilding(con.iSufiShrine) > 0: 
					iNumMonasteries += 1
		
		# Base Piety range: 20-92
		iPiety = 20
		iPiety += 10 * iNumStateReligions / iNumCities
		iPiety += max(0, 10 - (10 * iNumNonStateReligions / iNumCities))
		iPiety += 10 * iNumTemples / iNumCities
		iPiety += 10 * iNumMonasteries / iNumCities
		iPiety += 30 * iNumCathedrals / iNumCities
		iPiety += 12 * iNumWonders / max(1, len(lWonders))
		iPiety += 10 * iNumShrines
		
		# Civics:
		iReligionCivic = gc.getPlayer(iPlayer).getCivics(4)
		if iReligionCivic == con.iPaganismCivic:
			iPiety -= 10
		elif iStateReligion != con.iHinduism and iReligionCivic == con.iFreeReligionCivic:
			iPiety -= 5
		elif iStateReligion == con.iHinduism and iReligionCivic != con.iCasteSystemCivic:
			iPiety -= 5
		
		# Safavid UP: Piety
		if iPlayer == con.iSafavids:
			iPiety *= 3
			iPiety /= 2
		
		# Commander of the Faithful
		if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).getProjectCount(con.iCaliph):
			iPiety *= 4
			iPiety /= 3
		
		# Protector of the Holy Sepulchre
		if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).getProjectCount(con.iProtector) > 0:
			iPiety *= 5
			iPiety /= 4
		
		return min(100, iPiety)


	def onBuildingBuilt(self, iPlayer, iBuilding):
		
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		iTemplePiety = 2
		iMonasteryPiety = 2
		iCathedralPiety = 5
		iWonderPiety = 10
		iInnPiety = -1
		iBrothelPiety = -2
		if iStateReligion == con.iSunni or iStateReligion == con.iShia:
			iBrothelPiety -= 1
		if gc.getPlayer(iPlayer).getCivics(1) == con.iReligiousLawCivic:
			iInnPiety -= 1
			iBrothelPiety -= 1
	
		if iStateReligion == con.iCatholicism:
			if iBuilding == con.iCatholicTemple: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iNormanChapel: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iCatholicMonastery: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iCatholicCathedral: self.changePiety(iPlayer, iCathedralPiety)
			elif iBuilding == con.iBrothel: self.changePiety(iPlayer, iBrothelPiety)
		elif iStateReligion == con.iOrthodoxy:
			if iBuilding == con.iOrthodoxTemple: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iOrthodoxMonastery: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iOrthodoxCathedral: self.changePiety(iPlayer, iCathedralPiety)
			elif iBuilding == con.iBagratiCathedral: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iNarekavank: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iBrothel: self.changePiety(iPlayer, iBrothelPiety)
		elif iStateReligion == con.iSunni:
			if iBuilding == con.iSunniTemple: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iSunniMonastery: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iSunniCathedral: self.changePiety(iPlayer, iCathedralPiety)
			elif iBuilding == con.iSufiShrine: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iSpiralMinaret: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iMinaretOfJam: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iQutbMinar: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iBlueMosque: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iMevlanasTomb: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iInn: self.changePiety(iPlayer, iInnPiety)
			elif iBuilding == con.iBrothel: self.changePiety(iPlayer, iBrothelPiety)
		elif iStateReligion == con.iShia:
			if iBuilding == con.iShiaTemple: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iShiaMonastery: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iShiaCathedral: self.changePiety(iPlayer, iCathedralPiety)
			elif iBuilding == con.iSufiShrine: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iAlAzhar: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iShahMosque: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iMevlanasTomb: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iImamRezaShrine: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iInn: self.changePiety(iPlayer, iInnPiety)
			elif iBuilding == con.iBrothel: self.changePiety(iPlayer, iBrothelPiety)
		elif iStateReligion == con.iHinduism:
			if iBuilding == con.iHinduTemple: self.changePiety(iPlayer, iTemplePiety)
			elif iBuilding == con.iHinduMonastery: self.changePiety(iPlayer, iMonasteryPiety)
			elif iBuilding == con.iHinduCathedral: self.changePiety(iPlayer, iCathedralPiety)
			elif iBuilding == con.iTowerOfVictory: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iRaniKiVav: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iHinduShrine: self.changePiety(iPlayer, iWonderPiety)
			elif iBuilding == con.iBrothel: self.changePiety(iPlayer, iBrothelPiety)


	def onTechAcquired(self, iTech, iPlayer):
		
		if iPlayer >= con.iNumPlayers: return
		
		if iTech in [con.iReligiousUnity, con.iReligiousPhilosophy, con.iReligiousArchitecture, con.iMosaicArt, con.iMusicTheory]:
			self.changePiety(iPlayer, 2)


	def makePilgrim(self):
		"""Generate a pilgrim at a random city."""
		
		# make a list of eligible players, count each player several times depending on piety
		playerList = []
		for iPlayer in range(con.iNumPlayers):
			pPlayer = gc.getPlayer(iPlayer)
			iPiety = sd.getPiety(iPlayer)
			if pPlayer.isAlive() and iPiety > 20:
				for i in range(iPiety/10 - 1):
					playerList.append(iPlayer)
		
		if len(playerList) > 1:
		
			# determine the recipient
			iRandNum = gc.getGame().getSorenRandNum(len(playerList), 'Random Player')
			iPlayer = playerList[iRandNum]
			pPlayer = gc.getPlayer(iPlayer)
			
			pCity = utils.getRandomCity(iPlayer)
			tCoords = utils.getPilgrimageSite(iPlayer)
			
			# make the pilgrim
			if pCity != -1:
				if pCity.getX() != tCoords[0] and pCity.getY() != tCoords[1]:
					pPlayer.initUnit(con.iPilgrim, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					szText = localText.getText("TXT_KEY_MINOR_EVENT_PILGRIM_ARRIVED", (pCity.getName(), gc.getMap().plot(tCoords[0],tCoords[1]).getPlotCity().getName()))
					CyInterface().addMessage(iPlayer, False, con.iDuration, szText, "AS2D_RELIGION_CONVERT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getUnitInfo(con.iPilgrim).getButton(), ColorTypes(con.iGreen), pCity.getX(), pCity.getY(), True, True)


	def onChangeWar(self, argsList):
		bIsWar, iTeam, iRivalTeam = argsList
		
		if iTeam >= con.iNumPlayers or iRivalTeam >= con.iNumPlayers: return
		
		bSameReligion = False
		if gc.getPlayer(iTeam).getStateReligion() == gc.getPlayer(iRivalTeam).getStateReligion():
			bSameReligion = True
		
		# when war is declared on a brother in faith, reduce piety by one-fourth of victim's piety
		if bSameReligion and bIsWar and not utils.isAVassal(iTeam):
			iRivalPiety = sd.getPiety(iRivalTeam)
			if iRivalPiety >= con.iFavorLevel_Apostate:
				iPenalty = iRivalPiety / 4
				# double penalty for being the Commander of the Faithful
				if gc.getTeam(iTeam).getProjectCount(con.iCaliph): 
					iPenalty *= 2
				# +50% penalty for attacking the Protector or Commander...
				if gc.getTeam(iRivalTeam).getProjectCount(con.iProtector) or gc.getTeam(iRivalTeam).getProjectCount(con.iCaliph): 
					iPenalty *= 3
					iPenalty /= 2
				self.changePiety(iTeam, -iPenalty)


	def onCityRazed(self, argsList):
		city, iPlayer = argsList
		
		if iPlayer >= con.iNumPlayers: return
		
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		
		# huge piety loss for killing brothers in faith
		if city.isHasReligion(iStateReligion):
			iPenalty = city.getPopulation() * 2 + 10
			if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).getProjectCount(con.iCaliph):
				iPenalty *= 3
				iPenalty /= 2
			self.changePiety(iPlayer, -iPenalty)
			# small bonus for razing infidel cities
		elif city.getReligionCount() > 0:
			if city.getReligionCount() == 2 and iStateReligion in [con.iCatholicism, con.iOrthodoxy] and (city.isHasReligion(con.iOrthodoxy) or city.isHasReligion(con.iCatholicism)):
				pass
			else:
				sd.setPiety(iPlayer, sd.getPiety(iPlayer) + 1)
		
		# apply diplomatic penalty
		for iReligion in range(con.iNumReligions):
			if city.isHasReligion(iReligion):
				for iLoopPlayer in range(con.iNumPlayers):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if iLoopPlayer != iPlayer and pLoopPlayer.isAlive() and pLoopPlayer.getStateReligion() == iReligion:
						pLoopPlayer.AI_changeAttitudeExtra(iPlayer, -1)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		pNewOwner = gc.getPlayer(iNewOwner)
		iStateReligion = pNewOwner.getStateReligion()
		
		# Seljuks spread Islam in Anatolia
		iGameTurn = gc.getGame().getGameTurn()
		if iNewOwner == con.iBarbarian and iGameTurn >= getTurnForYear(1058) and iGameTurn < getTurnForYear(1070):
			if city.plot().getRegionID() in [con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond, con.rVaspurakan]:
				if bConquest and not city.isHasReligion(con.iSunni):
					city.setHasReligion(con.iSunni, True, True, True)
		
		# Make sure stupid AI civs don't switch religions if they capture their first city
		if bConquest and pNewOwner.getNumCities() <= 1 and not pNewOwner.isHuman() and iStateReligion > 0:
			if not city.isHasReligion(iStateReligion):
				city.setHasReligion(iStateReligion, True, True, True)


	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner, city, bMassacre = argsList
		
		pOwner = gc.getPlayer(iOwner)
		iStateReligion = pOwner.getStateReligion()
		
		# UP: Ghorids - Zeal
		if iOwner == con.iGhorids:
			if iStateReligion > 0 and not city.isHasReligion(iStateReligion):
				city.setHasReligion(iStateReligion, True, True, True)
				# +2 piety bonus
				self.changePiety(iOwner, 2)
				# +3 bonus from Minaret of Jam
				if iStateReligion == con.iSunni or iStateReligion == con.iShia:
					apCityList = PyPlayer(iOwner).getCityList()
					for pCity in apCityList:
						if pCity.getNumBuilding(con.iMinaretOfJam):
							self.changePiety(iOwner, 3)
							break
		
		# massacre the disbelievers
		if bMassacre and city.getReligionCount() > 0:
			
			# remove religions and count the loot
			iNumOldReligions = city.getReligionCount()
			iLootModifier = 2 * city.getPopulation() / city.getReligionCount() + 1
			iLoot = 0
			
			if iOwner == con.iBarbarian or pOwner.getStateReligion() == -1:
				if utils.getYear() < 1020:
					lReligions = con.tPersecutionOrder[con.iShia] # Shia dynasties
				elif utils.getYear() < 1215:
					lReligions = con.tPersecutionOrder[con.iSunni] # Turks
				elif utils.getYear() < 1300:
					lReligions = con.tPersecutionOrder[con.iBuddhism] # Mongols
				else:
					lReligions = con.tPersecutionOrder[con.iSunni] # Turks
			else:
				lReligions = con.tPersecutionOrder[pOwner.getStateReligion()]
				
			for iReligion in lReligions:
				if city.isHasReligion(iReligion) and iReligion != pOwner.getStateReligion() and not city.isHolyCityByType(iReligion):
					if iReligion == con.iCatholicism and pOwner.getStateReligion() == con.iOrthodoxy: 
						continue
					if iReligion == con.iOrthodoxy and pOwner.getStateReligion() == con.iCatholicism: 
						continue
					iTempLoot = 2
					iTempLoot += iLootModifier
					for iBuildingLoop in range(gc.getNumBuildingInfos()):
						if iBuildingLoop < con.iPlague:
							if city.getNumRealBuilding(iBuildingLoop):
								if gc.getBuildingInfo(iBuildingLoop).getPrereqReligion() == iReligion:
									city.setNumRealBuilding(iBuildingLoop, 0)
									iTempLoot += iLootModifier
					if iReligion == con.iJudaism:
						iTempLoot = iTempLoot*3/2
					iLoot += iTempLoot
					
					city.setHasReligion(iReligion, False, False, False)
					sd.setPiety(iOwner, sd.getPiety(iOwner) + 1)
					city.changeHurryAngerTimer(city.flatHurryAngerLength()/2)
					
					# apply diplomatic penalty
					for iLoopPlayer in range(con.iNumPlayers):
						pLoopPlayer = gc.getPlayer(iLoopPlayer)
						if pLoopPlayer.isAlive() and iLoopPlayer != iOwner:
							if pLoopPlayer.getStateReligion() == iReligion:
								pLoopPlayer.AI_changeAttitudeExtra(iOwner, -1)
					
					# Barbarians remove just 1 religion
					if iOwner == con.iBarbarian:
						break
			
			# proceed only if at least one religion was removed
			if city.getReligionCount() < iNumOldReligions:
				iPopulationMassacred = 0
				if city.getPopulation() > 1:
					iPopulationMassacred = city.getPopulation() * (iNumOldReligions - city.getReligionCount()) / iNumOldReligions
					iPopulationMassacred = min(iPopulationMassacred, city.getPopulation()/2)
					city.changePopulation(-iPopulationMassacred)
				
				iLoot = iLoot/2 + gc.getGame().getSorenRandNum(iLoot/2, 'random loot')
				if iOwner == con.iGhaznavids: # Ghaznavid UP
					iLoot *= 2
				pOwner.changeGold(iLoot)
				
				iHuman = utils.getHumanID()
				if iOwner == iHuman:
					CyInterface().addMessage(iHuman, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_MASSACRE", (city.getName(), iLoot)), "AS2D_COMBAT", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, ColorTypes(con.iGreen), -1, -1, False, False)
				elif city.isRevealed(iHuman, False):
					CyInterface().addMessage(iHuman, False, con.iDuration, localText.getText("TXT_KEY_MESSAGE_MASSACRE_OTHER", (pOwner.getCivilizationAdjectiveKey(), city.getName())), "AS2D_COMBAT", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, ColorTypes(con.iRed), -1, -1, False, False)
				
				return max(0, iPopulationMassacred)


	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		
		# piety change for missionary activity
		if bSuccess:
			iPlayer = pUnit.getOwner()
			if iPlayer >= con.iNumPlayers: return
			iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
			if iReligion == iStateReligion:
				# +2 bonus for spreaing state religion
				self.changePiety(iPlayer, 2)
				# +3 bonus from Minaret of Jam
				if iStateReligion == con.iSunni or iStateReligion == con.iShia:
					apCityList = PyPlayer(iPlayer).getCityList()
					for pCity in apCityList:
						if pCity.getNumBuilding(con.iMinaretOfJam):
							self.changePiety(iPlayer, 3)
							break
			else:
				# -5 penalty for spreading non-state religion
				self.changePiety(iPlayer, -5) 


	# Some stuff from Charlemagne mod
	def doPietyEffects(self, iPlayer):
		
		pPlayer = gc.getPlayer(iPlayer)
		iPiety = sd.getPiety(iPlayer)
		iFavorLevel = utils.getFavorLevel(iPlayer)
		
		if iPiety < 0 or pPlayer.getStateReligion() < 0: return
		
		# stability bonus/penalty is in Stability.py
		
		# Loop through all of this player's cities
		apCityList = PyPlayer(iPlayer).getCityList()
		for pyCity in apCityList:
			pCity = pyCity.GetCy()
			
			# Reset extra happiness to 0
			pCity.changeExtraHappiness(-pCity.getExtraHappiness())
			
			if not iPlayer == con.iBuyids:

				# Apply Happiness bonus
				pCity.changeExtraHappiness(con.tFavorLevelsHappinessBonus[iFavorLevel])

				# Buyid UP - Happiness in Iranian Cities
			elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rHormuz, con.rFars, con.rKerman, con.rLuristan, con.rKurdistan, con.rYazd, con.rWesternKhorasan, con.rJibal, con.rMazandaran]:
				pCity.changeExtraHappiness(con.tFavorLevelsHappinessBonus[iFavorLevel] + 2)
			else:
				pCity.changeExtraHappiness(con.tFavorLevelsHappinessBonus[iFavorLevel])

	def onUnitBuilt(self, argsList):
		'Unit Completed'
		pCity, pUnit = argsList
		
		iPlayer = pCity.getOwner()
		if iPlayer >= con.iNumPlayers: return
		
		# blessed promotion for pious players
		iFavor = utils.getFavorLevel(iPlayer)
		if iFavor > 0:
			if con.tFavorLevelsBlessing[iFavor] > 0:
				if pUnit.getDomainType() == DomainTypes.DOMAIN_LAND:
					if pUnit.baseCombatStr() > 0:
						pUnit.setHasPromotion(con.iBlessed, True)


	def checkAIHolyWar(self, iPlayer):
		"""Determine whether it is a good idea to call for a holy war, and against whom.
		If a good target is found, call the war."""
		
		pPlayer = gc.getPlayer(iPlayer)
		targetList = utils.getHolyWarTargets(iPlayer)
		iBestWeight = -1
		iBestTarget = -1
		for tTarget in targetList:
			pTarget = gc.getPlayer(tTarget[0])
			iWeight = tTarget[2]
			iWeight = iWeight * pTarget.getPower() / pPlayer.getPower()
			civList = utils.getHolyWarParticipants(iPlayer, tTarget[0])
			iWeight *= len(civList)
			if iWeight > iBestWeight:
				iBestWeight = iWeight
				iBestTarget = tTarget[0]
		
		if gc.getGame().getSorenRandNum(100, 'Jihad!') < iBestWeight:
			sd.setVal('iLastHolyWarTurn', gc.getGame().getGameTurn())
			sd.setVal('iHolyWarTarget', iBestTarget)
			if utils.isActive(utils.getHumanID()):
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, localText.getText("TXT_KEY_HOLY_WAR_CALLED", (pPlayer.getName(), gc.getPlayer(iBestTarget).getCivilizationDescription(0))), "AS2D_DECLAREWAR", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
