# Rhye's and Fall of Civilization - Historical Victory Goals


from CvPythonExtensions import *
import math
import CvUtil
import PyHelpers   
import Popup
import Consts as con
import RFCUtils
import DynamicCivs
from random import shuffle
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer
DynamicCivs = DynamicCivs.DynamicCivs()

iNumPlayers = con.iNumPlayers
iNumTotalPlayers = con.iBarbarian
iBarbarian = con.iBarbarian
tCapitals = con.tCapitals

iParCities3 = con.iParCities3
iParCitiesE = con.iParCitiesE
iParCivics3 = con.iParCivics3
iParCivics1 = con.iParCivics1
iParCivicsE = con.iParCivicsE
iParDiplomacy3 = con.iParDiplomacy3
iParDiplomacyE = con.iParDiplomacyE
iParEconomy3 = con.iParEconomy3
iParEconomy1 = con.iParEconomy1
iParEconomyE = con.iParEconomyE
iParExpansion3 = con.iParExpansion3
iParExpansion1 = con.iParExpansion1
iParExpansionE = con.iParExpansionE

tBirth = con.tBirth
tFall = con.tFall
tFallRespawned = con.tFallRespawned

class Stability:


##################################################
### Secure storage & retrieval of script data ###
################################################   


	def getBaseStabilityLastTurn( self, iCiv ):
		return sd.getBaseStabilityLastTurn(iCiv)

	def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
		sd.setBaseStabilityLastTurn(iCiv, iNewValue)

	def getStability( self, iCiv ):
		return sd.getStability(iCiv)

	def setStability( self, iCiv, iNewValue ):
		sd.setStability(iCiv, iNewValue)

	def getCombatResultTempModifier( self, iCiv ):
		return sd.getCombatResultTempModifier(iCiv)

	def setCombatResultTempModifier( self, iCiv, iNewValue ):
		sd.setCombatResultTempModifier(iCiv, iNewValue)

	def getGNPold( self, iCiv ):
		return sd.getGNPold(iCiv)

	def setGNPold( self, iCiv, iNewValue ):
		sd.setGNPold(iCiv, iNewValue)

	def getGNPnew( self, iCiv ):
		return sd.getGNPnew(iCiv)

	def setGNPnew( self, iCiv, iNewValue ):
		sd.setGNPnew(iCiv, iNewValue)

	def getRebelCiv( self ):
		return sd.getRebelCiv()

	def getLatestRebellionTurn( self, iCiv ):
		return sd.getLatestRebellionTurn(iCiv)

	def getPartialBaseStability( self, iCiv ):
		return sd.getPartialBaseStability(iCiv)

	def setPartialBaseStability( self, iCiv, iNewValue ):
		sd.setPartialBaseStability(iCiv, iNewValue)

	def getOwnedPlotsLastTurn( self, iCiv ):
		return sd.getOwnedPlotsLastTurn(iCiv)

	def setOwnedPlotsLastTurn( self, iCiv, iNewValue ):
		sd.setOwnedPlotsLastTurn(iCiv, iNewValue)

	def getOwnedCitiesLastTurn( self, iCiv ):
		return sd.getOwnedCitiesLastTurn(iCiv)

	def setOwnedCitiesLastTurn( self, iCiv, iNewValue ):
		sd.setOwnedCitiesLastTurn(iCiv, iNewValue)

	def getStabilityParameters( self, iParameter ):
		return sd.getStabilityParameters(iParameter)

	def setStabilityParameters( self, iParameter, iNewValue ):
		sd.setStabilityParameters(iParameter, iNewValue)

	def getLastRecordedStabilityStuff( self, iParameter ):
		return sd.getLastRecordedStabilityStuff(iParameter)

	def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
		sd.setLastRecordedStabilityStuff(iParameter, iNewValue)


