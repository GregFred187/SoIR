# Rhye's and Fall of Civilization - Barbarian units and cities

from CvPythonExtensions import *
import CvUtil
import UnitArtStyler
import Consts as con
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()

### Constants ###

iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iIndependent3 = con.iIndependent3
iIndependent4 = con.iIndependent4
iBarbarian = con.iBarbarian

# iCiv, Name, Year, X, Y, iReligion, Skip
tMinorCities = (
	(iIndependent,  "Marv",		 	 810, 83, 53, [con.iZoroastrianism], 0), # before Samanid spawn
	(iIndependent2, "Zaranj",	 	 861, 84, 35, [con.iZoroastrianism, con.iSunni], 0),
	(iIndependent3, "Herat",	 	 875, 85, 44, [con.iZoroastrianism, con.iSunni], 0),
	(iIndependent3, "Yazd",			1000, 69, 38, [con.iZoroastrianism], 0),
	(iIndependent4, "Purushapura",	1005, 102, 43, [con.iBuddhism, con.iHinduism], 0),
	(iIndependent4, "Baku",			1010, 62, 61, [con.iShia], 0),
	(iIndependent,  "Akka",			1025, 32, 39, [con.iJudaism, con.iSunni, con.iOrthodoxy], 0), # before Crusader spawn
	(iIndependent2, "Qazvin",		1030, 60, 49, [con.iSunni], 0), # if razed
	(iIndependent,  "Tarabulus", 	 995, 35, 46, [con.iOrthodoxy, con.iShia], 0),
	(iIndependent,  "Tarabulus",	1045, 35, 46, [con.iOrthodoxy, con.iShia], 0), # again, before Antioch spawn
	(iIndependent,  "Marv",			1050, 83, 53, [con.iZoroastrianism, con.iSunni], 0), # if razed
	(iBarbarian,    "Balkh",		1060, 95, 51, [con.iZoroastrianism, con.iSunni], 0), # if razed
	(iIndependent3, "Kashgar",		1070, 111, 58, [con.iBuddhism, con.iZoroastrianism], 0),
	(iIndependent,  "Homs",			1070, 38, 47, [con.iSunni, con.iShia], 0), # before Antioch spawn
	(iIndependent2, "Sis",			1078, 35, 53, [con.iOrthodoxy], 0), # before Armenia respawn
	(iIndependent,  "Edessa",		1090, 40, 52, [con.iOrthodoxy], 0), # if razed, before Antioch spawn
	(iIndependent4, "Ormuz",		1100, 72, 28, [con.iSunni], 0),
	(iIndependent3, "Al-Mosul",		1105, 48, 49, [con.iSunni, con.iShia], 0), # if razed, before Zengid spawn
	(iIndependent4, "Mazar-e Sharif",1120,96, 51, [con.iSunni], 0), # if Balkh is razed
	(iIndependent2, "Al-Aqabah",	1150, 32, 31, [con.iSunni], 0), # before Ayyubid spawn
	(iIndependent,  "Yazd",			1170, 75, 34, [con.iZoroastrianism], 0), # if razed
	(iIndependent3, "Kerman",		1190, 75, 34, [con.iZoroastrianism, con.iSunni, con.iShia], 0), # if razed
	(iIndependent,  "Limassol",		1191, 29, 46, [con.iOrthodoxy, con.iCatholicism], 0), # if neither Nicosia nor Famagusta are built
	(iIndependent2, "Zabol",		1200, 84, 35, [con.iSunni], 0), # if Zaranj is razed
	(iBarbarian,    "Herat",		1250, 85, 44, [con.iSunni], 0), # if razed
	(iBarbarian,    "Bukhara",		1300, 89, 59, [con.iSunni], 0), # if razed
	(iIndependent,  "Mashhad",		1330, 77, 51, [con.iSunni], 0), # if nishapur is razed
	(iIndependent4, "Vijayanagara",	1355, 111,  3, [con.iHinduism], 0), # after Bahmanid spawn
	(iBarbarian,    "Khiveh",		1360, 83, 63, [con.iSunni], 0), # if razed
	(iBarbarian,    "Tabriz",		1375, 55, 54, [con.iShia], 0), # kara koyunlu
	(iIndependent,  "Turbat",		1450, 85, 26, [con.iSunni], 0),
	(iIndependent2, "Jodhpur",		1459, 103, 25, [con.iHinduism], 0),
	(iIndependent3, "Gwadar",		1480, 81, 24, [con.iSunni], 0),
	(iIndependent4, "Suq",			1490, 66,  1, [con.iCatholicism], 0),
	(iIndependent,  "Ahmednagar",	1494, 108, 11, [con.iSunni, con.iShia], 0),
	(iIndependent2, "Murwab",		1500, 63, 25, [con.iSunni], 0),
	(iIndependent,  "Marv",			1505, 83, 53, [con.iSunni], 0), # if razed
	
)

# These cities will receive extra defense if controlled by indeps/barbs: Start, End, X, Y
tMinorStates = (
	(1336, 1646, 111, 3), # Vijayanagara
	(1400, 1700, 106, 21), # Chittor
	(1270, 1700, 37, 1), # Aksum
	(1450, 1700, 103, 25), # Jodhpur
)

# for random unit generation
earlyBulgarians = [con.iArcher_Caucasian, con.iAxeman_Caucasian, con.iSpearman_Caucasian]
lateBulgarians = [con.iSwordsman_Kipchak, con.iAxeman_Caucasian, con.iHorseArcher_Kipchak]
turkomanBarbs = [con.iTurkomanRaider, con.iHeavyHorseArcher]
bedouinBarbs1 = [con.iArcher_Bedouin]
bedouinBarbs2 = [con.iHorseman_Bedouin, con.iArcher_Bedouin]
bedouinBarbs3 = [con.iHorseman_Bedouin, con.iCamelArcher, con.iCamelRider]
afghanBarbs = [con.iJavelinman_Turkish, con.iAxeman_Persian, con.iSwordsman_Persian]
earlySupport = [con.iSpearman, con.iArcher, con.iJavelinman, con.iSwordsman]
lateSupport = [con.iHeavySpearman, con.iMarksman, con.iJavelinman]


