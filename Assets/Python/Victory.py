# Rhye's and Fall of Civilization - Historical Victory Goals
# The Sword of Islam - Religious Victory Goals


from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
localText = CyTranslator()

# initialise player variables
iByzantium = con.iByzantium
iMakuria = con.iMakuria
iAbbasids = con.iAbbasids
iChauhan = con.iChauhan
iMalwa = con.iMalwa
iSamanids = con.iSamanids
iArmenia = con.iArmenia
iYemen = con.iYemen
iBuyids = con.iBuyids
iFatimids = con.iFatimids
iGhaznavids = con.iGhaznavids
iGujarat = con.iGujarat
iGeorgia = con.iGeorgia
iSeljuks = con.iSeljuks
iSindh = con.iSindh
iRum = con.iRum
iKhwarezm = con.iKhwarezm
iAntioch = con.iAntioch
iCrusaders = con.iCrusaders
iZengids = con.iZengids
iGhorids = con.iGhorids
iOman = con.iOman
iAyyubids = con.iAyyubids
iMamluks = con.iMamluks
iOttomans = con.iOttomans
iBahmanids = con.iBahmanids
iTimurids = con.iTimurids
iAkKoyunlu = con.iAkKoyunlu
iSafavids = con.iSafavids
iPortugal = con.iPortugal
iMughals = con.iMughals

iReligiousVictory = 7
iHistoricalVictory = 8


