from CvPythonExtensions import *
import CvUtil
import CvEventManager
import PyHelpers

from StoredData import sd
from RFCUtils import utils
import Consts as con
import Resources
import Religions
import CityNameManager
import RiseAndFall
import Barbs
import AIWars
import Victory
import Stability
import Plague
import Communications
import DynamicCivs
import Companies
import Titles
import DataLoader
import UnitArtStyler
import BugTimer

gc = CyGlobalContext()

if gc.getMap().getMapScriptName(): # Baldyr: loads stored data on module reload
	sd.load()

PyPlayer = PyHelpers.PyPlayer
PyGame = PyHelpers.PyGame()
PyInfo = PyHelpers.PyInfo

iNumPlayers = con.iNumPlayers

class CvRFCEventHandler:

	def __init__(self, eventManager):
		
		self.lastRegionID = -1
		self.bStabilityOverlay = False
		self.EventKeyDown = 6
		self.EventKeyUp = 7
		self.eventManager = eventManager
		
		# initialize base class
		eventManager.addEventHandler("GameStart", self.onGameStart)
		eventManager.addEventHandler("OnLoad", self.onLoadGame)
		eventManager.addEventHandler("OnPreSave", self.onPreSave)
		eventManager.addEventHandler("BeginGameTurn", self.onBeginGameTurn)
		eventManager.addEventHandler("EndGameTurn", self.onEndGameTurn)
		eventManager.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn)
		eventManager.addEventHandler("EndPlayerTurn", self.onEndPlayerTurn)
		eventManager.addEventHandler("firstContact", self.onFirstContact)
		eventManager.addEventHandler("cityAcquired", self.onCityAcquired)
		eventManager.addEventHandler("cityAcquiredAndKept", self.onCityAcquiredAndKept)
		eventManager.addEventHandler("cityRazed", self.onCityRazed)
		eventManager.addEventHandler("cityBuilt", self.onCityBuilt)
		eventManager.addEventHandler("combatResult", self.onCombatResult)
		eventManager.addEventHandler("buildingBuilt", self.onBuildingBuilt)
		eventManager.addEventHandler("projectBuilt", self.onProjectBuilt)
		eventManager.addEventHandler("techAcquired", self.onTechAcquired)
		eventManager.addEventHandler("religionSpread", self.onReligionSpread)
		eventManager.addEventHandler("unitSpreadReligionAttempt", self.onUnitSpreadReligionAttempt)
		eventManager.addEventHandler("playerChangeStateReligion", self.onPlayerChangeStateReligion)
		eventManager.addEventHandler("vassalState", self.onVassalState)
		eventManager.addEventHandler("changeWar", self.onChangeWar)
		eventManager.addEventHandler("unitBuilt", self.onUnitBuilt)
		eventManager.addEventHandler("revolution", self.onRevolution)
		eventManager.addEventHandler("setPlayerAlive", self.onSetPlayerAlive)
		eventManager.addEventHandler("greatPersonBorn", self.onGreatPersonBorn)
		eventManager.addEventHandler("kbdEvent", self.onKbdEvent)		
		
		self.rnf = RiseAndFall.RiseAndFall()
		self.cnm = CityNameManager.CityNameManager()
		self.res = Resources.Resources()
		self.rel = Religions.Religions()
		self.barb = Barbs.Barbs()
		self.aiw = AIWars.AIWars()
		self.vic = Victory.Victory()
		self.sta = Stability.Stability()
		self.pla = Plague.Plague()
		self.com = Communications.Communications()
		self.dc = DynamicCivs.DynamicCivs()
		self.corp = Companies.Companies()
		self.tit = Titles.Titles()


	def onGameStart(self, argsList):
		'Called at the start of the game'
		
		DataLoader.setup()
		sd.setup()
		self.rnf.setup()
		self.sta.setup()
		self.aiw.setup()
		self.pla.setup()
		self.dc.setup()
		self.rel.setup()
		self.tit.setup()
		sd.save()
		
		# Georgian UP: Restoration
		gc.getPlayer(con.iGeorgia).changeGoldenAgeModifier(100)
		
		# set relations
		gc.getPlayer(con.iTimurids).AI_changeAttitudeExtra(con.iMughals, 2)
		gc.getPlayer(con.iAbbasids).AI_changeAttitudeExtra(con.iMakuria, 2)
		gc.getPlayer(con.iMakuria).AI_changeAttitudeExtra(con.iAbbasids, 1)
		
		# update unit art styles of independents
		for iLoopPlayer in range(con.iIndependent, con.iIndependent4 + 1):
			unitList = PyPlayer(iLoopPlayer).getUnitList()
			for pUnit in unitList:
				UnitArtStyler.updateUnitArt(pUnit)

		return 0


	def onPreSave(self, argsList):
		'called before a game is actually saved'
		sd.save() # pickle & save script data


	def onLoadGame(self, argsList):
		sd.load() # load & unpickle script data
		return 0


	def onBeginGameTurn(self, argsList):
		'Called at the beginning of the end of each turn'
		iGameTurn = argsList[0]
		
		# timer = BugTimer.Timer('onBeginGameTurn')
		
		# print ("iGameTurn", iGameTurn)
		# self.printDebug(iGameTurn)
		
		self.rnf.checkTurn(iGameTurn)
		self.res.checkTurn(iGameTurn)
		self.barb.checkTurn(iGameTurn)
		self.rel.checkTurn(iGameTurn)
		self.sta.checkTurn(iGameTurn)
		self.aiw.checkTurn(iGameTurn)
		self.pla.checkTurn(iGameTurn)
		self.com.checkTurn(iGameTurn)
		self.corp.checkTurn(iGameTurn)
		
		# Fourth Crusade
		pByzantium = gc.getPlayer(con.iByzantium)
		if sd.getVal('iFourthCrusadeTurn'):
			if iGameTurn == sd.getVal('iFourthCrusadeTurn') and pByzantium.isAlive():
				sd.delVal('iFourthCrusadeTurn')
				city = gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getPlotCity()
				pByzantium.initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_FOURTH_CRUSADE_REVOLT"), True, city.getID(), city.getX(), city.getY(), -1, -1, -1, -1, -1, -1, "")
		if sd.getVal('iFourthCrusadeYear'):
			if iGameTurn == getTurnForYear(sd.getVal('iFourthCrusadeYear')) and pByzantium.isAlive():
				pByzantium.trigger(gc.getInfoTypeForString("EVENTTRIGGER_FOURTH_CRUSADE"))
		
		# Refugees
		if sd.getVal('tRazedCityData'):
			map = CyMap()
			tRazedCityData = sd.getVal('tRazedCityData') #(city.getNameKey(), city.getX(), city.getY())
			sd.delVal('tRazedCityData')
			cityList = []
			for x in range(tRazedCityData[0]-12, tRazedCityData[0]+12, 1):
				if x >= 0 and x < map.getGridWidth():
					for y in range(tRazedCityData[1]-12, tRazedCityData[1]+12, 1):
						if y >= 0 and y < map.getGridHeight():
							plot = map.plot(x, y)
							if plot.isCity():
								targetCity = plot.getPlotCity()
								cityList.append(targetCity)
			if cityList:
				targetCity = cityList[gc.getGame().getSorenRandNum(len(cityList), 'Random city')]
				gc.getPlayer(targetCity.getOwner()).initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_REFUGEES"), True, targetCity.getID(), targetCity.getX(), targetCity.getY(), -1, -1, -1, -1, -1, -1, tRazedCityData[2])
		
		# AI "Luck": 0 = no effect, 5 = small, 10 = medium, 15 = high, 20 = silly
		# iLuckFactor = 10
		
		# Fatimids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iFatimids]):
			# gc.getPlayer(con.iFatimids).setLuck(20 * iLuckFactor)
		# if iGameTurn == getTurnForYear(100):
			# gc.getPlayer(con.iFatimids).setLuck(0)
		# if iGameTurn == getTurnForYear(1050):
			# gc.getPlayer(con.iFatimids).setLuck(-10 * iLuckFactor)
		
		# Ghaznavids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iGhaznavids]):
			# gc.getPlayer(con.iGhaznavids).setLuck(10 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1140):
			# gc.getPlayer(con.iGhaznavids).setLuck(-10 * iLuckFactor)
		
		# Rum
		# if iGameTurn == getTurnForYear(con.tBirth[con.iRum]):
			# gc.getPlayer(con.iRum).setLuck(10 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1180):
			# gc.getPlayer(con.iRum).setLuck(-5 * iLuckFactor)
		
		# Ghorids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iGhorids]):
			# gc.getPlayer(con.iGhorids).setLuck(25 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1206):
			# gc.getPlayer(con.iGhorids).setLuck(0)
		
		# Ayyubids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iAyyubids]):
			# gc.getPlayer(con.iAyyubids).setLuck(10 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1220):
			# gc.getPlayer(con.iAyyubids).setLuck(-10 * iLuckFactor)
		
		# Khwarezm
		# if iGameTurn == getTurnForYear(con.tBirth[con.iKhwarezm]):
			# gc.getPlayer(con.iKhwarezm).setLuck(25 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1200):
			# gc.getPlayer(con.iKhwarezm).setLuck(-10 * iLuckFactor)
		
		# Timurids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iTimurids]):
			# gc.getPlayer(con.iTimurids).setLuck(30 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1447):
			# gc.getPlayer(con.iTimurids).setLuck(0)
		# if iGameTurn == getTurnForYear(1500):
			# gc.getPlayer(con.iTimurids).setLuck(-10 * iLuckFactor)
		
		# Ottomans
		# if iGameTurn == getTurnForYear(con.tBirth[con.iOttomans]):
			# gc.getPlayer(con.iOttomans).setLuck(15 * iLuckFactor)
		# if iGameTurn == getTurnForYear(con.tBirth[con.iOttomans]+100):
			# gc.getPlayer(con.iOttomans).setLuck(25 * iLuckFactor)
		# if iGameTurn == getTurnForYear(con.tBirth[con.iOttomans]+153):
			# gc.getPlayer(con.iOttomans).setLuck(10 * iLuckFactor)
		
		# Safavids & Ak Koyunlu
		# if iGameTurn == getTurnForYear(con.tBirth[con.iSafavids]):
			# gc.getPlayer(con.iSafavids).setLuck(25 * iLuckFactor)
			# gc.getPlayer(con.iAkKoyunlu).setLuck(-10 * iLuckFactor)
		# if iGameTurn == getTurnForYear(con.tBirth[con.iSafavids]+25):
			# gc.getPlayer(con.iSafavids).setLuck(10 * iLuckFactor)
		
		# Mughals
		# if iGameTurn == getTurnForYear(con.tBirth[con.iMughals]):
			# gc.getPlayer(con.iMughals).setLuck(25 * iLuckFactor)
		# if iGameTurn == getTurnForYear(con.tBirth[con.iMughals]+25):
			# gc.getPlayer(con.iMughals).setLuck(10 * iLuckFactor)
		
		# Mamluks
		# if iGameTurn == getTurnForYear(1400):
			# gc.getPlayer(con.iMamluks).setLuck(-5 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1500):
			# gc.getPlayer(con.iMamluks).setLuck(-10 * iLuckFactor)
		
		# Buyids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iSeljuks]):
			# gc.getPlayer(con.iBuyids).setLuck(-10 * iLuckFactor)
		
		# Abbasids
		# if iGameTurn == getTurnForYear(1225):
			# gc.getPlayer(con.iAbbasids).setLuck(-10 * iLuckFactor)
		
		# Georgia
		# if iGameTurn == getTurnForYear(1450):
			# gc.getPlayer(con.iAbbasids).setLuck(-10 * iLuckFactor)
		
		# Armenia
		# if iGameTurn == getTurnForYear(1375):
			# gc.getPlayer(con.iAbbasids).setLuck(-10 * iLuckFactor)
		
		# Seljuks
		# if iGameTurn == getTurnForYear(1180):
			# gc.getPlayer(con.iSeljuks).setLuck(-10 * iLuckFactor)
		
		# Crusaders
		# if iGameTurn == getTurnForYear(con.tBirth[con.iAntioch]):
			# gc.getPlayer(con.iAntioch).setLuck(5 * iLuckFactor)
		# if iGameTurn == getTurnForYear(con.tBirth[con.iCrusaders]):
			# gc.getPlayer(con.iCrusaders).setLuck(5 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1209):
			# gc.getPlayer(con.iAntioch).setLuck(0)
			# gc.getPlayer(con.iCrusaders).setLuck(0)
		# if iGameTurn == getTurnForYear(1280):
			# gc.getPlayer(con.iAntioch).setLuck(-10 * iLuckFactor)
			# gc.getPlayer(con.iCrusaders).setLuck(-10 * iLuckFactor)
		
		# Zengids
		# if iGameTurn == getTurnForYear(con.tBirth[con.iZengids]):
			# gc.getPlayer(con.iZengids).setLuck(10 * iLuckFactor)
		# if iGameTurn == getTurnForYear(1140):
			# gc.getPlayer(con.iZengids).setLuck(0)
		# if iGameTurn == getTurnForYear(1240):
			# gc.getPlayer(con.iZengids).setLuck(-10 * iLuckFactor)
		
		# timer.log()
		
		# GOLD DEBUG
		
		# goldList = sd.getVal("goldList")
		
		# if goldList:
			# for i in range(iNumPlayers):
				# if gc.getPlayer(i).getGold() > goldList[i] + 400:
					# utils.echo("ALERT! %s's gold skyrockets!" %(gc.getPlayer(i).getCivilizationShortDescription(0)))
		
		# goldList = []
		# for i in range(iNumPlayers):
			# goldList.append(gc.getPlayer(i).getGold())
		
		# sd.setVal("goldList", goldList)


	def onEndGameTurn(self, argsList):
		'Called at the end of the end of each turn'
		iGameTurn = argsList[0]
		
		self.sta.checkImplosion(iGameTurn)


	def onBeginPlayerTurn(self, argsList):
		'Called at the beginning of a players turn'
		iGameTurn, iPlayer = argsList
		
		# timer = BugTimer.Timer('onBeginPlayerTurn')
		
		pPlayer = gc.getPlayer(iPlayer)
		
		if self.rnf.getDeleteMode(0) != -1:
			self.rnf.deleteMode(iPlayer)
		
		self.pla.checkPlayerTurn(iGameTurn, iPlayer)
		
		if pPlayer.isAlive() and iPlayer < iNumPlayers:
			self.vic.checkPlayerTurn(iGameTurn, iPlayer)
			sd.setLastTurnAlive(iPlayer, iGameTurn)
			if pPlayer.getNumCities() > 0:
				self.sta.updateBaseStability(iGameTurn, iPlayer)
		
		# timer.log()

		# Zengid UP - extra Gold for crusader cities
		if iPlayer == con.iZengids:

			iGold = 0
			iFrankishCities = gc.getPlayer(con.iCrusaders).getNumCities()
			iNormanCities = gc.getPlayer(con.iAntioch).getNumCities()
			iGold = 2*(iFrankishCities + iNormanCities)

			if iGold > 0:
				gc.getPlayer(con.iZengids).changeGold(iGold)
				ZENmessageUP = CyTranslator().getText("TXT_KEY_UP_ZEN3", ())
				CyInterface().addMessage(iPlayer, False, con.iDuration, (ZENmessageUP+str(iGold)), "", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, None, gc.getInfoTypeForString("COLOR_CYAN"), -1, -1, False, False);

		# trigger Buyid UP - see Religions
		if iPlayer == con.iBuyids:
			self.rel.doPietyEffects(iPlayer)

	def onEndPlayerTurn(self, argsList):
		'Called at the end of a players turn'
		iGameTurn, iPlayer = argsList


	def onFirstContact(self, argsList):
		'Contact'
		iTeamX,iHasMetTeamY = argsList


	def onBuildingBuilt(self, argsList):
		'Building Completed'
		city, iBuildingType = argsList
		
		iOwner = city.getOwner()
		if iOwner < iNumPlayers:
			self.sta.onBuildingBuilt(iOwner, iBuildingType, city)
			self.rel.onBuildingBuilt(iOwner, iBuildingType)
			self.vic.onBuildingBuilt(iOwner, iBuildingType, city)
		
		# Mevlana's Tomb
		if iBuildingType == con.iMevlanasTomb:
			if not city.isHasReligion(con.iSunni):
				city.setHasReligion(con.iSunni, True, True, True)
			if not city.isHasReligion(con.iShia):
				city.setHasReligion(con.iShia, True, True, True)
			if not city.isHasCorporation(con.iSufi):
				city.setHasCorporation(con.iSufi, True, True, True)
			sd.setVal('iMevlanaOwner', city.getOwner())
		
		# Ibn Battuta's Embassy
		if iBuildingType == con.iIbnBattuta:
			lRegions = [con.rPalestine, con.rLowerEgypt, con.rHejaz, con.rSinai, con.rRedSea, con.rMediterraneanSea, con.rThrace, con.rAsia, con.rLycia, con.rSyria, con.rNorthernSyria, con.rJordan, con.rPersianGulf, con.rMesopotamia, con.rPontus, con.rBithynia, con.rBlackSea, con.rLesserArmenia, con.rAzerbaijan, con.rJibal, con.rLuristan, con.rKurdistan, con.rAsuristan, con.rSistan, con.rBactria, con.rWesternKhorasan, con.rEasternKhorasan, con.rKhwarezm, con.rTaklaMakan, con.rSogd, con.rGujarat, con.rMaharashtra, con.rGoa, con.rUttarBharat, con.rGandhar, con.rGird, con.rMalwa, con.rPunjab, con.rYemen, con.rEdessa, con.rVaspurakan, con.rJazira, con.rArabianSea]
			utils.revealPlots(iOwner, utils.getRegionPlotList(lRegions, True))
		
		# Other wonders
		if iBuildingType == con.iTopkapiPalace:
			sd.setVal('iTopkapiOwner', city.getOwner())
		if iBuildingType == con.iIbnBattuta:
			sd.setVal('iIbnBattutaOwner', city.getOwner())

		# trigger Buyid UP - see Religions
		if iOwner == con.iBuyids:
			self.rel.doPietyEffects(iOwner)

	def onProjectBuilt(self, argsList):
		'Project Completed'
		pCity, iProjectType = argsList


	def onTechAcquired(self, argsList):
		'Tech Acquired'
		iTechType, iTeam, iPlayer, bAnnounce = argsList
		
		if iPlayer < iNumPlayers:
			self.vic.onTechAcquired(iTechType, iPlayer) # Ottomans
			self.res.onTechAcquired(iTechType)
			self.rel.onTechAcquired(iTechType, iPlayer)
			if gc.getPlayer(iPlayer).isAlive() and gc.getGame().getGameTurn() > getTurnForYear(con.tBirth[iPlayer]):
				self.sta.onTechAcquired(iTechType, iPlayer)
			# End of Georgian UP: Restoration
			if iPlayer == con.iGeorgia:
				if gc.getPlayer(iPlayer).getCurrentEra() > 1:
					gc.getPlayer(iPlayer).changeGoldenAgeModifier(-100)


	def onReligionSpread(self, argsList):
		'Religion Has Spread to a City'
		iReligion, iOwner, pSpreadCity = argsList


	def onCityBuilt(self, argsList):
		'City Built'
		city = argsList[0]
		
		iOwner = city.getOwner()
		player = gc.getPlayer(iOwner)
		
		self.cnm.assignName(city)
		self.tit.onCityBuilt(city)
		
		# Reveal hidden relics
		hiddenRelics = sd.getVal('hiddenRelics')
		bFound = False
		for i in hiddenRelics.keys():
			if hiddenRelics[i] == city.plot().getRegionID():
				if player.getStateReligion() in [gc.getBuildingInfo(i).getPrereqReligion(), gc.getBuildingInfo(i).getOrPrereqReligion()]:
					utils.makeUnit(con.relics[i][0], iOwner, (city.getX(), city.getY()), 1, UnitAITypes.UNITAI_MERCHANT)
					del hiddenRelics[i]
					bFound = True
		sd.setVal('hiddenRelics', hiddenRelics)
		if bFound:
			player.initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_RELIC_RECOVERED"), True, city.getID(), city.getX(), city.getY(), -1, -1, -1, -1, -1, -1, "")
		
		#Rhye - delete culture of barbs and minor civs to prevent weird unhappiness
		pCurrent = gc.getMap().plot(city.getX(), city.getY())
		for i in range(con.iNumTotalPlayers - iNumPlayers):
			iMinorCiv = i + iNumPlayers
			pCurrent.setCulture(iMinorCiv, 0, True)
		pCurrent.setCulture(con.iBarbarian, 0, True)
		
		if iOwner < iNumPlayers:
			utils.spreadMajorCulture(iOwner, city.getX(), city.getY())
			if player.getNumCities() < 2:
				player.AI_updateFoundValues(False); # fix for settler maps not updating after 1st city is founded

		# trigger Buyid UP - see Religions
		if iOwner == con.iBuyids:
			self.rel.doPietyEffects(iOwner)

		# create Portugal UB
		if iOwner == con.iPortugal:
			city.setNumRealBuilding(con.iMarineAcademy, True)

	def onCityRazed(self, argsList):
		'City Razed'
		city, iPlayer = argsList
		
		iPreviousOwner = city.getOwner()
		if iPreviousOwner == iPlayer and city.getPreviousOwner() != -1:
			iPreviousOwner = city.getPreviousOwner()
		
		self.sta.onCityRazed(iPreviousOwner)
		self.pla.onCityRazed(argsList)
		self.rel.onCityRazed(argsList)
		self.vic.onCityRazed(iPlayer) # Timurids
		
		# Crusades UP
		if iPreviousOwner < iNumPlayers:
			plot = gc.getMap().plot(city.getX(),city.getY())
			if plot.getRegionID() in utils.getCoreRegions(iPreviousOwner):
				sd.setHasLostCity(iPreviousOwner, True)
		
		# Patronage UP
		if iPlayer == con.iTimurids:
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.getNumCities() > 0:
				iCulture = city.getPopulation() * 40 + city.getCulture(iPreviousOwner) / 4
				capital = pPlayer.getCapitalCity()
				capital.changeCulture(iPlayer, iCulture, True)
				CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_PATRONAGE", (city.getName(), capital.getName(), iCulture)), "AS2D_CULTUREEXPANDS", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getCommerceInfo(CommerceTypes.COMMERCE_CULTURE).getButton(), ColorTypes(con.iWhite), capital.getX(), capital.getY(), True, True)
		
		# Wonders
		if city.getNumRealBuilding(con.iMevlanasTomb):
			sd.delVal('iMevlanaOwner')
		if city.getNumRealBuilding(con.iTopkapiPalace):
			sd.delVal('iTopkapiOwner')
		if city.getNumRealBuilding(con.iIbnBattuta):
			sd.delVal('iIbnBattutaOwner')
		
		# Refugees
		sd.setVal('tRazedCityData', (city.getX(), city.getY(), city.getNameKey()))

		# Bahmanid UP - create free Dakhanis in capital Part I
		if iPlayer == con.iBahmanids:
			pPlayer = gc.getPlayer(iPlayer)
			capital = pPlayer.getCapitalCity()
			if sd.getRazedByBahmanids() != sd.getSpawnByBahmanids():
				utils.makeUnit(con.iDakhani, con.iBahmanids, (capital.getX(), capital.getY()), 2*(sd.getRazedByBahmanids() - sd.getSpawnByBahmanids()), UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2,))
				sd.setSpawnByBahmanids(sd.getRazedByBahmanids())
				CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_BAH3", (city.getName(), )), "", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, None, gc.getInfoTypeForString("COLOR_CYAN"), -1, -1, False, False);

		# trigger Buyid UP - see Religions
		if iPlayer == con.iBuyids:
			self.rel.doPietyEffects(iPlayer)

	def onCityAcquired(self, argsList):
		'City Acquired'
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		pNewOwner = gc.getPlayer(iNewOwner)
		
		# timer = BugTimer.Timer('onCityAcquired')
		
		self.cnm.renameCity(city, iNewOwner)
		self.rnf.checkCapitalsOnCapture(city, iNewOwner) # edead: free capital move for the AI
		
		if iNewOwner < iNumPlayers:
			utils.spreadMajorCulture(iNewOwner, city.getX(), city.getY())
			self.pla.onCityAcquired(iPreviousOwner, iNewOwner, city)
			self.dc.onCityAcquired(argsList)
		
		self.sta.onCityAcquired(iPreviousOwner, iNewOwner, city, bConquest, bTrade)
		self.rel.onCityAcquired(argsList)
		
		# Crusades UP
		if iPreviousOwner < iNumPlayers:
			plot = gc.getMap().plot(city.getX(),city.getY())
			if plot.getRegionID() in utils.getCoreRegions(iPreviousOwner):
				sd.setHasLostCity(iPreviousOwner, True)
		
		self.vic.onCityAcquired(argsList)
		self.corp.onCityAcquired(argsList)
		self.tit.onCityAcquired(argsList)
		
		# Move the palace to historical backup capital
		if iPreviousOwner < iNumPlayers:
			if (city.getX(), city.getY()) == con.tCapitals[iPreviousOwner]:
				self.rnf.moveCapital(con.tBackupCapitals[iPreviousOwner], iPreviousOwner, True)
		
		# Wonders
		if city.getNumRealBuilding(con.iMevlanasTomb):
			sd.setVal('iMevlanaOwner', iNewOwner)
		if city.getNumRealBuilding(con.iTopkapiPalace):
			sd.setVal('iTopkapiOwner', iNewOwner)
		if city.getNumRealBuilding(con.iIbnBattuta):
			sd.setVal('iIbnBattutaOwner', iNewOwner)
		if city.getNumRealBuilding(con.iHouseOfWisdom):
			if iNewOwner == con.iBarbarian and utils.getYear() > 1240 and utils.getYear() < 1300:
				for x in range(city.getX()-1, city.getX()+2):
					for y in range(city.getY()-1, city.getY()+2):
						plot = gc.getMap().plot(x, y)
						for i in range(plot.getNumUnits()):
							unit = plot.getUnit(0)
							if plot.getUnit(0).getUnitType() == con.iMongolHorseArcher and plot.getUnit(0).getOwner() == con.iBarbarian:
								city.setNumRealBuilding(con.iHouseOfWisdom, 0)
								if utils.isActive(utils.getHumanID()):
									CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_EVENT_HOUSE_OF_WISDOM_DESTROYED", (city.getName(), )), "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, None, gc.getInfoTypeForString("COLOR_WHITE"), -1, -1, False, False);
								return
		
		# Mongol massacre of GPs
		if city.plot().getRegionID() in [con.rMesopotamia, con.rAsuristan, con.rJazira, con.rKhwarezm]:
			if iNewOwner == con.iBarbarian and utils.getYear() > 1220 and utils.getYear() < 1300:
				iPop = city.getPopulation()
				if iPop > 2:
					city.changePopulation(-iPop / 3)
				for iSpecialistType in range(7,14):
					for iSpecialist in range(city.getFreeSpecialistCount(iSpecialistType)):
						if gc.getGame().getSorenRandNum(100, 'Chance to kill a GP') < 60:
							city.changeFreeSpecialistCount(iSpecialistType, -1)
		
		# Reveal hidden relics
		hiddenRelics = sd.getVal('hiddenRelics')
		bFound = False
		for i in hiddenRelics.keys():
			if hiddenRelics[i] == city.plot().getRegionID():
				if city.plot().getRegionID() == con.rPalestine and city.getX() != con.tJerusalem[0] and city.getY() != con.tJerusalem[1]:
					continue
				if pNewOwner.getStateReligion() in [gc.getBuildingInfo(i).getPrereqReligion(), gc.getBuildingInfo(i).getOrPrereqReligion()]:
					utils.makeUnit(con.relics[i][0], iNewOwner, (city.getX(), city.getY()), 1, UnitAITypes.UNITAI_MERCHANT)
					del hiddenRelics[i]
					bFound = True
		if bFound:
			sd.setVal('hiddenRelics', hiddenRelics)
			pNewOwner.initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_RELIC_RECOVERED"), True, city.getID(), city.getX(), city.getY(), -1, -1, -1, -1, -1, -1, "")
		
		# Capture relics
		bFoundAgain = False
		if iNewOwner < iNumPlayers:
			for i in con.relics.keys():
				if city.getNumRealBuilding(i) > 0:
					city.setNumRealBuilding(i, 0)
					utils.makeUnit(con.relics[i][0], iNewOwner, (city.getX(), city.getY()), 1, UnitAITypes.UNITAI_MERCHANT)
					bFoundAgain = True
		if bFoundAgain and not bFound:
			pNewOwner.initTriggeredData(gc.getInfoTypeForString("EVENTTRIGGER_RELIC_RECOVERED"), True, city.getID(), city.getX(), city.getY(), -1, -1, -1, -1, -1, -1, "")
		
		# Timurid UP
		sd.setVal('iPreviousOwner', iPreviousOwner)
		
		# timer.log()
		
		# if (bConquest):
			# if (iPreviousOwner == utils.getHumanID() and iNewOwner != con.iBarbarian):
				# self.rnf.collapseHuman(iPreviousOwner, city, iNewOwner)
			# if (self.rnf.getExileData(0) == city.getX() and self.rnf.getExileData(1) == city.getY()):
				# if (iNewOwner == utils.getHumanID() and self.rnf.getExileData(2) != -1):
					# self.rnf.escape(city)

		# trigger Buyid UP - see Religions
		if iNewOwner == con.iBuyids:
			self.rel.doPietyEffects(iNewOwner)

		# create Portugal UB
		if iNewOwner == con.iPortugal:
			city.setNumRealBuilding(con.iMarineAcademy, True)

	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner,city,bMassacre = argsList
		
		iVictims = self.rel.onCityAcquiredAndKept(argsList) # massacre
		self.vic.onCityAcquiredAndKept(argsList) # Timurids
		
		# Patronage UP
		if iOwner == con.iTimurids and bMassacre and iVictims > 0:
			pPlayer = gc.getPlayer(iOwner)
			iPreviousOwner = sd.getVal('iPreviousOwner')
			if pPlayer.getNumCities() > 0 and iPreviousOwner:
				iCulture = iVictims * 40 + city.getCulture(iPreviousOwner) / 8
				city.changeCulture(iPreviousOwner, -(city.getCulture(iPreviousOwner) / 8), True)
				capital = pPlayer.getCapitalCity()
				capital.changeCulture(iOwner, iCulture, True)
				CyInterface().addMessage(iOwner, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_PATRONAGE", (city.getName(), capital.getName(), iCulture)), "AS2D_CULTUREEXPANDS", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getCommerceInfo(CommerceTypes.COMMERCE_CULTURE).getButton(), ColorTypes(con.iWhite), capital.getX(), capital.getY(), True, True)
		
		# Bahmanid UP - create free Dakhanis in capital Part II
		if iOwner == con.iBahmanids:
			pPlayer = gc.getPlayer(iOwner)
			capital = pPlayer.getCapitalCity()
			if sd.getRazedByBahmanids() != sd.getSpawnByBahmanids():
				utils.makeUnit(con.iDakhani, con.iBahmanids, (capital.getX(), capital.getY()), 2*(sd.getRazedByBahmanids() - sd.getSpawnByBahmanids()))
				sd.setSpawnByBahmanids(sd.getRazedByBahmanids())
				CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_BAH3", (city.getName(), )), "", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, None, gc.getInfoTypeForString("COLOR_WHITE"), -1, -1, False, False);

		# trigger Buyid UP - see Religions
		if iOwner == con.iBuyids:
			self.rel.doPietyEffects(iOwner)

		# create Portugal UB
		if iOwner == con.iPortugal:
			city.setNumRealBuilding(con.iMarineAcademy, True)

	def onCombatResult(self, argsList):
		pWinningUnit, pLosingUnit = argsList
		
		self.vic.onCombatResult(argsList) # Mamluks
		self.sta.onCombatResult(argsList)
		self.rnf.immuneMode(argsList)


	def onPlayerChangeStateReligion(self, argsList):
		'Player changes his state religion'
		iPlayer, iNewReligion, iOldReligion = argsList
		
		if iPlayer < iNumPlayers:
			self.rel.onPlayerChangeStateReligion(argsList)
			self.dc.onPlayerChangeStateReligion(argsList)
			self.corp.onPlayerChangeStateReligion(argsList)
			self.tit.onPlayerChangeStateReligion(argsList)
			self.vic.onPlayerChangeStateReligion(argsList)


	def onVassalState(self, argsList):
		'Vassal State'
		iMaster, iVassal, bVassal = argsList
		
		self.dc.onVassalState(argsList)


	def onChangeWar(self, argsList):
		'War Status Changes'
		bIsWar, iTeam, iRivalTeam = argsList
		
		if bIsWar and iTeam < iNumPlayers and iRivalTeam < iNumPlayers:
			self.rel.onChangeWar(argsList)


	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		
		self.rel.onUnitSpreadReligionAttempt(argsList)
		self.vic.onUnitSpreadReligionAttempt(argsList) # Oman


	def onUnitBuilt(self, argsList):
		'Unit Completed'
		pCity, pUnit = argsList
		
		iPlayer = pUnit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		iUnitType = pUnit.getUnitType()
		
		self.rel.onUnitBuilt(argsList)
		
		# Slave Barracks (+4 XP for Ghulams)
		if pCity.getNumRealBuilding(con.iSlaveBarracks) > 0:
			if iUnitType == con.iGhulamLancer or iUnitType == con.iGhulamHorseArcher or iUnitType == con.iGhulamGuard:
				pUnit.setExperience(pUnit.getExperience() + 4, -1)
		
		# Arabian Sheikh (+2 XP)
		if iUnitType == con.iArabianSheikh:
			pUnit.setExperience(pUnit.getExperience() + 2, -1)
		
		# Update UnitArtStyle for independents
		if iPlayer >= con.iNumPlayers and iPlayer != con.iBarbarian:
			UnitArtStyler.updateUnitArt(pUnit)
		

	def onRevolution(self, argsList):
		'Called at the start of a revolution'
		iPlayer = argsList[0]
		
		if iPlayer < iNumPlayers:
			self.dc.onRevolution(iPlayer)


	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayer, bNewValue = argsList
		
		if iPlayer < iNumPlayers:
			self.tit.onSetPlayerAlive(argsList)
			self.res.onSetPlayerAlive(argsList)


	def onGreatPersonBorn(self, argsList):
		'Unit Promoted'
		pUnit, iPlayer, pCity = argsList
		
		self.vic.onGreatPersonBorn(argsList) # Chauhan


	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'
		
		eventType, key, mx, my, px, py = argsList
		
		# Rhye: RFC debug
		iHuman = utils.getHumanID()
		
		if eventType == self.EventKeyDown and key == InputTypes.KB_N and self.eventManager.bAlt:
			print("ALT-N")
			self.printStabilityDebug()
		
		if eventType == self.EventKeyDown and key == InputTypes.KB_C and self.eventManager.bAlt and self.eventManager.bShift:
			print("SHIFT-ALT-C") #picks a dead civ so that autoplay can be started with game.AIplay xx
			iDebugDeadCiv = iSamanids
			#gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.iCalendar, True, iDebugDeadCiv, False, False)
			utils.makeUnit(con.iSpearman, iDebugDeadCiv, (0,0), 1)
			gc.getGame().setActivePlayer(iDebugDeadCiv, False)
			gc.getPlayer(iDebugDeadCiv).setPlayable(True)
		
		if eventType == self.EventKeyDown and key == InputTypes.KB_Q and self.eventManager.bAlt and self.eventManager.bShift:
			print("SHIFT-ALT-Q") #enables squatting
			self.rnf.setCheatMode(True);
			CyInterface().addMessage(iHuman, True, con.iDuration, "EXPLOITER!!! ;)", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
		
		# Baldyr: Stability Cheat
		if self.rnf.getCheatMode() and key == InputTypes.KB_S and self.eventManager.bAlt and self.eventManager.bShift:
			print("SHIFT-ALT-S") #boosts stability by +10 for the human player
			sd.setStability(iHuman, sd.getStability(iHuman)+10)
		
		# edead: SoI Debug
		if eventType == self.EventKeyDown and key == InputTypes.KB_N and self.eventManager.bCtrl and gc.getGame().isDebugMode():
			print("CTRL-N")
			utils.launchDebugScreen()
		
		# edead: province highlight
		if eventType == self.EventKeyDown and px >= 0 and py >= 0 and int(key) == 45 and self.eventManager.bCtrl and not self.eventManager.bAlt:
			
			plot = gc.getMap().plot(px,py)
			iActivePlayer = gc.getGame().getActivePlayer()
			iActiveTeam = gc.getPlayer(iActivePlayer).getTeam()
			iRegionID = plot.getRegionID()
			
			# do not show provinces of unrevealed tiles
			if not plot.isRevealed(iActiveTeam, False) and not gc.getGame().isDebugMode():
				return
			
			# do not redraw if already drawn
			if self.lastRegionID == iRegionID:
				return
			
			map = CyMap()
			engine = CyEngine()
			
			# clear the highlight
			engine.clearAreaBorderPlots(AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			#engine.clearColoredPlots(PlotLandscapeLayers.PLOT_LANDSCAPE_LAYER_RECOMMENDED_PLOTS)
			
			# cache the plot's coords
			self.lastRegionID = plot.getRegionID()
			
			# select an appriopriate color
			if plot.isWater():
				return
			else:
				iLevel = utils.getRegionStabilityLevel(iHuman, iRegionID)
				if iLevel == 4:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_CORE")).getColor()
				elif iLevel == 3:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_BORDER")).getColor()
				elif iLevel == 2:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_CONTESTED")).getColor()
				elif iLevel == 1:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_OUTSIDE")).getColor()
				else:
					color = gc.getColorInfo(gc.getInfoTypeForString("COLOR_HIGHLIGHT_FOREIGN")).getColor()
			
			# apply the highlight
			for i in range(map.numPlots()):
				plot = map.plotByIndex(i)
				if plot.getRegionID() == iRegionID and (gc.getGame().isDebugMode() or plot.isRevealed(iActiveTeam, False)):
					engine.fillAreaBorderPlot(plot.getX(), plot.getY(), color, AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			
			return
		
		# clear all hightlights
		if (eventType == self.EventKeyUp and self.eventManager.bCtrl) or (eventType == self.EventKeyDown):
			CyEngine().clearAreaBorderPlots(AreaBorderLayers.AREA_BORDER_LAYER_HIGHLIGHT_PLOT)
			self.lastRegionID = -1


	def printDebug(self, iGameTurn):
		
		# if (iGameTurn % 50 == 1):
			# self.printEmbassyDebug()
		# if (iGameTurn % 20 == 0):
			# self.printPlotsDebug()
		if (iGameTurn % 10 == 0): 
			self.printStabilityDebug()


	def printStabilityDebug(self):
		print ("Stability")
		for iCiv in range(iNumPlayers):
			if (gc.getPlayer(iCiv).isAlive()):
				print ("Base:", sd.getBaseStabilityLastTurn(iCiv), "Modifier:", sd.getStability(iCiv)-sd.getBaseStabilityLastTurn(iCiv), "Total:", sd.getStability(iCiv), "civic", gc.getPlayer(iCiv).getCivics(5), gc.getPlayer(iCiv).getCivilizationDescription(0))
			else:
				print ("dead", iCiv)
		for i in range(con.iNumStabilityParameters):
			print("Parameter", i, utils.getStabilityParameters(i))
		for i in range(iNumPlayers):
			print (gc.getPlayer(i).getCivilizationShortDescription(0), "PLOT OWNERSHIP ABROAD:", self.sta.getOwnedPlotsLastTurn(i), "CITY OWNERSHIP LOST:", self.sta.getOwnedCitiesLastTurn(i) )