#######################################
### Main methods (Event-Triggered) ###
#####################################  


	def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
		
		if (gc.getPlayer(iPlayer).isHuman()):
			if (bPreviousAmount):
				self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
			else:
				self.setStabilityParameters(iParameter, 0 + iAmount)


	def setup(self):
		
		utils.setStartingStabilityParameters(utils.getHumanID())


	def checkTurn(self, iGameTurn):
			
			#moved here with its own stored value to save loading time (scrolls the map only once instead of every player)
			if (iGameTurn % utils.getTurns(6) == 0): #3 is too short to detect any change; must be a multiple of 3 anyway
				
				map = CyMap()
				lOwnedPlots = []
				lOwnedCities = []
				for j in range(iNumPlayers):
					lOwnedPlots.append(0)
					lOwnedCities.append(0)
				for i in range(map.numPlots()):
					plot = map.plotByIndex(i)
					iOwner = plot.getOwner()
					iRegionID = plot.getRegionID()
					if iOwner >= 0 and iOwner < iNumPlayers and (plot.isHills() or plot.isFlatlands()):
						if not iRegionID in utils.getCoreRegions(iOwner) and not iRegionID in utils.getNormalRegions(iOwner) and not iRegionID in utils.getBroaderRegions(iOwner):
							lOwnedPlots[iOwner] += 1
						if plot.isCity():
							cityOwner = plot.getPlotCity().getOwner()
							for iLoopPlayer in range(iNumPlayers):
								if (iLoopPlayer != cityOwner and gc.getPlayer(iLoopPlayer).isAlive() and iGameTurn >= getTurnForYear(tBirth[iLoopPlayer]) + utils.getTurns(30) and iGameTurn >= self.getLatestRebellionTurn(iLoopPlayer) + utils.getTurns(15)):
									if iRegionID in utils.getCoreRegions(iLoopPlayer) and not iRegionID in utils.getCoreRegions(iOwner): # allows overlapping - edead
										lOwnedCities[iLoopPlayer] += 1
				for iLoopPlayer in range(iNumPlayers):
					self.setOwnedPlotsLastTurn(iLoopPlayer, lOwnedPlots[iLoopPlayer])
					self.setOwnedCitiesLastTurn(iLoopPlayer, lOwnedCities[iLoopPlayer])

				#for up/down arrows
				if (iGameTurn % 3 == 0 and gc.getActivePlayer().getNumCities() > 0):  #numcities required to test autoplay with minor civs
					self.setLastRecordedStabilityStuff(0, self.getStability(utils.getHumanID()))
					self.setLastRecordedStabilityStuff(1, utils.getParCities())
					self.setLastRecordedStabilityStuff(2, utils.getParCivics())
					self.setLastRecordedStabilityStuff(3, utils.getParEconomy())
					self.setLastRecordedStabilityStuff(4, utils.getParExpansion())
					self.setLastRecordedStabilityStuff(5, utils.getParDiplomacy())
			
			for iPlayer in range(iNumPlayers):
				iTempNormalizationThreshold = self.getStability(iPlayer)
				iStability = iTempNormalizationThreshold
				if iGameTurn % utils.getTurns(10) == 7:
					if iStability < -40:
						if iGameTurn < getTurnForYear(tFall[iPlayer]) or (sd.getCivStatus(iPlayer) == 1 and iGameTurn < getTurnForYear(tFallRespawned[iPlayer])):
							self.setStability(iPlayer, iStability + 1)
				elif iGameTurn % utils.getTurns(10) == 8:
					if not gc.getPlayer(iPlayer).isGoldenAge():
						if iStability > 80:
							self.setStability(iPlayer, iStability - 2)
						elif iStability > 40:
							self.setStability(iPlayer, iStability - 1)
				iStability = self.getStability(iPlayer)
				if iGameTurn % utils.getTurns(12) == 7:
					if iGameTurn >= getTurnForYear(1500) and iStability < 40:
						if iGameTurn < getTurnForYear(tFall[iPlayer]) or (sd.getCivStatus(iPlayer) == 1 and iGameTurn < getTurnForYear(tFallRespawned[iPlayer])):
							self.setStability(iPlayer, iStability + 1)
				iStability = self.getStability(iPlayer)
				if iGameTurn % utils.getTurns(20) == 6:
					if iGameTurn >= getTurnForYear(1250) and iGameTurn < getTurnForYear(1500) and iStability < 20:
						if iGameTurn < getTurnForYear(tFall[iPlayer]) or (sd.getCivStatus(iPlayer) == 1 and iGameTurn < getTurnForYear(tFallRespawned[iPlayer])):
							self.setStability(iPlayer, iStability + 1)
				elif iGameTurn % utils.getTurns(20) == 11:
					iPermanentModifier = iStability - self.getBaseStabilityLastTurn(iPlayer)
					if iPermanentModifier > 15:
						self.setStability(iPlayer, iStability - 1)
					if iPermanentModifier < -40:
						self.setStability(iPlayer, iStability + 1)
				elif iGameTurn % utils.getTurns(20) == 17:
					if iPlayer != utils.getHumanID():
						if iGameTurn > getTurnForYear(tFall[iPlayer]) or (sd.getCivStatus(iPlayer) == 1 and iGameTurn < getTurnForYear(tFallRespawned[iPlayer])):
							self.setStability(iPlayer, iStability - 1)
						if iGameTurn > getTurnForYear(tFall[iPlayer] + 100) or (sd.getCivStatus(iPlayer) == 1 and iGameTurn < getTurnForYear(tFallRespawned[iPlayer]) + 100):
							self.setStability(iPlayer, iStability - 1)
				#print("stability wave", self.getStability(iPlayer) - iTempNormalizationThreshold)
				self.setParameter(iPlayer, iParDiplomacyE, True, self.getStability(iPlayer) - iTempNormalizationThreshold)



	def updateBaseStability(self, iGameTurn, iPlayer):
		
		pPlayer = gc.getPlayer(iPlayer)
		teamPlayer = gc.getTeam(pPlayer.getTeam())
		
		iCivic0 = pPlayer.getCivics(0)
		iCivic1 = pPlayer.getCivics(1)
		iCivic2 = pPlayer.getCivics(2)
		iCivic3 = pPlayer.getCivics(3)
		iCivic4 = pPlayer.getCivics(4)
		
		if (iGameTurn % 3 != 0):
			iNewBaseStability = self.getPartialBaseStability(iPlayer)
			iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts() #used later
			iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION) #used later
			iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD) #used later
			iPopulation = pPlayer.getRealPopulation() #used later
			iEraModifier = pPlayer.getCurrentEra() #used later
		
		else:   #every 3 turns
			
			# DIPLOMACY
			
			iNewBaseStability = 0
			iNewBaseStability += 5*teamPlayer.getDefensivePactTradingCount() # +5 per defensive pact
			iNewBaseStability += 1*teamPlayer.getOpenBordersTradingCount() # +1 per open borders
			
			# -3 for unstable neighbor
			for iLoopCiv in range(iNumPlayers):
				if (iLoopCiv in con.lNeighbours[iPlayer]):
					if (gc.getPlayer(iLoopCiv).isAlive()):
						if (self.getStability(iLoopCiv) < -20):
							if (self.getStability(iPlayer) >= 0):
								iNewBaseStability -= 3
								#print("iNewBaseStability neighbours", iNewBaseStability, iPlayer)
								break
			
			# Vassal: +10 and from -5 to +5 per Master's stability
			for iLoopCiv in range( iNumPlayers ):
				if (teamPlayer.isVassal(iLoopCiv)):
					iNewBaseStability += 10
					#print("iNewBaseStability vassal",iNewBaseStability, iPlayer)
					iNewBaseStability += min(5,max(-5,self.getStability(iLoopCiv)/4))
					break
			
			# Master: +2 (+5 w/Vassalage) and from -2 to +2 per Vassal's stability;
			for iLoopCiv2 in range(iNumPlayers):
				if (gc.getTeam(gc.getPlayer(iLoopCiv2).getTeam()).isVassal(iPlayer)):
					iNewBaseStability += 2
					iNewBaseStability += min(2, max(-2, self.getStability(iLoopCiv2)/4))
					if iCivic1 == 6:
						iNewBaseStability += 3
			
			iNumContacts = 0
			for iLoopCiv3 in range(iNumPlayers):
				if (pPlayer.canContact(iLoopCiv3) and iLoopCiv3 != iPlayer):
					iNumContacts += 1
			iNewBaseStability -= (iNumContacts/3 - 4)
			
			self.setParameter(iPlayer, iParDiplomacy3, False, iNewBaseStability)
			
			# EXPANSION
			
			iTempExpansionThreshold = iNewBaseStability
			
			iMaxPlotsAbroad = 40
			iHandicap = gc.getGame().getHandicapType()
			if (iHandicap == 0):
				iMaxPlotsAbroad = 44
			elif (iHandicap == 2):
				iMaxPlotsAbroad = 36
			iNumPlotsAbroad = max(0,self.getOwnedPlotsLastTurn(iPlayer)-iMaxPlotsAbroad)
			iExpansionPenalty = iNumPlotsAbroad*2/7
			
			iExpansionPenalty = iExpansionPenalty * self.getExpansionPercent(iPlayer) / 100
			
			if not utils.isTitleValid(iPlayer, con.iRomanEmperor): # roman emperor effect: no penalty for lost core cities
				if self.getOwnedCitiesLastTurn(iPlayer) <= 20:
					iExpansionPenalty += self.getOwnedCitiesLastTurn(iPlayer)*7
				else:
					iExpansionPenalty += (self.getOwnedCitiesLastTurn(iPlayer)-6)*10

			iNewBaseStability -= iExpansionPenalty
			
			# Titles
			if teamPlayer.getProjectCount(con.iShahanshah):
				iNewBaseStability += 10
			
			self.setParameter(iPlayer, iParExpansion3, False, iNewBaseStability - iTempExpansionThreshold)
			
			# CIVICS
			
			iTempCivicThreshold = iNewBaseStability
			iStateReligion = pPlayer.getStateReligion()
			
			if iCivic0 == 0: # tribal federation + ? 
				if iCivic1 == 8: iNewBaseStability -= 3 # bureaucracy
				if iCivic3 == 15: iNewBaseStability += 2 # decentralization
				iNewBaseStability += max(-2, min(4, (7 - (pPlayer.getTotalPopulation() / pPlayer.getNumCities()))))

			if iCivic0 == 3: # empire + ?
				if iCivic3 == 18: iNewBaseStability -= 2 # merchant republic
				elif iCivic3 == 19: iNewBaseStability += 1 # state monopoly
				
			if iCivic0 == 4: # absolutism + ?
				if iCivic3 == 18: iNewBaseStability -= 3 # merchant republic
				elif iCivic3 == 19: iNewBaseStability += 2 # state monopoly
				if iCivic4 == 23: iNewBaseStability += 2 # persecution
				elif iCivic4 == 24: iNewBaseStability -= 3 # free religion
				iNewBaseStability += 1 + teamPlayer.getAtWarCount(True)
				
			if iCivic1 == 6: # vassalage + ?
				if iCivic2 == 13: iNewBaseStability += 2 # serfdom
				if iCivic3 == 16: iNewBaseStability += 1 # agrarianism
				elif iCivic3 == 17: iNewBaseStability -= 2 # market economy
				elif iCivic3 == 18: iNewBaseStability -= 3 # merchant capitalism
				if teamPlayer.isHasTech(con.iProfessionalArmies):
					iNewBaseStability -= 2
			
			if iCivic2 == 12: # caste system
				if iStateReligion == con.iHinduism:
					iNewBaseStability += 2
				else:
					iNewBaseStability -= 2
			
			if iCivic1 == 7: # religious law + ?
				if iCivic4 == 20 or iCivic4 == 24: # shamanism & free religion
					iNewBaseStability -= 5
				elif iCivic4 == 22 or iCivic4 == 23: # theocracy & persecution
					iNewBaseStability += 1
				if iStateReligion == con.iSunni or iStateReligion == con.iShia:
					iNewBaseStability += 2
				else:
					iNewBaseStability -= 2
			
			if iCivic2 == 13 and iCivic3 == 16: # serfdom + agrarianism
				iNewBaseStability += 2
			
			if iCivic3 == 17 and iCivic2 == 14: # market economy + free labor
				iNewBaseStability += 2
			
			if iCivic2 == 14 and iCivic4 == 24: # free labor + free religion
				iNewBaseStability += 2
			
			if iCivic0 == 1 and iCivic3 == 18: # monarchy + merchant capitalism
				iNewBaseStability -= 2
			
			if iCivic2 == 11: # slavery
				if iCivic4 == 24: iNewBaseStability -= 3 # free religion
				if iStateReligion == con.iHinduism: iNewBaseStability -= 2
				iNewBaseStability -= pPlayer.getCurrentEra()
			
			if iCivic1 == 7: # bureaucracy
				iNewBaseStability += min(2, max(-5,(6 - pPlayer.getNumCities())))
			
			if iCivic0 == 2: # aristocracy
				iNewBaseStability += max(-5,(6 - pPlayer.getNumCities()))
			
			if iCivic0 == 3: # empire
				iNewBaseStability += min(5, max(-3,(pPlayer.getNumCities() - 6)))
			
			if iCivic0 == 1: # dynasticism
				if self.getStability(iPlayer) < 0:
					iNewBaseStability += self.getStability(iPlayer) / -4
			
			self.setParameter(iPlayer, iParCivics3, False, iNewBaseStability - iTempCivicThreshold)
			
			# CITIES
			
			apCityList = PyPlayer(iPlayer).getCityList()
			
			iTempExpansionPenalty = 0
			
			for pLoopCity in apCityList:
				iTempCityPenalty = 0
				regionID = gc.getMap().plot(pLoopCity.GetCy().getX(),pLoopCity.GetCy().getY()).getRegionID()
				for iLoop in range(iNumPlayers):
					if iGameTurn > getTurnForYear(tBirth[iLoop]) and iLoop != iPlayer:
						if regionID in utils.getCoreRegions(iLoop) and not regionID in utils.getCoreRegions(iPlayer):
							if iGameTurn < getTurnForYear(tFall[iLoop]):
								if regionID in utils.getNormalRegions(iPlayer) or regionID in utils.getBroaderRegions(iPlayer):
									iTempCityPenalty = 2
								else:
									iTempCityPenalty = 3
							else:
								if regionID in utils.getNormalRegions(iPlayer) or regionID in utils.getBroaderRegions(iPlayer):
									iTempCityPenalty = 1
								else:
									iTempCityPenalty = 2
							break
						elif regionID in utils.getNormalRegions(iLoop) or regionID in utils.getBroaderRegions(iLoop):
							if regionID not in utils.getCoreRegions(iPlayer) and regionID not in utils.getNormalRegions(iLoop) and regionID not in utils.getBroaderRegions(iLoop):
								iTempCityPenalty = 1
				iTempExpansionPenalty += iTempCityPenalty
			
			iTempExpansionPenalty = iTempExpansionPenalty * self.getExpansionPercent(iPlayer) / 100
			
			# Roman Emperor effect
			if iTempExpansionPenalty < 0 and utils.isTitleValid(iPlayer, con.iRomanEmperor):
				iTempExpansionPenalty /= 2
			
			iNewBaseStability -= iTempExpansionPenalty
			self.setParameter(iPlayer, iParExpansion3, True, -iTempExpansionPenalty)
			
			iTotalTempCityStability = 0
			
			for pCity in apCityList:
				city = pCity.GetCy()
				pCurrent = gc.getMap().plot(city.getX(), city.getY())
				iTempCityStability = 0
				
				if (city.angryPopulation(0) > 0):
					iTempCityStability -= 2
				if (city.healthRate(False, 0) < 0):
					iTempCityStability -= 1
				if (city.getReligionBadHappiness() > 0):
					if iPlayer != con.iFatimids: # UP: Tolerance
						iTempCityStability -= max(2, city.getReligionBadHappiness())
				if (city.getHurryAngerModifier() > 0):
					iTempCityStability -= 3
				if (city.getNoMilitaryPercentAnger() > 0):
					iTempCityStability -= 2
				if (city.getWarWearinessPercentAnger() > 0):
					iTempCityStability -= 1
				
				if (iTempCityStability <= -5): #middle check, for optimization
					iTotalTempCityStability += max(-5,iTempCityStability)
					#print("iTotalTempCityStability", iTotalTempCityStability, city.getName(), iPlayer)
					if (iTotalTempCityStability <= -10): #middle check, for optimization
						break
					else:
						continue
				
				# instability from non-state religion - skip if player has free religion civic or tolerant trait
				iTempReligionStability = 0
				if iCivic4 != 24 and iPlayer != con.iFatimids:
					for iLoop in range(con.iNumReligions):
						if city.isHasReligion(iLoop) and pPlayer.getStateReligion() != iLoop:
							if not (iPlayer == con.iAntioch and city.getNumRealBuilding(con.iNormanChapel) and iLoop == con.iOrthodoxy):
								iTempReligionStability -= 1
				if not city.isHasReligion(pPlayer.getStateReligion()):
					if not (iPlayer == con.iAntioch and pPlayer.getStateReligion() == con.iCatholicism and city.getNumRealBuilding(con.iNormanChapel)):
						iTempReligionStability -= 1
					
				iTempReligionStability = max(-4, iTempReligionStability)
				iTempCityStability += iTempReligionStability
				
				for iLoop in range(iNumTotalPlayers+1):
					if (iLoop != iPlayer):
						if (pCurrent.getCulture(iLoop) > 0):
							if (pCurrent.getCulture(iPlayer) == 0): #division by zero may happen
								iTempCityStability -= 2
							else:
								if (pCurrent.getCulture(iLoop)*100/pCurrent.getCulture(iPlayer) >= 15):
									if (iPlayer == con.iOttomans or iPlayer == con.iMughals or iPlayer == con.iRum or iPlayer == con.iSafavids): #they have too much foreign culture
										iTempCityStability -= 1
									else:
										iTempCityStability -= 2
									break
				
				if (iTempCityStability < 0):
					iTotalTempCityStability += max(-5,iTempCityStability)
					#print("iTotalTempCityStability", iTotalTempCityStability, city.getName(), iPlayer)
				
				if (iTotalTempCityStability <= -12): #middle check, for optimization
					break

			if iTotalTempCityStability < 0:
				iTotalTempCityStability += max(-12, iTotalTempCityStability)
				# Roman Emperor effect
				if utils.isTitleValid(iPlayer, con.iRomanEmperor):
					iTotalTempCityStability /= 2
				iNewBaseStability += iTotalTempCityStability
				#print("iNewBaseStability city check", iNewBaseStability, iPlayer)
			
			self.setParameter(iPlayer, iParCities3, False, iTotalTempCityStability)
			
			# BUILDINGS
			
			iTempBuildingsStability = 0
			
			for pCity in apCityList:
				city = pCity.GetCy()
				
				if city.getNumRealBuilding(con.iCourthouse) or city.getNumRealBuilding(con.iDivan) or city.getNumRealBuilding(con.iChancery):
					iTempBuildingsStability += 1
				if city.getNumRealBuilding(con.iBuddhistMonastery) and city.isHasReligion(con.iBuddhism):
					iTempBuildingsStability += 1
				if (city.getNumRealBuilding(con.iCatholicTemple) and iStateReligion == con.iCatholicism) \
					or (city.getNumRealBuilding(con.iOrthodoxTemple) and iStateReligion == con.iOrthodoxy) \
					or (city.getNumRealBuilding(con.iSunniTemple) and iStateReligion == con.iSunni) \
					or (city.getNumRealBuilding(con.iShiaTemple) and iStateReligion == con.iShia) \
					or (city.getNumRealBuilding(con.iHinduTemple) and iStateReligion == con.iHinduism):
						iTempBuildingsStability += 1
				if city.getNumRealBuilding(con.iSacredSeal):
					iTempBuildingsStability += 4
				# elif (city.getNumRealBuilding(con.iCatholicCathedral) and iStateReligion == con.iCatholicism) \
					# or (city.getNumRealBuilding(con.iOrthodoxCathedral) and iStateReligion == con.iOrthodoxy) \
					# or (city.getNumRealBuilding(con.iSunniCathedral) and iStateReligion == con.iSunni) \
					# or (city.getNumRealBuilding(con.iShiaCathedral) and iStateReligion == con.iShia) \
					# or (city.getNumRealBuilding(con.iHinduCathedral) and iStateReligion == con.iHinduism):
						# self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
				# elif city.getNumRealBuilding(con.iDungeon) or city.getNumRealBuilding(con.iMausoleum): #jail
					# self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
			
			iNewBaseStability += iTempBuildingsStability
			self.setParameter(iPlayer, iParCities3, True, iTempBuildingsStability)
			
			# HAPPINESS
			
			iHappiness = -10
			if (pPlayer.calculateTotalCityHappiness() > 0):
				iHappiness = int((1.0 * pPlayer.calculateTotalCityHappiness()) / (pPlayer.calculateTotalCityHappiness() + \
					pPlayer.calculateTotalCityUnhappiness()) * 100) - 60
			iNewBaseStability += iHappiness/10
			self.setParameter(iPlayer, iParCities3, True, iHappiness/10)
			
			# PIETY
			
			iPietyBonus = con.tFavorLevelsStabilityBonus[utils.getFavorLevel(iPlayer)]
			if iPlayer == utils.getHumanID():
				iPietyBonus *= 3
				iPietyBonus /= 2
			iNewBaseStability += iPietyBonus
			self.setParameter(iPlayer, iParCities3, True, iPietyBonus)
			
			# ECONOMY
			
			iTempEconomyThreshold = iNewBaseStability
			iImports = pPlayer.calculateTotalImports(YieldTypes.YIELD_COMMERCE)
			iExports = pPlayer.calculateTotalExports(YieldTypes.YIELD_COMMERCE)
			iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts()
			iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
			iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD)
			iPopulation = pPlayer.getTotalPopulation()
			iEraModifier = pPlayer.getCurrentEra()
			
			iTradeBalance = (iImports + iExports) / 5 - iEraModifier*2
			iTradeBalance = min(6, max(-6, iTradeBalance))
			iAgricultureBalance = int(5*(float(iAgriculture) / iPopulation - 2)) - 2
			iAgricultureBalance = min(4, max(-8, iAgricultureBalance))
			iEconomyBalance = int(5*(float(iEconomy-8) * (1-iEraModifier/5) / iPopulation - 2))
			iEconomyBalance = min(8, max(-8, iEconomyBalance))
			iIndustryBalance = int(5*(float(iIndustry) * (1-iEraModifier/10) / iPopulation - 2))
			iIndustryBalance = min(4, max(-4, iIndustryBalance))
			
			# Decentralization civic
			iTotalBalance = iTradeBalance + iAgricultureBalance + iEconomyBalance + iIndustryBalance
			if iCivic4 == 14 and iTotalBalance < 0:
				iTotalBalance /= 3
			
			iNewBaseStability = iNewBaseStability + iTotalBalance
			
			self.setParameter(iPlayer, iParEconomy3, False, iNewBaseStability - iTempEconomyThreshold)
			
			self.setPartialBaseStability(iPlayer, iNewBaseStability)

		#every turn

		if (iGameTurn >= getTurnForYear(tBirth[iPlayer])+utils.getTurns(15)):
			self.setGNPnew(iPlayer, self.getGNPnew(iPlayer) + (iEconomy + 4*iIndustry + 2*iAgriculture)/7)
			if (iGameTurn % utils.getTurns(3) == 2):
				iTempEconomyThreshold = self.getStability(iPlayer)
				iMaxShrink = 7
				iMaxGrowth = 3
				iNegativeFasterGrowth = (self.getGNPnew(iPlayer)-4)/3 - self.getGNPold(iPlayer)/3   #-1:-1 -2:-2 -3:-2 -4:-2 -5:-3 -6:-3 -7:-3 -8:-4 
				iNegativeNormalGrowth = (self.getGNPnew(iPlayer)-3)/3 - self.getGNPold(iPlayer)/3   #-1:-1 -2:-1 -3:-2 -4:-2 -5:-2 -6:-3 -7:-3 -8:-3 
				iNegativeSlowerGrowth = (self.getGNPnew(iPlayer)-1)/3 - self.getGNPold(iPlayer)/3   #-1: 0 -2:-1 -3:-1 -4:-1 -5:-2 -6:-2 -7:-2 -8:-3 
				
				iPositiveFasterGrowth = self.getGNPnew(iPlayer)/3 - self.getGNPold(iPlayer)/3   # 0: 0 +1: 0 +2: 0 +3:+1 +4:+1 +5:+1 +6:+2 +7:+2 +8:+2 +9:+3   
				iPositiveNormalGrowth = self.getGNPnew(iPlayer)/4 - self.getGNPold(iPlayer)/4	   # 0: 0 +1: 0 +2: 0 +3: 0 +4:+1 +5:+1 +6:+1 +7:+1 +8:+2 +9:+2 
				iPositiveSlowerGrowth = self.getGNPnew(iPlayer)/5 - self.getGNPold(iPlayer)/5	   # 0: 0 +1: 0 +2: 0 +3: 0 +4: 0 +5:+1 +6:+1 +7:+1 +8:+1 +9:+1 

				iNegativeGrowth = iNegativeNormalGrowth
				iPositiveGrowth = iPositiveNormalGrowth
				if iPlayer in [con.iByzantium, con.iMakuria, con.iAbbasids, con.iChauhan, con.iSamanids]: #counterbalance their stagnation due to the very early start
					iNegativeGrowth = iNegativeSlowerGrowth
					iPositiveGrowth = iPositiveSlowerGrowth
				if iPlayer in [con.iMamluks, con.iTimurids, con.iAkKoyunlu, con.iOttomans, con.iSafavids, con.iMughals]: #counterbalance their late start
					iNegativeGrowth = iNegativeFasterGrowth
					iPositiveGrowth = iPositiveFasterGrowth
				
				if (self.getGNPnew(iPlayer) < self.getGNPold(iPlayer)):
					self.setStability(iPlayer, self.getStability(iPlayer) + max(-iMaxShrink, iNegativeGrowth))
				elif (self.getGNPnew(iPlayer) >= self.getGNPold(iPlayer)):
					self.setStability(iPlayer, self.getStability(iPlayer) + min(iMaxGrowth, iPositiveGrowth))
				
				self.setParameter(iPlayer, iParEconomyE, True, self.getStability(iPlayer) - iTempEconomyThreshold)

		iTempEconomyThreshold = iNewBaseStability

		if (iGameTurn % utils.getTurns(3) == 2):
			self.setGNPold(iPlayer, self.getGNPnew(iPlayer))
			self.setGNPnew(iPlayer, 0)

		self.setParameter(iPlayer, iParEconomy1, False, iNewBaseStability - iTempEconomyThreshold)

		iTempCivicThreshold = iNewBaseStability
		self.setParameter(iPlayer, iParCivics1, False, iNewBaseStability - iTempCivicThreshold)

		iTempExpansionThreshold = iNewBaseStability
		iNumPlayerCities = pPlayer.getNumCities()
		iNumCitiesThreshold = 7 + pPlayer.getCurrentEra() # edead
		if iNumPlayerCities >= iNumCitiesThreshold:
			iNewBaseStability -= (iNumPlayerCities-iNumCitiesThreshold+3)*(iNumPlayerCities-iNumCitiesThreshold+3)/9
		self.setParameter(iPlayer, iParExpansion1, False, iNewBaseStability - iTempExpansionThreshold)

		if (self.getCombatResultTempModifier(iPlayer) != 0):
			iTempExpansionThreshold = iNewBaseStability
			iNewBaseStability += max(-20, min(20,self.getCombatResultTempModifier(iPlayer)))
			self.setParameter(iPlayer, iParExpansion1, True, iNewBaseStability - iTempExpansionThreshold) 
			if (self.getCombatResultTempModifier(iPlayer) <= -4 -(iEraModifier/2)): #great loss
				self.setStability(iPlayer, self.getStability(iPlayer) -1)
				self.setParameter(iPlayer, iParDiplomacyE, True, -1)
			if (abs(self.getCombatResultTempModifier(iPlayer)) >= 4):
				self.setCombatResultTempModifier(iPlayer, self.getCombatResultTempModifier(iPlayer)/2)
			else:
				self.setCombatResultTempModifier(iPlayer, 0)
		
		if (pPlayer.getAnarchyTurns() != 0):
			iTempCivicsThreshold = self.getStability(iPlayer)
			if (self.getStability(iPlayer) > 24):
				#print("Stability: anarchy permanent", self.getStability(iPlayer) - self.getStability(iPlayer)/8, iPlayer)
				self.setStability(iPlayer, self.getStability(iPlayer) - self.getStability(iPlayer)/8/utils.getTurns(1)) # edead: penalty scaling                               
			else:
				#print("Stability: anarchy permanent", 3, iPlayer)
				self.setStability(iPlayer, self.getStability(iPlayer)-3/utils.getTurns(1)) # edead: penalty scaling
			self.setParameter(iPlayer, iParCivicsE, True, self.getStability(iPlayer) - iTempCivicsThreshold)
			iNewBaseStability -= (self.getStability(iPlayer)+30)/2
			self.setParameter(iPlayer, iParCivics1, True, -(self.getStability(iPlayer)+30)/2) 
			#print("iNewBaseStability anarchy",iNewBaseStability, iPlayer)
		
		if (pPlayer.isGoldenAge()):
			iNewBaseStability += 20
			#print("iNewBaseStability golden",iNewBaseStability, iPlayer)
			self.setParameter(iPlayer, iParEconomy1, True, 20) 
		
		sd.setStability(iPlayer, self.getStability(iPlayer) - self.getBaseStabilityLastTurn(iPlayer) + iNewBaseStability)
		# if (self.getStability(iPlayer) < -80):
			# self.setStability(iPlayer, -80)
		# if (self.getStability(iPlayer) > 80):
			# self.setStability(iPlayer, 80)
		
		self.setBaseStabilityLastTurn(iPlayer, iNewBaseStability)


	def onCityBuilt(self, iPlayer, x, y):
		
		iTempExpansionThreshold = self.getStability(iPlayer)
		iGameTurn = gc.getGame().getGameTurn()
		if (iGameTurn <= getTurnForYear(tBirth[iPlayer]) + utils.getTurns(20)):
			self.setStability(iPlayer, self.getStability(iPlayer) + 3)
		else:
			self.setStability(iPlayer, self.getStability(iPlayer) + 1)
		if (gc.getPlayer(iPlayer).getNumCities() == 1):
			self.setStability(iPlayer, self.getStability(iPlayer) + 1)
		self.setParameter(iPlayer, iParExpansionE, True, self.getStability(iPlayer) - iTempExpansionThreshold) 


	def onCityAcquired(self, owner, playerType, city, bConquest, bTrade):
		
		iGameTurn = gc.getGame().getGameTurn()
		if playerType < iNumPlayers:
			iBirth = getTurnForYear(tBirth[playerType])
		else:
			iBirth = 0
		if (owner < iNumPlayers):
			iTotalCityLostModifier = 0
			if (bTrade and (iGameTurn == iBirth or iGameTurn == iBirth+1 or iGameTurn == iBirth+2)):
				iTotalCityLostModifier = 3 #during a civ birth
				if (not gc.getPlayer(owner).isHuman()):
					iTotalCityLostModifier += 1
			elif (bTrade and playerType == self.getRebelCiv() and iGameTurn == self.getLatestRebellionTurn(playerType)):
				iTotalCityLostModifier = 2 #during a civ resurrection
			else:
				iTotalCityLostModifier = max(-5,(16 - gc.getPlayer(owner).getNumCities())/2) #conquering 40 cities and immediately releasing them is an exploit - cap added
				if (bTrade):
					iTotalCityLostModifier += 2
					#self.setParameter(owner, iParDiplomacyE, True, -1)
					if (gc.getPlayer(owner).isHuman()): #anti-exploit
						if (city.isOccupation()):
							self.setStability(owner, self.getStability(owner) - 3) 
							self.setParameter(owner, iParDiplomacyE, True, - 3)
							self.setStability(playerType, self.getStability(owner) + 3)
							self.setParameter(playerType, iParDiplomacyE, True, + 3)
				if (city.getX() == tCapitals[owner][0] and city.getY() == tCapitals[owner][1]):
						iTotalCityLostModifier += 5
				if (playerType == con.iBarbarian):
						iTotalCityLostModifier += 1
			self.setParameter(owner, iParExpansionE, True, -iTotalCityLostModifier) 
			self.setStability(owner, self.getStability(owner) - iTotalCityLostModifier )
			#print("Stability - city lost", iTotalCityLostModifier, owner)
		
		if (playerType < iNumPlayers):
			iTempExpansionThreshold = self.getStability(playerType)
			if (iGameTurn == iBirth or iGameTurn == iBirth+1 or iGameTurn == iBirth+2):
				self.setStability(playerType, self.getStability(playerType) + 3)
			elif (owner >= iNumPlayers):
				self.setStability(playerType, self.getStability(playerType) + max(0,min(5,(12 - gc.getPlayer(playerType).getNumCities())/2)) )
			else:
				self.setStability(playerType, self.getStability(playerType) + max(0,min(5,(12 - gc.getPlayer(playerType).getNumCities())/2)) )
			#print("Stability - city acquired", playerType)
			# Start Samanid UP
			if playerType == con.iSamanids and bConquest:
				self.setStability(playerType, self.getStability(playerType) + 2)
			# End Samanid UP
			if (owner < con.iNumPlayers):
				if (city.getX() == tCapitals[owner][0] and city.getY() == tCapitals[owner][1]):
					self.setStability(playerType, self.getStability(playerType) + 3)
					#print("Stability - capital city acquired", playerType)
			self.setParameter(playerType, iParExpansionE, True, self.getStability(playerType) - iTempExpansionThreshold)


	def onCityRazed(self, iOwner):
		
		if iOwner < iNumPlayers:
			self.setStability(iOwner, self.getStability(iOwner)-3)
			self.setParameter(iOwner, iParExpansionE, True, -3)


	def onTechAcquired(self, iTech, iPlayer):
		
		if iPlayer >= iNumPlayers: return
		
		iTempCivicsThreshold = self.getStability(iPlayer)
		if iTech in [con.iReligiousUnity, con.iMovableType]:
			self.setStability(iPlayer, self.getStability(iPlayer)-2)
		elif iTech in [con.iCastleBuilding, con.iLevyArmies, con.iMilitaryDrill, con.iProfessionalArmies, con.iMatchlock, con.iFlintlock, con.iMilitaryScience]:
				self.setStability(iPlayer, self.getStability(iPlayer)-1)
		elif iTech in [con.iCivilService, con.iWelfareState, con.iAdministrativeReforms, con.iSyncretism, con.iImperialism]:
				self.setStability(iPlayer, self.getStability(iPlayer)+1)
		
		self.setParameter(iPlayer, iParCivicsE, True, self.getStability(iPlayer) - iTempCivicsThreshold)


	def onBuildingBuilt(self, iPlayer, iBuilding, city):
		
		if iPlayer >= iNumPlayers: return
		
		iTempCitiesThreshold = self.getStability(iPlayer)
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		
		if iBuilding == con.iPalace: # palace
			self.setStability(iPlayer, self.getStability(iPlayer) - 5 )
		elif iBuilding == con.iForbiddenPalace: # summer palace
			self.setStability(iPlayer, self.getStability(iPlayer) + 5 )
		elif con.iBridge33 >= iBuilding >= con.iHeroicEpic: # wonder
			self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
		
		self.setParameter(iPlayer, iParCitiesE, True, self.getStability(iPlayer) - iTempCitiesThreshold)


	def onProjectBuilt(self, iPlayer, iProject):
		pass


	def onCombatResult(self, argsList):
		
		pWinningUnit,pLosingUnit = argsList
		iWinningPlayer = pWinningUnit.getOwner()
		iLosingPlayer = pLosingUnit.getOwner()
		
		if iWinningPlayer < iNumPlayers:
			self.setCombatResultTempModifier(iWinningPlayer, self.getCombatResultTempModifier(iWinningPlayer) + 1)
		if iLosingPlayer < iNumPlayers:
			self.setCombatResultTempModifier(iLosingPlayer, self.getCombatResultTempModifier(iLosingPlayer) - 2)


	def onReligionSpread(self, iReligion, iPlayer):
		
		if iPlayer < iNumPlayers:  
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.getStateReligion() != iReligion:
				self.setStability(iPlayer, self.getStability(iPlayer) -1)
				self.setParameter(iPlayer, iParCitiesE, True, -1)


	def checkImplosion(self, iGameTurn):
		
		if iGameTurn % utils.getTurns(10) == 5:
			for iPlayer in range(iNumPlayers):
				pPlayer = gc.getPlayer(iPlayer)
				if pPlayer.isAlive() and iGameTurn >= getTurnForYear(tBirth[iPlayer]) + utils.getTurns(25) and not pPlayer.isGoldenAge():
					if self.getStability(iPlayer) < -40: #civil war
						
						iHuman = utils.getHumanID()
						
						# Portugal can't collapse
						if iPlayer == con.iPortugal:
							utils.secedeRandomCity(iPlayer)
							return
						
						# Roman Emperor: secede a few foreign cities instead of starting civil war
						if utils.isTitleValid(iPlayer, con.iRomanEmperor):
							cityList = []
							tempList = []
							apCityList = PyPlayer(iPlayer).getCityList()
							minCities = max(1, len(apCityList)/8)
							maxCities = max(1, len(apCityList)/5)
							if self.getStability(iPlayer) < -50:
								minCities = max(1, len(apCityList)/5)
								maxCities = max(1, len(apCityList)/4)
							elif self.getStability(iPlayer) < -60:
								minCities = max(1, len(apCityList)/5)
								maxCities = max(1, len(apCityList)/3)
							elif self.getStability(iPlayer) < -80:
								minCities = max(1, len(apCityList)/4)
								maxCities = max(1, len(apCityList)/3)
							shuffle(apCityList)
							capital = pPlayer.getCapitalCity()
							for pyCity in apCityList:
								city = pyCity.GetCy()
								iRegion = gc.getMap().plot(pyCity.getX(), pyCity.getY()).getRegionID()
								if iRegion not in utils.getCoreRegions(iPlayer) and iRegion not in utils.getNormalRegions(iPlayer) and iRegion not in utils.getBroaderRegions(iPlayer):
									tempList.append(city)
							for city in tempList:
								iDistance = utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY())
								if iDistance > 40:
									cityList.append(city)
									if len(cityList) >= maxCities:
										break
							if len(cityList) < minCities:
								for city in tempList:
									if city not in cityList:
										iDistance = utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY())
										iRegion = gc.getMap().plot(pyCity.getX(), pyCity.getY()).getRegionID()
										if iDistance > 30 or iRegion in con.lUnrulyRegions or city.isOccupation() or city.isDisorder():
											cityList.append(city)
											if len(cityList) >= maxCities:
												break
							if len(cityList) < minCities:
								for city in tempList:
									if city not in cityList:
										if city.getHurryAngerModifier() > 0 or city.getNoMilitaryPercentAnger() > 0 or city.angryPopulation(0) > 0 or city.getReligionBadHappiness() > 0 or city.getWarWearinessPercentAnger() > 0:
											cityList.append(city)
											if len(cityList) >= maxCities:
												break
							if len(cityList) < minCities:
								for city in tempList:
									if city not in cityList:
										pCurrent = gc.getMap().plot(city.getX(), city.getY())
										for iLoop in range(iNumTotalPlayers+1):
											if iLoop != iPlayer:
												if pCurrent.getCulture(iLoop) > pCurrent.getCulture(iPlayer)/2:
													cityList.append(city)
													break
										if len(cityList) >= maxCities:
											break
							
							cityNames = []
							for city in cityList:
								result = utils.secedeCity(city, True)
								if result:
									cityNames.append(result)
									tempCity = city
							
							if len(cityNames) > 1:
								if iPlayer == iHuman and pPlayer.getNumCities() > 0:
									cityString = ', '.join(cityNames)
									CyInterface().addMessage(iHuman, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_NEW_IMPLOSION_YOU", ()), "AS2D_CITYCAPTURE", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
									CyInterface().addMessage(iHuman, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_SECESSION_MULTI", (cityString, )), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
								elif len(cityNames) >= minCities and utils.isActive(iHuman) and gc.getPlayer(iHuman).canContact(iPlayer):
									CyInterface().addMessage(iHuman, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_NEW_IMPLOSION", (gc.getPlayer(iPlayer).getCivilizationDescription(0), )), "AS2D_CITYCAPTURE", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, "", ColorTypes(con.iRed), -1, -1, False, False)
							elif len(cityNames) == 1 and tempCity and iPlayer == iHuman and pPlayer.getNumCities() > 0:
								CyInterface().addMessage(iHuman, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_SECESSION", (tempCity.getName(), )), "AS2D_CITY_REVOLT", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, ArtFileMgr.getInterfaceArtInfo("INTERFACE_RESISTANCE").getPath(), ColorTypes(con.iRed), tempCity.getX(), tempCity.getY(), True, True)
							
							continue 
						
						if not utils.canCollapse(iPlayer):
							continue
						
						# normal collapse
						if iPlayer != iHuman:
							if gc.getPlayer(iHuman).canContact(iPlayer):
								CyInterface().addMessage(iHuman, False, con.iDuration, pPlayer.getCivilizationDescription(0) + " " + \
									localText.getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
							utils.killAndFragmentCiv(iPlayer, False)
						else:
							if gc.getPlayer(iPlayer).getNumCities() > 1:
								CyInterface().addMessage(iPlayer, True, con.iDuration, localText.getText("TXT_KEY_STABILITY_CIVILWAR_HUMAN", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
								utils.killAndFragmentCiv(iPlayer, True)
								utils.setStartingStabilityParameters(iPlayer)
								self.setGNPold(iPlayer, 0)
								self.setGNPnew(iPlayer, 0)
						
						return
	
	
	def getExpansionPercent(self, iPlayer):
		"""Returns the Expansion stability modifier for a given player."""
		
		iExpansionPercent = 100
		if gc.getPlayer(iPlayer).getCivics(0) == con.iEmpireCivic: # Empire civic
			iExpansionPercent -= 40
		if iPlayer == sd.getVal('iTopkapiOwner'): # Topkapi Palace wonder
			iExpansionPercent -= 25
		return iExpansionPercent