class Victory:


	def checkPlayerTurn(self, iGameTurn, iPlayer):
		
		iHuman = utils.getHumanID()
		pPlayer = gc.getPlayer(iPlayer)
		
		# HISTORICAL VICTORY
		if gc.getGame().isVictoryValid(iHistoricalVictory):
		
			if iPlayer == iByzantium:
				if pPlayer.isAlive():
					
					# Byzantine UHV1: Make Constantinople the city with highest culture in 1000
					if iGameTurn == getTurnForYear(1000):
						if self.isTopCityCulture(iByzantium, con.tConstantinople):
							sd.setGoal(iByzantium, 0, 1)
						else:
							sd.setGoal(iByzantium, 0, 0)
					
					# Byzantine UHV2: control 15 provinces in 1290
					if iGameTurn == getTurnForYear(1290):
						if self.getNumProvinces(iByzantium) >= 15:
							sd.setGoal(iByzantium, 1, 1)
						else:
							sd.setGoal(iByzantium, 1, 0)
					
					# Byzantine UHV3: be the wealthiest civ in 1500
					if iGameTurn == getTurnForYear(1500):
						if self.isHighestGold(iByzantium) and utils.isActive(iHuman):
							sd.setGoal(iByzantium, 2, 1)
						else:
							sd.setGoal(iByzantium, 2, 0)
			
			elif iPlayer == iAbbasids:
				if pPlayer.isAlive():
					
					# Abbasid UHV1: Control 3 Holy Shrines in 950
					if iGameTurn == getTurnForYear(950):
						if self.getNumShrines(iAbbasids) >= 3:
							sd.setGoal(iAbbasids, 0, 1)
						else:
							sd.setGoal(iAbbasids, 0, 0)
					
					# Abbasid UHV2: Best tech and culture in 950
					if iGameTurn == getTurnForYear(950):
						if self.isTopTech(iAbbasids) and self.isTopCulture(iAbbasids):
							sd.setGoal(iAbbasids, 1, 1)
						else:
							sd.setGoal(iAbbasids, 1, 0)
					
					# Abbasid UHV3: Spread Sunni faith to 50% by 1250 AD
					if sd.getGoal(iAbbasids, 2) == -1:
						if iGameTurn <= getTurnForYear(1250):
							religionPercent = gc.getGame().calculateReligionPercent(con.iSunni)
							if religionPercent >= 50.0:
								if utils.isActive(iHuman):
									sd.setGoal(iAbbasids, 2, 1)
						else:
							sd.setGoal(iAbbasids, 2, 0)
			
			elif iPlayer == iChauhan:
				if pPlayer.isAlive():
					
					# Chauhan UHV1: Do not allow Islam in India (excl. Sindh and Gandhar) in 1200
					if iGameTurn == getTurnForYear(1200):
						bSuccess = self.isFreeOfIslam([con.rDuggar, con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rKarnataka])
						if bSuccess:
							sd.setGoal(iChauhan, 0, 1)
						else:
							sd.setGoal(iChauhan, 0, 0)
					
					# Chauhan UHV2: Gain 3 Great Generals by 1200
					if iGameTurn == getTurnForYear(1200)+1:
						if sd.getGoal(iChauhan, 1) == -1:
							sd.setGoal(iChauhan, 1, 0)
					
					# Chauhan UHV1: Do not allow Islam in India in 1400
					if iGameTurn == getTurnForYear(1400):
						bSuccess = self.isFreeOfIslam([con.rDuggar, con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rKarnataka, con.rGandhar, con.rSindh])
						if bSuccess:
							sd.setGoal(iChauhan, 2, 1)
						else:
							sd.setGoal(iChauhan, 2, 0)
			
			elif iPlayer == iMalwa:
				if pPlayer.isAlive():
					
					# Malwa UHV1: Build 3 Sanskrit Colleges and 3 Hindu Mandirs by 1060, see onBuildingBuilt()
					if iGameTurn == getTurnForYear(1060)+1:
						if sd.getGoal(iMalwa, 0) == -1:
							sd.setGoal(iMalwa, 0, 0)
					
					# Malwa UHV2: Settle 5 different Great People in your capital by 1300
					if sd.getGoal(iMalwa, 1) == -1:
						if iGameTurn <= getTurnForYear(1300):
							iCount = 0
							if pPlayer.getNumCities() > 0:
								capital = pPlayer.getCapitalCity()
								if self.countUniqueGreatPeople((capital.getX(), capital.getY())) >= 5:
									sd.setGoal(iMalwa, 1, 1)
						else:
							sd.setGoal(iMalwa, 1, 0)
					
					# Malwa UHV3: Have a city with legendary culture by 1300 AD
					if sd.getGoal(iMalwa, 2) == -1:
						if iGameTurn <= getTurnForYear(1300):
							if self.isHasLegendaryCity(iMalwa):
								sd.setGoal(iMalwa, 2, 1)
						else:
							sd.setGoal(iMalwa, 2, 0)
			
			elif iPlayer == iMakuria:
				if pPlayer.isAlive():
					
					# Makurian UHV1: Obtain 6 luxury resources by 1000
					if sd.getGoal(iMakuria, 0) == -1:
						if iGameTurn <= getTurnForYear(1000):
							if self.getNumLuxuries(iMakuria) >= 6:
								sd.setGoal(iMakuria, 0, 1)
						else:
							sd.setGoal(iMakuria, 0, 0)
					
					# Makurian UHV2: Never lose a city before 1200, see onCityAcquired()
					if iGameTurn == getTurnForYear(1200):
						if sd.getGoal(iMakuria, 1) == -1:
							sd.setGoal(iMakuria, 1, 1)
					
					# Makurian UHV3: Mediterranean & Red Sea Access in 1300
					if iGameTurn == getTurnForYear(1300):
						bMediterranean, bRedSea = self.getMakurianUHV3()
						if bMediterranean and bRedSea:
							sd.setGoal(iMakuria, 2, 1)
						else:
							sd.setGoal(iMakuria, 2, 0)
			
			elif iPlayer == iSamanids:
				if pPlayer.isAlive():
					
					# Samanid UHV1: Best culture in 1000
					if iGameTurn == getTurnForYear(1000):
						if self.isTopCulture(iSamanids):
							sd.setGoal(iSamanids, 0, 1)
						else:
							sd.setGoal(iSamanids, 0, 0)
					
					# Samanid UHV2: Never lose a city before 1070, see onCityAcquired()
					if iGameTurn == getTurnForYear(1070):
						if sd.getGoal(iSamanids, 1) == -1:
							sd.setGoal(iSamanids, 1, 1)
					
					# Samanid UHV3: Gain control of at least 8 provinces before 1140
					if sd.getGoal(iSamanids, 2) == -1:
						if iGameTurn <= getTurnForYear(1140):
							if pPlayer.getNumCities() >= 8: # efficiency
								if self.getNumProvinces(iSamanids) >= 8:
									sd.setGoal(iSamanids, 2, 1)
						else:
							sd.setGoal(iSamanids, 2, 0)
			
			elif iPlayer == iArmenia:
				if pPlayer.isAlive():
				
					# Armenian UHV1: Build an Orthodox Cathedral by 1045
					if sd.getGoal(iArmenia, 0) == -1:
						if iGameTurn == getTurnForYear(1045)+1:
							sd.setGoal(iArmenia, 0, 0)
					
					# Armenian UHV3: Control provinces in 1200
					if iGameTurn == getTurnForYear(1200):
						bControl = True
						regionList = [con.rGreaterArmenia, con.rLesserArmenia, con.rKars, con.rVaspurakan]
						for regionID in regionList:
							if not utils.checkRegionControl(iArmenia, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iArmenia, 1, 1)
						else:
							sd.setGoal(iArmenia, 1, 0)
					
					# Armenian UHV3: Have at least 20,000 Culture by 1330
					if sd.getGoal(iArmenia, 2) == -1:
						if iGameTurn <= getTurnForYear(1330):
							if pPlayer.isHuman(): # efficiency
								if pPlayer.countTotalCulture() >= utils.getTurns(25000):
									sd.setGoal(iArmenia, 2, 1)
						else:
							sd.setGoal(iArmenia, 2, 0)


			elif iPlayer == iYemen:
				if pPlayer.isAlive():
				
					# Yemen UHV1: Build 3 Sufi Shrines by 1140
					if sd.getGoal(iYemen, 0) == -1:
						if iGameTurn == getTurnForYear(1140)+1:
							sd.setGoal(iYemen, 0, 0)
					
					# Yemen UHV2: Hold the title of Sharif of Hejaz in 1250
					if iGameTurn == getTurnForYear(1250):
						if gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iSharif):
							sd.setGoal(iYemen, 1, 1)
						else:
							sd.setGoal(iYemen, 1, 0)
					
					# Yemen UHV3: Obtain 4 coffee by 1500
					if sd.getGoal(iYemen, 2) == -1:
						if iGameTurn <= getTurnForYear(1500):
							if pPlayer.getNumAvailableBonuses(con.iCoffee) >= 4:
								sd.setGoal(iYemen, 2, 1)
						else:
							sd.setGoal(iYemen, 2, 0)

			
			elif iPlayer == iBuyids:
				if pPlayer.isAlive():
				
					# Buyid UHV1: Claim the title of Shahanshah - in Titles.py
					
					# Buyid UHV2: Hold the title of Commander of the Faithful in in 1000 AD
					if sd.getGoal(iBuyids, 1) == -1:
						if iGameTurn == getTurnForYear(1000):
							if gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iCaliph):
								sd.setGoal(iBuyids, 1, 1)
							else:
								sd.setGoal(iBuyids, 1, 0)
					
					# Buyids UHV3: Control Iraq by 1035 AD
					if iGameTurn <= getTurnForYear(1035):
						if sd.getGoal(iBuyids, 2) == -1:
							regionList = [con.rMesopotamia, con.rKhuzestan, con.rHormuz, con.rOman]
							if self.checkRegions(iBuyids, regionList, True):
								sd.setGoal(iBuyids, 2, 1)
							elif iGameTurn >= getTurnForYear(1035):
								sd.setGoal(iBuyids, 2, 0)
			
			elif iPlayer == iGujarat:
				if pPlayer.isAlive():
					
					# Gujarat UHV1: Become a Hindu Saint by 1140 AD
					if sd.getGoal(iGujarat, 0) == -1:
						if iGameTurn <= getTurnForYear(1140):
							if sd.getPiety(iGujarat) > 90 and pPlayer.getStateReligion() == con.iHinduism:
								sd.setGoal(iGujarat, 0, 1)
						else:
							sd.setGoal(iGujarat, 0, 0)
					
					# Gujarat UHV2: Control or vassalize provinces in 1200
					if iGameTurn == getTurnForYear(1200):
						if sd.getGoal(iGujarat, 1) == -1:
							bControl = True
							regionList = [con.rGujarat, con.rSindh, con.rMalwa]
							for regionID in regionList:
								if not utils.checkRegionControl(iGujarat, regionID, True):
									bControl = False
							if bControl:
								sd.setGoal(iGujarat, 1, 1)
							else:
								sd.setGoal(iGujarat, 1, 0)
					
					# Gujarat UHV3: Have the world's highest population in 1240 AD
					if iGameTurn == getTurnForYear(1240):
						if self.isHighestPopulation(iGujarat):
							sd.setGoal(iGujarat, 2, 1)
						else:
							sd.setGoal(iGujarat, 2, 0)
			
			elif iPlayer == iGhaznavids:
				if pPlayer.isAlive():
					
					# Ghaznavid UHV1: 3,000 gold in 1180
					if iGameTurn == getTurnForYear(1180):
						if pPlayer.getGold() >= utils.getTurns(3000):
							sd.setGoal(iGhaznavids, 0, 1)
						else:
							sd.setGoal(iGhaznavids, 0, 0)
					
					# Ghaznavid UHV2: Own cities in provinces in 1180
					if iGameTurn == getTurnForYear(1180):
						if sd.getGoal(iGhaznavids, 1) == -1:
							bControl = True
							regionList = [con.rPunjab, con.rSindh, con.rBalochistan, con.rSistan, con.rEasternKhorasan, con.rBactria, con.rHindukush]
							for regionID in regionList:
								if not utils.checkRegionOwnedCity(iGhaznavids, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iGhaznavids, 1, 1)
							else:
								sd.setGoal(iGhaznavids, 1, 0)
					
					# Ghaznavid UHV3: 10,000 gold in 1300
					if sd.getGoal(iGhaznavids, 2) == -1:
						if iGameTurn <= getTurnForYear(1300):
							if pPlayer.getGold() >= utils.getTurns(10000):
								sd.setGoal(iGhaznavids, 2, 1)
						else:
							sd.setGoal(iGhaznavids, 2, 0)
			
			elif iPlayer == iFatimids:
				if pPlayer.isAlive():
					
					# Fatimid UHV1: Control provinces in 1160
					if iGameTurn == getTurnForYear(1160):
						bControl = True
						regionList = [con.rUpperEgypt, con.rLowerEgypt, con.rPalestine, con.rSyria, con.rNorthernSyria, con.rJordan, con.rHejaz]
						for regionID in regionList:
							if not utils.checkRegionControl(iFatimids, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iFatimids, 0, 1)
						else:
							sd.setGoal(iFatimids, 0, 0)
					
					# Fatimid UHV2: Spread Shia faith to 30% by 1250 AD
					if sd.getGoal(iFatimids, 1) == -1:
						religionPercent = gc.getGame().calculateReligionPercent(con.iShia)
						if religionPercent >= 30.0:
							sd.setGoal(iFatimids, 1, 1)
					
					# Fatimid UHV3: expire check only; rest in Titles.py
					if sd.getGoal(iFatimids, 2) == -1:
						if iGameTurn > getTurnForYear(1250):
							sd.setGoal(iFatimids, 2, 0)

			
			elif iPlayer == iGeorgia:
				if pPlayer.isAlive():
					
					# Georgian UHV1: Control or vassalize provinces in 1210
					if iGameTurn == getTurnForYear(1210):
						if sd.getGoal(iGeorgia, 0) == -1:
							bControl = True
							regionList = [con.rTrebizond, con.rGreaterArmenia, con.rGeorgia, con.rKars, con.rVaspurakan, con.rShirvan]
							for regionID in regionList:
								if not utils.checkRegionControl(iGeorgia, regionID, True):
									bControl = False
							if bControl:
								sd.setGoal(iGeorgia, 0, 1)
							else:
								sd.setGoal(iGeorgia, 0, 0)
					
					# Georgian UHV2: Control 5 Castles and 5 Orthodox Churches and 5 Orthodox Monasteries by 1210
					if sd.getGoal(iGeorgia, 1) == -1:
						if iGameTurn <= getTurnForYear(1210):
							iNumCastles = self.getNumBuildings(iGeorgia, con.iCastle)
							iNumTemples = self.getNumBuildings(iGeorgia, con.iOrthodoxTemple)
							iNumMonasteries = self.getNumBuildings(iGeorgia, con.iOrthodoxMonastery)
							if iNumCastles >= 5 and iNumTemples >= 5 and iNumMonasteries >= 5:
								sd.setGoal(iGeorgia, 1, 1)
						else:
							sd.setGoal(iGeorgia, 1, 0)
					
					# Georgian UHV3: No barbs or non-Christians in Caucasus in 1330
					if iGameTurn == getTurnForYear(1330):
						bFound = False
						regionList = [con.rGreaterArmenia, con.rKars, con.rVaspurakan, con.rGeorgia, con.rShirvan, con.rLesserArmenia]
						for regionID in regionList:
							for iCiv in range(con.iBarbarian+1):
								if utils.checkRegionOwnedCity(iCiv, regionID):
									if iCiv == con.iBarbarian or gc.getPlayer(iCiv).getStateReligion() not in [-1, con.iCatholicism, con.iOrthodoxy]:
										bFound = True
										break
						if bFound:
							sd.setGoal(iGeorgia, 2, 0)
						else:
							sd.setGoal(iGeorgia, 2, 1)
			
			elif iPlayer == iGhorids:
				if pPlayer.isAlive():
					
					# Ghorid UHV1: Build a Palace in Delhi by 1250
					if sd.getGoal(iGhorids, 0) == -1:
						if iGameTurn == getTurnForYear(1250)+1:
							sd.setGoal(iGhorids, 0, 0)
					
					# Ghorid UHV2: Become a Sunni Saint by 1250 AD
					if sd.getGoal(iGhorids, 1) == -1:
						if iGameTurn <= getTurnForYear(1250):
							if sd.getPiety(iGhorids) > 90 and pPlayer.getStateReligion() == con.iSunni:
								sd.setGoal(iGhorids, 1, 1)
						else:
							sd.setGoal(iGhorids, 1, 0)
					
					# Ghorid UHV3: Control provinces in 1400
					if iGameTurn == getTurnForYear(1400):
						bControl = True
						regionList = [con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rSindh]
						for regionID in regionList:
							if not utils.checkRegionControl(iGhorids, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iGhorids, 2, 1)
						else:
							sd.setGoal(iGhorids, 2, 0)
			
			elif iPlayer == iSindh:
				if pPlayer.isAlive():
					
					# Sindh UHV1: Be the most productive civ in 1140
					if iGameTurn == getTurnForYear(1140):
						if self.isMostProductive(iSindh):
							sd.setGoal(iSindh, 0, 1)
						else:
							sd.setGoal(iSindh, 0, 0)
					
					# Sindh UHV2: Control provinces in 1200
					if iGameTurn == getTurnForYear(1200):
						bControl = True
						regionList = [con.rSindh, con.rGujarat]
						for regionID in regionList:
							if not utils.checkRegionControl(iSindh, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iSindh, 1, 1)
						else:
							sd.setGoal(iSindh, 1, 0)
					
					# Sindh UHV3: Build 4 Sufi Shrines by 1330
					if sd.getGoal(iSindh, 2) == -1:
						if iGameTurn == getTurnForYear(1330)+1:
							sd.setGoal(iSindh, 2, 0)
			
			elif iPlayer == iSeljuks:
				if pPlayer.isAlive():
					
					# Seljuk UHV1: 9% land
					if sd.getGoal(iSeljuks, 0) == -1:
						if iGameTurn <= getTurnForYear(1200):
							totalLand = gc.getMap().getLandPlots()
							ownedLand = pPlayer.getTotalLand()
							if totalLand > 0:
								landPercent = (ownedLand * 100.0) / totalLand
							else:
								landPercent = 0.0
							if landPercent >= 8.995:
								sd.setGoal(iSeljuks, 0, 1)
						else:
							sd.setGoal(iSeljuks, 0, 0)
					
					# Seljuk UHV2: Have at least 2 vassals in 1200
					if iGameTurn == getTurnForYear(1200):
						if self.getNumVassals(iSeljuks) >= 2:
							sd.setGoal(iSeljuks, 1, 1)
						else:
							sd.setGoal(iSeljuks, 1, 0)
					
					# Seljuk UHV3: Best culture in 1300
					if iGameTurn == getTurnForYear(1300):
						if self.isTopCulture(iSeljuks):
							sd.setGoal(iSeljuks, 2, 1)
						else:
							sd.setGoal(iSeljuks, 2, 0)
			
			elif iPlayer == iRum:
				if pPlayer.isAlive():
					
					# Rum UHV1: Control at least 6 provinces in Thrace and Anatolia in 1190
					if iGameTurn == getTurnForYear(1190):
						iNumProvinces = 0
						regionList = [con.rThrace, con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond]
						for regionID in regionList:
							if utils.checkRegionControl(iRum, regionID):
								iNumProvinces += 1
						if iNumProvinces >= 6:
							sd.setGoal(iRum, 0, 1)
						else:
							sd.setGoal(iRum, 0, 0)
					
					# Rum UHV2: Control at least 5 Sufi Shrines in 1290
					if iGameTurn == getTurnForYear(1290):
						iNumShrines = 0
						apCityList = PyPlayer(iRum).getCityList()
						for pCity in apCityList:
							if pCity.getNumBuilding(con.iSufiShrine): iNumShrines += 1
						if iNumShrines >= 5:
							sd.setGoal(iRum, 1, 1)
						else:
							sd.setGoal(iRum, 1, 0)
					
					# Rum UHV3: Control all of Thrace and Anatolia in 1460
					if iGameTurn == getTurnForYear(1460):
						if sd.getGoal(iRum, 2) == -1:
							bControl = True
							regionList = [con.rThrace, con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond]
							for regionID in regionList:
								if not utils.checkRegionControl(iRum, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iRum, 2, 1)
							else:
								sd.setGoal(iRum, 2, 0)
			
			elif iPlayer == iKhwarezm:
				if pPlayer.isAlive():
					
					# Khwarezmian UHV1: Obtain 5 silk by 1230
					if sd.getGoal(iKhwarezm, 0) == -1:
						if iGameTurn <= getTurnForYear(1230):
							if pPlayer.getNumAvailableBonuses(con.iSilk) >= 5:
								sd.setGoal(iKhwarezm, 0, 1)
						else:
							sd.setGoal(iKhwarezm, 0, 0)
					
					# Khwarezmian UHV3: Never lose a city to barbarians before 1350, see onCityAcquired()
					if iGameTurn == getTurnForYear(1350):      
						if sd.getGoal(iKhwarezm, 2) == -1:
								sd.setGoal(iKhwarezm, 2, 1)
		
			elif iPlayer == iAntioch:
				if pPlayer.isAlive():
					
					# Antioch UHV1: Control provinces in 1190
					if iGameTurn == getTurnForYear(1190):
						if sd.getGoal(iAntioch, 0) == -1:
							bControl = utils.checkRegionControl(iAntioch, con.rNorthernSyria, True)
							iCount = 0
							if utils.checkRegionControl(iAntioch, con.rEdessa, True): iCount += 1
							if utils.checkRegionControl(iAntioch, con.rCilicia, True): iCount += 1
							if utils.checkRegionControl(iAntioch, con.rSyria, True): iCount += 1
							if utils.checkRegionControl(iAntioch, con.rLebanon, True): iCount += 1
							if utils.checkRegionControl(iAntioch, con.rLesserArmenia, True): iCount += 1
							if bControl and iCount >= 3:
								sd.setGoal(iAntioch, 0, 1)
							else:
								sd.setGoal(iAntioch, 0, 0)
					
					# Antioch UHV2: open borders x 6 by 1270
					if sd.getGoal(iAntioch, 1) == -1:
						if iGameTurn <= getTurnForYear(1270):
							if self.getNumOpenBorders(iAntioch) >= 6:
								sd.setGoal(iAntioch, 1, 1)
						else:
							sd.setGoal(iAntioch, 1, 0)

					# Antioch UHV3: Control at least 3 Venetian Quarters in 1290
					if iGameTurn == getTurnForYear(1290):
						if self.getNumBuildings(iAntioch, con.iVenetianQuarter) >= 3:
							sd.setGoal(iAntioch, 2, 1)
						else:
							sd.setGoal(iAntioch, 2, 0)
					
			elif iPlayer == iCrusaders:
				if pPlayer.isAlive():
					
					# Crusader UHV1: Control provinces in 1190
					if iGameTurn == getTurnForYear(1190):
						bControl = True
						regionList = [con.rPalestine, con.rJordan, con.rCyprus]
						for regionID in regionList:
							if not utils.checkRegionControl(iCrusaders, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iCrusaders, 0, 1)
						else:
							sd.setGoal(iCrusaders, 0, 0)
					
					# Crusader UHV2: Obtain 8 silk + incense + spices by 1290
					if sd.getGoal(iCrusaders, 1) == -1:
						if iGameTurn <= getTurnForYear(1290):
							nBonuses = 0
							nBonuses += pPlayer.getNumAvailableBonuses(con.iSilk)
							nBonuses += pPlayer.getNumAvailableBonuses(con.iIncense)
							nBonuses += pPlayer.getNumAvailableBonuses(con.iSpices)
							if nBonuses >= 8:
								sd.setGoal(iCrusaders, 1, 1)
						else:
							sd.setGoal(iCrusaders, 1, 0)
					
					# Crusader UHV3: Become a Catholic Saint by 1290 AD
					if sd.getGoal(iCrusaders, 2) == -1:
						if iGameTurn <= getTurnForYear(1290):
							if sd.getPiety(iCrusaders) > 90 and pPlayer.getStateReligion() == con.iCatholicism:
								sd.setGoal(iCrusaders, 2, 1)
						else:
							sd.setGoal(iCrusaders, 2, 0)
						
			elif iPlayer == iZengids:
				if pPlayer.isAlive():
					
					# Zengid UHV1: Conquer or vassalize Egypt by 1250 AD 
					if iGameTurn == getTurnForYear(1250)-1:
						if sd.getGoal(iZengids, 0) == -1:
							regionList = [con.rLowerEgypt, con.rUpperEgypt]
							if self.checkRegions(iZengids, regionList, True):
								sd.setGoal(iZengids, 0, 1)
							else:
								sd.setGoal(iZengids, 0, 0)
					
					# Zengid UHV2: Ensure that there are no Christian states in Egypt, Cilicia, and the Levant in 1291 AD
					if iGameTurn == getTurnForYear(1291):
						bFound = False
						regionList = [con.rCilicia, con.rPalestine, con.rJordan, con.rSyria, con.rLebanon, con.rNorthernSyria, con.rUpperEgypt, con.rLowerEgypt]
						for regionID in regionList:
							for iCiv in range(con.iBarbarian+1):
								if utils.checkRegionOwnedCity(iCiv, regionID):
									if iCiv == con.iBarbarian or gc.getPlayer(iCiv).getStateReligion() in [con.iCatholicism, con.iOrthodoxy]:
										bFound = True
										break
						if bFound:
							sd.setGoal(iZengids, 1, 0)
						else:
							sd.setGoal(iZengids, 1, 1)
					

					# Zengid UHV3: Never lose a city to barbarians until 1400 AD - see onCityAcquired
					if iGameTurn == getTurnForYear(1400):
						if sd.getGoal(iZengids, 2) == -1:
							sd.setGoal(iZengids, 2, 1)

			elif iPlayer == iOman:
				if pPlayer.isAlive():
					
					# Oman UHV1: Spread Islam to 5 non-Islamic coastal cities you do not control
					if iGameTurn == getTurnForYear(1470)+1:
						if sd.getGoal(iOman, 0) == -1:
							sd.setGoal(iOman, 0, 0)
					
					# Omani UHV2: obtain 50k gold by 1600
					if sd.getGoal(iOman, 1) == -1:
						if iGameTurn <= getTurnForYear(1600):
							if pPlayer.getGold() >= utils.getTurns(50000):
								sd.setGoal(iOman, 1, 1)
						else:
							sd.setGoal(iOman, 1, 0)
					
					# Omani UHV3: No Portuguese ports in Arabia, Persia and Africa in 1600
					if iGameTurn == getTurnForYear(1600):
						regionList = [21,22,23,27,28,29,30,31,32,33,34,35,38,39,48,52,54,67,70]
						if self.getRegionsOwnedCity(iPortugal, regionList, True):
							sd.setGoal(iOman, 2, 0)
						else:
							sd.setGoal(iOman, 2, 1)
			
			elif iPlayer == iAyyubids:
				if pPlayer.isAlive():
				
					# Ayyubid UHV1: Trade Relations with Venetians and Genoese
					if iGameTurn == getTurnForYear(1245):
						if pPlayer.countCorporations(con.iVenetians) and pPlayer.countCorporations(con.iGenoans):
							sd.setGoal(iAyyubids, 0, 1)
						else:
							sd.setGoal(iAyyubids, 0, 0)
				
					# Ayyubid UHV2: Control provinces in 1245
					if iGameTurn == getTurnForYear(1245):
						bControl = True
						regionList = [con.rUpperEgypt, con.rLowerEgypt, con.rPalestine, con.rLebanon, con.rSyria, con.rNorthernSyria, con.rJordan, con.rHejaz, con.rYemen]
						for regionID in regionList:
							if not utils.checkRegionControl(iAyyubids, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iAyyubids, 1, 1)
						else:
							sd.setGoal(iAyyubids, 1, 0)
					
					# Ayyubid UHV3: Have the highest score in 1500
					if iGameTurn == getTurnForYear(1500):
						if gc.getGame().getRankTeam(0) == pPlayer.getTeam():
							sd.setGoal(iAyyubids, 2, 1)
						else:
							sd.setGoal(iAyyubids, 2, 0)
			
			elif iPlayer == iMamluks:
				if pPlayer.isAlive():
					# Mamluk UHV1: Make Cairo the most populous city in the world in 1380
					if iGameTurn == getTurnForYear(1380):
						if self.isTopCityPopulation(iMamluks, con.tFustat):
							sd.setGoal(iMamluks, 0, 1)
						else:
							sd.setGoal(iMamluks, 0, 0)
					
					# Mamluk UHV2: Control provinces in 1500
					if iGameTurn == getTurnForYear(1500):
						if sd.getGoal(iMamluks, 1) == -1:
							bControl = True
							regionList = [con.rUpperEgypt, con.rLowerEgypt, con.rPalestine, con.rLebanon, con.rSyria, con.rNorthernSyria, con.rJordan, con.rHejaz]
							for regionID in regionList:
								if not utils.checkRegionControl(iMamluks, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iMamluks, 1, 1)
							else:
								sd.setGoal(iMamluks, 1, 0)
			
			elif iPlayer == iOttomans:
				if pPlayer.isAlive():
					
					# Ottoman UHV2: Hold the title of Roman Emperor in 1450
					if iGameTurn == getTurnForYear(1450):
						if gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iRomanEmperor):
							sd.setGoal(iOttomans, 1, 1)
						else:
							sd.setGoal(iOttomans, 1, 0)
					
					# Ottoman UHV3: Control or vassalize provinces in 1660
					if iGameTurn == getTurnForYear(1660):
						if sd.getGoal(iOttomans, 2) == -1:
							regionList = [con.rThrace, con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond, con.rGreaterArmenia, con.rGeorgia, con.rKars, con.rVaspurakan, con.rShirvan, con.rSyria, con.rNorthernSyria, con.rPalestine, con.rLebanon, con.rJordan, con.rHejaz, con.rUpperEgypt, con.rLowerEgypt, con.rAsuristan, con.rMesopotamia, con.rJazira, con.rEdessa]
							if self.checkRegions(iOttomans, regionList, True):
								sd.setGoal(iOttomans, 2, 1)
							else:
								sd.setGoal(iOttomans, 2, 0)
			
			elif iPlayer == iBahmanids:
				if pPlayer.isAlive():
					# Bahmanid UHV1: Never lose a city to the portuguese until 1600 -> see onCityAcquired
					if iGameTurn == getTurnForYear(1600):
						if sd.getGoal(iZengids, 2) == -1:
							sd.setGoal(iZengids, 2, 1)

					# Bahmanid UHV2: Controll the south of Hindustan in 1550 AD
					if iGameTurn == getTurnForYear(1550):
						if sd.getGoal(iBahmanids, 1) == -1:
							bControl = True
							regionList = [con.rGujarat, con.rMaharashtra, con.rKarnataka, con.rMalwa, con.rGoa]
							for regionID in regionList:
								if not utils.checkRegionControl(iBahmanids, regionID):
									bControl = False
							if bControl:
								sd.setGoal(iBahmanids, 1, 1)
							else:
								sd.setGoal(iBahmanids, 1, 0)
								
					# Bahmanid UHV3: Raze or massacre the population of at least 8 hindu cities -> see onCityAcquiredAndKept

								
			elif iPlayer == iTimurids:
				if pPlayer.isAlive():
					
					# Timurid UHV2: Make Samarkand the city with highest culture in 1500
					if iGameTurn == getTurnForYear(1500):
						if self.isTopCityCulture(iTimurids, con.tCapitals[iTimurids]):
							sd.setGoal(iTimurids, 1, 1)
						else:
							sd.setGoal(iTimurids, 1, 0)
					
					# Timurid UHV3: 11% land
					if sd.getGoal(iTimurids, 2) == -1:
						if iGameTurn <= getTurnForYear(1600):
							totalLand = gc.getMap().getLandPlots()
							ownedLand = pPlayer.getTotalLand()
							if totalLand > 0:
								landPercent = (ownedLand * 100.0) / totalLand
							else:
								landPercent = 0.0
							if landPercent >= 10.995:
								sd.setGoal(iTimurids, 2, 1)
						else:
							sd.setGoal(iTimurids, 2, 0)
		
			elif iPlayer == iAkKoyunlu:
				if pPlayer.isAlive():
					
					# Ak Koyunlu UHV1: Control provinces in 1440
					if iGameTurn == getTurnForYear(1440):
						bControl = True
						regionList = [con.rJazira, con.rAsuristan, con.rAzerbaijan]
						for regionID in regionList:
							if not utils.checkRegionControl(iAkKoyunlu, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iAkKoyunlu, 0, 1)
						else:
							sd.setGoal(iAkKoyunlu, 0, 0)
					
					# Ak Koyunlu UHV2: Control provinces in 1480
					if iGameTurn == getTurnForYear(1480):
						bControl = True
						regionList = [con.rJazira, con.rAsuristan, con.rAzerbaijan, con.rMesopotamia, con.rKhuzestan, con.rLesserArmenia, con.rShirvan]
						for regionID in regionList:
							if not utils.checkRegionControl(iAkKoyunlu, regionID):
								bControl = False
						if bControl:
							sd.setGoal(iAkKoyunlu, 1, 1)
						else:
							sd.setGoal(iAkKoyunlu, 1, 0)
					
					# Ak Koyunlu UHV3: Moved to Titles.py
			
			elif iPlayer == iSafavids:
				if pPlayer.isAlive():
				
				# Safavid UHV1: Moved to Titles.py
				
				# Safivid UHV3: Make Shia most popular religion
					if sd.getGoal(iSafavids, 2) == -1:
						if self.isTopReligion(con.iShia):
							sd.setGoal(iSafavids, 2, 1)

			elif iPlayer == iPortugal:
				if pPlayer.isAlive():
					# Portuguese UHV1: Control all coastal cities on the Arabian Sea, Red Sea, and Persian Gulf by 1590
					if iGameTurn == getTurnForYear(1590):
						bControl = True
						for iCiv in range(con.iNumPlayers):
							if iCiv != iPortugal:
								apCityList = PyPlayer(iCiv).getCityList()
								for pCity in apCityList:
									city = CyMap().plot(pCity.getX(), pCity.getY()).getPlotCity()
									if city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
										if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rKarnataka, con.rGoa, con.rMaharashtra, con.rGujarat, con.rSindh, con.rBalochistan, con.rMakran, con.rHormuz, con.rFars, con.rKhuzestan, con.rMesopotamia, con.rArabia, con.rBahrain, con.rOman, con.rMahra, con.rHadhramaut, con.rYemen, con.rHejaz, con.rJordan, con.rUpperEgypt, con.rAksum, con.rMerebMellash, con.rSuqutra]:
											bControl = False
											break
										elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rSinai, con.rLowerEgypt]:
											if pCity.getY() < 33:
												bControl = False
												break
						if bControl == True:
							sd.setGoal(iPortugal, 0, 1)
						else:
							sd.setGoal(iPortugal, 0, 0)
					# Portuguese UHV2: 15 luxuries in 1620
					if iGameTurn == getTurnForYear(1620):
						iNumLuxuries = self.getNumLuxuries(iPortugal)
						if iNumLuxuries >= 15:
							sd.setGoal(iPortugal, 1, 1)
						else:
							sd.setGoal(iPortugal, 1, 0)

					# Portuguese UHV3: 15,000 gold in 1650
					if sd.getGoal(iPortugal, 2) == -1:
						if iGameTurn == getTurnForYear(1650):
							if pPlayer.getGold() >= utils.getTurns(10000):
								sd.setGoal(iPortugal, 2, 1)
							else:
								sd.setGoal(iPortugal, 2, 0)

			elif iPlayer == iMughals:
				if pPlayer.isAlive():
					
					# Mughal UHV2: Have a city with legendary culture
					if sd.getGoal(iMughals, 1) == -1:
						if self.isHasLegendaryCity(iMughals):
							sd.setGoal(iMughals, 1, 1)
					
					# Mughal UHV3: Control provinces in 1650
					if iGameTurn == getTurnForYear(1650):
						regionList = [con.rGandhar, con.rDuggar, con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rSindh, con.rKarnataka]
						if self.checkRegions(iMughals, regionList):
							sd.setGoal(iMughals, 2, 1)
						else:
							sd.setGoal(iMughals, 2, 0)
			
			#generic checks
			if pPlayer.isAlive() and iPlayer < con.iNumPlayers:
				if sd.get2OutOf3(iPlayer) == False:
					if utils.countAchievedGoals(iPlayer) == 2:
						#intermediate bonus
						sd.set2OutOf3(iPlayer, True)
						if pPlayer.getNumCities() > 0: #this check is needed, otherwise game crashes
							pPlayer.changeGoldenAgeTurns(pPlayer.getGoldenAgeLength()) # edead
							iWarCounter = 0
							iRndnum = gc.getGame().getSorenRandNum(con.iNumPlayers, 'civs')
							iHandicap = gc.getGame().getHandicapType()
							for i in range(iRndnum, con.iNumPlayers + iRndnum):
								iCiv = i % con.iNumPlayers
								pCiv = gc.getPlayer(iCiv)
								if pCiv.isAlive() and pCiv.canContact(iPlayer):                                                                
									if pCiv.AI_getAttitude(iPlayer) <= 0:
										teamCiv = gc.getTeam(pCiv.getTeam())
										if not teamCiv.isAtWar(iPlayer) and not teamCiv.isDefensivePact(iPlayer) and not utils.isAVassal(iCiv):
											teamCiv.AI_setWarPlan(iPlayer, WarPlanTypes.WARPLAN_PREPARING_TOTAL) # edead: prepare for total war
											iWarCounter += 1
											if iWarCounter == 1 + max(1, iHandicap):
												break
			if gc.getGame().getWinner() == -1:
				if sd.getGoal(iPlayer, 0) == 1 and sd.getGoal(iPlayer, 1) == 1 and sd.getGoal(iPlayer, 2) == 1:
					gc.getGame().setWinner(iPlayer, iHistoricalVictory)
				
		# RELIGIOUS VICTORY
		if gc.getGame().isVictoryValid(iReligiousVictory) and iPlayer == iHuman:
			if iGameTurn >= getTurnForYear(con.tBirth[iPlayer]) and gc.getPlayer(iPlayer).getStateReligion() != -1:
				for i in range(3):
					if sd.getReligiousGoal(iPlayer, i) == -1:
						if self.getURV(iPlayer, i):
							sd.setReligiousGoal(iPlayer, i, 1)
				if gc.getGame().getWinner() == -1:
					if sd.getReligiousGoal(iPlayer, 0) == 1 and sd.getReligiousGoal(iPlayer, 1) == 1 and sd.getReligiousGoal(iPlayer, 2) == 1:
						gc.getGame().setWinner(iPlayer, iReligiousVictory)
			

	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		iYear = utils.getYear()
		
		# Makurian UHV2: Never lose a city before 1200 AD
		if iPreviousOwner == iMakuria:
			if gc.getPlayer(iPreviousOwner).isAlive():
				if bConquest:
					if sd.getGoal(iMakuria, 1) == -1:
						if iYear < 1200:
							sd.setGoal(iMakuria, 1, 0)
		
		# Samanid UHV2: Never lose a city before 1070 AD
		elif iPreviousOwner == iSamanids:
			if gc.getPlayer(iPreviousOwner).isAlive():
				if (bConquest):
					if (sd.getGoal(iSamanids, 1) == -1):
						if iYear < 1070:
							sd.setGoal(iSamanids, 1, 0)
		
		# Khwarezmian UHV3: Never lose a city to barbarians before 1350 AD
		elif iPreviousOwner == iKhwarezm:
			if gc.getPlayer(iPreviousOwner).isAlive():
				if bConquest:
					if sd.getGoal(iKhwarezm, 2) == -1:
						if iNewOwner == con.iBarbarian and iYear < 1350:
							sd.setGoal(iKhwarezm, 2, 0)

		# Zengid UHV3: Never lose a city to barbarians until 1400 AD
		elif iPreviousOwner == iZengids:
			if gc.getPlayer(iPreviousOwner).isAlive():
				if bConquest:
					if sd.getGoal(iZengids, 2) == -1:
						if iNewOwner == con.iBarbarian and iYear <= 1400:
							sd.setGoal(iZengids, 2, 0)

		# Bahmanid UHV1: Never lose a city to the portuguese until 1600
		elif iPreviousOwner == iBahmanids:
			if gc.getPlayer(iPreviousOwner).isAlive():
				if bConquest:
					if sd.getGoal(iBahmanids, 0) == -1:
						if iNewOwner == con.iPortugal and iYear <= 1600:
							sd.setGoal(iBahmanids, 0, 0)

	def onCityAcquiredAndKept(self, argsList):
		iOwner,pCity,bMassacre = argsList

		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		# Timurid UHV1: Raze or massacre 9 cities - part I
		if bMassacre and iOwner == iTimurids:
			if gc.getPlayer(iOwner).isAlive():
				sd.setRazedByMongols(sd.getRazedByMongols() + 1)
				if sd.getGoal(iTimurids, 0) == -1:
					if sd.getRazedByMongols() >= 9:
						sd.setGoal(iTimurids, 0, 1)

		# Bahmanid UHV3: Raze or massacre the population of at least 8 hindu cities - part I
		if bMassacre and iOwner == iBahmanids:
			if gc.getPlayer(iOwner).isAlive():
				# city = CyMap().plot(pCity.getX(), pCity.getY()).getPlotCity()
				# if city.isHasReligion(con.iSunni):
				sd.setRazedByBahmanids(sd.getRazedByBahmanids() + 1)
				if sd.getGoal(iBahmanids, 2) == -1:
					if sd.getRazedByBahmanids() >= 8:
						sd.setGoal(iBahmanids, 2, 1)

	def onCityRazed(self, iPlayer):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		# Timurid UHV1: Raze or massacre 7 cities - part II
		if iPlayer == iTimurids:
			if gc.getPlayer(iPlayer).isAlive():
				sd.setRazedByMongols(sd.getRazedByMongols() + 1)
				if sd.getGoal(iTimurids, 0) == -1:
					if sd.getRazedByMongols() >= 9:
						sd.setGoal(iTimurids, 0, 1)

		# Bahmanid UHV3: Raze or massacre the population of at least 6 hindu cities - part II
		if iPlayer == iBahmanids:
			if gc.getPlayer(iPlayer).isAlive():
				# city = CyMap().plot(pCity.getX(), pCity.getY()).getPlotCity()
				# if city.isHasReligion(con.iHinduism):
				sd.setRazedByBahmanids(sd.getRazedByBahmanids() + 1)
				if sd.getGoal(iBahmanids, 2) == -1:
					if sd.getRazedByBahmanids() >= 6:
						sd.setGoal(iBahmanids, 2, 1)

	def onTechAcquired(self, iTech, iPlayer):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		# Ottoman UHV1: Be the first to discover Military Drill, Matchlock & Flintlock
		if iPlayer == iOttomans:
			if gc.getPlayer(iPlayer).isAlive():
				if sd.getGoal(iOttomans, 0) == -1:
					if iTech == con.iMilitaryDrill:
						sd.setOttomanTechs(0, 1)
						for iCiv in range(con.iNumPlayers):
							if iCiv != iOttomans:
								if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True:
									sd.setOttomanTechs(0, 0)
					elif iTech == con.iMatchlock:
						sd.setOttomanTechs(1, 1)
						for iCiv in range(con.iNumPlayers):
							if iCiv != iOttomans:
								if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True:
									sd.setOttomanTechs(1, 0)
					elif iTech == con.iFlintlock:
						sd.setOttomanTechs(2, 1)
						for iCiv in range(con.iNumPlayers):
							if iCiv != iOttomans:
								if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True:
									sd.setOttomanTechs(2, 0)
					#print ("sd.getOttomanTechs", sd.getOttomanTechs(0), sd.getOttomanTechs(1), sd.getOttomanTechs(2))
					if sd.getOttomanTechs(0) == 1 and sd.getOttomanTechs(1) == 1 and sd.getOttomanTechs(2) == 1:
						sd.setGoal(iOttomans, 0, 1)
					elif sd.getOttomanTechs(0) == 0 or sd.getOttomanTechs(1) == 0 or sd.getOttomanTechs(2) == 0:
						sd.setGoal(iOttomans, 0, 0)


	def onBuildingBuilt(self, iPlayer, iBuilding, city):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		iGameTurn = gc.getGame().getGameTurn()
		pPlayer = gc.getPlayer(iPlayer)
		
		# Armenian UHV1: Build an Orthodox Cathedral by 1045
		if iPlayer == iArmenia:
			if pPlayer.isAlive():
				if sd.getGoal(iArmenia, 0) == -1:
					if iGameTurn <= getTurnForYear(1045):
						if iBuilding == con.iOrthodoxCathedral or iBuilding == con.iBagratiCathedral:
							sd.setGoal(iArmenia, 0, 1)
		
		# Yemen UHV1: Build 3 Sufi Shrines
		elif iPlayer == iYemen:
			if pPlayer.isAlive():
				if sd.getGoal(iYemen, 0) == -1:
					if iGameTurn <= getTurnForYear(1140):
						if iBuilding == con.iSufiShrine:
							sd.setWondersBuilt(iYemen, sd.getWondersBuilt(iYemen) + 1)
						if sd.getWondersBuilt(iYemen) == 3:
							sd.setGoal(iYemen, 0, 1)
					else:
						if sd.getWondersBuilt(iYemen) != 3:
							sd.setGoal(iYemen, 0, 0)
		
		# Sindh UHV3: Build 4 Sufi Shrines
		elif iPlayer == iSindh:
			if pPlayer.isAlive():
				if sd.getGoal(iSindh, 2) == -1:
					if iGameTurn <= getTurnForYear(1330):
						if iBuilding == con.iSufiShrine:
							sd.setWondersBuilt(iSindh, sd.getWondersBuilt(iSindh) + 1)
						if sd.getWondersBuilt(iSindh) == 4:
							sd.setGoal(iSindh, 2, 1)
		
		# Ghorid UHV1: Build a Palace in Delhi
		elif iPlayer == iGhorids:
			if pPlayer.isAlive():
				if sd.getGoal(iGhorids, 0) == -1:
					if iGameTurn <= getTurnForYear(1250):
						if iBuilding == con.iPalace:
							#if (city.getX(), city.getY()) == con.tLahore or (city.getX(), city.getY()) == con.tDelhi:
							if (city.getX(), city.getY()) == con.tDelhi:
								sd.setGoal(iGhorids, 0, 1)
								# Change the name & flag to Delhi Sultanate
								# gc.getPlayer(iGhorids).setCivName(localText.getText("TXT_KEY_CIV_DELHI_DESC_DEFAULT", ()), localText.getText("TXT_KEY_CIV_DELHI_SHORT_DESC", ()), localText.getText("TXT_KEY_CIV_DELHI_ADJECTIVE", ()))
								# gc.getPlayer(iPlayer).setFlag("Art/Interface/TeamColor/FlagDECAL_Delhi.dds")
		
		# Safavid UHV2: Build 4 Great Wonders
		elif iPlayer == iSafavids:
			if pPlayer.isAlive():
				if sd.getGoal(iSafavids, 1) == -1:
					if con.iBridge33 >= iBuilding >= con.iGreatLighthouse:
						sd.setWondersBuilt(iSafavids, sd.getWondersBuilt(iSafavids) + 1)
						if sd.getWondersBuilt(iSafavids) == 4:
							sd.setGoal(iSafavids, 1, 1)
		
		# Malwa UHV1: Build 3 Sanskrit Schools and 3 Hindu Mandirs by 1060 AD
		elif iPlayer == iMalwa:
			if pPlayer.isAlive():
				if sd.getGoal(iMalwa, 0) == -1:
					if iGameTurn <= getTurnForYear(1060):
						iNumColleges, iNumTemples = sd.getVal('lMalwaBuildings')
						if iBuilding == con.iSanskritCollege:
							iNumColleges += 1
							sd.setVal('lMalwaBuildings', (iNumColleges, iNumTemples))
						elif iBuilding == con.iHinduTemple:
							iNumTemples += 1
							sd.setVal('lMalwaBuildings', (iNumColleges, iNumTemples))
						if iNumColleges >= 3 and iNumTemples >= 3:
							sd.setGoal(iMalwa, 0, 1)
		
		# Mughal UHV1: Build the Shalimar Gardens, the Taj Mahal and the Red Fort
		if iBuilding == con.iShalimarGardens or iBuilding == con.iTajMahal or iBuilding == con.iRedFort:
			if iPlayer == iMughals:
				if pPlayer.isAlive():
					if sd.getGoal(iMughals, 0) == -1:
						sd.setWondersBuilt(iMughals, sd.getWondersBuilt(iMughals) + 1)
						if sd.getWondersBuilt(iMughals) == 3:
							sd.setGoal(iMughals, 0, 1)
			else:
				sd.setGoal(iMughals, 0, 0)
		

	def onCombatResult(self, argsList):
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		pWinningUnit,pLosingUnit = argsList
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
		
		# Mamluk UHV3: Sink 5 Portuguese ships
		if pWinningPlayer.getID() == iMamluks:
			if sd.getGoal(iMamluks, 2) == -1:
				if cLosingUnit.getDomainType() == gc.getInfoTypeForString("DOMAIN_SEA") and pLosingPlayer.getID() == iPortugal:
					sd.setNumSinks(sd.getNumSinks() + 1)
					if sd.getNumSinks() == 5:
						sd.setGoal(iMamluks, 2, 1)


	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList
		
		if not gc.getGame().isVictoryValid(iHistoricalVictory):
			return
		
		# Oman UHV1: Spread Islam to 5 non-Islamic coastal cities you do not control
		if pUnit.getOwner() == iOman and bSuccess:
			if sd.getGoal(iOman, 0) == -1 and gc.getGame().getGameTurn() <= getTurnForYear(1470):
				city = CyMap().plot(pUnit.getX(), pUnit.getY()).getPlotCity()
				if (iReligion == con.iSunni and not city.isHasReligion(con.iShia)) or (iReligion == con.iShia and not city.isHasReligion(con.iSunni)):
					if city.getOwner() != iOman and city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
						sd.setNumConversions(sd.getNumConversions() + 1)
						if sd.getNumConversions() == 5:
							sd.setGoal(iOman, 0, 1)


	def onGreatPersonBorn(self, argsList):
		pUnit, iPlayer, pCity = argsList
		
		iGameTurn = gc.getGame().getGameTurn()
		
		# Chauhan UHV2: Gain 3 Great Generals by 1200 AD
		if iPlayer == iChauhan:
			if pUnit.getUnitType() >= con.iGreatGeneral and pUnit.getUnitType() <= con.iGreatGeneral5:
				if sd.getGoal(iChauhan, 1) == -1:
					if gc.getGame().getGameTurn() <= getTurnForYear(1200):
						sd.setNumGenerals(sd.getNumGenerals() + 1)
						if sd.getNumGenerals() == 3:
							sd.setGoal(iChauhan, 1, 1)


	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		
		for i in range(3):
			sd.setReligiousGoal(iPlayer, i, -1)
	
	
	def getMakurianUHV3(self):
		bMediterranean = False
		bRedSea = False
		medRegions = [con.rUpperEgypt, con.rLowerEgypt, con.rPalestine, con.rLebanon, con.rSyria, con.rNorthernSyria, con.rCilicia, con.rLycia, con.rThrace, con.rAsia, con.rCyprus, con.rRhodes]
		redRegions = [con.rSinai, con.rAksum, con.rMerebMellash, con.rJordan, con.rHejaz, con.rYemen, con.rHadhramaut, con.rSuqutra, con.rMahra, con.rOman, con.rBahrain, con.rMesopotamia]
		for regionID in medRegions:
			if utils.checkRegionOwnedCity(iMakuria, regionID, True):
				bMediterranean = True
				break
		for regionID in redRegions:
			if utils.checkRegionOwnedCity(iMakuria, regionID, True):
				bRedSea = True
				break
		return bMediterranean, bRedSea
	
	
	def calculateTopCityCulture(self, x, y):
		"""Returns the CyCity object with the highest culture,
		but if no city is located at (x,y), returns -1."""
		iBestCityValue = 0
		pCurrent = gc.getMap().plot( x, y )
		if pCurrent.isCity():
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()
				for pCity in apCityList:
					iTotalCityValue = pCity.GetCy().getCultureTimes100(pCity.getOwner())
					if iTotalCityValue > iBestCityValue:
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1


	def calculateTopCityPopulation(self, x, y):
		"""Returns the CyCity object with the highest population,
		but if no city is located at (x,y), returns -1."""		
		iBestCityValue = 0
		pCurrent = gc.getMap().plot( x, y )
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()
				for pCity in apCityList:
					iTotalCityValue = pCity.getPopulation()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1


	def getNumOpenBorders(self, iPlayer):
		"""Returns the number of Open Borders agreements that iPlayer has."""
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		iCount = 0
		for iLoopCiv in range(con.iNumPlayers):
			if iLoopCiv != iPlayer:
				if pTeam.isOpenBorders(iLoopCiv):
					iCount += 1
		return iCount


	def getNumBuildings(self, iPlayer, iBuilding):
		"""Returns the number of iBuilding that iPlayer has in his cities."""
		iCount = 0
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.getNumBuilding(iBuilding): iCount += 1
		return iCount


	def getNumProvinces(self, iPlayer):
		"""Returns the number of regions (provinces) that iPlayer controls."""
		iNumProvinces = 0
		regionList = []
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			regionID = gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID()
			if regionID not in regionList and utils.checkRegionControl(iPlayer, regionID):
				regionList.append(regionID)
				iNumProvinces += 1
		return iNumProvinces


	def isHighestGold(self, iPlayer):
		"""Checks whether iPlayer has the highest amount of Gold."""
		bHighest = True
		iGold = gc.getPlayer(iPlayer).getGold()
		for iLoopCiv in range(con.iNumPlayers):
			if iLoopCiv != iPlayer and gc.getPlayer(iLoopCiv).isAlive():
				if gc.getPlayer(iLoopCiv).getGold() > iGold:
					bHighest = False
					break
		return bHighest


	def isTopCityCulture(self, iPlayer, tCoords):
		"""Checks whether the city at tCoords(x,y) is the city with the highest culture."""
		bestCity = self.calculateTopCityCulture(tCoords[0], tCoords[1])
		if bestCity != -1:
			if bestCity.getOwner() == iPlayer and bestCity.getX() == tCoords[0] and bestCity.getY() == tCoords[1]:
				return True
		return False


	def isTopCityPopulation(self, iPlayer, tCoords):
		"""Checks whether the city at tCoords(x,y) is the city with the highest population."""
		bestCity = self.calculateTopCityPopulation(tCoords[0], tCoords[1])
		if bestCity != -1:
			if bestCity.getOwner() == iPlayer and bestCity.getX() == tCoords[0] and bestCity.getY() == tCoords[1]:
				return True
		return False


	def getNumShrines(self, iPlayer):
		"""Returns the number of Shrines belonging to iPlayer."""
		iNumShrines = 0
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.getNumBuilding(con.iCatholicShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iOrthodoxShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iHinduShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iSunniShrine): iNumShrines += 1
			if pCity.getNumBuilding(con.iShiaShrine): iNumShrines += 1
		return iNumShrines
	
	
	def isPlayerHasBuilding(self, iPlayer, iBuilding):
		"""Checks whether iPlayers has at least one iBuilding in his cities."""
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.GetCy().getNumRealBuilding(iBuilding): 
				return True
		return False
	
	
	def isCityHasBuilding(self, tCoords, iBuilding):
		"""Checks whether the city at tCoords(x,y) has iBuilding."""
		plot = gc.getMap().plot(tCoords[0], tCoords[1])
		if plot.isCity():
			if plot.getPlotCity().getNumRealBuilding(iBuilding): 
				return True
		return False
	
	
	def isRegionHasBuilding(self, regionID, iBuilding):
		"""Checks whether any city in the region (province) has iBuilding."""
		plotList = utils.getRegionPlotList([regionID])
		for tCoords in plotList:
			if self.isCityHasBuilding(tCoords, iBuilding):
				return True
		return False


	def isTopTech(self, iPlayer):
		"""Checks whether iPlayer has accumulated the higest amount of Science."""
		iNumTotalTechs = gc.getNumTechInfos()
		bTopTech = True
		iNumTechs = 0
		for iTechLoop in range(iNumTotalTechs):
			if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTechLoop):
				iNumTechs += 1
		for iPlayerLoop in range(con.iNumPlayers):
			if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
				iPlayerNumTechs = 0
				for iTechLoop in range(iNumTotalTechs):
					if gc.getTeam(gc.getPlayer(iPlayerLoop).getTeam()).isHasTech(iTechLoop):
						iPlayerNumTechs = iPlayerNumTechs + 1
				if iPlayerNumTechs >= iNumTechs:
					bTopTech = False
					break
		return bTopTech


	def isTopCulture(self, iPlayer):
		"""Checks whether iPlayer has accumulated the higest number of Culture."""
		bTopCulture = True
		iCulture = gc.getPlayer(iPlayer).countTotalCulture()
		for iPlayerLoop in range(con.iNumPlayers):
			if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
				if gc.getPlayer(iPlayerLoop).countTotalCulture() > iCulture:
					bTopCulture = False
					break
		return bTopCulture


	def isHighestPopulation(self, iPlayer):
		"""Checks whether iPlayer has the highest total population."""
		iPop = gc.getPlayer(iPlayer).getRealPopulation()
		bHighest = True
		for iLoopCiv in range(con.iNumPlayers):
			if iPop < gc.getPlayer(iLoopCiv).getRealPopulation():
				bHighest = False
				break
		return bHighest


	def isMostProductive(self, iPlayer):
		"""Checks whether iPlayer has the highest amount of total Production in this cities."""
		iTopValue = 0
		iTopCiv = -1
		for iLoopPlayer in range(con.iNumPlayers):
			pLoopPlayer = gc.getPlayer(iLoopPlayer)
			if pLoopPlayer.getNumCities() > 0:
				iValue = pLoopPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
				if iValue > iTopValue:
					iTopValue = iValue
					iTopCiv = iLoopPlayer
		return (iTopCiv == iPlayer)


	def getNumVassals(self, iPlayer):
		"""Returns the number of vassals belonging to iPlayer."""
		iCounter = 0
		for iCiv in range(con.iNumPlayers):
			if iCiv != iPlayer:
				if gc.getPlayer(iCiv).isAlive():
					if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iPlayer):
						iCounter += 1
		return iCounter


	def getNumLuxuries(self, iPlayer):
		"""Returns the number of happiness-giving resources available to iPlayer."""
		nLuxuries = 0
		pPlayer = gc.getPlayer(iPlayer)
		for iBonus in range(con.iNumResources):
			if gc.getBonusInfo(iBonus).getHappiness() > 0:
				if pPlayer.getNumAvailableBonuses(iBonus) > 0:
					nLuxuries += 1
		return nLuxuries


	def getRegionsOwnedCity(self, iPlayer, regionList, bCoastal=False):
		"""Checks whether the player has any city in the provided list of regions (provinces)."""
		bFound = False
		for regionID in regionList:
			if utils.checkRegionOwnedCity(iPlayer, regionID, bCoastal):
				bFound = True
				break
		return bFound


	def isFreeOfIslam(self, regionList):
		"""Checks whether there is Sunni or Shia Islam present in the list of regions (provinces)."""
		bSuccess = True
		for regionID in regionList:
			plotList = utils.getRegionPlotList([regionID])
			for tPlot in plotList:
				pCurrent = gc.getMap().plot(tPlot[0], tPlot[1])
				if pCurrent.isCity():
					if pCurrent.getPlotCity().isHasReligion(con.iSunni) or pCurrent.getPlotCity().isHasReligion(con.iShia):
						bSuccess = False
						break
		return bSuccess


	def isHasLegendaryCity(self, iPlayer):
		"""Checks whether iPlayer has a city with Legendary culture."""
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			if pCity.GetCy().countTotalCultureTimes100() >= utils.getTurns(2500000):
				return True
		return False


	def isTopReligion(self, iReligion, bAllowDraw=False):
		"""Checks whether iReligion is the most popular religion. If bAllowDraw is set to True,
		the function will return True even in case of a draw with another religion."""
		religionPercent = gc.getGame().calculateReligionPercent(iReligion)
		bFirst = True
		for iLoop in range(con.iNumReligions):
			if iLoop != iReligion:
				if gc.getGame().calculateReligionPercent(iLoop) >= religionPercent:
					if bAllowDraw and gc.getGame().calculateReligionPercent(iLoop) == religionPercent:
						continue
					bFirst = False
					break
		return bFirst


	def checkRegions(self, iPlayer, regionList, bVassal=False):
		"""Checks whether iPlayer and his vassals (if bVassal is True) control
		all regions (provinces) in regionList."""
		for regionID in regionList:
			if not utils.checkRegionControl(iPlayer, regionID, bVassal):
				return False
		return True
	
	
	def countUniqueGreatPeople(self, tCoords):
		"""Returns the number of Great People settled at tCoords(x,y)."""
		iCount = 0
		plot = gc.getMap().plot(tCoords[0], tCoords[1])
		if plot.isCity():
			city = plot.getPlotCity()
			iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
			for i in range(iGreatPriest, iGreatPriest+7, 1):
				iCount += min(1, city.getFreeSpecialistCount(i))
		return iCount
	
	
	def countRelics(self, iPlayer):
		"""Returns the number of relic units and reliquaries belonging to iPlayer."""
		iCount = 0
		iReligion = gc.getPlayer(iPlayer).getStateReligion()
		playerHelper = PyPlayer(iPlayer)
		apCityList = playerHelper.getCityList()
		for iRelic in con.relics.keys():
			if gc.getBuildingInfo(iRelic).getStateReligion() != iReligion and gc.getBuildingInfo(iRelic).getOrStateReligion() != iReligion:
				continue
			if playerHelper.hasUnitType(con.relics[iRelic][0]):
				iCount += 1
			for pCity in apCityList:
				iCount += pCity.getNumBuilding(iRelic)
		return iCount
	
	
	def countVassalReligions(self, iPlayer):
		"""Returns the number of unique state religions found among vassals of iPlayer."""
		religionList = []
		iTeam = gc.getPlayer(iPlayer).getTeam()
		for iLoopPlayer in range(con.iNumPlayers):
			if iLoopPlayer != iPlayer:
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if gc.getTeam(pLoopPlayer.getTeam()).isVassal(iPlayer) and pLoopPlayer.getStateReligion() != -1:
					religionList.append(pLoopPlayer.getStateReligion())
		return len(utils.uniq(religionList))
	
	
	def countPlayersByMinAttitude(self, iPlayer, iMinAttitude=4):
		"""Returns the number of players with attitude towards iPlayer being 
		greater or equal to iMinAttitude; The default of 4 is ATTITUDE_FRIENDLY."""
		iCount = 0
		for iLoopPlayer in range(con.iNumPlayers):
			if iLoopPlayer != iPlayer and gc.getPlayer(iLoopPlayer).isAlive():
				if gc.getPlayer(iLoopPlayer).AI_getAttitude(iPlayer) >= iMinAttitude:
					iCount += 1
		return iCount
	
	
	def getTopPopulationRegion(self):
		"""Returns the ID of the most populous region (province)."""
		data = {}
		for iProvince in range(con.iNumRegions):
			data[iProvince] = 0
		for iLoopPlayer in range(con.iBarbarian + 1):
			apCityList = PyPlayer(iLoopPlayer).getCityList()
			for pCity in apCityList:
				data[pCity.GetCy().plot().getRegionID()] += pCity.getPopulation()
		key = -1
		for key, value in sorted(data.iteritems(), key=lambda (k,v): (v,k)):
			pass
		return key
	
	
	def getIcon(self, bVal):
		"""Returns a green check mark if bVal is True, or a red cross if bVal is False."""
		if bVal:
			return u"%c" %(CyGame().getSymbolID(FontSymbols.POWER_CHAR) + 14)
		else:
			return u"%c" %(CyGame().getSymbolID(FontSymbols.POWER_CHAR) + 15)


	def getUHVHelp(self, iPlayer, iGoal):
		"""Returns an array of help strings used by the Victory Screen table."""
		
		aHelp = []
		pPlayer = gc.getPlayer(iPlayer)
		
		# the info is outdated or irrelevant once the goal has been accomplished or failed
		if sd.getGoal(iPlayer, iGoal) == 1:
			aHelp.append(self.getIcon(True) + localText.getText("TXT_KEY_VICTORY_GOAL_ACCOMPLISHED", ()))
			return aHelp
		elif sd.getGoal(iPlayer, iGoal) == 0:
			aHelp.append(self.getIcon(False) + localText.getText("TXT_KEY_VICTORY_GOAL_FAILED", ()))
			return aHelp
		
		if iPlayer == iByzantium:
			if iGoal == 0: 
				aHelp.append(self.getIcon(self.isTopCityCulture(iByzantium, con.tConstantinople)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_CULTURE_CITY", (localText.getText("TXT_KEY_VICTORY_CONSTANTINOPLE", ()), )))
			elif iGoal == 1:
				iCount = self.getNumProvinces(iByzantium)
				aHelp.append(self.getIcon(iCount >= 15) + localText.getText("TXT_KEY_VICTORY_PROVINCES_CONTROLLED", (iCount, 15)))
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isHighestGold(iByzantium)) + localText.getText("TXT_KEY_VICTORY_GREATEST_WEALTH", ()))
		
		elif iPlayer == iAbbasids:
			if iGoal == 0: 
				iCount = self.getNumShrines(iAbbasids)
				aHelp.append(self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_SHRINES_CONTROLLED", (iCount, 3)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(self.isTopTech(iAbbasids)) + localText.getText("TXT_KEY_VICTORY_BEST_TECHS", ()) + ', ' + self.getIcon(self.isTopCulture(iAbbasids)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_CULTURE", ()))
			elif iGoal == 2:
				fPercent = gc.getGame().calculateReligionPercent(con.iSunni)
				aHelp.append(self.getIcon(fPercent >= 50.0) + localText.getText("TXT_KEY_VICTORY_RELIGION_SPREAD_TO", (gc.getReligionInfo(con.iSunni).getTextKey(), str(fPercent), 50)))
		
		elif iPlayer == iMakuria:
			if iGoal == 0: 
				iCount = self.getNumLuxuries(iMakuria)
				aHelp.append(self.getIcon(iCount >= 6) + localText.getText("TXT_KEY_VICTORY_LUXURY_RESOURCES", (iCount, 6)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iMakuria, 1) != 0) + localText.getText("TXT_KEY_VICTORY_NO_CITIES_LOST", ()))
			elif iGoal == 2:
				bMedSea, bRedSea = self.getMakurianUHV3()
				aHelp.append(self.getIcon(bMedSea) + localText.getText("TXT_KEY_VICTORY_MEDITERRANEAN_SEA_ACCESS", ()) + ', ' + self.getIcon(bRedSea) + localText.getText("TXT_KEY_VICTORY_RED_SEA_ACCESS", ()))
		
		elif iPlayer == iChauhan:
			if iGoal == 0: 
				bSuccess = self.isFreeOfIslam([con.rDuggar, con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rKarnataka])
				aHelp.append(self.getIcon(bSuccess) + localText.getText("TXT_KEY_VICTORY_NO_ISLAM_IN_HINDUSTAN", ()))
			elif iGoal == 1:
				iCount = sd.getNumGenerals()
				aHelp.append(self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_GREAT_GENERALS_CREATED", (iCount, 3)))
			elif iGoal == 2:
				bSuccess = self.isFreeOfIslam([con.rDuggar, con.rPunjab, con.rGird, con.rUttarBharat, con.rRajputana, con.rMaharashtra, con.rMalwa, con.rGujarat, con.rKarnataka, con.rGandhar, con.rSindh])
				aHelp.append(self.getIcon(bSuccess) + localText.getText("TXT_KEY_VICTORY_NO_ISLAM_IN_HINDUSTAN_AND_GANDHAR", ()))
		
		elif iPlayer == iMalwa:
			if iGoal == 0: 
				iNumColleges, iNumTemples = sd.getVal('lMalwaBuildings')
				aHelp.append(self.getIcon(iNumColleges >= 3) + localText.getText("TXT_KEY_VICTORY_SANSKRIT_COLLEGES", (iNumColleges, 3)) + ', ' + self.getIcon(iNumTemples >= 3) + localText.getText("TXT_KEY_VICTORY_HINDU_MANDIRS", (iNumTemples, 3)))
			elif iGoal == 1:
				iCount = 0
				if pPlayer.getNumCities() > 0:
					capital = pPlayer.getCapitalCity()
					iCount = self.countUniqueGreatPeople((capital.getX(), capital.getY()))
				aHelp.append(self.getIcon(iCount >= 5) + localText.getText("TXT_KEY_VICTORY_GREAT_PEOPLE_SETTLED", (iCount, 5)))
			elif iGoal == 2:
				bSuccess = self.isHasLegendaryCity(iMalwa)
				aHelp.append(self.getIcon(bSuccess) + localText.getText("TXT_KEY_VICTORY_LEGENDARY_CITIES", (bSuccess and 1 or 0, 1)))
		
		elif iPlayer == iSamanids:
			if iGoal == 0: 
				aHelp.append(self.getIcon(self.isTopCulture(iSamanids)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_CULTURE", ()))
			elif iGoal == 1:
				aHelp.append(self.getIcon(sd.getGoal(iSamanids, 1) != 0) + localText.getText("TXT_KEY_VICTORY_NO_CITIES_LOST", ()))
			elif iGoal == 2:
				iCount = self.getNumProvinces(iSamanids)
				aHelp.append(self.getIcon(iCount >= 8) + localText.getText("TXT_KEY_VICTORY_PROVINCES_CONTROLLED", (iCount, 8)))
		
		elif iPlayer == iArmenia:
			if iGoal == 0: 
				aHelp.append(self.getIcon(False) + localText.getText("TXT_KEY_VICTORY_ORTHODOX_CATHEDRALS_BUILT", (0, 1)))
			elif iGoal == 1:
				bGreaterArmenia = utils.checkRegionControl(iArmenia, con.rGreaterArmenia)
				bLesserArmenia = utils.checkRegionControl(iArmenia, con.rLesserArmenia)
				bKars = utils.checkRegionControl(iArmenia, con.rKars)
				bVaspurakan = utils.checkRegionControl(iArmenia, con.rVaspurakan)
				aHelp.append(self.getIcon(bGreaterArmenia) + utils.getRegionName(con.rGreaterArmenia) + ', ' + self.getIcon(bLesserArmenia) + utils.getRegionName(con.rLesserArmenia) + ', ' + self.getIcon(bKars) + utils.getRegionName(con.rKars) + ', ' + self.getIcon(bVaspurakan) + utils.getRegionName(con.rVaspurakan))
			elif iGoal == 2:
				iCount = pPlayer.countTotalCulture()
				aHelp.append(self.getIcon(iCount >= utils.getTurns(25000)) + localText.getText("TXT_KEY_VICTORY_TOTAL_CULTURE", (iCount, utils.getTurns(25000))))

		elif iPlayer == iYemen:
			if iGoal == 0: 
				iCount = sd.getWondersBuilt(iYemen)
				aHelp.append(self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_SUFI_SHRINES_BUILT", (iCount, 3)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iSharif)) + gc.getProjectInfo(con.iSharif).getText())
			elif iGoal == 2:
				iCount = pPlayer.getNumAvailableBonuses(con.iCoffee)
				aHelp.append(self.getIcon(iCount >= 4) + localText.getText("TXT_KEY_VICTORY_RESOURCES", (gc.getBonusInfo(con.iCoffee).getTextKey(), iCount, 4)))
		
		elif iPlayer == iBuyids:
			if iGoal == 0: 
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iShahanshah)) + gc.getProjectInfo(con.iShahanshah).getText())
			elif iGoal == 1:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iCaliph)) + gc.getProjectInfo(con.iCaliph).getText())
			elif iGoal == 2:
				bMesopotamia = utils.checkRegionControl(iBuyids, con.rMesopotamia)	
				bKhuzestan = utils.checkRegionControl(iBuyids, con.rKhuzestan)	
				bHormuz = utils.checkRegionControl(iBuyids, con.rHormuz)	
				bOman = utils.checkRegionControl(iBuyids, con.rOman)	
				aHelp.append(self.getIcon(bMesopotamia) + utils.getRegionName(con.rMesopotamia) + ', ' + self.getIcon(bKhuzestan) + utils.getRegionName(con.rKhuzestan) + ', ' + self.getIcon(bHormuz) + utils.getRegionName(con.rHormuz) + ', ' + self.getIcon(bOman) + utils.getRegionName(con.rOman))	

		elif iPlayer == iGujarat:
			if iGoal == 0:
				iPiety = sd.getPiety(iGujarat)
				bReligion = (pPlayer.getStateReligion() == con.iHinduism)
				aHelp.append(self.getIcon(bReligion) + localText.getText("TXT_KEY_VICTORY_STATE_RELIGION", (gc.getReligionInfo(con.iHinduism).getTextKey(), )) + ', ' + self.getIcon(iPiety > 90) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 91)))
			elif iGoal == 1:
				bGujarat = utils.checkRegionControl(iGujarat, con.rGujarat, True)
				bSindh = utils.checkRegionControl(iGujarat, con.rSindh, True)
				bMalwa = utils.checkRegionControl(iGujarat, con.rMalwa, True)
				aHelp.append(self.getIcon(bGujarat) + utils.getRegionName(con.rGujarat) + ', ' + self.getIcon(bSindh) + utils.getRegionName(con.rSindh) + ', ' + self.getIcon(bMalwa) + utils.getRegionName(con.rMalwa))
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isHighestPopulation(iGujarat)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_POPULATION", ()))
		
		elif iPlayer == iGhaznavids:
			if iGoal == 0:
				aHelp.append(self.getIcon(pPlayer.getGold() >= utils.getTurns(3000)) + localText.getText("TXT_KEY_VICTORY_GOLD", (pPlayer.getGold(), utils.getTurns(3000))))
			elif iGoal == 1:
				bPunjab = utils.checkRegionOwnedCity(iGhaznavids, con.rPunjab)
				bSindh = utils.checkRegionOwnedCity(iGhaznavids, con.rSindh)
				bBalochistan = utils.checkRegionOwnedCity(iGhaznavids, con.rBalochistan)
				bSistan = utils.checkRegionOwnedCity(iGhaznavids, con.rSistan)
				bEasternKhorasan = utils.checkRegionOwnedCity(iGhaznavids, con.rEasternKhorasan)
				bBactria = utils.checkRegionOwnedCity(iGhaznavids, con.rBactria)
				bHindukush = utils.checkRegionOwnedCity(iGhaznavids, con.rHindukush)
				aHelp.append(self.getIcon(bPunjab) + utils.getRegionName(con.rPunjab) + ', ' + self.getIcon(bSindh) + utils.getRegionName(con.rSindh) + ', ' + self.getIcon(bBalochistan) + utils.getRegionName(con.rBalochistan) + ', ' + self.getIcon(bSistan) + utils.getRegionName(con.rSistan) + ', ' + self.getIcon(bEasternKhorasan) + utils.getRegionName(con.rEasternKhorasan) + ', ')
				aHelp.append(self.getIcon(bBactria) + utils.getRegionName(con.rBactria) + ', ' + self.getIcon(bHindukush) + utils.getRegionName(con.rHindukush))
			elif iGoal == 2:
				aHelp.append(self.getIcon(pPlayer.getGold() >= utils.getTurns(10000)) + localText.getText("TXT_KEY_VICTORY_GOLD", (pPlayer.getGold(), utils.getTurns(10000))))
		
		elif iPlayer == iFatimids:
			if iGoal == 0:
				bUpperEgypt = utils.checkRegionControl(iFatimids, con.rUpperEgypt)
				bLowerEgypt = utils.checkRegionControl(iFatimids, con.rLowerEgypt)
				bPalestine = utils.checkRegionControl(iFatimids, con.rPalestine)
				bLebanon = utils.checkRegionControl(iFatimids, con.rLebanon)
				bSyria = utils.checkRegionControl(iFatimids, con.rSyria)
				bNorthernSyria = utils.checkRegionControl(iFatimids, con.rNorthernSyria)
				bJordan = utils.checkRegionControl(iFatimids, con.rJordan)
				bHejaz = utils.checkRegionControl(iFatimids, con.rHejaz)
				aHelp.append(self.getIcon(bUpperEgypt) + utils.getRegionName(con.rUpperEgypt) + ', ' + self.getIcon(bLowerEgypt) + utils.getRegionName(con.rLowerEgypt) + ', ' + self.getIcon(bPalestine) + utils.getRegionName(con.rPalestine) + ', ' + self.getIcon(bLebanon) + utils.getRegionName(con.rLebanon) + ', ' + self.getIcon(bSyria) + utils.getRegionName(con.rSyria) + ', ')
				aHelp.append(self.getIcon(bNorthernSyria) + utils.getRegionName(con.rNorthernSyria) + ', ' + self.getIcon(bJordan) + utils.getRegionName(con.rJordan) + ', ' + self.getIcon(bHejaz) + utils.getRegionName(con.rHejaz))
			elif iGoal == 1:
				fPercent = gc.getGame().calculateReligionPercent(con.iShia)
				aHelp.append(self.getIcon(fPercent >= 30.0) + localText.getText("TXT_KEY_VICTORY_RELIGION_SPREAD_TO", (gc.getReligionInfo(con.iShia).getTextKey(), str(fPercent), 30)))
			elif iGoal == 2:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iCaliph)) + gc.getProjectInfo(con.iCaliph).getText())
		
		elif iPlayer == iGeorgia:
			if iGoal == 0:
				bGeorgia = utils.checkRegionControl(iGeorgia, con.rGeorgia, True)
				bShirvan = utils.checkRegionControl(iGeorgia, con.rShirvan, True)
				bKars = utils.checkRegionControl(iGeorgia, con.rKars, True)
				bGreaterArmenia = utils.checkRegionControl(iGeorgia, con.rGreaterArmenia, True)
				bVaspurakan = utils.checkRegionControl(iGeorgia, con.rVaspurakan, True)
				bTrebizond = utils.checkRegionControl(iGeorgia, con.rTrebizond, True)
				aHelp.append(self.getIcon(bGeorgia) + utils.getRegionName(con.rGeorgia) + ', ' + self.getIcon(bShirvan) + utils.getRegionName(con.rShirvan) + ', ' + self.getIcon(bKars) + utils.getRegionName(con.rKars) + ', ' + self.getIcon(bGreaterArmenia) + utils.getRegionName(con.rGreaterArmenia) + ', ' + self.getIcon(bVaspurakan) + utils.getRegionName(con.rVaspurakan) + ', ' + self.getIcon(bTrebizond) + utils.getRegionName(con.rTrebizond))
			if iGoal == 1:
				iNumCastles = self.getNumBuildings(iGeorgia, con.iCastle)
				iNumTemples = self.getNumBuildings(iGeorgia, con.iOrthodoxTemple)
				iNumMonasteries = self.getNumBuildings(iGeorgia, con.iOrthodoxMonastery)
				aHelp.append(self.getIcon(iNumCastles >= 5) + localText.getText("TXT_KEY_VICTORY_CASTLES", (iNumCastles, 5)) + ', ' + self.getIcon(iNumTemples >= 5) + localText.getText("TXT_KEY_VICTORY_CHURCHES", (iNumTemples, 5)) + ', ' + self.getIcon(iNumMonasteries >= 5) + localText.getText("TXT_KEY_VICTORY_MONASTERIES", (iNumMonasteries, 5)))
			if iGoal == 2:
				regionList = [con.rGreaterArmenia, con.rKars, con.rVaspurakan, con.rGeorgia, con.rShirvan, con.rLesserArmenia]
				resultList = []
				for regionID in regionList:
					for iCiv in range(con.iBarbarian+1):
						if utils.checkRegionOwnedCity(iCiv, regionID):
							if iCiv == con.iBarbarian or gc.getPlayer(iCiv).getStateReligion() not in [-1, con.iCatholicism, con.iOrthodoxy]:
								resultList.append(regionID)
								break
				aHelp.append(self.getIcon(con.rGeorgia not in resultList) + utils.getRegionName(con.rGeorgia) + ', ' + self.getIcon(con.rShirvan not in resultList) + utils.getRegionName(con.rShirvan) + ', ' + self.getIcon(con.rKars not in resultList) + utils.getRegionName(con.rKars) + ', ' + self.getIcon(con.rGreaterArmenia not in resultList) + utils.getRegionName(con.rGreaterArmenia) + ', ' + self.getIcon(con.rLesserArmenia not in resultList) + utils.getRegionName(con.rLesserArmenia) + ', ' + self.getIcon(con.rVaspurakan not in resultList) + utils.getRegionName(con.rVaspurakan))
		
		elif iPlayer == iGhorids:
			if iGoal == 0:
				bComplete = False
				if sd.getGoal(iGhorids, 0) == 1: bComplete = True
				aHelp.append(self.getIcon(bComplete) + localText.getText("TXT_KEY_VICTORY_PALACE_BUILT_IN_DELHI", ()))
			elif iGoal == 1:
				iPiety = sd.getPiety(iGhorids)
				bReligion = (pPlayer.getStateReligion() == con.iSunni)
				aHelp.append(self.getIcon(bReligion) + localText.getText("TXT_KEY_VICTORY_STATE_RELIGION", (gc.getReligionInfo(con.iSunni).getTextKey(), )) + ', ' + self.getIcon(iPiety > 90) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 91)))
			elif iGoal == 2:
				bPunjab = utils.checkRegionControl(iGhorids, con.rPunjab)
				bSindh = utils.checkRegionControl(iGhorids, con.rSindh)
				bRajputana = utils.checkRegionControl(iGhorids, con.rRajputana)
				bGujarat = utils.checkRegionControl(iGhorids, con.rGujarat)
				bUttarBharat = utils.checkRegionControl(iGhorids, con.rUttarBharat)
				bGird = utils.checkRegionControl(iGhorids, con.rGird)
				bMalwa = utils.checkRegionControl(iGhorids, con.rMalwa)
				bMaharashtra = utils.checkRegionControl(iGhorids, con.rMaharashtra)
				aHelp.append(self.getIcon(bPunjab) + utils.getRegionName(con.rPunjab) + ', ' + self.getIcon(bSindh) + utils.getRegionName(con.rSindh) + ', ' + self.getIcon(bRajputana) + utils.getRegionName(con.rRajputana) + ', ' + self.getIcon(bGujarat) + utils.getRegionName(con.rGujarat) + ', ' + self.getIcon(bUttarBharat) + utils.getRegionName(con.rUttarBharat) + ', ')
				aHelp.append(self.getIcon(bGird) + utils.getRegionName(con.rGird) + ', ' + self.getIcon(bMalwa) + utils.getRegionName(con.rMalwa) + ', ' + self.getIcon(bMaharashtra) + utils.getRegionName(con.rMaharashtra))
		
		elif iPlayer == iSindh:
			if iGoal == 0:
				aHelp.append(self.getIcon(self.isMostProductive(iSindh)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_PRODUCTION", ()))
			elif iGoal == 1:
				bSindh = utils.checkRegionControl(iSindh, con.rSindh)
				bGujarat = utils.checkRegionControl(iSindh, con.rGujarat)
				aHelp.append(self.getIcon(bSindh) + utils.getRegionName(con.rSindh) + ', ' + self.getIcon(bGujarat) + utils.getRegionName(con.rGujarat))
			elif iGoal == 2:
				iCount = sd.getWondersBuilt(iSindh)
				aHelp.append(self.getIcon(iCount >= 4) + localText.getText("TXT_KEY_VICTORY_SUFI_SHRINES_BUILT", (iCount, 4)))
		
		elif iPlayer == iSeljuks:
			if iGoal == 0:
				totalLand = gc.getMap().getLandPlots()
				ownedLand = pPlayer.getTotalLand()
				if totalLand > 0:
					landPercent = (ownedLand * 100.0) / totalLand
				else:
					landPercent = 0.0
				aHelp.append(self.getIcon(landPercent >= 8.995) + localText.getText("TXT_KEY_VICTORY_LAND_AREA", ()) + ': ' + u"%.2f" % landPercent + '% / 9%')
			elif iGoal == 1:
				iCount = self.getNumVassals(iSeljuks)
				aHelp.append(self.getIcon(iCount >= 2) + localText.getText("TXT_KEY_VICTORY_VASSALS", (iCount, 2)))
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isTopCulture(iSeljuks)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_CULTURE", ()))
		
		elif iPlayer == iRum:
			if iGoal == 0:
				iNumProvinces = 0
				regionList = [con.rThrace, con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond]
				for regionID in regionList:
					if utils.checkRegionControl(iRum, regionID):
						iNumProvinces += 1
				aHelp.append(self.getIcon(iNumProvinces >= 6) + localText.getText("TXT_KEY_VICTORY_PROVINCES_HELD", (iNumProvinces, 6)))
			elif iGoal == 1:
				iCount = self.getNumBuildings(iRum, con.iSufiShrine)
				aHelp.append(self.getIcon(iCount >= 5) + localText.getText("TXT_KEY_VICTORY_SUFI_SHRINES_CONTROLLED", (iCount, 5)))
			elif iGoal == 2:
				bThrace = utils.checkRegionControl(iRum, con.rThrace)
				bAsia = utils.checkRegionControl(iRum, con.rAsia)
				bBithynia = utils.checkRegionControl(iRum, con.rBithynia)
				bLycia = utils.checkRegionControl(iRum, con.rLycia)
				bPontus = utils.checkRegionControl(iRum, con.rPontus)
				bGalatia = utils.checkRegionControl(iRum, con.rGalatia)
				bPaphlagonia = utils.checkRegionControl(iRum, con.rPaphlagonia)
				bCilicia = utils.checkRegionControl(iRum, con.rCilicia)
				bCappadocia = utils.checkRegionControl(iRum, con.rCappadocia)
				bTrebizond = utils.checkRegionControl(iRum, con.rTrebizond)
				bLesserArmenia = utils.checkRegionControl(iRum, con.rLesserArmenia)
				aHelp.append(self.getIcon(bThrace) + utils.getRegionName(con.rThrace) + ', ' + self.getIcon(bAsia) + utils.getRegionName(con.rAsia) + ', ' + self.getIcon(bBithynia) + utils.getRegionName(con.rBithynia) + ', ' + self.getIcon(bLycia) + utils.getRegionName(con.rLycia) + ', ' + self.getIcon(bPontus) + utils.getRegionName(con.rPontus) + ', ' + self.getIcon(bGalatia) + utils.getRegionName(con.rGalatia) + ', ' + self.getIcon(bPaphlagonia) + utils.getRegionName(con.rPaphlagonia) + ', ')
				aHelp.append(self.getIcon(bCilicia) + utils.getRegionName(con.rCilicia) + ', ' + self.getIcon(bCappadocia) + utils.getRegionName(con.rCappadocia) + ', ' + self.getIcon(bTrebizond) + utils.getRegionName(con.rTrebizond) + ', ' + self.getIcon(bLesserArmenia) + utils.getRegionName(con.rLesserArmenia))
		
		elif iPlayer == iKhwarezm:
			if iGoal == 0:
				iCount = pPlayer.getNumAvailableBonuses(con.iSilk)
				aHelp.append(self.getIcon(iCount >= 5) + localText.getText("TXT_KEY_VICTORY_RESOURCES", (gc.getBonusInfo(con.iSilk).getTextKey(), iCount, 5)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iShahanshah)) + gc.getProjectInfo(con.iShahanshah).getText())
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iKhwarezm, 2) != 0) + localText.getText("TXT_KEY_VICTORY_NO_CITIES_LOST", ()))
 		
		elif iPlayer == iAntioch:
			if iGoal == 0:
				bNorthernSyria = utils.checkRegionControl(iAntioch, con.rNorthernSyria, True)
				iCount = 0
				if utils.checkRegionControl(iAntioch, con.rEdessa, True): iCount += 1
				if utils.checkRegionControl(iAntioch, con.rCilicia, True): iCount += 1
				if utils.checkRegionControl(iAntioch, con.rSyria, True): iCount += 1
				if utils.checkRegionControl(iAntioch, con.rLebanon, True): iCount += 1
				if utils.checkRegionControl(iAntioch, con.rLesserArmenia, True): iCount += 1
				aHelp.append(self.getIcon(bNorthernSyria) + utils.getRegionName(con.rNorthernSyria) + ', ' + self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_ADJACENT_PROVINCES", (iCount, 3)))
			elif iGoal == 1:
				iCount = self.getNumOpenBorders(iAntioch)
				aHelp.append(self.getIcon(iCount >= 6) + localText.getText("TXT_KEY_VICTORY_OPEN_BORDERS_AGREEMENTS", (iCount, 6)))
			elif iGoal == 2:
				iCount = self.getNumBuildings(iAntioch, con.iVenetianQuarter)
				aHelp.append(self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_VENETIAN_QUARTERS", (iCount, 3)))
		
		elif iPlayer == iCrusaders:
			if iGoal == 0: 
				bPalestine = utils.checkRegionControl(iCrusaders, con.rPalestine, True)
				bJordan = utils.checkRegionControl(iCrusaders, con.rJordan, True)
				bCyprus = utils.checkRegionControl(iCrusaders, con.rCyprus, True)
				aHelp.append(self.getIcon(bPalestine) + utils.getRegionName(con.rPalestine) + ', ' + self.getIcon(bJordan) + utils.getRegionName(con.rJordan) + ', ' + self.getIcon(bCyprus) + utils.getRegionName(con.rCyprus))
			elif iGoal == 1:
				iCount = pPlayer.getNumAvailableBonuses(con.iSilk) + pPlayer.getNumAvailableBonuses(con.iIncense) + pPlayer.getNumAvailableBonuses(con.iSpices)
				aHelp.append(self.getIcon(iCount >= 8) + localText.getText("TXT_KEY_VICTORY_TOTAL_SILK_INCENSE_SPICES", (iCount, 8)))
			elif iGoal == 2:
				iPiety = sd.getPiety(iCrusaders)
				bReligion = (pPlayer.getStateReligion() == con.iCatholicism)
				aHelp.append(self.getIcon(bReligion) + localText.getText("TXT_KEY_VICTORY_STATE_RELIGION", (gc.getReligionInfo(con.iCatholicism).getTextKey(), )) + ', ' + self.getIcon(iPiety > 90) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 91)))
		
		elif iPlayer == iZengids:
			if iGoal == 0: 
				bUpperEgypt = utils.checkRegionControl(iZengids, con.rUpperEgypt)
				bLowerEgypt = utils.checkRegionControl(iZengids, con.rLowerEgypt)
				aHelp.append(self.getIcon(bUpperEgypt) + utils.getRegionName(con.rUpperEgypt) + ', ' + self.getIcon(bLowerEgypt) + utils.getRegionName(con.rLowerEgypt))
			elif iGoal == 1:
				regionList = [con.rCilicia, con.rPalestine, con.rJordan, con.rSyria, con.rLebanon, con.rNorthernSyria, con.rUpperEgypt, con.rLowerEgypt]
				resultList = []
				for regionID in regionList:
					for iCiv in range(con.iBarbarian+1):
						if utils.checkRegionOwnedCity(iCiv, regionID):
							if gc.getPlayer(iCiv).getStateReligion() in [con.iCatholicism, con.iOrthodoxy]:
								resultList.append(regionID)
								break
				aHelp.append(self.getIcon(con.rCilicia not in resultList) + utils.getRegionName(con.rCilicia) + ', ' + self.getIcon(con.rPalestine not in resultList) + utils.getRegionName(con.rPalestine) + ', ' + self.getIcon(con.rJordan not in resultList) + utils.getRegionName(con.rJordan) + ', ' + self.getIcon(con.rSyria not in resultList) + utils.getRegionName(con.rSyria) + ', ' + self.getIcon(con.rLebanon not in resultList) + utils.getRegionName(con.rLebanon) + ', ' + self.getIcon(con.rNorthernSyria not in resultList) + utils.getRegionName(con.rNorthernSyria) + ', ' + self.getIcon(con.rUpperEgypt not in resultList) + utils.getRegionName(con.rUpperEgypt) + ', ' + self.getIcon(con.rLowerEgypt not in resultList) + utils.getRegionName(con.rLowerEgypt))
		
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getGoal(iZengids, 2) != 0) + localText.getText("TXT_KEY_VICTORY_NO_CITIES_LOST", ()))

		elif iPlayer == iOman:
			if iGoal == 0: 
				aHelp.append(self.getIcon(sd.getNumConversions() >= 5) + localText.getText("TXT_KEY_VICTORY_SUCCESSFUL_CONVERSIONS", (sd.getNumConversions(), 5)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(pPlayer.getGold() >= utils.getTurns(50000)) + localText.getText("TXT_KEY_VICTORY_GOLD", (pPlayer.getGold(), utils.getTurns(50000))))
			elif iGoal == 2:
				bAfrica = not self.getRegionsOwnedCity(iPortugal, [21,22,27,28], True)
				bArabia = not self.getRegionsOwnedCity(iPortugal, [23,29,30,31,32,33,34,35,38,39,48], True)
				bPersia = not self.getRegionsOwnedCity(iPortugal, [52,54,67,70], True)
				aHelp.append(self.getIcon(bAfrica) + localText.getText("TXT_KEY_VICTORY_AFRICA", ()) + ', ' + self.getIcon(bArabia) + localText.getText("TXT_KEY_VICTORY_ARABIA", ()) + ', ' + self.getIcon(bPersia) + localText.getText("TXT_KEY_VICTORY_PERSIA", ()))
		
		elif iPlayer == iAyyubids:
			if iGoal == 0: 
				aHelp.append(self.getIcon(pPlayer.countCorporations(con.iVenetians)) + localText.getText("TXT_KEY_VICTORY_VENETIANS", ()) + ', ' + self.getIcon(pPlayer.countCorporations(con.iGenoans)) + localText.getText("TXT_KEY_VICTORY_GENOANS", ()))
			elif iGoal == 1:
				bUpperEgypt = utils.checkRegionControl(iAyyubids, con.rUpperEgypt)
				bLowerEgypt = utils.checkRegionControl(iAyyubids, con.rLowerEgypt)
				bPalestine = utils.checkRegionControl(iAyyubids, con.rPalestine)
				bLebanon = utils.checkRegionControl(iAyyubids, con.rLebanon)
				bSyria = utils.checkRegionControl(iAyyubids, con.rSyria)
				bNorthernSyria = utils.checkRegionControl(iAyyubids, con.rNorthernSyria)
				bJordan = utils.checkRegionControl(iAyyubids, con.rJordan)
				bHejaz = utils.checkRegionControl(iAyyubids, con.rHejaz)
				bYemen = utils.checkRegionControl(iAyyubids, con.rYemen)
				aHelp.append(self.getIcon(bUpperEgypt) + utils.getRegionName(con.rUpperEgypt) + ', ' + self.getIcon(bLowerEgypt) + utils.getRegionName(con.rLowerEgypt) + ', ' + self.getIcon(bPalestine) + utils.getRegionName(con.rPalestine) + ', ' + self.getIcon(bLebanon) + utils.getRegionName(con.rLebanon) + ', ' + self.getIcon(bSyria) + utils.getRegionName(con.rSyria) + ', ')
				aHelp.append(self.getIcon(bNorthernSyria) + utils.getRegionName(con.rNorthernSyria) + ', ' + self.getIcon(bJordan) + utils.getRegionName(con.rJordan) + ', ' + self.getIcon(bHejaz) + utils.getRegionName(con.rHejaz) + ', ' + self.getIcon(bYemen) + utils.getRegionName(con.rYemen))
			elif iGoal == 2:
				aHelp.append(self.getIcon(gc.getGame().getRankTeam(0) == pPlayer.getTeam()) + localText.getText("TXT_KEY_VICTORY_HIGHEST_SCORE", ()) + ' ' + gc.getPlayer(gc.getGame().getRankTeam(0)).getCivilizationShortDescription(0))
		
		elif iPlayer == iMamluks:
			if iGoal == 0: 
				aHelp.append(self.getIcon(self.isTopCityPopulation(iMamluks, con.tFustat)) + localText.getText("TXT_KEY_VICTORY_HIGHEST_POPULATION_IN_CAIRO", ()))
			elif iGoal == 1:
				bUpperEgypt = utils.checkRegionControl(iMamluks, con.rUpperEgypt)
				bLowerEgypt = utils.checkRegionControl(iMamluks, con.rLowerEgypt)
				bPalestine = utils.checkRegionControl(iMamluks, con.rPalestine)
				bLebanon = utils.checkRegionControl(iMamluks, con.rLebanon)
				bSyria = utils.checkRegionControl(iMamluks, con.rSyria)
				bNorthernSyria = utils.checkRegionControl(iMamluks, con.rNorthernSyria)
				bJordan = utils.checkRegionControl(iMamluks, con.rJordan)
				bHejaz = utils.checkRegionControl(iMamluks, con.rHejaz)
				aHelp.append(self.getIcon(bUpperEgypt) + utils.getRegionName(con.rUpperEgypt) + ', ' + self.getIcon(bLowerEgypt) + utils.getRegionName(con.rLowerEgypt) + ', ' + self.getIcon(bPalestine) + utils.getRegionName(con.rPalestine) + ', ' + self.getIcon(bLebanon) + utils.getRegionName(con.rLebanon) + ', ' + self.getIcon(bSyria) + utils.getRegionName(con.rSyria) + ', ')
				aHelp.append(self.getIcon(bNorthernSyria) + utils.getRegionName(con.rNorthernSyria) + ', ' + self.getIcon(bJordan) + utils.getRegionName(con.rJordan) + ', ' + self.getIcon(bHejaz) + utils.getRegionName(con.rHejaz))
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getNumSinks() >= 5) + localText.getText("TXT_KEY_VICTORY_PORTUGUESE_SHIPS_SUNK", (sd.getNumSinks(), 5)))
		
		elif iPlayer == iOttomans:
			if iGoal == 0: 
				bMilitaryDrill = gc.getTeam(pPlayer.getTeam()).isHasTech(con.iMilitaryDrill)
				bMatchlock = gc.getTeam(pPlayer.getTeam()).isHasTech(con.iMatchlock)
				bFlintlock = gc.getTeam(pPlayer.getTeam()).isHasTech(con.iFlintlock)
				aHelp.append(self.getIcon(bMilitaryDrill) + gc.getTechInfo(con.iMilitaryDrill).getText() + ', ' + self.getIcon(bMatchlock) + gc.getTechInfo(con.iMatchlock).getText() + ', ' + self.getIcon(bFlintlock) + gc.getTechInfo(con.iFlintlock).getText())
			elif iGoal == 1:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iRomanEmperor)) + gc.getProjectInfo(con.iRomanEmperor).getText())
			elif iGoal == 2:
				bThrace = utils.checkRegionControl(iOttomans, con.rThrace, True)
				bAnatolia = self.checkRegions(iOttomans, [con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond], True)
				bCaucasus = self.checkRegions(iOttomans, [con.rGreaterArmenia, con.rGeorgia, con.rKars, con.rVaspurakan, con.rShirvan], True)
				bLevant = self.checkRegions(iOttomans, [con.rSyria, con.rNorthernSyria, con.rLebanon, con.rPalestine, con.rJordan], True)
				bMesopotamia = self.checkRegions(iOttomans, [con.rAsuristan, con.rMesopotamia, con.rJazira, con.rEdessa], True)
				bEgypt = self.checkRegions(iOttomans, [con.rUpperEgypt, con.rLowerEgypt], True)
				bHejaz = utils.checkRegionControl(iOttomans, con.rHejaz, True)
				aHelp.append(self.getIcon(bThrace) + utils.getRegionName(con.rThrace) + ', ' + self.getIcon(bAnatolia) + localText.getText("TXT_KEY_VICTORY_ANATOLIA", ()) + ', ' + self.getIcon(bCaucasus) + localText.getText("TXT_KEY_VICTORY_CAUCASUS", ()) + ', ' + self.getIcon(bLevant) + localText.getText("TXT_KEY_VICTORY_LEVANT", ()) + ', ' + self.getIcon(bMesopotamia) + localText.getText("TXT_KEY_VICTORY_MESOPOTAMIA", ()) + ', ' + self.getIcon(bEgypt) + localText.getText("TXT_KEY_VICTORY_EGYPT", ()) + ', ' + self.getIcon(bHejaz) + utils.getRegionName(con.rHejaz))
		
		elif iPlayer == iBahmanids:
			if iGoal == 0:
				aHelp.append(self.getIcon(sd.getGoal(iBahmanids, 0) != 0) + localText.getText("TXT_KEY_VICTORY_NO_CITIES_LOST", ()))
			elif iGoal == 1:
				bGujarat = utils.checkRegionControl(iBahmanids, con.rGujarat)
				bMaharashtra = utils.checkRegionControl(iBahmanids, con.rMaharashtra)
				bKarnataka = utils.checkRegionControl(iBahmanids, con.rKarnataka)
				bMalwa = utils.checkRegionControl(iBahmanids, con.rMalwa)
				bGoa = utils.checkRegionControl(iBahmanids, con.rGoa)
				aHelp.append(self.getIcon(bGujarat) + utils.getRegionName(con.rGujarat) + ', ' + self.getIcon(bMaharashtra) + utils.getRegionName(con.rMaharashtra) + ', ' + self.getIcon(bKarnataka) + utils.getRegionName(con.rKarnataka) + ', ' + self.getIcon(bMalwa) + utils.getRegionName(con.rMalwa) + ', ' + self.getIcon(bGoa) + utils.getRegionName(con.rGoa) + ', ')
			elif iGoal == 2:
				aHelp.append(self.getIcon(sd.getRazedByBahmanids() >= 8) + localText.getText("TXT_KEY_VICTORY_CITIES_RAZED_OR_MASSACRED", (sd.getRazedByBahmanids(), 8)))
		
		elif iPlayer == iTimurids:
			if iGoal == 0: 
				aHelp.append(self.getIcon(sd.getRazedByMongols() >= 9) + localText.getText("TXT_KEY_VICTORY_CITIES_RAZED_OR_MASSACRED", (sd.getRazedByMongols(), 9)))
			elif iGoal == 1:
				aHelp.append(self.getIcon(self.isTopCityCulture(iTimurids, con.tCapitals[iTimurids])) + localText.getText("TXT_KEY_VICTORY_HIGHEST_CULTURE_CITY", (localText.getText("TXT_KEY_VICTORY_SAMARKAND", ()), )))
			elif iGoal == 2:
				totalLand = gc.getMap().getLandPlots()
				ownedLand = pPlayer.getTotalLand()
				if totalLand > 0:
					landPercent = (ownedLand * 100.0) / totalLand
				else:
					landPercent = 0.0
				aHelp.append(self.getIcon(landPercent >= 10.995) + localText.getText("TXT_KEY_VICTORY_LAND_AREA", ()) + ': ' + u"%.2f" % landPercent + '% / 11%')
		
		elif iPlayer == iAkKoyunlu:
			if iGoal == 0:
				bJazira = utils.checkRegionControl(iAkKoyunlu, con.rJazira)
				bAsuristan = utils.checkRegionControl(iAkKoyunlu, con.rAsuristan)
				bAzerbaijan = utils.checkRegionControl(iAkKoyunlu, con.rAzerbaijan)
				aHelp.append(self.getIcon(bJazira) + utils.getRegionName(con.rJazira) + ', ' + self.getIcon(bAsuristan) + utils.getRegionName(con.rAsuristan) + ', ' + self.getIcon(bAzerbaijan) + utils.getRegionName(con.rAzerbaijan))
			elif iGoal == 1:
				bJazira = utils.checkRegionControl(iAkKoyunlu, con.rJazira)
				bAsuristan = utils.checkRegionControl(iAkKoyunlu, con.rAsuristan)
				bAzerbaijan = utils.checkRegionControl(iAkKoyunlu, con.rAzerbaijan)
				bMesopotamia = utils.checkRegionControl(iAkKoyunlu, con.rMesopotamia)
				bKhuzestan = utils.checkRegionControl(iAkKoyunlu, con.rKhuzestan)
				bLesserArmenia = utils.checkRegionControl(iAkKoyunlu, con.rLesserArmenia)
				bShirvan = utils.checkRegionControl(iAkKoyunlu, con.rShirvan)
				aHelp.append(self.getIcon(bJazira) + utils.getRegionName(con.rJazira) + ', ' + self.getIcon(bAsuristan) + utils.getRegionName(con.rAsuristan) + ', ' + self.getIcon(bAzerbaijan) + utils.getRegionName(con.rAzerbaijan) + ', ' + self.getIcon(bMesopotamia) + utils.getRegionName(con.rMesopotamia) + ', ' + self.getIcon(bKhuzestan) + utils.getRegionName(con.rKhuzestan) + ', ' + self.getIcon(bLesserArmenia) + utils.getRegionName(con.rLesserArmenia) + ', ' + self.getIcon(bShirvan) + utils.getRegionName(con.rShirvan))
			elif iGoal == 2:
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iShahanshah)) + gc.getProjectInfo(con.iShahanshah).getText())
		
		elif iPlayer == iSafavids:
			if iGoal == 0: 
				aHelp.append(self.getIcon(gc.getTeam(pPlayer.getTeam()).getProjectCount(con.iShahanshah)) + gc.getProjectInfo(con.iShahanshah).getText())
			elif iGoal == 1:
				iCount = sd.getWondersBuilt(iSafavids)
				aHelp.append(self.getIcon(iCount >= 4) + localText.getText("TXT_KEY_VICTORY_GREAT_WONDERS_BUILT", (iCount, 4)))
			elif iGoal == 2:
				aHelp.append(self.getIcon(self.isTopReligion(con.iShia)) + localText.getText("TXT_KEY_VICTORY_RELIGION_RANKED_FIRST", (gc.getReligionInfo(con.iShia).getTextKey(), )))
		
		elif iPlayer == iPortugal:
			if iGoal == 0:
				iTotalCities = 0
				iPortugueseCities = 0
				for iCiv in range(con.iNumPlayers):
					if iCiv == iPortugal:
						apCityList = PyPlayer(iCiv).getCityList()
						for pCity in apCityList:
							city = CyMap().plot(pCity.getX(), pCity.getY()).getPlotCity()
							if city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rKarnataka, con.rGoa, con.rMaharashtra, con.rGujarat, con.rSindh, con.rBalochistan, con.rMakran, con.rHormuz, con.rFars, con.rKhuzestan, con.rMesopotamia, con.rArabia, con.rBahrain, con.rOman, con.rMahra, con.rHadhramaut, con.rYemen, con.rHejaz, con.rJordan, con.rUpperEgypt, con.rAksum, con.rMerebMellash, con.rSuqutra]:
									iPortugueseCities += 1
									iTotalCities += 1
								elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rSinai, con.rLowerEgypt]:
									if pCity.getY() < 33:
										iPortugueseCities += 1
										iTotalCities += 1
					else:
						apCityList = PyPlayer(iCiv).getCityList()
						for pCity in apCityList:
							city = CyMap().plot(pCity.getX(), pCity.getY()).getPlotCity()
							if city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
								if gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rKarnataka, con.rGoa, con.rMaharashtra, con.rGujarat, con.rSindh, con.rBalochistan, con.rMakran, con.rHormuz, con.rFars, con.rKhuzestan, con.rMesopotamia, con.rArabia, con.rBahrain, con.rOman, con.rMahra, con.rHadhramaut, con.rYemen, con.rHejaz, con.rJordan, con.rUpperEgypt, con.rAksum, con.rMerebMellash, con.rSuqutra]:
									iTotalCities += 1
								elif gc.getMap().plot(pCity.getX(), pCity.getY()).getRegionID() in [con.rSinai, con.rLowerEgypt]:
									if pCity.getY() < 33:
										iTotalCities += 1
				aHelp.append(self.getIcon(iPortugueseCities==iTotalCities) + localText.getText("TXT_KEY_VICTORY_OCEAN_PORTS", ())+ str(iPortugueseCities) + '/' + str(iTotalCities))
			elif iGoal == 1:
				iCount = self.getNumLuxuries(iPortugal)
				aHelp.append(self.getIcon(iCount >= 15) + localText.getText("TXT_KEY_VICTORY_LUXURY_RESOURCES", (iCount, 15)))
			elif iGoal == 2:
				aHelp.append(self.getIcon(pPlayer.getGold() >= utils.getTurns(10000)) + localText.getText("TXT_KEY_VICTORY_GOLD", (pPlayer.getGold(), utils.getTurns(10000))))

		elif iPlayer == iMughals:
			if iGoal == 0:
				bGardens = self.getNumBuildings(iMughals, con.iShalimarGardens)
				bTajMahal = self.getNumBuildings(iMughals, con.iTajMahal)
				bRedFort = self.getNumBuildings(iMughals, con.iRedFort)
				aHelp.append(self.getIcon(bGardens) + localText.getText("TXT_KEY_BUILDING_SHALIMAR_GARDENS", ()) + ', ' + self.getIcon(bTajMahal) + localText.getText("TXT_KEY_BUILDING_TAJ_MAHAL", ()) + ', ' + self.getIcon(bRedFort) + localText.getText("TXT_KEY_BUILDING_RED_FORT", ()))
			elif iGoal == 1:
				bSuccess = self.isHasLegendaryCity(iMughals)
				aHelp.append(self.getIcon(bSuccess) + localText.getText("TXT_KEY_VICTORY_LEGENDARY_CITIES", (bSuccess and 1 or 0, 1)))
			elif iGoal == 2:
				bGandhar = utils.checkRegionControl(iMughals, con.rGandhar)
				bDuggar = utils.checkRegionControl(iMughals, con.rDuggar)
				bPunjab = utils.checkRegionControl(iMughals, con.rPunjab)
				bSindh = utils.checkRegionControl(iMughals, con.rSindh)
				bRajputana = utils.checkRegionControl(iMughals, con.rRajputana)
				bGujarat = utils.checkRegionControl(iMughals, con.rGujarat)
				bUttarBharat = utils.checkRegionControl(iMughals, con.rUttarBharat)
				bGird = utils.checkRegionControl(iMughals, con.rGird)
				bMalwa = utils.checkRegionControl(iMughals, con.rMalwa)
				bMaharashtra = utils.checkRegionControl(iMughals, con.rMaharashtra)
				bKarnataka = utils.checkRegionControl(iMughals, con.rKarnataka)
				aHelp.append(self.getIcon(bGandhar) + utils.getRegionName(con.rGandhar) + ', ' + self.getIcon(bDuggar) + utils.getRegionName(con.rDuggar) + ', ' + self.getIcon(bPunjab) + utils.getRegionName(con.rPunjab) + ', ' + self.getIcon(bSindh) + utils.getRegionName(con.rSindh) + ', ' + self.getIcon(bRajputana) + utils.getRegionName(con.rRajputana) + ', ' + self.getIcon(bGujarat) + utils.getRegionName(con.rGujarat) + ', ')
				aHelp.append(self.getIcon(bUttarBharat) + utils.getRegionName(con.rUttarBharat) + ', ' + self.getIcon(bGird) + utils.getRegionName(con.rGird) + ', ' + self.getIcon(bMalwa) + utils.getRegionName(con.rMalwa) + ', ' + self.getIcon(bMaharashtra) + utils.getRegionName(con.rMaharashtra) + ', ' + self.getIcon(bKarnataka) + utils.getRegionName(con.rKarnataka))
		
		return aHelp
		
		
	def getURV(self, iPlayer, iGoal, bHelp=False):
		"""This method combines URV checking and assembling of help strings 
		for the Victory Screen (if bHelp is set to True)."""
		
		bGoal = False
		aHelp = []
		player = gc.getPlayer(iPlayer)
		iReligion = player.getStateReligion()
		
		# the info is outdated or irrelevant once the goal has been accomplished or failed
		if bHelp and sd.getReligiousGoal(iPlayer, iGoal) == 1:
			aHelp.append(self.getIcon(True) + localText.getText("TXT_KEY_VICTORY_GOAL_ACCOMPLISHED", ()))
			return aHelp
		
		if iReligion == con.iSunni:
			if iGoal == 0:
				fPercent = gc.getGame().calculateReligionPercent(con.iSunni)
				bGoal = (fPercent >= 50.0)
				aHelp.append(self.getIcon(fPercent >= 50.0) + localText.getText("TXT_KEY_VICTORY_RELIGION_SPREAD_TO", (gc.getReligionInfo(con.iSunni).getTextKey(), str(fPercent), 50)))
			elif iGoal == 1:
				iCount = self.countUniqueGreatPeople(con.tMecca)
				bGoal = (iCount >= 7)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_GP_IN_MECCA", (iCount, 7)))
			elif iGoal == 2:
				iPiety = sd.getPiety(iPlayer)
				bGoal = (iPiety >= 100)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 100)))
		
		if iReligion == con.iShia:
			if iGoal == 0:
				iNumSaints = 0
				iGreatPriest = gc.getInfoTypeForString("SPECIALIST_GREAT_PRIEST")
				for iLoopPlayer in range(con.iNumPlayers):
					if gc.getPlayer(iLoopPlayer).getStateReligion() == con.iShia:
						apCityList = PyPlayer(iLoopPlayer).getCityList()
						for pCity in apCityList:
							iNumSaints += pCity.GetCy().getFreeSpecialistCount(iGreatPriest)
				bGoal = (iNumSaints >= 11)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_GREAT_SAINTS_SETTLED", (iNumSaints, 11)))
			elif iGoal == 1:
				bMecca = (gc.getMap().plot(con.tMecca[0],con.tMecca[1]).getOwner() == iPlayer)
				bMedina = (gc.getMap().plot(con.tMedina[0],con.tMedina[1]).getOwner() == iPlayer)
				bKufah = (gc.getMap().plot(con.tNajaf[0],con.tNajaf[1]).getOwner() == iPlayer)
				iNumRelics = self.countRelics(iPlayer)
				bGoal = (bMecca and bMedina and bKufah and iNumRelics >= 3)
				aHelp.append(self.getIcon(bMecca) + localText.getText("TXT_KEY_VICTORY_MECCA", ()) + ', ' + self.getIcon(bMedina) + localText.getText("TXT_KEY_VICTORY_MEDINA", ()) + ', ' + self.getIcon(bKufah) + localText.getText("TXT_KEY_VICTORY_KUFAH", ()) + ', ' + self.getIcon(iNumRelics >= 3) + localText.getText("TXT_KEY_VICTORY_ISLAMIC_RELICS", (iNumRelics, 3)))
			elif iGoal == 2:
				bGoal = self.isTopReligion(con.iShia)
				if bHelp:
					iPercent = int(gc.getGame().calculateReligionPercent(con.iShia))
					if bGoal:
						aHelp.append(self.getIcon(bGoal) + gc.getReligionInfo(con.iShia).getText() + ': ' + str(iPercent) + '%')
					else:
						iRivalPercent = 0
						for iLoopReligion in range(gc.getNumReligionInfos()):
							if iLoopReligion != iReligion and self.isTopReligion(iLoopReligion, bAllowDraw=True):
								iRivalPercent = int(gc.getGame().calculateReligionPercent(iLoopReligion))
								break
						aHelp.append(self.getIcon(bGoal) + gc.getReligionInfo(con.iShia).getText() + ': ' + str(iPercent) + '% (' + gc.getReligionInfo(iLoopReligion).getText() + ': ' + str(iRivalPercent) + '%)')
		
		if iReligion == con.iCatholicism:
			if iGoal == 0:
				iCount = 0
				city = gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1]).getPlotCity()
				for iRelic in con.relics.keys():
					if gc.getBuildingInfo(iRelic).getStateReligion() == iReligion or gc.getBuildingInfo(iRelic).getOrStateReligion() == iReligion:
						iCount += city.getNumRealBuilding(iRelic)
				bGoal = (iCount >= 3)
				aHelp.append(self.getIcon(iCount >= 3) + localText.getText("TXT_KEY_VICTORY_JERUSALEM_RELICS", (iCount, 3)))
			elif iGoal == 1:
				iCount = self.countVassalReligions(iPlayer)
				bGoal = (iCount >= 3)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_VASSAL_RELIGIONS", (iCount, 3)))
			elif iGoal == 2:
				fCatholicism = gc.getGame().calculateReligionPercent(con.iCatholicism)
				fOrthodoxy = gc.getGame().calculateReligionPercent(con.iOrthodoxy)
				iPercent = int(100.0 * fCatholicism / fOrthodoxy)
				bGoal = (iPercent >= 100)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_CATHOLICISM_VS_ORTHODOXY_RATIO", (iPercent, 100)))
		
		if iReligion == con.iOrthodoxy:
			if iGoal == 0:
				bConstantinople = self.isCityHasBuilding(con.tConstantinople, con.iOrthodoxCathedral)
				bAntioch = self.isCityHasBuilding(con.tAntioch, con.iOrthodoxCathedral)
				bJerusalem = self.isCityHasBuilding(con.tJerusalem, con.iOrthodoxCathedral)
				bAlexandria = self.isCityHasBuilding(con.tAlexandria, con.iOrthodoxCathedral)
				bGoal = (bConstantinople and bAntioch and bJerusalem and bAlexandria)
				aHelp.append(self.getIcon(bConstantinople) + localText.getText("TXT_KEY_VICTORY_CONSTANTINOPLE", ()) + ',' + self.getIcon(bAntioch) + localText.getText("TXT_KEY_VICTORY_ANTIOCH", ()) + ',' + self.getIcon(bJerusalem) + localText.getText("TXT_KEY_VICTORY_JERUSALEM", ()) + ',' + self.getIcon(bAlexandria) + localText.getText("TXT_KEY_VICTORY_ALEXANDRIA", ()))
			elif iGoal == 1:
				iCount = self.countPlayersByMinAttitude(iPlayer, 4)
				bGoal = (iCount >= 5)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_FRIENDS", (iCount, 5)))
			elif iGoal == 2:
				iPiety = sd.getPiety(iPlayer)
				bGoal = (iPiety >= 100)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 100)))
		
		if iReligion == con.iHinduism:
			if iGoal == 0:
				iPiety = sd.getPiety(iPlayer)
				bGoal = (iPiety >= 100)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_PIETY", (iPiety, 100)))
			elif iGoal == 1:
				city = gc.getMap().plot(con.tDwarka[0], con.tDwarka[1]).getPlotCity()
				iGoldPerTurn = city.getCommerceRate(CommerceTypes.COMMERCE_GOLD)
				bShrine = (city.getNumRealBuilding(con.iHinduShrine) > 0)
				bGoal = (bShrine and iGoldPerTurn >= 100)
				aHelp.append(self.getIcon(bShrine) + localText.getText("TXT_KEY_VICTORY_HINDU_SHRINE_BUILT", ()) + ', ' + self.getIcon(iGoldPerTurn >= 100) + localText.getText("TXT_KEY_VICTORY_GOLD_PER_TURN", (iGoldPerTurn, 100)))
			elif iGoal == 2:
				iTopRegion = self.getTopPopulationRegion()
				bGoal = utils.checkRegionControl(iPlayer, iTopRegion)
				aHelp.append(self.getIcon(bGoal) + localText.getText("TXT_KEY_VICTORY_MOST_POPULOUS_PROVINCE", (utils.getRegionName(iTopRegion), )))
		
		if bHelp:
			return aHelp
		else:
			return bGoal
	