class Barbs:


	def checkTurn(self, iGameTurn):
		
		iHuman = utils.getHumanID()
		iHandicap = gc.getGame().getHandicapType() - 1
		
		# Randomness
		iRand1 = gc.getGame().getSorenRandNum(2, 'Random spawn size for this turn')
		iRand2 = gc.getGame().getSorenRandNum(2, 'Another one')
		iRand3 = gc.getGame().getSorenRandNum(2, 'One more')
		
		# Independent cities
		for i in range(len(tMinorCities)):
			if tMinorCities[i][6] == 0:
				iTurn = getTurnForYear(tMinorCities[i][2])
				if iGameTurn == iTurn or iGameTurn == iTurn + 5 or iGameTurn == iTurn + 10:
					if self.foundCity(tMinorCities[i][0], tMinorCities[i][1], tMinorCities[i][3], tMinorCities[i][4], tMinorCities[i][5]):
						tMinorCities[i][6] == 1
		
		# Random cities
		if iGameTurn == getTurnForYear(900):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 20:
				self.foundCity(iIndependent4, "Al-Qatif", 60, 26, [con.iSunni])
		if iGameTurn == getTurnForYear(928):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 10:
				city = self.foundCity(iIndependent, "Sariya", 66, 49, [con.iShia])
		if iGameTurn == getTurnForYear(965):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 20:
				city = self.foundCity(iIndependent, "Lefkousia", 30, 47, [con.iOrthodoxy])
				if city and not city.isNone() and gc.getPlayer(con.iByzantium).isAlive():
					city.setCulture(con.iByzantium, 9, True)
		if iGameTurn == getTurnForYear(990):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 10:
				self.foundCity(iIndependent, "Tartus", 35, 47, [con.iOrthodoxy, con.iSunni])
		if iGameTurn == getTurnForYear(1020):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 10:
				self.foundCity(iIndependent2, "Ayla", 32, 31, [con.iSunni])
		if iGameTurn == getTurnForYear(1100):
			if gc.getGame().getSorenRandNum(100, 'Random city') < 50:
				city = self.foundCity(iIndependent, "Famagusta", 30, 46, [con.iOrthodoxy])
				if city and not city.isNone():
					if gc.getPlayer(con.iByzantium).isAlive():
						city.setCulture(con.iByzantium, 9, True)
					if gc.getPlayer(con.iCrusaders).isAlive():
						city.setCulture(con.iCrusaders, 9, True)
		
		# Independent states - extra defense for minor cities
		if iGameTurn % 20 == 10 and iGameTurn >= getTurnForYear(1270):
			for tMinorCity in tMinorStates:
				if iGameTurn > getTurnForYear(tMinorCity[0]) and iGameTurn < getTurnForYear(tMinorCity[1]):
					plot = gc.getMap().plot(tMinorCity[2], tMinorCity[3])
					iOwner = plot.getOwner()
					if plot.isCity() and plot.getNumUnits() < 4 and iOwner >= con.iNumPlayers:
						utils.makeUnit(self.getRandomUnit(lateSupport), iOwner, (tMinorCity[2], tMinorCity[3]), 1)
		
		# Zengid spawn
		if iGameTurn == getTurnForYear(1127)-1:
			pUnit = self.spawnUnits(con.iZengids, (42,52),(49,48), con.iLancer_Turkish, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				pUnit.setHasPromotion(con.iFlanking1, True)
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_ZENGI",()))
			self.spawnUnits(con.iZengids, (42,52),(49,48), con.iIqtadar, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(con.iZengids, (42,52),(49,48), con.iLancer_Turkish, 3 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(con.iZengids, (42,52),(49,48), con.iArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(con.iZengids, (48,49),(48,49), con.iArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(con.iZengids, (42,52),(49,48), con.iSpearman, 1, iGameTurn, 1, 0, utils.outerInvasion)
		if iGameTurn == getTurnForYear(1127) or iGameTurn == getTurnForYear(1127)+1:
			if gc.getPlayer(con.iZengids).getNumCities() < 2:
				self.spawnUnits(con.iZengids, (42,52),(49,48), con.iIqtadar, 1, iGameTurn, 1, 0, utils.outerInvasion)
				self.spawnUnits(con.iZengids, (42,52),(49,48), con.iLancer_Turkish, 1, iGameTurn, 1, 0, utils.outerInvasion)
				self.spawnUnits(con.iZengids, (42,52),(49,48), con.iArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
				self.spawnUnits(con.iZengids, (42,52),(49,48), con.iTrebuchet, 1, iGameTurn, 1, 0, utils.outerInvasion)
		
		# Kharijites in Mesopotamia
		if iGameTurn >= getTurnForYear(750) and iGameTurn <= getTurnForYear(1000):
			self.spawnUnits(iBarbarian, (44,51),(57,30), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab]), 1, iGameTurn, 15, 13, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KHARIJITE",()))
		
		# Greek peasants
		if iGameTurn >= getTurnForYear(760) and iGameTurn < getTurnForYear(900):
			self.spawnUnits(iBarbarian, (0,65),(31,52), con.iPeasant, 1, iGameTurn, 25, 11, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))
			self.spawnUnits(iBarbarian, (0,65),(36,52), con.iPeasant, iRand1, iGameTurn, 25, 10, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))
			self.spawnUnits(iBarbarian, (8,63),(4,65), con.iPeasant, 1, iGameTurn, 25, 11, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))
		if iGameTurn >= getTurnForYear(900) and iGameTurn < getTurnForYear(1100):
			self.spawnUnits(iBarbarian, (0,65),(31,52), con.iPeasant, 1, iGameTurn, 20, 11, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))
			self.spawnUnits(iBarbarian, (0,65),(36,52), con.iPeasant, iRand1, iGameTurn, 20, 10, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))

		# Caucasian peasants
		if iGameTurn >= getTurnForYear(900) and iGameTurn <= getTurnForYear(1150):
			pUnit = self.spawnUnits(iBarbarian, (47,66),(56,55), con.iPeasant, 1, iGameTurn, 25, 17, utils.innerInvasion, UnitAITypes.UNITAI_PILLAGE, localText.getText("TXT_KEY_BARB_REBEL",()))
			if pUnit:
				pUnit.setArtDefineTag("ART_DEF_UNIT_PEASANT_CAUCASIAN")
			
		# Armenian rebels
		if iGameTurn == getTurnForYear(830):
			self.spawnUnits(iBarbarian, (38,63),(46,57), self.getRandomUnit([con.iJavelinman_Caucasian, con.iAxeman_Caucasian, con.iArcher_Caucasian, con.iSpearman_Caucasian]), 1 + iRand1 + iHandicap, iGameTurn, 15, 13, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_CIV_ARMENIA_ADJECTIVE",()))
			self.spawnUnits(iBarbarian, (38,63),(46,57), self.getRandomUnit([con.iJavelinman_Caucasian, con.iAxeman_Caucasian, con.iArcher_Caucasian, con.iSpearman_Caucasian]), 1 + iRand1 + iHandicap, iGameTurn, 15, 13, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_CIV_ARMENIA_ADJECTIVE",()))
			
		# Muslim raiders in Anatolia
		if iGameTurn >= getTurnForYear(760) and iGameTurn < getTurnForYear(900):
			self.spawnUnits(iBarbarian, (33,65),(42,56), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian]), 1, iGameTurn, 15, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		if iGameTurn >= getTurnForYear(900) and iGameTurn < getTurnForYear(1040):
			self.spawnUnits(iBarbarian, (33,65),(42,56), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iHorseman_Persian]), 1, iGameTurn, 12, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		
		# Muslim raiders in Caucasus
		if iGameTurn >= getTurnForYear(870) and iGameTurn < getTurnForYear(950):
			self.spawnUnits(iBarbarian, (47,62),(59,54), self.getRandomUnit([con.iArcher_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1, iGameTurn, 15, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		if iGameTurn >= getTurnForYear(950) and iGameTurn < getTurnForYear(1030):
			self.spawnUnits(iBarbarian, (47,62),(59,54), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iHorseman_Persian]), 1, iGameTurn, 10, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		
		# Bulgarians
		if iGameTurn == getTurnForYear(811):
			pUnit = self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_KHAN_KRUM",()), con.iGreatGeneral2)
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
		if iGameTurn >= getTurnForYear(836) and iGameTurn < getTurnForYear(1018):
			self.spawnUnits(iBarbarian, (15,69),(19,62), self.getRandomUnit(earlyBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BULGARIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion)
		if iGameTurn >= getTurnForYear(780) and iGameTurn < getTurnForYear(1018):
			self.spawnUnits(iBarbarian, (15,69),(19,62), self.getRandomUnit(earlyBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BULGARIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion)
		if iGameTurn >= getTurnForYear(1185) and iGameTurn < getTurnForYear(1396):
			self.spawnUnits(iBarbarian, (15,69),(19,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BULGARIAN",()), [con.iWoodsman1, con.iWoodsman2])
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1 + iHandicap, iGameTurn, 20, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
		if iGameTurn == getTurnForYear(917):
			pUnit = self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_TSAR_SIMEON",()), con.iGreatGeneral2)
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
			self.spawnUnits(iBarbarian, (15,69),(19,62), con.iBulgarianRaider, 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])

		# Serbians
		if iGameTurn >= getTurnForYear(1170) and iGameTurn < getTurnForYear(1190):
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), con.iVlastela, 3 + iRand3 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion)
		if iGameTurn >= getTurnForYear(1180) and iGameTurn < getTurnForYear(1200):
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), con.iVlastela, 3 + iRand3 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion)
		if iGameTurn >= getTurnForYear(1190) and iGameTurn < getTurnForYear(1210):
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), self.getRandomUnit(lateBulgarians), 1 + iRand1 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SERBIAN",()), [con.iWoodsman1])
			self.spawnUnits(iBarbarian, (5,69),(13,62), con.iVlastela, 3 + iRand3 + iHandicap, iGameTurn, 20, 1, utils.outerInvasion)

		# Muslim invaders in India
		if iGameTurn >= getTurnForYear(780) and iGameTurn < getTurnForYear(920):
			self.spawnUnits(iBarbarian, (103,32),(105,17), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand1 + iHandicap, iGameTurn, 9, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		if iGameTurn >= getTurnForYear(950) and iGameTurn < getTurnForYear(1057):
			self.spawnUnits(iBarbarian, (95,37),(105,20), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iHorseman_Persian]), 1 + iRand1 + iHandicap, iGameTurn, 12, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		if iGameTurn >= getTurnForYear(980) and iGameTurn < getTurnForYear(1150):
			self.spawnUnits(iBarbarian, (100,25),(104,19), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iHorseman_Persian]), 1 + iRand1 + iHandicap, iGameTurn, 12, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		
		# Gurjars
		if iGameTurn >= getTurnForYear(800) and iGameTurn < getTurnForYear(900):
			self.spawnUnits(iBarbarian, (104,29),(112,13), self.getRandomUnit([con.iSpearman_Indian, con.iArcher_Indian, con.iJavelinman_Indian]), 1, iGameTurn, 9, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_GURJAR",()))
		if iGameTurn >= getTurnForYear(900) and iGameTurn < getTurnForYear(1030):
			self.spawnUnits(iBarbarian, (104,29),(112,13), self.getRandomUnit([con.iSpearman_Indian, con.iArcher_Indian, con.iSwordsman_Indian]), 1, iGameTurn, 13, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_GURJAR",()))

		# Early Rajputs
		if iGameTurn >= getTurnForYear(920) and iGameTurn < getTurnForYear(1100):
			self.spawnUnits(iBarbarian, (102,30),(113,13), self.getRandomUnit([con.iHorseman_Indian, con.iSwordsman_Indian]), 1, iGameTurn, 18, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_RAJPUT",()))
			
		# Tulunids
		if iGameTurn == getTurnForYear(880) or iGameTurn == getTurnForYear(890):
			self.spawnUnits(iBarbarian, (36,44),(38,37), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TULUNID",()))
			if gc.getMap().plot(con.tJerusalem[0],con.tJerusalem[1]).getOwner() < con.iNumPlayers:
				self.spawnUnits(iBarbarian, (30,39),(33,31), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TULUNID",()))
		
		# Ikhshidids
		if iGameTurn == getTurnForYear(935) or iGameTurn == getTurnForYear(946):
			self.spawnUnits(iBarbarian, (36,44),(38,37), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ILKSHIDIDS",()))
			if gc.getMap().plot(con.tJerusalem[0],con.tJerusalem[1]).getOwner() < con.iNumPlayers:
				self.spawnUnits(iBarbarian, (30,39),(33,31), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ILKSHIDIDS",()))
		
		# Hamdanids
		if iGameTurn == getTurnForYear(889):
			self.spawnUnits(iBarbarian, (38,55),(44,49), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HAMDANID",()))
			self.spawnUnits(iBarbarian, (38,55),(44,49), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HAMDANID",()))
		if iGameTurn > getTurnForYear(890) and iGameTurn < getTurnForYear(930):
			self.spawnUnits(iBarbarian, (38,55),(44,49), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1, iGameTurn, 10, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HAMDANID",()))
			self.spawnUnits(iBarbarian, (44,53),(49,47), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab, con.iAxeman_Persian, con.iSpearman_Harafisha]), 1, iGameTurn, 10, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HAMDANID",()))
		
		# Qarmatian revolt
		if iGameTurn == getTurnForYear(889):
			# Revolts in Kufah, Basra, Ahvaz
			kufah = gc.getMap().plot(50,37).getPlotCity()
			basra = gc.getMap().plot(57,33).getPlotCity()
			wasit = gc.getMap().plot(54,38).getPlotCity()
			ahvaz = gc.getMap().plot(59,36).getPlotCity()
			for city in [kufah, basra, wasit, ahvaz]:
				if city and not city.isNone():
					iRevoltTurns = gc.getGame().getSorenRandNum(3, 'Revolt turns')
					city.changeCultureUpdateTimer(iRevoltTurns);
					city.changeOccupationTimer(iRevoltTurns);
			CyInterface().addMessage(con.iAbbasids, False, con.iDuration, localText.getText("TXT_KEY_EVENT_QARMATIAN_REVOLT", ()), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, None, gc.getInfoTypeForString("COLOR_RED"), -1, -1, False, False);
			self.spawnUnits(iBarbarian, (55,36),(60,26), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab, con.iSpearman_Harafisha]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARMATIAN",()))
			self.spawnUnits(iBarbarian, (55,36),(60,26), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab, con.iSpearman_Harafisha]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARMATIAN",()))
		if iGameTurn > getTurnForYear(889) and iGameTurn < getTurnForYear(952):
			self.spawnUnits(iBarbarian, (55,36),(60,26), self.getRandomUnit([con.iArcher_Arab, con.iSwordsman_Arab, con.iSpearman_Harafisha, con.iMaceman_Harafisha]), 1, iGameTurn, 12, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARMATIAN",()))
		
		# Saffarids
		if iGameTurn >= getTurnForYear(900) and iGameTurn < getTurnForYear(1003):
			self.spawnUnits(iBarbarian, (82,50),(86,39), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iJavelinman_Turkish]), 1, iGameTurn, 15, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SAFFARID",()))
			self.spawnUnits(iBarbarian, (82,50),(86,39), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iJavelinman_Turkish]), 1, iGameTurn, 20, 15, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SAFFARID",()))
		
		# Ziyarids and Buyids in Western Iran and Mesopotamia
		if iGameTurn == getTurnForYear(928)-1:
			self.invasionAlert("TXT_KEY_INVASION_ZIYARIDS", [con.iAbbasids, con.iArmenia, con.iByzantium, con.iSamanids])
		if iGameTurn == getTurnForYear(928) and iGameTurn == getTurnForYear(932):
			self.spawnUnits(iBarbarian, (50,50),(53,34), con.iSwordsman_Persian, 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ZIYARID",()))
			self.spawnUnits(iBarbarian, (50,50),(53,34), con.iDaylamiTribesman, 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ZIYARID",()))
			self.spawnUnits(iBarbarian, (50,50),(53,34), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian]), 0 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ZIYARID",()))
			# if iGameTurn == getTurnForYear(934)-1:
				# self.invasionAlert("TXT_KEY_INVASION_BUYIDS", [con.iAbbasids, con.iArmenia, con.iByzantium, con.iSamanids])
		if iGameTurn == getTurnForYear(934)+1 or iGameTurn == getTurnForYear(945) or iGameTurn == getTurnForYear(979):
			pUnit = self.spawnUnits(con.iBuyids, (50,50),(53,34), con.iSwordsman_Persian, 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, "", [con.iCityRaider1])
			if not pUnit:
				pUnit = self.spawnUnits(con.iBuyids, (49,53),(54,33), con.iSwordsman_Persian, 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, "", [con.iCityRaider1])
			if pUnit:
				utils.makeUnit(con.iDaylamiTribesman, con.iBuyids, (pUnit.getX(), pUnit.getY()), 2 + iRand2 + iHandicap, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, [con.iCombat1])
				utils.makeUnit(con.iCatapult, con.iBuyids, (pUnit.getX(), pUnit.getY()), 1, UnitAITypes.UNITAI_ATTACK_CITY_LEMMING, [con.iCityRaider1, con.iCityRaider2])
		if iGameTurn == getTurnForYear(934)+6 or iGameTurn == getTurnForYear(945)+5 or iGameTurn == getTurnForYear(979)+5:
			self.spawnUnits(con.iBuyids, (50,50),(53,34), con.iArcher_Persian, 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.NO_UNITAI, "", [con.iCityGarrison1])
		
		# Uqaylids
		if iGameTurn == getTurnForYear(989):
			self.spawnUnits(iBarbarian, (38,55),(44,49), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UQAYLID",()))
			self.spawnUnits(iBarbarian, (38,55),(44,49), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UQAYLID",()))
		if iGameTurn == getTurnForYear(1002):
			self.spawnUnits(iBarbarian, (26,54),(47,48), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian]), 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UQAYLID",()))
			self.spawnUnits(iBarbarian, (26,54),(47,48), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Persian]), 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UQAYLID",()))
		
		# Qarakhanids
		if iGameTurn == getTurnForYear(990)-1:
			self.invasionAlert("TXT_KEY_INVASION_QARAKHANIDS", [con.iAbbasids, con.iSamanids])
		if iGameTurn == getTurnForYear(990):
			self.spawnUnits(iBarbarian, (86,62),(95,56), con.iHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARAKHANID",()))
			self.spawnUnits(iBarbarian, (86,62),(95,56), con.iHorseArcher, 1 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARAKHANID",()))
		if iGameTurn > getTurnForYear(990) and iGameTurn < getTurnForYear(1010):
			self.spawnUnits(iBarbarian, (86,62),(95,56), con.iHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARAKHANID",()))
			self.spawnUnits(iBarbarian, (89,63),(96,49), con.iHorseArcher, 1 + iRand2 + iHandicap, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_QARAKHANID",()))
		
		# Tajiks
		if not gc.getPlayer(con.iSamanids).isAlive():
			if iGameTurn >= getTurnForYear(990) and iGameTurn < getTurnForYear(1200):
				self.spawnUnits(iBarbarian, (93,56),(102,48), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iJavelinman_Turkish]), 1, iGameTurn, 30, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TAJIK",()))
			if iGameTurn >= getTurnForYear(1200):
				self.spawnUnits(iBarbarian, (93,56),(102,48), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iLancer]), 1, iGameTurn, 30, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TAJIK",()))
		
		# Alans, Circassians
		if iGameTurn >= getTurnForYear(1040) and iGameTurn < getTurnForYear(1130):
			self.spawnUnits(iBarbarian, (44,69),(60,64), self.getRandomUnit([con.iAxeman_Caucasian, con.iArcher_Caucasian, con.iSwordsman_Kipchak]), 1 + iRand1 + iHandicap, iGameTurn, 15, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ALAN",()))
			self.spawnUnits(iBarbarian, (44,69),(60,64), self.getRandomUnit([con.iAxeman_Caucasian, con.iArcher_Caucasian, con.iSwordsman_Kipchak]), 1 + iRand1 + iHandicap, iGameTurn, 20, 10, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_CIRCASSIAN",()))
		elif iGameTurn >= getTurnForYear(1130) and iGameTurn < getTurnForYear(1220):
			self.spawnUnits(iBarbarian, (44,69),(60,64), self.getRandomUnit([con.iSwordsman_Kipchak, con.iHorseArcher_Kipchak]), 1 + iRand1 + iHandicap, iGameTurn, 17, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ALAN",()))
			self.spawnUnits(iBarbarian, (44,69),(60,64), self.getRandomUnit([con.iSwordsman_Kipchak, con.iHorseArcher_Kipchak]), 1 + iRand1 + iHandicap, iGameTurn, 23, 10, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_CIRCASSIAN",()))
		
		# Sallarids in Azerbaijan
		if iGameTurn >= getTurnForYear(942) and iGameTurn <= getTurnForYear(979):
			self.spawnUnits(iBarbarian, (53,55),(59,51), con.iDaylamiTribesman, 1, iGameTurn, 8, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SALLARID",()))
		
		# Tahirids in Khorasan
		if iGameTurn >= getTurnForYear(820) and iGameTurn <= getTurnForYear(872):
			self.spawnUnits(iBarbarian, (79,55),(87,47), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iJavelinman_Turkish]), 1, iGameTurn, 12, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TAHIRID",()))
		
		# Kartids in Khorasan
		if iGameTurn >= getTurnForYear(1231) and iGameTurn <= getTurnForYear(1389):
			self.spawnUnits(iBarbarian, (75,55),(85,43), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iHorseman_Persian]), 1 + iRand1, iGameTurn, 20, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARTID",()))
			self.spawnUnits(iBarbarian, (75,55),(85,43), self.getRandomUnit([con.iSwordsman_Persian, con.iAxeman_Persian, con.iHorseman_Persian]), iRand2 + iHandicap, iGameTurn, 20, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARTID",()))
		
		# Seljuks invade Khorasan
		if iGameTurn == getTurnForYear(1031)-1:
			self.invasionAlert("TXT_KEY_INVASION_SELJUKS_1")
		if iGameTurn >= getTurnForYear(1031) and iGameTurn < getTurnForYear(1036):
			self.spawnUnits(iBarbarian, (78,54),(87,47), con.iHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",()))
			self.spawnUnits(iBarbarian, (86,61),(92,50), con.iHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",()))
		
		# Seljuks invade Caucasus and Anatolia
		if iGameTurn == getTurnForYear(1058)-1:
			self.invasionAlert("TXT_KEY_INVASION_SELJUKS_2")
		if iGameTurn >= getTurnForYear(1058) and iGameTurn < getTurnForYear(1068)-1:
			self.spawnUnits(iBarbarian, (46,60),(58,55), con.iHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",())) # Caucasus
			self.spawnUnits(iBarbarian, (34,62),(41,55), con.iHorseArcher, 3 + iRand2 + iHandicap, iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",()))
			self.spawnUnits(iBarbarian, (27,65),(33,53), con.iHorseArcher, 4 + iRand1 + iHandicap, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",()))
			self.spawnUnits(iBarbarian, (36,62),(50,56), con.iHorseArcher, 3 + iRand2 + iHandicap, iGameTurn, 2, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SELJUKS",())) # Lesser Armenia
		
		# Artuqids
		if iGameTurn == getTurnForYear(1104):
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iSwordsman_Persian, con.iMaceman_Turkish]), 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iJavelinman_Turkish]), 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iHorseArcher]), 1 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
		if iGameTurn == getTurnForYear(1119):
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iSwordsman_Persian, con.iMaceman_Turkish]), 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iHorseArcher]), 2 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
		if iGameTurn == getTurnForYear(1198):
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iMarksman_Turkish, con.iMaceman_Turkish]), 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
			self.spawnUnits(iBarbarian, (37,55),(42,51), self.getRandomUnit([con.iHorseArcher]), 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_ARTUQID",()))
		
		# Assassins
		if iGameTurn >= getTurnForYear(1090) and iGameTurn < getTurnForYear(1256):
			self.spawnUnits(iBarbarian, (58,51),(66,45), con.iFidai, 1, iGameTurn, 20, 13, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_NIZARI",()))
			self.spawnUnits(iBarbarian, (35,52),(39,37), con.iFidai, 1, iGameTurn, 20, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_NIZARI",()))
		
		# Muslim Rebels
		if iGameTurn > getTurnForYear(1099) and (gc.getPlayer(con.iAntioch).isAlive() or gc.getPlayer(con.iCrusaders).isAlive()):
			if iGameTurn % utils.getTurns(15) == 3:
				if self.isChristianRegion(con.rSyria):
					self.spawnUnits(iBarbarian, (37,46),(40,39), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Kurdish, con.iMaceman_Harafisha, con.iMaceman_Turkish]), 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
			elif iGameTurn % utils.getTurns(15) == 8:
				if self.isChristianRegion(con.rJordan):
					self.spawnUnits(iBarbarian, (33,38),(39,33), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Kurdish, con.iMaceman_Harafisha, con.iMaceman_Turkish]), 1, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
			elif iGameTurn % utils.getTurns(15) == 13:
				if self.isChristianRegion(con.rPalestine):
					self.spawnUnits(iBarbarian, (32,39),(38,33), self.getRandomUnit([con.iSwordsman_Arab, con.iAxeman_Kurdish, con.iMaceman_Harafisha, con.iMaceman_Turkish]), 1, iGameTurn, 15, 13, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MUSLIM",()))
		
		# Mongols invade Khwarezm
		if iGameTurn == getTurnForYear(1218)-1:
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_KHWAREZM", [con.iAbbasids, con.iByzantium, con.iArmenia, con.iGeorgia, con.iFatimids, con.iSeljuks, con.iRum, con.iKhwarezm, con.iAntioch, con.iCrusaders, con.iAyyubids, con.iSamanids, con.iGhaznavids, con.iGhorids])
		if iGameTurn == getTurnForYear(1218):
			pUnit = self.spawnUnits(iBarbarian, (82,69),(92,53), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_SUBUTAI",()), con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
				pUnit.setHasPromotion(con.iFlanking3, True)
				pUnit.setHasPromotion(con.iFeintAttack, True)
				pUnit.setHasPromotion(con.iEncirclement, True)
			self.spawnUnits(iBarbarian, (95,69),(99,63), con.iMongolHorseArcher, self.getInvasionForce(3, con.iKhwarezm) + iHandicap, iGameTurn, 1, 0, utils.outerInvasion) # Otrar
			self.spawnUnits(iBarbarian, (82,69),(92,53), con.iMongolHorseArcher, self.getInvasionForce(5, con.iKhwarezm) + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(iBarbarian, (82,69),(92,53), con.iMongolHorseArcher, self.getInvasionForce(5, con.iKhwarezm) + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(iBarbarian, (81,68),(93,56), con.iMongolHorseArcher, self.getInvasionForce(5, con.iKhwarezm) + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(iBarbarian, (81,68),(93,56), con.iMongolHorseArcher, self.getInvasionForce(5, con.iKhwarezm), iGameTurn, 1, 0, utils.outerInvasion)
		
		# Mongols recon Caucasus
		if iGameTurn == getTurnForYear(1220):
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_CAUCASUS", [con.iAbbasids, con.iByzantium, con.iArmenia, con.iGeorgia, con.iFatimids, con.iSeljuks, con.iRum, con.iKhwarezm, con.iAntioch, con.iCrusaders, con.iAyyubids])
		if iGameTurn == getTurnForYear(1220)+1:
			self.spawnUnits(iBarbarian, (46,69),(63,56), con.iMongolHorseArcher, 1 + iRand1, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(iBarbarian, (46,69),(63,56), con.iMongolHorseArcher, 1 + iRand2, iGameTurn, 1, 0, utils.outerInvasion)

		# Mongols invade India
		if iGameTurn == getTurnForYear(1221):
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_INDIA", [con.iSamanids, con.iSeljuks, con.iGhaznavids, con.iGhorids, con.iKhwarezm, con.iChauhan, con.iGujarat, con.iSindh])
		if iGameTurn == getTurnForYear(1221)+1:
			func = utils.outerInvasion
			if utils.getHumanID() not in [con.iGhorids, con.iGhaznavids, con.iChauhan]:
				func = utils.innerInvasion
			if not self.spawnUnits(iBarbarian, (98,47),(101,44), con.iMongolHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, func): # Gandhar
				self.spawnUnits(iBarbarian, (98,47),(101,44), con.iMongolHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Gandhar
			if not self.spawnUnits(iBarbarian, (101,42),(104,36), con.iMongolHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, func): # Punjab
				self.spawnUnits(iBarbarian, (101,42),(104,36), con.iMongolHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Punjab
			pUnit = self.spawnUnits(iBarbarian, (101,42),(104,36), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, func)
			if not pUnit:
				pUnit = self.spawnUnits(iBarbarian, (101,42),(104,36), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, utils.innerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_BALA",()), con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iFeintAttack, True)
		if iGameTurn == getTurnForYear(1235):
			func = utils.outerInvasion
			if utils.getHumanID() not in [con.iGhorids, con.iGhaznavids, con.iChauhan]:
				func = utils.innerInvasion
			if not self.spawnUnits(iBarbarian, (103,44),(106,40), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, func): # Duggar & Punjab
				self.spawnUnits(iBarbarian, (103,44),(106,40), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Duggar & Punjab
			if not self.spawnUnits(iBarbarian, (103,44),(106,40), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, func): # Duggar & Punjab
				self.spawnUnits(iBarbarian, (103,44),(106,40), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Duggar & Punjab
			
		# Mongols invade Eastern and Northern Iran
		if iGameTurn == getTurnForYear(1225):
			pUnit = self.spawnUnits(iBarbarian, (71,52),(84,43), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_BAIJU",()), con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
				pUnit.setHasPromotion(con.iFeintAttack, True)
			self.spawnUnits(iBarbarian, (71,52),(84,43), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Greater Khorasan
			self.spawnUnits(iBarbarian, (71,52),(84,43), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Greater Khorasan
		elif iGameTurn == getTurnForYear(1225)+2:
			self.spawnUnits(iBarbarian, (58,55),(70,45), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # North Iran
			self.spawnUnits(iBarbarian, (58,55),(70,45), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # North Iran

		# Mongols invade Caucasus
		if iGameTurn == getTurnForYear(1236)-1:
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_CAUCASUS_2", [con.iAbbasids, con.iByzantium, con.iArmenia, con.iGeorgia, con.iFatimids, con.iSeljuks, con.iRum, con.iKhwarezm, con.iAntioch, con.iCrusaders, con.iAyyubids])
		if iGameTurn == getTurnForYear(1236):
			self.spawnUnits(iBarbarian, (46,69),(63,56), con.iMongolHorseArcher, 6 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			self.spawnUnits(iBarbarian, (46,69),(63,56), con.iMongolHorseArcher, 6 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion)
			
		# More Mongol raids into Caucasus
		if iGameTurn >= getTurnForYear(1240) and iGameTurn <= getTurnForYear(1330):
			self.spawnUnits(iBarbarian, (46,69),(63,56), con.iMongolHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 10, 4, utils.outerInvasion)
		
		# Mongols invade Anatolia
		if iGameTurn == getTurnForYear(1241)-1:
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_ANATOLIA", [con.iAbbasids, con.iByzantium, con.iArmenia, con.iGeorgia, con.iFatimids, con.iSeljuks, con.iRum, con.iKhwarezm, con.iAntioch, con.iCrusaders, con.iAyyubids])
		elif iGameTurn == getTurnForYear(1241):
			self.spawnUnits(iBarbarian, (40,60),(42,57), con.iMongolHorseArcher, 4 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Lesser Armenia
			self.spawnUnits(iBarbarian, (40,60),(42,57), con.iMongolHorseArcher, 4 + iRand3 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Lesser Armenia
		elif iGameTurn == getTurnForYear(1241)+1:
			self.spawnUnits(iBarbarian, (33,61),(36,59), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Eastern
			self.spawnUnits(iBarbarian, (33,61),(36,59), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Eastern
		elif iGameTurn == getTurnForYear(1241)+2:
			self.spawnUnits(iBarbarian, (31,63),(33,58), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Eastern
			self.spawnUnits(iBarbarian, (31,63),(33,58), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Eastern
		elif iGameTurn == getTurnForYear(1241)+3:
			self.spawnUnits(iBarbarian, (27,58),(31,56), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Central
			self.spawnUnits(iBarbarian, (27,58),(31,56), con.iMongolHorseArcher, self.getInvasionForce(4, con.iRum), iGameTurn, 1, 0, utils.innerInvasion) # Central
		
		# Mongols invade Iran and Mesopotamia
		if iGameTurn == getTurnForYear(1250):
			self.spawnUnits(iBarbarian, (68,40),(76,32), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Kerman
			self.spawnUnits(iBarbarian, (68,40),(76,32), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Kerman
		elif iGameTurn == getTurnForYear(1250)+1:
			self.spawnUnits(iBarbarian, (60,48),(67,38), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Central Iran
			self.spawnUnits(iBarbarian, (60,48),(67,38), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Central Iran
		elif iGameTurn == getTurnForYear(1250)+2:
			self.spawnUnits(iBarbarian, (55,52),(63,41), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Western Iran
			self.spawnUnits(iBarbarian, (55,52),(63,41), con.iMongolHorseArcher, self.getInvasionForce(6, con.iSeljuks), iGameTurn, 1, 0, utils.outerInvasion) # Western Iran
			self.invasionAlert("TXT_KEY_INVASION_MONGOLS_MESOPOTAMIA", [con.iAbbasids, con.iByzantium, con.iArmenia, con.iGeorgia, con.iFatimids, con.iSeljuks, con.iRum, con.iKhwarezm, con.iAntioch, con.iCrusaders, con.iAyyubids])
		elif iGameTurn == getTurnForYear(1250)+3:
			pUnit = self.spawnUnits(iBarbarian, (52,44),(53,41), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, utils.innerInvasion)
			if pUnit:
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
				pUnit.setHasPromotion(con.iFeintAttack, True)
				pUnit.setHasPromotion(con.iEncirclement, True)
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_HULAGU_KHAN",()), con.iGreatGeneral5)
			self.spawnUnits(iBarbarian, (51,49),(53,45), con.iMongolHorseArcher, self.getInvasionForce(6, con.iAbbasids) + iRand1, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
			self.spawnUnits(iBarbarian, (52,44),(53,41), con.iMongolHorseArcher, self.getInvasionForce(6, con.iAbbasids) + iRand2, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
			self.spawnUnits(iBarbarian, (56,39),(58,36), con.iMongolHorseArcher, self.getInvasionForce(6, con.iAbbasids) + iRand3, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
			self.spawnUnits(iBarbarian, (52,40),(52,36), con.iMongolHorseArcher, 2 + iRand3 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
		elif iGameTurn == getTurnForYear(1250)+4:
			self.spawnUnits(iBarbarian, (51,49),(53,45), con.iMongolHorseArcher, 2 + iRand1, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
			self.spawnUnits(iBarbarian, (52,44),(53,41), con.iMongolHorseArcher, 2 + iRand2, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
			self.spawnUnits(iBarbarian, (56,39),(58,36), con.iMongolHorseArcher, 2 + iRand3, iGameTurn, 1, 0, utils.innerInvasion) # Mesopotamia
		
		# Mongol invasion of Syria
		if iGameTurn == getTurnForYear(1259):
			self.spawnUnits(iBarbarian, (35,55),(38,42), con.iMongolHorseArcher, 6 + iRand1 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion) # Syria
			self.spawnUnits(iBarbarian, (35,49),(38,42), con.iMongolHorseArcher, 6 + iRand2 + iRand3 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion) # Syria
		
		# Raids against Syria
		if iGameTurn >= getTurnForYear(1265) and iGameTurn <= getTurnForYear(1330):
			self.spawnUnits(iBarbarian, (36,54),(43,40), con.iMongolHorseArcher, self.getInvasionForce(2, con.iMamluks), iGameTurn, 8, 0, utils.outerInvasion) # Northern Syria

		# Chagatai khanate invades India
		if iGameTurn == getTurnForYear(1280):
			self.spawnUnits(iBarbarian, (98,47),(101,44), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Gandhar
			pUnit = self.spawnUnits(iBarbarian, (98,47),(101,44), con.iMongolHorseArcher, 1, iGameTurn, 1, 0, utils.innerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_DUWA_KHAN",()), con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iFlanking1, True)
				pUnit.setHasPromotion(con.iFlanking2, True)
				pUnit.setHasPromotion(con.iFeintAttack, True)
		if iGameTurn == getTurnForYear(1292)-1:
			self.invasionAlert("TXT_KEY_INVASION_CHAGATAI_INDIA", [con.iSamanids, con.iSeljuks, con.iGhaznavids, con.iGhorids, con.iKhwarezm, con.iChauhan, con.iGujarat, con.iSindh])
		if iGameTurn == getTurnForYear(1292):
			self.spawnUnits(iBarbarian, (103,44),(106,40), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.innerInvasion) # Duggar & Punjab
		if iGameTurn == getTurnForYear(1292)+2:
			self.spawnUnits(iBarbarian, (104,44),(109,35), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion) # Northern India
		if iGameTurn == getTurnForYear(1292)+3:
			self.spawnUnits(iBarbarian, (104,44),(109,35), con.iMongolHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion) # Northern India
			
		# Hashids (Yemen)
		if iGameTurn > getTurnForYear(1000):
			self.spawnUnits(iBarbarian, (45,9),(58,1), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 40, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HASHID",()), [con.iDesertAdaptation])
		
		# Bedouins in Arabian Peninsula
		if iGameTurn >= getTurnForYear(900) and iGameTurn < getTurnForYear(1100):
			self.spawnUnits(iBarbarian, (37,46),(53,9), self.getRandomUnit(bedouinBarbs1), 1, iGameTurn, 25, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # center
			self.spawnUnits(iBarbarian, (43,10),(59,1), self.getRandomUnit(bedouinBarbs1), 1, iGameTurn, 30, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # yemen
			self.spawnUnits(iBarbarian, (34,34),(40,20), self.getRandomUnit(bedouinBarbs1), 1, iGameTurn, 30, 24, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HASHEMITE",()), [con.iDesertAdaptation]) # hejaz
		elif iGameTurn >= getTurnForYear(1100) and iGameTurn < getTurnForYear(1200):
			self.spawnUnits(iBarbarian, (34,48),(38,33), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 30, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # syria
			self.spawnUnits(iBarbarian, (37,46),(53,9), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 25, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # center
			self.spawnUnits(iBarbarian, (43,10),(59,1), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 30, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # yemen
			self.spawnUnits(iBarbarian, (34,34),(40,20), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 30, 24, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HASHEMITE",()), [con.iDesertAdaptation]) # hejaz
		elif iGameTurn >= getTurnForYear(1200):
			self.spawnUnits(iBarbarian, (34,48),(38,33), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 25, 15, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # syria
			self.spawnUnits(iBarbarian, (37,46),(53,9), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 25, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # center
			self.spawnUnits(iBarbarian, (43,10),(59,1), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 30, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # yemen
			self.spawnUnits(iBarbarian, (67,22),(75,7), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 25, 10, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation]) # oman
			self.spawnUnits(iBarbarian, (34,34),(40,20), self.getRandomUnit(bedouinBarbs3), 1, iGameTurn, 30, 24, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_HASHEMITE",()), [con.iDesertAdaptation]) # hejaz
		
		# Bedouins in Nubia
		if iGameTurn >= getTurnForYear(850) and iGameTurn <= getTurnForYear(1000):
			self.spawnUnits(iBarbarian, (18,18),(25,6), self.getRandomUnit(bedouinBarbs1), 1, iGameTurn, 20, 19, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (29,20),(33,7), self.getRandomUnit(bedouinBarbs1), 1, iGameTurn, 30, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
		if iGameTurn >= getTurnForYear(1000) and iGameTurn <= getTurnForYear(1300):
			self.spawnUnits(iBarbarian, (18,18),(25,6), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 20, 19, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (29,20),(33,7), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 16, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
		if iGameTurn >= getTurnForYear(1317) and iGameTurn <= getTurnForYear(1350):
			self.spawnUnits(iBarbarian, (18,18),(25,6), self.getRandomUnit(bedouinBarbs3), 1 + iRand1 + iHandicap, iGameTurn, 4, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (18,18),(25,6), self.getRandomUnit(bedouinBarbs3), 1 + iRand2 + iHandicap, iGameTurn, 4, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (18,18),(25,6), self.getRandomUnit(bedouinBarbs2), 1, iGameTurn, 4, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
		if iGameTurn > getTurnForYear(1350):
			self.spawnUnits(iBarbarian, (18,18),(29,7), self.getRandomUnit(bedouinBarbs3), 1 + iRand1 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_BEDOUIN",()), [con.iDesertAdaptation])
		
		# Generic Turkomans
		if iGameTurn >= getTurnForYear(1000) and iGameTurn < getTurnForYear(1300):
			self.spawnUnits(iBarbarian, (77,69),(93,49), con.iHorseArcher, 1, iGameTurn, 15, 7, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
			self.spawnUnits(iBarbarian, (69,54),(83,37), con.iHorseArcher, 1, iGameTurn, 25, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
		if iGameTurn >= getTurnForYear(1300) and iGameTurn < getTurnForYear(1500):
			self.spawnUnits(iBarbarian, (77,69),(93,49), con.iHeavyHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 15, 9, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
			self.spawnUnits(iBarbarian, (69,54),(83,37), con.iHeavyHorseArcher, 2 + iHandicap, iGameTurn, 25, 16, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
		if iGameTurn >= getTurnForYear(1510):
			self.spawnUnits(iBarbarian, (77,69),(93,49), con.iHeavyHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 10, 2, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
			self.spawnUnits(iBarbarian, (69,54),(83,37), con.iHeavyHorseArcher, 2 + iHandicap, iGameTurn, 20, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()))
		
		# Kara Koyunlu
		if iGameTurn == getTurnForYear(1370): # Herat
			self.spawnUnits(iBarbarian, (82,48),(86,41), self.getRandomUnit(turkomanBarbs), 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARA_KOYUNLU",()), [con.iFlanking1])
			self.spawnUnits(iBarbarian, (82,48),(86,41), self.getRandomUnit(turkomanBarbs), 2 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARA_KOYUNLU",()), [con.iFlanking1])
		if iGameTurn >= getTurnForYear(1373) and iGameTurn < getTurnForYear(1468): # Tabriz
			self.spawnUnits(iBarbarian, (51,57),(59,42), self.getRandomUnit(turkomanBarbs), 2 + iRand1 + iHandicap, iGameTurn, 12, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARA_KOYUNLU",()), [con.iFlanking1])
			self.spawnUnits(iBarbarian, (51,57),(59,42), self.getRandomUnit(turkomanBarbs), 2 + iRand2 + iHandicap, iGameTurn, 12, 1, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_KARA_KOYUNLU",()), [con.iFlanking1])
		
		# Pseudo-Timurids
		if iGameTurn == getTurnForYear(1398)-1 and iHuman != con.iTimurids: # Northern India
			self.spawnUnits(iBarbarian, (103,44),(109,35), con.iHeavyHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKO_MONGOL",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (104,44),(109,35), con.iHeavyHorseArcher, 3 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKO_MONGOL",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
		if iGameTurn == getTurnForYear(1399)-1: # Eastern Anatolia & Syria
			self.spawnUnits(iBarbarian, (41,58),(51,49), con.iHeavyHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKO_MONGOL",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (35,55),(40,37), con.iHeavyHorseArcher, 3 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKO_MONGOL",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
		if iGameTurn == getTurnForYear(1400)-1 and iHuman != con.iTimurids: # Caucasus
			self.spawnUnits(iBarbarian, (50,63),(59,52), con.iHeavyHorseArcher, 2 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (47,61),(59,52), con.iHeavyHorseArcher, 2 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
		if iGameTurn == getTurnForYear(1401)-1: # Anatolia
			self.spawnUnits(iBarbarian, (26,65),(41,55), con.iHeavyHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (26,65),(43,55), con.iHeavyHorseArcher, 1 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
		if iGameTurn == getTurnForYear(1402)-1: # Anatolia
			self.spawnUnits(iBarbarian, (26,65),(41,55), con.iHeavyHorseArcher, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (26,65),(43,55), con.iHeavyHorseArcher, 3 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TURKOMAN",()), [con.iCombat1, con.iFlanking1, con.iFlanking2])
		
		# Uzbek invasion
		if iGameTurn >= getTurnForYear(1500)-1 and iGameTurn <= getTurnForYear(1507)-1:
			if iGameTurn == getTurnForYear(1500)-1:
				pUnit = self.spawnUnits(iBarbarian, (87,64),(94,55), con.iHeavyHorseArcher, 1, iGameTurn, 1, 0, utils.outerInvasion)
				if pUnit:
					pUnit.setHasPromotion(con.iFlanking1, True)
					self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_MUHAMMAD_SHAYBANI",()))
			self.spawnUnits(iBarbarian, (77,69),(93,49), con.iHeavyHorseArcher, self.getInvasionForce(4, con.iTimurids), iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UZBEK",()))
			self.spawnUnits(iBarbarian, (87,64),(94,55), con.iHeavyHorseArcher, self.getInvasionForce(4, con.iTimurids), iGameTurn, 2, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UZBEK",()))
			self.spawnUnits(iBarbarian, (91,54),(98,49), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iTimurids), iGameTurn, 3, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UZBEK",()))
			if iGameTurn == getTurnForYear(1500)-1:
				self.spawnUnits(iBarbarian, (77,69),(93,49), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iTimurids), iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UZBEK",()))
				self.spawnUnits(iBarbarian, (87,64),(94,55), con.iHeavyHorseArcher, self.getInvasionForce(3, con.iTimurids), iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_UZBEK",()))
		
		# Afghans
		if iGameTurn >= getTurnForYear(1000) and iGameTurn <= getTurnForYear(1370):
			self.spawnUnits(iBarbarian, (87,47),(94,33), self.getRandomUnit(afghanBarbs), 1, iGameTurn, 24, 8, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_AFGHAN",()), [con.iGuerilla1])
		if iGameTurn >= getTurnForYear(1400) and iGameTurn <= getTurnForYear(1500):
			self.spawnUnits(iBarbarian, (87,47),(94,33), con.iPashtunWarrior, 1 + iRand1 + iHandicap, iGameTurn, 20, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK)
			self.spawnUnits(iBarbarian, (87,47),(94,33), con.iHeavyHorseArcher, 1 + iRand1 + iHandicap, iGameTurn, 20, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_TAJIK",()))
		if iGameTurn >= getTurnForYear(1550):
			self.spawnUnits(iBarbarian, (87,47),(94,33), con.iPashtunWarrior, 1 + iRand2 + iHandicap, iGameTurn, 20, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK)
			self.spawnUnits(iBarbarian, (87,47),(94,33), con.iPashtunCavalry, 1, iGameTurn, 20, 4, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK)
		
		# Sher Shah Suri
		if iGameTurn == getTurnForYear(1537):
			iHumanModifier = 0
			if iHuman in [con.iMughals, con.iChauhan, con.iGhorids]:
				iHumanModifier = 1 + iRand1
			pUnit = self.spawnUnits(iBarbarian, (111,36),(114,21), con.iAfghanInfantry, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_SHER_SHAH",()), con.iGreatGeneral5)
				pUnit.setHasPromotion(con.iCityRaider1, True)
				pUnit.setHasPromotion(con.iCityRaider2, True)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				if iHumanModifier > 0:
					pUnit.setHasPromotion(con.iCombat3, True)
			self.spawnUnits(iBarbarian, (111,36),(114,21), con.iAfghanPikeman, 1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
			self.spawnUnits(iBarbarian, (111,36),(114,21), con.iAfghanInfantry, 1 + iHumanModifier + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCityRaider1])
		
		# Hemu
		if iGameTurn == getTurnForYear(1555):
			iHumanModifier = 0
			if iHuman in [con.iMughals, con.iChauhan, con.iGhorids]:
				iHumanModifier = 1 + iRand1
			pUnit = self.spawnUnits(iBarbarian, (111,36),(114,21), con.iHeavyWarElephant, 1, iGameTurn, 1, 0, utils.outerInvasion)
			if pUnit:
				self.makeLeader(pUnit, localText.getText("TXT_KEY_BARB_HEMU",()), con.iGreatGeneral4)
				pUnit.setHasPromotion(con.iCombat1, True)
				pUnit.setHasPromotion(con.iCombat2, True)
				pUnit.setHasPromotion(con.iCombat3, True)
				if iHumanModifier > 0:
					pUnit.setHasPromotion(con.iCombat4, True)
			self.spawnUnits(iBarbarian, (111,36),(114,21), con.iAfghanPikeman, 1 + iHumanModifier + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1])
			self.spawnUnits(iBarbarian, (111,36),(114,21), con.iAfghanInfantry, 1 + iHumanModifier + iRand3 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCityRaider1])
		
		# Sikhs
		if iGameTurn > getTurnForYear(1627):
			self.spawnUnits(iBarbarian, (100,31),(106,41), con.iHeavySwordsman_Rajput, 1, iGameTurn, 12, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_SIKH",()), [con.iCombat1])
			
		# Funj (Sennar)
		if iGameTurn == getTurnForYear(1504):
			self.spawnUnits(iBarbarian, (24,6),(35,0), con.iHeavyLancer, 3 + iRand1 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_FUNJ",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (24,6),(35,0), con.iHeavyLancer, 3 + iRand2 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_FUNJ",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (24,6),(35,0), con.iMarksman_Bedouin, 2 + iRand3 + iHandicap, iGameTurn, 1, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_FUNJ",()), [con.iDesertAdaptation])
		if iGameTurn > getTurnForYear(1504):
			self.spawnUnits(iBarbarian, (24,6),(35,0), con.iHeavyLancer, 1, iGameTurn, 16, 12, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_FUNJ",()), [con.iDesertAdaptation])
			self.spawnUnits(iBarbarian, (24,6),(35,0), con.iMarksman_Bedouin, 1, iGameTurn, 12, 6, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_FUNJ",()), [con.iDesertAdaptation])
		
		# Rajputs
		if iGameTurn < getTurnForYear(1200):
			self.spawnUnits(iBarbarian, (102,29),(114,13), con.iSwordsman_Indian, 1, iGameTurn, 18, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_RAJPUT",()))
		if iGameTurn >= getTurnForYear(1200) and iGameTurn < getTurnForYear(1500):
			self.spawnUnits(iBarbarian, (102,29),(114,13), con.iRajputCavalry, 1, iGameTurn, 30, 15, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK)
			self.spawnUnits(iBarbarian, (102,29),(114,13), con.iHeavySwordsman_Rajput, 1, iGameTurn, 30, 10, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_RAJPUT",()))
		if iGameTurn >= getTurnForYear(1500):
			self.spawnUnits(iBarbarian, (104,30),(114,13), con.iRajputCavalry, 1 + iRand1, iGameTurn, 10, 3, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iCombat1, con.iFlanking1, con.iFlanking2])
			self.spawnUnits(iBarbarian, (104,30),(114,13), con.iHeavySwordsman_Rajput, 1 + iRand2, iGameTurn, 12, 5, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_RAJPUT",()), [con.iCombat1, con.iShock])
		
		# Maratha
		if iGameTurn >= getTurnForYear(1640) and iGameTurn < getTurnForYear(1660):
			self.spawnUnits(iBarbarian, (106,18),(114,8), self.getRandomUnit([con.iMarathaCavalry, con.iMarathaWarrior]), 1, iGameTurn, 8, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iGuerilla1])
		if iGameTurn >= getTurnForYear(1660):
			self.spawnUnits(iBarbarian, (106,18),(114,8), self.getRandomUnit([con.iMarathaCavalry, con.iMarathaWarrior]), 1, iGameTurn, 8, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, "", [con.iGuerilla1, con.iGuerilla2])
			self.spawnUnits(iBarbarian, (106,18),(114,8), con.iArquebusier_Indian, 1, iGameTurn, 8, 0, utils.outerInvasion, UnitAITypes.UNITAI_ATTACK, localText.getText("TXT_KEY_BARB_MARATHA",()), [con.iGuerilla1, con.iGuerilla2])
		
		# Mediterranean pirates
		if iGameTurn > getTurnForYear(900) and iGameTurn < getTurnForYear(1250):
			self.spawnUnits(iBarbarian, (15,60),(33,36), con.iWarGalley, 1, iGameTurn, 20, 0, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, localText.getText("TXT_KEY_BARB_PIRATE",()), [], [con.iCoast, con.iSea])
		if iGameTurn > getTurnForYear(1250):
			self.spawnUnits(iBarbarian, (15,60),(33,36), con.iWarGalley, 1, iGameTurn, 15, 0, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, localText.getText("TXT_KEY_BARB_PIRATE",()), [], [con.iCoast, con.iSea])
		
		# Indian Sea pirates
		if getTurnForYear(1100) > iGameTurn > getTurnForYear(1000):
			self.spawnUnits(iBarbarian, (32,33),(106,0), con.iDhow, 1, iGameTurn, 20, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, localText.getText("TXT_KEY_BARB_PIRATE",()), [], [con.iCoast, con.iSea])
		if getTurnForYear(1250) > iGameTurn > getTurnForYear(1100):
			self.spawnUnits(iBarbarian, (32,33),(106,0), con.iDhow, 1, iGameTurn, 16, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, localText.getText("TXT_KEY_BARB_PIRATE",()), [con.iCombat1], [con.iCoast, con.iSea])
		if iGameTurn > getTurnForYear(1250):
			self.spawnUnits(iBarbarian, (32,33),(106,0), con.iDhow, 1, iGameTurn, 15, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA, localText.getText("TXT_KEY_BARB_PIRATE",()), [con.iCombat1, con.iCombat2], [con.iCoast, con.iSea])
		
		# Portugal
		if iGameTurn == getTurnForYear(1507):
			tPlot = (66, 1) # Soqotra
			tSeaPlot = utils.findSeaPlots(tPlot, 3, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 4, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				cityOwner = gc.getMap().plot(tPlot[0], tPlot[1]).getOwner()
				gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(cityOwner, True, -1)
			
			tPlot = (75, 20) # Muscat
			tSeaPlot = utils.findSeaPlots(tPlot, 4, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 3, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 6, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				cityOwner = gc.getMap().plot(tPlot[0], tPlot[1]).getOwner()
				gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(cityOwner, True, -1)
			
			tPlot = (72, 28) # Hormuz
			tSeaPlot = utils.findSeaPlots(tPlot, 4, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 3, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 6, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				cityOwner = gc.getMap().plot(tPlot[0], tPlot[1]).getOwner()
				gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(cityOwner, True, -1)
				
		if iGameTurn == getTurnForYear(1513):
			tPlot = (48, 1) # Aden
			tSeaPlot = utils.findSeaPlots(tPlot, 3, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 3, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 6, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				for tPlot in [(48,1), (47,1), (47,2), (46,2), (46,3)]:
					pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
					if pPlot.isCity():
						gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(pPlot.getOwner(), True, -1)
						break

		if iGameTurn == getTurnForYear(1515):
			tPlot = (63, 27) # Bahrain
			tSeaPlot = utils.findSeaPlots(tPlot, 3, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 4, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				for tPlot in [(63,25), (60,26)]:
					pPlot = gc.getMap().plot(tPlot[0], tPlot[1])
					if pPlot.isCity():
						gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(pPlot.getOwner(), True, -1)
						break
		
		if iGameTurn == getTurnForYear(1516):
			tPlot = (70, 27) # Hormuz
			tSeaPlot = utils.findSeaPlots(tPlot, 3, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 3, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2,))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 6, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				cityOwner = gc.getMap().plot(72, 28).getOwner()
				gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(cityOwner, True, -1)
						
		if iGameTurn == getTurnForYear(1531):
			tPlot = (103, 11) # Bombay
			tSeaPlot = utils.findSeaPlots(tPlot, 3, con.iPortugal)
			if tSeaPlot:
				utils.makeUnit(con.iCarrack, con.iPortugal, tSeaPlot, 3, UnitAITypes.UNITAI_ASSAULT_SEA, (con.iCombat1, con.iCombat2))
				utils.makeUnit(con.iCannon, con.iPortugal, tSeaPlot, 2, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2))
				utils.makeUnit(con.iHeavySwordsman, con.iPortugal, tSeaPlot, 6, UnitAITypes.UNITAI_ATTACK_CITY, (con.iCityRaider1, con.iCityRaider2, con.iAmphibious))
				utils.makeUnit(con.iArquebusier, con.iPortugal, tSeaPlot, 1, UnitAITypes.UNITAI_ATTACK, (con.iCombat1, con.iCombat2, con.iAmphibious))
				cityOwner = gc.getMap().plot(tPlot[0], tPlot[1]).getOwner()
				gc.getTeam(gc.getPlayer(con.iPortugal).getTeam()).declareWar(cityOwner, True, -1)
		
		# Further support for Portugal
		if iGameTurn > getTurnForYear(1507):
			if gc.getPlayer(con.iPortugal).getNumCities() > 0:
				if iGameTurn % 20 == 4:
					capital = gc.getPlayer(con.iPortugal).getCapitalCity()
					if capital.plot().getNumUnits() < 5:
						utils.makeUnit(con.iPikeman, con.iPortugal, (capital.getX(), capital.getY()), 1, UnitAITypes.UNITAI_COUNTER)
				elif iGameTurn % 20 == 14:
					capital = gc.getPlayer(con.iPortugal).getCapitalCity()
					if capital.plot().getNumUnits() < 5:
						utils.makeUnit(con.iArquebusier, con.iPortugal, (capital.getX(), capital.getY()), 1, UnitAITypes.UNITAI_CITY_DEFENSE)
		
		# Portuguese warships
		if iGameTurn >= getTurnForYear(1540) and iGameTurn < getTurnForYear(1640):
			self.spawnUnits(con.iPortugal, (32,33),(106,0), con.iCarrack, 1, iGameTurn, 15, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA)
		if iGameTurn >= getTurnForYear(1640):
			self.spawnUnits(con.iPortugal, (32,33),(106,0), con.iFrigate, 1, iGameTurn, 15, 7, utils.outerSeaSpawn, UnitAITypes.UNITAI_ATTACK_SEA)
		
		# Free Varangian Guard for the AI
		if iGameTurn == getTurnForYear(1081) or iGameTurn == getTurnForYear(1265):
			if utils.getHumanID() != con.iByzantium and gc.getMap().plot(con.tConstantinople[0], con.tConstantinople[1]).getOwner() == con.iByzantium:
				utils.makeUnit(con.iVarangianGuard, con.iByzantium, (con.tConstantinople[0], con.tConstantinople[1]), 1, UnitAITypes.UNITAI_CITY_DEFENSE, (con.iMercenary, con.iCombat1, con.iCombat2))







	def invasionAlert(self, textKey, playerList = []):
		
		iHuman = utils.getHumanID()
		if utils.isActive(iHuman):
			if not playerList or iHuman in playerList:
				szBuffer = localText.getText(textKey, ())
				CyInterface().addMessage(iHuman, False, con.iDuration, szBuffer, "AS2D_CIVIC_ADOPT", InterfaceMessageTypes.MESSAGE_TYPE_MAJOR_EVENT, None, gc.getInfoTypeForString("COLOR_WHITE"), -1, -1, False, False)


	def foundCity(self, iCiv, sName, iX, iY, lReligions=[]):
		
		if not self.checkRegion(iX, iY):
			return None
		
		pCiv = gc.getPlayer(iCiv)
		pCiv.initCity(iX, iY)
		city = gc.getMap().plot(iX, iY).getPlotCity()
		
		if not city or city.isNone():
			return None
		
		city.setName(sName, False)
		
		if utils.getYear() < 1050:
			pCiv.initUnit(con.iSpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		else:
			pCiv.initUnit(con.iHeavySpearman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		
		if utils.getYear() < 1000:
			pCiv.initUnit(con.iArcher, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		elif utils.getYear() < 1250:
			pCiv.initUnit(con.iMarksman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			city.setNumRealBuilding(con.iWalls, 1)
		else:
			pCiv.initUnit(con.iMarksman, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			city.setNumRealBuilding(con.iWalls, 1)
			city.setNumRealBuilding(con.iCastle, 1)
		
		UnitArtStyler.updateUnitArtAtPlot(city.plot())
		
		for iReligion in lReligions:
			city.setHasReligion(iReligion, True, False, False)
		
		return city


	# from Rhye's, simplified
	def checkRegion(self, plotX, plotY):
		
		cityPlot = gc.getMap().plot(plotX, plotY)
		iNumUnitsInAPlot = cityPlot.getNumUnits()
		
		#checks if the plot already belongs to someone
		if cityPlot.isOwned():
			if cityPlot.getOwner() != iBarbarian:
				return False
		
		#checks if there's a unit on the plot
		if iNumUnitsInAPlot:
			for i in range(iNumUnitsInAPlot):
				unit = cityPlot.getUnit(i)
				iOwner = unit.getOwner()
				if iOwner == iBarbarian:
					return False
		
		#checks the surroundings and allows only AI units
		for x in range(plotX-1, plotX+2):
			for y in range(plotY-1, plotY+2):
				currentPlot = gc.getMap().plot(x,y)
				if currentPlot.isCity():
					return False
				iNumUnitsInAPlot = currentPlot.getNumUnits()
				if iNumUnitsInAPlot:
					for i in range(iNumUnitsInAPlot):
						unit = currentPlot.getUnit(i)
						iOwner = unit.getOwner()
						pOwner = gc.getPlayer(iOwner)
						if pOwner.isHuman():
							return False
		
		return True


	def spawnUnits(self, iCiv, tTopLeft, tBottomRight, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, eUnitAIType = UnitAITypes.UNITAI_ATTACK, prefix = 0, promotionList = [], argsList = []):
		
		if iNumUnits <= 0: # edead
			return None
		pUnit = None # edead
		if (iTurn % utils.getTurns(iPeriod) == iRest):
			dummy, plotList = utils.squareSearch( tTopLeft, tBottomRight, function, argsList )
			if (len(plotList)):
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn units')
				result = plotList[rndNum]
				if (result):
					pUnit = utils.makeUnit(iUnitType, iCiv, result, iNumUnits, eUnitAIType, promotionList, prefix) # edead: pass the object
					# if eUnitAIType == UnitAITypes.UNITAI_PILLAGE: # edead
						# pUnit.getGroup().setActivityType(ActivityTypes.ACTIVITY_SLEEP) # edead: fortify rebels
		return pUnit # edead: pass the object


	def getRandomUnit(self, unitList):
		
		return unitList[gc.getGame().getSorenRandNum(len(unitList), 'Random unit')]

		
	def isChristianRegion(self, regionID):
		
		bFound = False
		plotList = utils.getRegionPlotList([regionID])
		for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					iOwner = pCurrent.getPlotCity().getOwner()
					if iOwner not in [con.iByzantium, con.iGeorgia, con.iArmenia, con.iAntioch, con.iCrusaders]:
						return False
					else:
						bFound = True
		return bFound

		
	def makeLeader(self, pUnit, szName, iLeaderType=con.iGreatGeneral):
		
		if pUnit:
			pUnit.setHasPromotion(con.iLeader, True)
			pUnit.setExperience(20, -1)
			pUnit.setLeaderUnitType(iLeaderType)
			pUnit.setName(szName)
	
	
	def getInvasionForce(self, iBaseNumUnits, iCiv):
		
		iNumUnits = iBaseNumUnits + gc.getGame().getHandicapType() - 1 + gc.getGame().getSorenRandNum(2, 'Random invasion force')
		iNumCities = gc.getPlayer(iCiv).getNumCities()
		if iNumCities >= 14:
			iNumUnits += 3
		elif iNumCities >= 11:
			iNumUnits += 2
		elif iNumCities >= 8:
			iNumUnits += 1
		return iNumUnits

